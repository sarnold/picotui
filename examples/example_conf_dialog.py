from picotui.context import Context
from picotui.screen import Screen
from picotui.dialogs import *


with Context():
    width, height = Screen.screen_size()

    d = DConfirmation(
        (width - 70) // 2,
        (height - 22) // 2,
        69,
        20,
        lines="Hello\nBig\nAmazing\nWorld".splitlines(),
        title="Logs:",
        ok_txt="Happy :)",
        cl_txt="Sad :("
    )

    res = d.result()


print(res)
