Changelog
=========


v1.2.3.1 (2025-07-21)
---------------------

Fixes
~~~~~
- Restore missing metadata bits, update changelog. [Stephen L Arnold]


v1.2.3 (2025-07-18)
-------------------

Changes
~~~~~~~
- Move metadata to setup.cfg, cleanup coverage bits. [Stephen L Arnold]
- Add docs build to needs for release job. [Stephen L Arnold]


v1.2.2 (2025-06-03)
-------------------

Changes
~~~~~~~
- Cleanup docs config and sphinx deps, add diagram workflow. [Stephen L
  Arnold]
- Allow passing button text in DConf and bg color in WButton. [Stephen L
  Arnold]

  * give buttons a name attribute equal to their lowercase text
  * add example_conf_dialog to examples, cleanup project/workflow files

Fixes
~~~~~
- Use correct coverage percent label on badge. [Stephen L Arnold]

  * add missing docs build to release workflow
  * add .gitchangelog.rc and link changelog to docs build


v1.2.1.1 (2025-06-03)
---------------------

New
~~~
- Add reuse config and cleanup readme badges. [Stephen L Arnold]

  * make LICENSE file a symlink to license text
- Add a simple WProgress widget class. [Stephen Arnold]
- Add input text validation to WLabel widget class. [Stephen Arnold]

  * this adds colors for valid/invalid text when .validate is True
- Add the obligatory workflows and a conda recipe. [Stephen L Arnold]

  * remove superfluous not-an-example file

Changes
~~~~~~~
- Use coverage run for unittests for now. [Stephen L Arnold]

  * picotui test fails with pytest when the shell is not interactive
- Button and confirmation dialog feature/fixes. [Stephen Arnold]

  * add next/prev button function
  * add size params to DConfirmation Dialog class
- Use deprecated format of license string for conda compatibility.
  [Stephen L Arnold]

  * this should hopefully be temporary until toml deps are supported [1],[2]
  * add conda-remove-defaults setting to miniconda setup

  [1] https://github.com/conda/conda/issues/10633
  [2] https://github.com/conda/conda-build/issues/5666
- Cleanup workflow branch cruft, update .gitignore. [Stephen L Arnold]
- Add some badging for github status and project metadata. [Stephen L
  Arnold]
- Remove windows from matrix workflows. [Stephen L Arnold]
- Add basic sphinx autoapi docs build with tox cmds and workflow.
  [Stephen L Arnold]

  * move widgets doc to docs/source, switch pytest to capture=no
  * cleanup coverage bits
- Add a tox file, cleanup tests, move examples to examples. [Stephen L
  Arnold]

  * pytest capture should be off for current widgets test or it will
    raise a termios exception
  * also allow asserts in tool.bandit config
- Migrate packaging to pyproject.toml, leave setup.py stub. [Stephen L
  Arnold]

Fixes
~~~~~
- Use correct project path in bandit workflow. [Stephen L Arnold]

  * cleanup coverage bits, stop tests from leaking
- Check explicitly if termios file descriptor is a tty. [Stephen L
  Arnold]

  * fixes annoying CI failures in non-interactive shell and does not
    seem to break anything else
- Apply bytes-not-strings correction for newer python. [Stephen L
  Arnold]
- Revert python matrix in conda workflow. [Stephen L Arnold]
- Use new pty slave to handle ioctl errors in termios. [Stephen L
  Arnold]

Other
~~~~~
- Revert "fix: dev: use new pty slave to handle ioctl errors in termios"
  [Stephen L Arnold]

  This reverts commit 88562eeb0190f49597a8dfa75886bb74dabdb607.
- Example_widgets: Add WPasswdEntry example. [simejo]
- Widgets: Added WPasswdEntry widget. [simejo]


v1.2.1 (2021-07-11)
-------------------
- Setup.py: Release 1.2.1. [Paul Sokolovsky]
- Example_menu: Show hint about pressing F9 to access menu. [Paul
  Sokolovsky]

  And also relayout the dialog correspondingly.
- Menu: WMenuBar: In case of permanent menubar, redraw screen, then draw
  menu. [Paul Sokolovsky]

  And not vice-versa, like was before (so menu bar was actually drawn over).


