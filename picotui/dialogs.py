from .widgets import *


def add_ok_cancel_buttons(d, ok_txt="OK", cl_txt="Cancel"):
    if d.h == 0:
        d.autosize(0, 1)
    if d.w < 20:
        d.w = 20
    hw = d.w // 2
    off1 = (hw + 1) // 2 - 4
    off2 = (d.w - hw) + hw // 2 - 4
    b = WButton(8, ok_txt)
    d.add(off1, d.h - 1, b)
    b.finish_dialog = ACTION_OK

    b = WButton(8, cl_txt)
    d.add(off2, d.h - 1, b)
    b.finish_dialog = ACTION_CANCEL


def add_next_prev_buttons(d, nxt_txt="Next", pre_txt="Back"):
    if d.h == 0:
        d.autosize(0, 1)
    if d.w < 20:
        d.w = 20
    hw = d.w // 2
    off1 = (hw + 1) // 2 - 4
    off2 = (d.w - hw) + hw // 2 - 4
    b = WButton(8, nxt_txt)
    d.add(off1, d.h - 1, b)
    b.finish_dialog = ACTION_NEXT

    b = WButton(8, pre_txt)
    d.add(off2, d.h - 1, b)
    b.finish_dialog = ACTION_PREV


class DTextEntry(Dialog):

    def __init__(self, entry_w, text, title=""):
        super().__init__(10, 5, title=title)
        self.entry = WTextEntry(entry_w, text)
        self.entry.finish_dialog = ACTION_OK
        self.add(1, 1, self.entry)

    def result(self):
        res = self.loop()
        if res == ACTION_OK:
            return self.entry.get()


class DMultiEntry(Dialog):

    def __init__(self, entry_w, entry_h, lines, title=""):
        super().__init__(10, 5, entry_w + 2, entry_h + 3, title=title)
        self.widget = WMultiEntry(entry_w, entry_h, lines)
        self.add(1, 1, self.widget)
        add_ok_cancel_buttons(self)

    def result(self):
        res = self.loop()
        if res == ACTION_CANCEL:
            return res
        return self.widget.content


class DConfirmation(Dialog):

    def __init__(self, x, y, entry_w, entry_h, lines, title="", ok_txt="OK", cl_txt="Cancel"):
        super().__init__(x, y, entry_w, entry_h, title=title)
        if not isinstance(lines, list):
            lines = [lines]
        i = 1
        for l in lines:
            self.add(2, i, WLabel(l))
            i += 1
        self.autosize(extra_w=1, extra_h=1)
        add_ok_cancel_buttons(self, ok_txt=ok_txt, cl_txt=cl_txt)

    def result(self):
        return self.loop()
