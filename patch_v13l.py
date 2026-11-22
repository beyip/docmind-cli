"""patch_v13l.py — part 12: never use absolute cursor addressing on a phone.

The photo the user sent is the case that was still broken: a phone/tablet where
`/mobil` had *not* been typed yet (mobile mode OFF).  In that state the
full-screen footer was allowed, and the footer paints itself with absolute
coordinates (`ESC[<rows>;1H`, `ESC[1;<rows-1>r`, `ESC[2K`).  On a phone the
real number of rows changes all the time (the on-screen keyboard opens and
closes) and Termux does not always report it, so the footer wrote over the
messages -- `DocMind > |  Canzen: -0/1,048,576 (0.0%)` in the screenshot.

Fix: the "is a footer allowed here?" answer must look at the *hardware*, not at
the mobile-mode switch: a phone/tablet never gets the footer, mobile mode or
not.  Same for the restore-footer path in the repl.
"""
import io
import sys

path = sys.argv[1]
src = io.open(path, encoding="utf-8").read()
N = "\n"
edits = []


def sub_raw(old, new, label, count=1):
    global src
    n = src.count(old)
    assert n == count, "[%s] expected %d match(es), found %d" % (label, count, n)
    src = src.replace(old, new, count)
    edits.append(label)


# 1) Hardware test helper on TerminalView + predicate uses it.
sub_raw(
    '   def _footer_allowed(self) -> bool:' + N +
    '     """True only when a full-screen footer makes sense on this terminal.' + N,
    '   def _footer_allowed(self) -> bool:' + N +
    '     """True only when a full-screen footer makes sense on this terminal.' + N,
    "anchor-check")

sub_raw(
    '     if _DM_MOBILE_MODE:' + N +
    '       return False' + N +
    '     try:' + N +
    '       rows, cols = self._size()' + N +
    '     except Exception:' + N +
    '       return False' + N +
    '     return bool(self.ansi and rows >= 8 and cols >= 46)',
    '     # Hardware first: a phone/tablet never gets a footer, mobile mode or not.' + N +
    '     # The footer is drawn with absolute row numbers, and on a phone the real' + N +
    '     # height changes whenever the on-screen keyboard opens -- that made the' + N +
    '     # footer paint itself over the messages.' + N +
    '     if _DM_MOBILE_MODE or _DM_PHONE_DEVICE:' + N +
    '       return False' + N +
    '     try:' + N +
    '       rows, cols = self._size()' + N +
    '     except Exception:' + N +
    '       return False' + N +
    '     return bool(self.ansi and rows >= 12 and cols >= 46)',
    "footer-forbidden-on-phone-hardware")

# 2) The repl-wide "footer is active" cleanup must also fire on a phone.
sub_raw(
    '      if _DM_MOBILE_MODE and getattr(self.ui.view, "footer_active", False):',
    '      if (_DM_MOBILE_MODE or _DM_PHONE_DEVICE) and getattr(self.ui.view, "footer_active", False):',
    "repl-footer-cleanup-on-phone")

# 3) Nothing may draw the footer before the predicate is consulted: start_footer
#    reads the size *before* asking, so a phone got a scroll region in some paths.
sub_raw(
    '   def start_footer(self, status: Callable[[], str], compact: Optional[Callable[[int], str]] = None) -> bool:' + N +
    '     self._footer = status' + N +
    '     self._compact_footer = compact' + N +
    '     rows, cols = self._size()' + N +
    '     if not self._footer_allowed():' + N +
    '       return False',
    '   def start_footer(self, status: Callable[[], str], compact: Optional[Callable[[int], str]] = None) -> bool:' + N +
    '     self._footer = status' + N +
    '     self._compact_footer = compact' + N +
    '     if not self._footer_allowed():' + N +
    '       self._footer = None' + N +
    '       self._compact_footer = None' + N +
    '       return False' + N +
    '     rows, cols = self._size()',
    "start-footer-checks-before-resize")

# 4) On a phone the status row may only be rewritten in place, never repeated:
#    if anything has been printed since it was drawn, print nothing at all and
#    let the caller put it back at the end of the turn.
sub_raw(
    '     key = "\\n".join(rows)' + N +
    '     if key == getattr(self, "_inline_status_key", ""):' + N +
    '       return',
    '     key = "\\n".join(rows)' + N +
    '     if key == getattr(self, "_inline_status_key", ""):' + N +
    '       return' + N +
    '     if _DM_PHONE_DEVICE and getattr(self, "_inline_status_key", ""):' + N +
    '       # A phone cannot be trusted with cursor-up rewriting: leave the old row' + N +
    '       # alone and print the new one only on a clean line.' + N +
    '       self._ensure_line_start()',
    "phone-inline-status-line-start")

# 5) A row rewritten in place may only be rewritten by a terminal that did not
#    change size in between: on a phone the keyboard changes the height, and the
#    "move up one row" then lands on the user's own line.
sub_raw(
    '     writable = bool(getattr(self.view, "ansi", False))' + N +
    '     can_rewrite = (writable and self._inline_status_rows == len(rows)' + N +
    '                    and getattr(self, "_inline_status_live", False))',
    '     writable = bool(getattr(self.view, "ansi", False))' + N +
    '     try:' + N +
    '       now_size = self.view._size()' + N +
    '     except Exception:' + N +
    '       now_size = None' + N +
    '     if now_size is not None and now_size != getattr(self, "_inline_status_size", now_size):' + N +
    '       # The screen was resized (keyboard opened/closed): moving the cursor up' + N +
    '       # would now land on a different row.  Start a fresh row instead.' + N +
    '       self._inline_status_live = False' + N +
    '       self._inline_status_rows_drawn = 0' + N +
    '     self._inline_status_size = now_size' + N +
    '     can_rewrite = (writable and self._inline_status_rows == len(rows)' + N +
    '                    and getattr(self, "_inline_status_live", False))',
    "no-rewrite-after-resize")

io.open(path, "w", encoding="utf-8").write(src)
print("applied %d edits:" % len(edits))
for e in edits:
    print("  - " + e)