v1.2 (2021-02-04)
-----------------
- Setup.py: Release 1.2. [Paul Sokolovsky]
- Basewidget: Widget.get_input: Process only presses of 1st mouse
  button. [Paul Sokolovsky]

  In the "normal Xterm tracking mode", both button presses and releases are
  reported. We act only on presses on 1st button, without any key modifiers.
- Basewidget: Widget.loop: Allow get_input() to return None to skip
  processing. [Paul Sokolovsky]
- Screen: Use "normal" Xterm mouse mode, instead of "X10 compat" mode.
  [Paul Sokolovsky]

  Turns out, "X10 compatability mode" is a niche legacy mode, which isn't
  even implemented by some terminal emulators, e.g. KDE Konsole.

  Reference for different mouse modes:
  https://www.x.org/docs/xterm/ctlseqs.pdf


v1.1.2 (2021-01-15)
-------------------
- Setup.py: Release 1.1.2. [Paul Sokolovsky]
- Example_widgets: Add a long choice for combobox. [Paul Sokolovsky]

  To make sure it's handled correctly.
- LICENSE: Update copyright years. [Paul Sokolovsky]
- Widgets: WComboBox: After selection from dropdown, reset textentry
  margin. [Paul Sokolovsky]

  Avoids artifacts when textentry contain a long string, scrolled out to the
  left.


v1.1.1 (2020-12-28)
-------------------
- Setup.py: Release 1.1.1. [Paul Sokolovsky]
- Defs: More codes for Home/End keys. [Paul Sokolovsky]


v1.1 (2020-11-06)
-----------------
- Setup.py: Release 1.1. [Paul Sokolovsky]
- Widgets: WDropDown: When opening dropdown, highlight current item.
  [Paul Sokolovsky]

  Previosuly, first item in popup was selected, instead of current.
- Examples/example_filter_listbox: Simplify example. [Paul Sokolovsky]

  Use WListBox.set_items(), and remove use of extra global vars and identity
  list comprehensions (which apparently were inherited from more complex
  examples, but not needed here).
- Widgets: WListBox: Add set_items() method. [Paul Sokolovsky]

  Abstracts away the need to both set .items and call set_lines() of
  EditorExt.
- Examples/README: Typo fix. [Paul Sokolovsky]
- Tests: Add test for rendering WListBox in case of non-str content.
  [tau3]
- Editor: Don't adjust margin for line length unless really needed.
  [Paul Sokolovsky]

  Don't try to access self.content[self.cur_line] to adjust off-screen left
  margin, if this margin is anyway 0. This in particular fixes (well, works
  around) rendering of subclassed widgets where self.content contains
  non-str objects.
- Docs: widgets.txt: Capture some doc on widget hierarchy. [Paul
  Sokolovsky]


v1.0.2 (2019-08-13)
-------------------
- Setup.py: Release 1.0.2, cleaned up stray files from distro. [Paul
  Sokolovsky]
- Examples/example_on_changed: Import defs. [Paul Sokolovsky]

  Got lost after cleaning up imports in the main package.
- Examples/example_filter_listbox: Clean up imports, import defs. [Paul
  Sokolovsky]


v1.0.1 (2019-07-23)
-------------------
- Setup.py: Release 1.0.1. [Paul Sokolovsky]
- README: Update for Pycopy project. [Paul Sokolovsky]


1.0.0-rc3 (2019-05-31)
----------------------
- Picotui/widgets.py: fix missing class name (something got lost
  somewhere) [Stephen Arnold]


1.0.0-rc2 (2019-05-28)
----------------------
- Picotui/widgets.py: add simple WProgress widget class. [Stephen
  Arnold]


1.0.0-rc1 (2019-05-22)
----------------------
- Setup.py: semver fix for actual 1.0.0 release. [Stephen Arnold]
- Widgets.py: add input text validation to WLabel widget class. [Stephen
  Arnold]

  * this adds colors for valid/invalid text when .validate is True
- Dialogs.py: button and confirmation dialog feature/fixes. [Stephen
  Arnold]

  * add next/prev button function
  * add size params to DConfirmation Dialog class
- Examples: fix a couple of missing (self) imports. [Stephen Arnold]


