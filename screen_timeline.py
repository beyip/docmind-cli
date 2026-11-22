"""screen_timeline.py — replay a real pty session into a screen grid *step by step*.

Unlike `screen_check.py` (which feeds the whole capture at once), this keeps the
cursor/scroll state between writes and can dump the screen at any moment:

    COLS=64 ROWS=12 PHONE=1 CMD1=/mobil CMD2=/mobil python3 screen_timeline.py
    COLS=64 ROWS=12 ROWS_AFTER=24 ...        # simulate the keyboard opening
"""
import json
import os
import pathlib
import pty
import re
import select
import shutil
import struct
import sys
import tempfile
import termios
import time
import fcntl

COLS = int(os.environ.get("COLS", "64"))
ROWS = int(os.environ.get("ROWS", "12"))
BIN = os.environ.get("BIN", "/home/user/deliverables/docmind_aggressive_engine/DocMind.py")


class Screen:
    def __init__(self, cols, rows):
        self.cols, self.rows = cols, rows
        self.grid = [[" "] * cols for _ in range(rows)]
        self.x = self.y = 0
        self.saved = (0, 0)
        self.st, self.sb = 0, rows - 1
        self.overwrites = 0
        self.log = []

    def _blank(self):
        return [" "] * self.cols

    def _scroll(self):
        self.grid.pop(self.st)
        self.grid.insert(self.sb, self._blank())

    def put(self, ch):
        if self.x >= self.cols:
            self.x = 0
            if self.y < self.sb:
                self.y += 1
            else:
                self._scroll()
            if self.y >= self.rows:
                self.y = self.rows - 1
        if self.y >= self.rows:
            self.y = self.rows - 1
        cell = self.grid[self.y][self.x]
        if cell != " " and ch != " ":
            self.overwrites += 1
            if len(self.log) < 40:
                self.log.append((self.y, self.x, "".join(self.grid[self.y]).rstrip()[:50], ch))
            if os.environ.get("TRACE") and len(self.log) < 40:
                ctx = self._data[max(0, self._off - 260): self._off + 1]
                print("CTX:", repr(ctx))
        self.grid[self.y][self.x] = ch
        self.x += 1

    def feed(self, data):
        data = getattr(self, "_tail", "") + data
        self._tail = data[-400:]
        self._data = data
        i = 0
        while i < len(data):
            self._off = i
            ch = data[i]
            if ch == "\x1b":
                m = re.match(r"\x1b\[([0-9;?]*)([A-Za-z])", data[i:])
                if m:
                    params, final = m.group(1), m.group(2)
                    nums = [p for p in params.replace("?", "").split(";") if p.isdigit()]
                    n = int(nums[0]) if nums else 1
                    if final == "A":
                        self.y = max(self.st, self.y - n)
                    elif final == "B":
                        self.y = min(self.sb if self.sb else self.rows - 1, self.y + n)
                    elif final == "C":
                        self.x = min(self.cols - 1, self.x + n)
                    elif final == "D":
                        self.x = max(0, self.x - n)
                    elif final == "G":
                        self.x = max(0, min(self.cols - 1, n - 1))
                    elif final in "Hf":
                        r = int(nums[0]) - 1 if len(nums) >= 1 else 0
                        c = int(nums[1]) - 1 if len(nums) >= 2 else 0
                        self.y = max(0, min(self.rows - 1, r))
                        self.x = max(0, min(self.cols - 1, c))
                    elif final == "r":
                        if len(nums) >= 2:
                            self.st = max(0, min(self.rows - 1, int(nums[0]) - 1))
                            self.sb = max(self.st, min(self.rows - 1, int(nums[1]) - 1))
                        else:
                            self.st, self.sb = 0, self.rows - 1
                        self.x, self.y = 0, self.st
                    elif final == "K":
                        mode = nums[0] if nums else 0
                        if mode == 2:
                            self.grid[self.y] = self._blank()
                        elif mode == 0:
                            for cx in range(self.x, self.cols):
                                self.grid[self.y][cx] = " "
                        elif mode == 1:
                            for cx in range(0, min(self.x + 1, self.cols)):
                                self.grid[self.y][cx] = " "
                    elif final == "J":
                        mode = nums[0] if nums else 0
                        if mode in (2, 3):
                            self.grid = [self._blank() for _ in range(self.rows)]
                        elif mode == 0:
                            for cx in range(self.x, self.cols):
                                self.grid[self.y][cx] = " "
                            for ry in range(self.y + 1, self.rows):
                                self.grid[ry] = self._blank()
                        elif mode == 1:
                            for cx in range(0, min(self.x + 1, self.cols)):
                                self.grid[self.y][cx] = " "
                            for ry in range(0, self.y):
                                self.grid[ry] = self._blank()
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
                m3 = re.match(r"\x1b\][^\x07]*(\x07|\x1b\\)", data[i:])
                if m3:
                    i += m3.end()
                    continue
                m4 = re.match(r"\x1b[()][A-Za-z0-9]", data[i:])
                if m4:
                    i += m4.end()
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
        return "\n".join("|" + "".join(r).rstrip() for r in self.grid)


