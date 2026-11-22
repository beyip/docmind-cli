"""Render what the phone screen actually shows (mini ANSI terminal emulator)."""
import os
import pty
import re
import select
import sys
import tempfile
import time
import json
import pathlib

COLS = int(os.environ.get("COLS", "40"))
ROWS = int(os.environ.get("ROWS", "24"))


EVENTS = []


class Screen:
    def __init__(self, cols, rows):
        self.cols, self.rows = cols, rows
        self.grid = [[" "] * cols for _ in range(rows)]
        self.x = self.y = 0
        self.saved = (0, 0)
        self.overwrites = 0
        self.st, self.sb = 0, rows - 1

    def _scroll(self):
        self.grid.pop(self.st)
        self.grid.insert(self.sb, [" "] * self.cols)

    def put(self, ch):
        if self.x >= self.cols:
            self.x = 0
            if self.y < self.sb:
                self.y += 1
        if self.y >= self.rows:
            self.y = self.rows - 1
        cell = self.grid[self.y][self.x]
        if cell != " " and ch != " ":
            self.overwrites += 1
            if os.environ.get("CTX"):
                o = getattr(self, "off", 0)
                EVENTS.append(("CTX", repr(self.data[max(0, o - 160):o + 1])[-300:]))
        if os.environ.get("TRACEPOS"):
            import traceback as _tb
            st = [f for f in _tb.extract_stack() if 'screen_check' not in f.filename]
            EVENTS.append(("POS", self.overwrites, self.y, self.x, repr(ch), "".join(self.grid[self.y]).rstrip()[:50], [ (f.filename.split('/')[-1], f.lineno) for f in st[-3:] ]))
            if len(EVENTS) < 12:
                EVENTS.append((self.y, self.x, "".join(self.grid[self.y]).rstrip()[:60], ch))
        self.grid[self.y][self.x] = ch
        self.x += 1

    def feed(self, data):
        i = 0
        self.data = data
        while i < len(data):
            self.off = i
            ch = data[i]
            if ch == "\x1b":
                m = re.match(r"\x1b\[([0-9;?]*)([A-Za-z])", data[i:])
                if m:
                    params, final = m.group(1), m.group(2)
                    n = int(params or "1") if params.isdigit() or not params else 1
                    if final == "A":
                        self.y = max(0, self.y - n)
                    elif final == "B":
                        self.y = min(self.rows - 1, self.y + n)
                    elif final == "C":
                        self.x = min(self.cols - 1, self.x + n)
                    elif final == "D":
                        self.x = max(0, self.x - n)
                    elif final == "r":
                        parts = [p for p in params.split(";") if p.isdigit()]
                        if len(parts) >= 2:
                            top, bot = int(parts[0]), int(parts[1])
                            self.st = max(0, min(self.rows - 1, top - 1))
                            self.sb = max(self.st, min(self.rows - 1, bot - 1))
                        else:
                            self.st, self.sb = 0, self.rows - 1
                        self.x, self.y = 0, self.st
                    elif final in "Hf":
                        row, col = (params.split(";") + ["1", "1"])[:2]
                        self.y = max(0, min(self.rows - 1, int(row or 1) - 1))
                        self.x = max(0, min(self.cols - 1, int(col or 1) - 1))
                    elif final == "K":
                        mode = params or "0"
                        if mode == "2":
                            self.grid[self.y] = [" "] * self.cols
                        elif mode == "0":
                            for cx in range(self.x, self.cols):
                                self.grid[self.y][cx] = " "
                        elif mode == "1":
                            for cx in range(0, min(self.x + 1, self.cols)):
                                self.grid[self.y][cx] = " "
                    elif final == "J":
                        mode = params or "0"
                        if mode in ("2", "3"):
                            self.grid = [[" "] * self.cols for _ in range(self.rows)]
                        elif mode == "0":
                            for cx in range(self.x, self.cols):
                                self.grid[self.y][cx] = " "
                            for ry in range(self.y + 1, self.rows):
                                self.grid[ry] = [" "] * self.cols
                        elif mode == "1":
                            for cx in range(0, min(self.x + 1, self.cols)):
                                self.grid[self.y][cx] = " "
                            for ry in range(0, self.y):
                                self.grid[ry] = [" "] * self.cols
                    i += m.end()
                    continue
                m2 = re.match(r"\x1b([78])", data[i:])
                if m2:
                    if m2.group(1) == "7":
                        self.saved = (self.x, self.y)
                    else:
                        self.x, self.y = self.saved
                    i += m2.end()
                    continue
                m3 = re.match(r"\x1b\][^\x07]*\x07", data[i:])
                if m3:
                    i += m3.end()
                    continue
                i += 1
                continue
            if ch in "\x00\x07\x0f":
                i += 1
                continue
            if ch == "\n":
                self.y += 1
                if self.y > self.sb:
                    self._scroll()
                    self.y = self.sb
                self.x = 0
            elif ch == "\r":
                self.x = 0
            elif ch == "\b":
                self.x = max(0, self.x - 1)
            elif ch == "\t":
                self.x = min(self.cols - 1, (self.x // 8 + 1) * 8)
            elif ord(ch) >= 32:
                self.put(ch)
            i += 1

    def dump(self):
        out = []
        for row in self.grid:
            out.append("|" + "".join(row).rstrip())
        return "\n".join(out)


def run(cols=COLS):
    home = tempfile.mkdtemp()
    cfg = pathlib.Path(home, ".docmind-single")
    cfg.mkdir(parents=True)
    cfg.joinpath("config.json").write_text(json.dumps({
        "language": "tr", "provider": "openai", "model": "gpt-4o-mini",
        "api_keys": {"openai": "sk-test"}, "setup_completed": True}), encoding="utf-8")
    pid, fd = pty.fork()
    if pid == 0:
        env = dict(HOME=home, COLUMNS=str(cols), LINES=str(ROWS), TERM="xterm-256color")
        if os.environ.get("PHONE") == "1":
            env["TERMUX_VERSION"] = "0.118"
        else:
            env["DOCMIND_DESKTOP"] = "1"
        os.environ.update(env)
        os.execv(sys.executable, [sys.executable,
                                  "/home/user/deliverables/docmind_aggressive_engine/DocMind.py"])
    import fcntl as _fcntl, struct as _struct, termios as _termios
    try:
        _fcntl.ioctl(fd, _termios.TIOCSWINSZ, _struct.pack("HHHH", ROWS, cols, 0, 0))
    except Exception:
        pass
    data = b""

    def pump(seconds):
        nonlocal data
        end = time.time() + seconds
        while time.time() < end:
            r, _, _ = select.select([fd], [], [], 0.1)
            if r:
                try:
                    data += os.read(fd, 65536)
                except OSError:
                    return

    pump(4)
    cmds = [os.environ.get("CMD1", "/mobil\n"), os.environ.get("CMD2", "/mobil status\n"), "/quit\n"]
    if os.environ.get("NOQUIT"):
        cmds = cmds[:-1]
    for cmd in cmds:
        if cmd:
            os.write(fd, cmd.encode())
            pump(1.6)
    try:
        os.kill(pid, 9)
    except Exception:
        pass
    text = data.decode("utf-8", "replace")
    text = re.sub(r"\x1b\[[0-9;?]*[hl]", "", text)      # private modes off
    text = re.sub(r"\x1b\[[0-9;]*m", "", text)          # colours off
    screen = Screen(cols, ROWS)
    screen.feed(text)
    print("=" * cols)
    print(screen.dump())
    print("=" * cols)
    print("characters overwritten (true overlap):", screen.overwrites)
    for ev in EVENTS:
        if ev[0] == "CTX":
            print("   CTX", ev[1])
        elif ev[0] == "POS":
            print("   POS", ev[1:])
        else:
            print("   overlap at row %d col %d: %r -> %r" % (ev[0], ev[1], ev[2], ev[3]))


run()