v1.0 (2018-02-17)
-----------------
- Setup: Release 1.0. [Paul Sokolovsky]
- Context: Print newline on de-initialization. [Paul Sokolovsky]

  To make sure entire screenful is scrolled up and console output starts
  on fresh line.
- Example_widgets: Convert to use Context. [Paul Sokolovsky]
- Examples/example_widgets_no_context: Copy of current example_widgets.
  [Paul Sokolovsky]

  The idea to convert the latter to Context.
- Examples/example_serialize: Tighten up imports. [Paul Sokolovsky]
- Example_widgets: Tighten up imports. [Paul Sokolovsky]
- Picotui: Tighten up imports. [Paul Sokolovsky]

  Limit use of "import \*", in few cases avoid re-exports.
- Widgets: Use __all__ to limit name re-export. [Paul Sokolovsky]

  First of all, we want to avoid defs.* leaking.
- Examples/example_on_changed: Switch to Context. [Paul Sokolovsky]
- Examples/example_serialize: Example for "serializing" dialog results.
  [Paul Sokolovsky]
- Example_widgets: Remove stale comment. [Paul Sokolovsky]
- Widgets: WMultiEntry: Implement set(). [Paul Sokolovsky]
- Widgets: WMultiEntry: Implement get(). [Paul Sokolovsky]

  Returns a list of lines in the wiget().
- Picotui: Add __init__.py package file. [Paul Sokolovsky]

  The original idea was to use "namespace package" which doesn't require
  __init__.py. But namespace packages used in distribution packages have
  various artifacts:
  https://packaging.python.org/guides/packaging-namespace-packages/#creating-a-namespace-package

  Given that "picotui" is a real package (not just a namespace for disparate
  modules), make it such by adding __init__.py.
- Widgets: WTextEntry: Rename get_text() -> get(). [Paul Sokolovsky]

  To comply with EditableWidget interface.

  Also, rename set_text() -> set().
- Widgets: WCompletionList: Use w.choice to access WCheckbox value.
  [Paul Sokolovsky]
- Basewidget: Add get() method to EditableWidget interface. [Paul
  Sokolovsky]

  And implement for ChoiceWidget.
- Widgets: Inherit from FocusableWidget and EditableWidget as required.
  [Paul Sokolovsky]

  .focusable class property is removed, isinstance(w, FocusableWidget) now
  used instead.
- Widgets: Sort WLabel and WFrame together. [Paul Sokolovsky]

  As non-focusable widgets.
- Basewidget: Introduce FocusableWidget and EditableWidget base classes.
  [Paul Sokolovsky]

  ChoiceWidget inherits from EditableWidget.
- Examples/example_on_changed: Update for ChoiceWidget refactor. [Paul
  Sokolovsky]

  Now all ChoiceWidget subclasses consistently provide widget value as
  w.choice.
- Menu: Comply with ChoiceWidget interface. [Paul Sokolovsky]
- Widgets: WRadioButton: Comply with ChoiceWidget interface. [Paul
  Sokolovsky]
- Basewidget: ItemSelWidget: Inherit from ChoiceWidget. [Paul
  Sokolovsky]
- Widgets: WDropDown: Inherit from ChoiceWidget. [Paul Sokolovsky]
- Widgets: WListBox: Inherit from and comply to ChoiceWidget. [Paul
  Sokolovsky]
- Editor: Explicitly call Widget constructor. [Paul Sokolovsky]

  To not play tricks will multiple inheritance diamond patterns.
- Widgets: WCheckbox: Inherit from ChoiceWidget. [Paul Sokolovsky]

  Thus, value is now stored in self.choice.
- Basewidget: Introduce ChoiceWidget abstract base class. [Paul
  Sokolovsky]
- Examples/example_screen_resize: Handling screen resizing. [Paul
  Sokolovsky]
- Screen: Add set_screen_resize() method. [Paul Sokolovsky]

  Sets a callback to run on terminal resize. Implemented using OS
  SIGWINCH signal, and thus won't work in a general case (e.g. over
  a serial connection).

  Also, picotui stores absolute coordinates for each widget, so, to
  handle resizing, all dialogs, etc. should be recreated from scratch
  with new size.
- README: Grammar/articles/clarifications. [Paul Sokolovsky]