def run():
    home = tempfile.mkdtemp()
    cfg = pathlib.Path(home, ".docmind-single")
    cfg.mkdir(parents=True)
    cfg.joinpath("config.json").write_text(json.dumps({
        "language": "en", "provider": "openai", "model": "gpt-4o-mini",
        "api_keys": {"openai": "sk-test"}, "setup_completed": True}), encoding="utf-8")
    rows_now = [ROWS]
    shutil.copy("/home/user/deliverables/docmind_aggressive_engine/DocMind.py", "/tmp/tl_docmind.py")
    pid, fd = pty.fork()
    if pid == 0:
        env = dict(HOME=home, COLUMNS=str(COLS), LINES=str(ROWS), TERM="xterm-256color",
                   PATH=os.environ.get("PATH", ""))
        if os.environ.get("PHONE") == "1":
            env["TERMUX_VERSION"] = "0.118"
        else:
            env["DOCMIND_DESKTOP"] = "1"
        os.execvpe(sys.executable, [sys.executable, BIN], env)

    def setsize(r):
        fcntl.ioctl(fd, termios.TIOCSWINSZ, struct.pack("HHHH", r, COLS, 0, 0))

    setsize(rows_now[0])
    buf = []
    screen = Screen(COLS, rows_now[0])

    def pump(seconds):
        end = time.time() + seconds
        while time.time() < end:
            r, _, _ = select.select([fd], [], [], 0.05)
            if r:
                try:
                    chunk = os.read(fd, 65536)
                except OSError:
                    return
                if not chunk:
                    return
                buf.append(chunk)
                if os.environ.get("PERCHUNK"):
                    d = re.sub(r"\x1b\[[0-9;?]*[hl]", "", chunk.decode("utf-8", "replace"))
                    print("--CHUNK--", repr(d[:220]))
                    if os.environ.get("STEP"):
                        sc = Screen(COLS, rows_now[0])
                        sc.grid = [r[:] for r in screen.grid]
                        sc.x, sc.y, sc.saved, sc.st, sc.sb = screen.x, screen.y, screen.saved, screen.st, screen.sb
                        sc.feed(d)
                        print(sc.dump().split("\n")[-6:])

    def drain():
        """Feed everything received so far into the screen."""
        data = b"".join(buf).decode("utf-8", "replace")
        buf.clear()
        data = re.sub(r"\x1b\[[0-9;?]*[hl]", "", data)
        screen.feed(data)

    pump(4 if not os.environ.get("FAST") else 2.5)
    drain()
    print("### after start (%dx%d)" % (COLS, rows_now[0]))
    print(screen.dump())
    for cmd in [c for c in (os.environ.get("CMD1"), os.environ.get("CMD2")) if c]:
        os.write(fd, (cmd + "\n").encode())
        pump(1.4)
        drain()
        print("### after %r" % cmd)
        print(screen.dump())
    if os.environ.get("RESIZE"):
        new = int(os.environ["RESIZE"])
        rows_now[0] = new
        setsize(new)
        try:
            old_rows = len(screen.grid)
            if new > old_rows:
                screen.grid = screen.grid + [[" "] * COLS for _ in range(new - old_rows)]
            else:
                # xterm drops lines from the top so the cursor stays on screen.
                shift = max(0, screen.y - (new - 1))
                screen.grid = screen.grid[shift:shift + new]
                screen.y -= shift
            screen.rows = new
            screen.sb = new - 1
            screen.st = 0
        except Exception:
            pass
        pump(1.5)
        drain()
        print("### after resize to %dx%d" % (COLS, new))
        print(screen.dump())
    os.write(fd, b"/quit\n")
    pump(1.2)
    drain()
    os.write(fd, b"/hlp\n")
    pump(1.2)
    drain()
    print("### after /hlp (typo -> suggestions)")
    print(screen.dump())
    print("### final")
    print(screen.dump())
    print("characters overwritten (true overlap):", screen.overwrites)
    for ev in screen.log[:12]:
        print("   overlap at row %d col %d: %r -> %r" % ev)
    try:
        os.kill(pid, 9)
    except Exception:
        pass


run()