v0.9.4 (2017-12-25)
-------------------
- Setup.py: Release 0.9.4. [Paul Sokolovsky]
- Basewidget: get_input: Work around incorrect UTF-8 partitioning. [Paul
  Sokolovsky]

  To get a complete UTF-8 char, convert terminal input from bytes to str,
  then back again.

  This is not ideal, but the whole terminal input handling needs to be
  reworked later anyway.
- Examples/example_filter_listbox: Example for dynamic changing listbox
  items. [Peter J. Schroeder]

  This example re-fills ListBox based on "changed" events of a DropDown.
- README: Update "examples" section. [Paul Sokolovsky]


v0.9.3 (2017-12-09)
-------------------
- Setup.py: Release 0.9.3. [Paul Sokolovsky]
- *_demo.py: Rename to example_*.py to sort together. [Paul Sokolovsky]
- README: Typos/punctuation/articles. [Paul Sokolovsky]
- Defs: Move color and key constants from screen.py. [Paul Sokolovsky]
- Symbols: Rename to defs, to host other constants too. [Paul
  Sokolovsky]
- Examples/README: Add examples dir README. [Paul Sokolovsky]
- Examples/example_on_changed: Add WListBox to the example. [Paul
  Sokolovsky]
- Widgets: WListBox: Emit "changed" events. [Peter J. Schroeder]
- Widgets_demo: Update for WButton "click" event instead of on_click()
  method. [Paul Sokolovsky]
- Widgets: WButton: Emit "click" event instead of calling on_click().
  [Paul Sokolovsky]

  Using adhoc on_click() method was a thinko, everything was supposed to be
  based on event handlers.


v0.9.2 (2017-11-24)
-------------------
- Setup.py: Release 0.9.2. [Paul Sokolovsky]
- README: Add "Documentation" and "Examples" sections. [Paul Sokolovsky]
- Example/example_on_changed: Add example for "changed" events. [Paul
  Sokolovsky]
- Widgets: WLabel: Allow to specify width. [Paul Sokolovsky]

  Useful when label text is dynamically changed, leftover characters will
  be cleared. By default, the width is set to the length of the initial
  value.
- Widgets: WRadioButton: Emit "changed" event on mouse interaction.
  [Paul Sokolovsky]

  Keyboard case is handled in ItemSelWidget base class.
- Basewidget: ItemSelWidget.move_sel: Emit "changed" signal. [Paul
  Sokolovsky]

  This should cover all subclasses, e.g WRadioButton.
- Widgets: WDropDown: Emit "changed" event. [Paul Sokolovsky]
- Widgets: WDropDown: Use Unicode down arrow symbol for dropdown. [Paul
  Sokolovsky]

  Instead of "v" symbol used before.
- Widgets: WDropDown: Allow to override dropdown height. [Paul
  Sokolovsky]
- Menu: Make selected item bold white. [Jonathan Neuschäfer]

  On some terminals (notably Linux's builtin virtual terminal), C_WHITE is
  indistinguishable from the default color, making it hard or impossible
  to see which item is selected.


v0.9.1 (2017-05-22)
-------------------
- Setup.py: Release 0.9.1. [Paul Sokolovsky]
- Widgets: WRadioButton: Inherit from ItemSelWidget. [Paul Sokolovsky]
- Basewidget: Move ItemSelWidget from menu.py, for reuse. [Paul
  Sokolovsky]
- Menu: ItemSelWidget: Rename move_focus() to move_sel(). [Paul
  Sokolovsky]

  We use term "focus" to designate currently selected widget. So, avoid
  reusing it for internal widget items, instead consistently use term
  "selection".
- Widgets: WRadioButton: Arrows change choice. [Kyle Perik]
- Widgets: WTextEntry: Add set_text() for symmetry with get_text().
  [Paul Sokolovsky]


v0.9 (2017-02-17)
-----------------
- Editorext: Add CharColorViewer widget. [Paul Sokolovsky]

  Viewer with color support, (echo line may consist of spans
  of different colors).
- Editorext: Add LineColorViewer widget. [Paul Sokolovsky]

  Viewer with colored lines, (whole line same color).
- Dialogs: add_ok_cancel_buttons: Automaticlaly autosize dialog if
  needed. [Paul Sokolovsky]
- Dialogs: Add confirmation (OK/Cancel) dialog. [Paul Sokolovsky]
- Menu: Improve cursor control. [Paul Sokolovsky]

  If menu is focused, cursor is disabled. When it closes, it signals main
  screen that it can reposition and enable cursor if needed.
- Screen: attr_color: Fix rendering of non-bright colors after bright.
  [Paul Sokolovsky]
- Screen: Make color names terse. Now prefixes are C_ and C_B_. [Paul
  Sokolovsky]

  Old names are long and unwieldy. Color name alone should be enough to make
  clear it's a color, but use prefixes for consistency and namespacing. "B"
  for bright is perhaps not immediately obvious, but a second though or look
  at the code can clear it up.
- Screen: attr_color: Allow to pass a single color pair argument. [Paul
  Sokolovsky]

  It's impractical to make all color users to pass/store 2 values, let's
  make it one value.
- Widgets: WButton: Use Left/Right for prev/next widget (besides
  Up/Down). [Paul Sokolovsky]

  This is convenient and expected in small dialogs.
- Widgets_demo: Show callback-executing buttons in addition to dialog
  ones. [Paul Sokolovsky]
- Widgets: WButton: Act only on Enter, for consistency with dialog
  buttons. [Paul Sokolovsky]

  Dialog finishing buttons work as generic dialog finishing widgets, and such
  can't be activated by Space (e.g. a line editing widget). So, be consistent
  and use just Enter for activation.
- Widgets: WButton: Pressing Space or Enter will activate a button.
  [Kyle Perik]


v0.8.2 (2016-10-07)
-------------------
- Setup.py: Release 0.8.2. [Paul Sokolovsky]
- Picotui/menu: WMenuBox: Support dropdown menu item selection with
  mouse. [Paul Sokolovsky]


v0.8.1 (2016-09-03)
-------------------
- Setup.py: Release 0.8.1. [Paul Sokolovsky]
- Widgets: WListBox: Handle show_line("", -1) call to clear empty lines.
  [Paul Sokolovsky]


v0.8 (2016-08-25)
-----------------
- Setup.py: Release 0.8. [Paul Sokolovsky]
- Menu_demo: Menu and application main loop demo. [Paul Sokolovsky]
- Dialogs_demo: Demo app to show off standard dialogs and context
  manager. [Paul Sokolovsky]
- Menu: Menu widgets (horizontal menu bar and vertical menu). [Paul
  Sokolovsky]
- Screen: Add set_screen_redraw() class method. [Paul Sokolovsky]

  Sets a function which can redraw entire screen background, to restore its
  state.
- Widgets: Dialog: Init some internal state on 1st call to redraw().
  [Paul Sokolovsky]

  Instead of in overriden loop(). Generally, avoid overriding loop()
  (there's no guarantee it will be called, input handling is done with
  handle_input()).
- Widgets: Dialog: Initialize .focus_w/.focus_idx. [Paul Sokolovsky]
- Context: Simple context manager to initialize picotui screen. [Paul
  Sokolovsky]
- Widgets: Dialog.autosize: Allow to reserve extra space at
  right/bottom. [Paul Sokolovsky]
- Dialogs: Implement DTextEntry dialog for single-line text entry. [Paul
  Sokolovsky]
- Dialog: New module for standard dialogs, starts with DMultiEntry.
  [Paul Sokolovsky]
- Widgets_demo.py: Disable console mouse support on exit. [Paul
  Sokolovsky]
- Setup.py: Add check for Python 3+. [Paul Sokolovsky]
- README: Explicitly mention Python3 requirement. [Paul Sokolovsky]


v0.7 (2016-08-18)
-----------------
- Setup.py: Release 0.7. [Paul Sokolovsky]
- README: Articles. [Paul Sokolovsky]
- README: Add screenshot. [Paul Sokolovsky]
- README: reST formatting. [Paul Sokolovsky]
- README: Rename to README.rst. [Paul Sokolovsky]
- Picotui.png: Screenshot of widgets_demo.py. [Paul Sokolovsky]
- Widgets_demo.py: Rework from older widgets_test.py. [Paul Sokolovsky]

  Now tries to show each widget in action.
- Widgets_test: Add WMultiEntry example. [Paul Sokolovsky]
- Editor: redraw(): Call .show_line() for empty surplus lines too. [Paul
  Sokolovsky]

  Instead of calling .clear_num_pos() derectly. Screen attribute overriding
  usually happens in .show_line(), so allows it to apply to surplus lines
  too. It's called as .show_line("", -1), so most of existing .show_line()
  overrides work without changes.
- Widgets: Add WMultiEntry widget (edit multiple lines of text). [Paul
  Sokolovsky]
- Widgets: Dialog.add: Allow to add raw string (convert to WLabel).
  [Paul Sokolovsky]
- Editorext: Add optional column param to goto_line() method. [Paul
  Sokolovsky]
- Screen: Add disable_mouse() call. [Paul Sokolovsky]

  Also, refactor enable_mouse().
- Widgets: WButton: Return self.finish_dialog on mouse click. [Paul
  Sokolovsky]

  For consistency with Enter key handling. (But Enter key handling happens
  in common dialog code. TODO: Make this consistent?)
- Widgets_test.py: Put cursor at the bottom of screen on exit. [Paul
  Sokolovsky]
- Basewidget: Parse mouse input in get_input(); factor handle_input()
  from loop(). [Paul Sokolovsky]


v0.6 (2016-08-15)
-----------------
- Setup.py: Release 0.6. [Paul Sokolovsky]
- Screen: Move screen_size() from editorext. [Paul Sokolovsky]
- Screen: Change argument order for goto() to be goto(x, y). [Paul
  Sokolovsky]

  For consistency with all other calls - we use standard X/Y coordinates.
- Screen: Add F2-F10 keys. [Paul Sokolovsky]
- Screen: Make KEY_ESC, KEY_F1 generally available. [Paul Sokolovsky]


v0.5 (2016-06-27)
-----------------
- Setup.py: Add, for publishing to PyPI. [Paul Sokolovsky]
- LICENSE: Add MIT license. [Paul Sokolovsky]
- Picotui/editorext: Missed case of update_screen() -> redraw() rename.
  [Paul Sokolovsky]
- Picotui: Introduce proper python package subdir. [Paul Sokolovsky]
- Widgets_test.py: Remove reference to not available .menu. [Paul
  Sokolovsky]
- README: Add manifesto in the form of Q&A session. [Paul Sokolovsky]
- Widgets_test.py: Example of widget usage. [Paul Sokolovsky]
- Widgets: WDropDown: Add handle_key(). [Paul Sokolovsky]
- Widgets: WComboBox: Allow to override popup height. [Paul Sokolovsky]
- Widgets: WListBox: Add render_line() to let override item rendering.
  [Paul Sokolovsky]
- Widgets: WComboBox: make popup_class a class property. [Paul
  Sokolovsky]
- Widgets: finish_dialog is now standard property for all widgets. [Paul
  Sokolovsky]

  And is handled by Dialog.loop() for case of pressing Enter, though
  apparently mouse handling should be widget-specific (as single mouse
  click usually selects widget).
- Widgets: Dialog: By default, Esc finishes dialog, but can be
  overriden. [Paul Sokolovsky]
- Widgets: Dialog: Allow to specify title. [Paul Sokolovsky]
- Editor: If there're no lines at all, don't try to handle cursor keys.
  [Paul Sokolovsky]

  Useful for list widgets.
- Widgets: WCompletionList: On prefix/substr change, reinit list
  completely. [Paul Sokolovsky]
- All: Use relative imports. [Paul Sokolovsky]

  Use https://github.com/pfalcon/py-runinpkg to run scripts inside package
  directory.
- Screen: Stay <py3.5 compatible by not using % against b"...". [Paul
  Sokolovsky]
- Editorext: Viewer: Call superclass method. [Paul Sokolovsky]
- Widgets: WListBox: Force cursor off, should be final. [Paul
  Sokolovsky]
- Editor: Make sure that ste_cursor() enables cursor. [Paul Sokolovsky]

  This is needed per focused widget protocol.
- Widgets: find_focusable_by_xy(): Return (None, None) if not found.
  [Paul Sokolovsky]
- Widgets: WPopupList: Close popup only if selection was actually made.
  [Paul Sokolovsky]

  I.e. when mosy click selected an item (not on empty space).
- Editor: handle_mouse(): Return True if event successfully processed.
  [Paul Sokolovsky]
- Basewidget: Event handler may return True to signify it processed
  event. [Paul Sokolovsky]
- Editor: handle_mouse(): Process click only if falls on existing line.
  [Paul Sokolovsky]
- README: Start, blame Ubuntu for bad Unicode font. [Paul Sokolovsky]
- Widgets: WComboBox: Handle mouse click on dropdown arrow. [Paul
  Sokolovsky]
- Widgets: WComboBox: Show a dropwdown arrow symbol by the field. [Paul
  Sokolovsky]
- Symbols: A file with various Unicode graphical symbols. [Paul
  Sokolovsky]
- Widgets: WAutoComplete: Allow to complete by prefix or substring.
  [Paul Sokolovsky]

  Mode changed by a checkbox shown in dropdown. Default is substring, like
  before.
- Widgets: WComboBox: Standardize on Down key to open popups. [Paul
  Sokolovsky]

  This will be used or completion too for example.
- Widgets: WComboBox: Allow to override widget used for popup. [Paul
  Sokolovsky]
- Widgets: WCheckbox: Send "changed" signal. [Paul Sokolovsky]
- Widgets: WTextEntry: Add get_text() method to get widget value. [Paul
  Sokolovsky]
- Widgets: WPopupList: Handle empty list properly. [Paul Sokolovsky]
- Widgets: WListBox: Need to disable cursor explicitly after all. [Paul
  Sokolovsky]
- Editor: Make adjust_cursor_eol() behave in case of empty widget
  content. [Paul Sokolovsky]

  This may happen e.g. when subclassing as list widget, where 0 items are
  pretty legitimate.
- Basewidget: Add basic support for event signals. [Paul Sokolovsky]
- Basewidget: longest(): return 0 in case of empty list. [Paul
  Sokolovsky]
- Widgets: Dialog: Properly update focus index for mouse navigation.
  [Paul Sokolovsky]
- Widgets: WTextEntry: Properly handle initial Backspace. [Paul
  Sokolovsky]

  Delete is handled in special manner automagically: remove all of old
  content.
- Widgets: WCheckbox: Allow to specify state, default unchecked. [Paul
  Sokolovsky]
- Widgets: Dialog: Make sure dialog is large enough to accommodate all
  widgets. [Paul Sokolovsky]
- Widgets: Add WAutoComplete widget. [Paul Sokolovsky]

  Like WComboBox, but shows not just static items in dropdown, but filters
  them based on text entry contents.
- Widgets: Add WComboBox widget. [Paul Sokolovsky]

  Text entry + drop down list.
- Basewidget: Add longest() helper method. [Paul Sokolovsky]

  Return length of the longest item in sequence.
- Widgets: WTextEntry: Reset just_started status on mouse click. [Paul
  Sokolovsky]
- Editor: Switch to standard widget .x & .y properties. [Paul
  Sokolovsky]
- Editorext: Update imports. [Paul Sokolovsky]
- Widgets: Add WTextEntry widget. [Paul Sokolovsky]
- Widgets: Rework text cursor handling. [Paul Sokolovsky]

  A currently focused widget has ability to control text cursor. Most widgets
  just have it off.
- Widgets: Add "focused" visual distinction for all focusable widgets.
  [Paul Sokolovsky]
- Widgets: Add key handler for all focusable widgets. [Paul Sokolovsky]
- Widgets: WButton: Allow to specify explicit width. [Paul Sokolovsky]

  To make different buttons have teh same width.
- Widgets: Dialog: implementing switching input focus from keyboard.
  [Paul Sokolovsky]

  By either global Tab/Shift+Tab keys, or by processing ACTION_PREV,
  ACTION_NEXT as returned from a particular widget's handler (which
  can e.g. return the, for KEY_UP/KEY_DOWN, if those keys are not
  used by widget itself).
- Widgets: Dialog.find_focusable_by_idx(): Search thru children
  cyclically. [Paul Sokolovsky]
- Screen: attr_color(): Make background color optional. [Paul
  Sokolovsky]
- Screen: Add key codes for Tab and Shift+Tab. [Paul Sokolovsky]
- Widgets: Add inital implementation of bunch of widgets. [Paul
  Sokolovsky]
- Basewidget: Add standard widget completion codes. [Paul Sokolovsky]
- Screen: Add color codes. [Paul Sokolovsky]
- Screen: Add wr_fixedw(), attr_color(), attr_reset(). [Paul Sokolovsky]

  attr_* functions means color support.
- Basewidget: Introduce Widget class, to serve as base to implement
  widgets. [Paul Sokolovsky]

  Editor class now inherits from it. Widget itself in turn inherits from
  Screen, to offer all teh screen output capabilities.
- Editor: Move key definitions to screen.py. [Paul Sokolovsky]
- Editorext: Move clear_box(), draw_box(), dialog_box() to screen. [Paul
  Sokolovsky]
- Editor: Finish update_screen() -> redraw() refactor. [Paul Sokolovsky]
- Editor: Move generic screen-handling functions to separate module,
  screen. [Paul Sokolovsky]
- Editor: Refactor input handling into handle_key() and handle_mouse().
  [Paul Sokolovsky]

  These are generic widget methods which can be overriden in subclasses to
  achieve substantially diffrent behavior.
- Editor.redraw(): Make an alias for update_screen() method. [Paul
  Sokolovsky]

  update_screen() is deprecated, to be removed.
- Editor.show_line(): Also accept index of the line to draw. [Paul
  Sokolovsky]
- Editor: Typo fix in comment. [Paul Sokolovsky]
- Editorext.clear_box(): Fix off-by-one error. [Paul Sokolovsky]
- Editor: Correct position cursor on mouse click. [Paul Sokolovsky]

  Take into account editor window bounds.
- Editoext: Add screeb_size() method to query screen size. [Paul
  Sokolovsky]

  Uses XTerm escape sequence or defaults to VT100 size.
- Editor: init_tty(): Make a class method. [Paul Sokolovsky]
- Editor: Standard VT100 screen height is 24, not 25. [Paul Sokolovsky]
- Editorext: Don't hardcode status line position. [Paul Sokolovsky]

  Calculate based on main editor pane position, and allow to override.
- Seditor: Absolutely minimal editor widget. [Paul Sokolovsky]
- Move show_cursor_status() from Editor to EditorExt. [Paul Sokolovsky]
- Editor: Remove inconsistent calls to show_cursor_status(). [Paul
  Sokolovsky]
- Move show_status() from Editor to EditorExt. [Paul Sokolovsky]
- Editorext: goto_line(): Make less jumpy. [Paul Sokolovsky]

  By just repositioning cursor if requested line is already visible on the
  screen.
- Editor: Fix PG_DN when there's less than screenful of lines. [Paul
  Sokolovsky]
- Editorext: dialog_edit_line: If left is not specified, center on
  screen. [Paul Sokolovsky]
- Editoext: LineEditor: Adjust col for long lines. [Paul Sokolovsky]
- Editor: Support editing lines longer than window width. [Paul
  Sokolovsky]

  By scrolling entire window right.
- Editor: Handle terminal input reading more correctly. [Paul
  Sokolovsky]

  Chars are processed one by one, unless first char is ESC, when entire read
  sequence processed at one. This is not yet correct enough to work across
  serial, but now supports pasting in local terminal.
- Add .gitignore. [Paul Sokolovsky]
- Editorext: Use relative import. [Paul Sokolovsky]
- Editorext: Various extended subclasses of basic editor component.
  [Paul Sokolovsky]
- Properly deal with case when num of lines to display < than window
  height. [Paul Sokolovsky]
- Deinit_tty(): Take care of position cursor past editor area on quit.
  [Paul Sokolovsky]
- Editor: Really allow to work within specified window on a screen.
  [Paul Sokolovsky]
- Editor: Allow to work within specified window on a screen. [Paul
  Sokolovsky]
- Editor: Implement Backspace and Delete keys. [Paul Sokolovsky]
- Editor: If handle_key() returns non-None, stop and return that value.
  [Paul Sokolovsky]

  This e.g. allows to implement single-line edit widget with Enter/Esc
  handling.
- Add basic implementation of terminal editor widget. [Paul Sokolovsky]
- Empty root commit. [Paul Sokolovsky]


