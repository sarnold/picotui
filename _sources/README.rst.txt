picotui
=======

|ci| |wheels| |conda| |coverage| |release|

|pre| |reuse| |cov| |pylint|

|tag| |license| |python| |contributors|

Picotui is a Text User Interface (TUI) widget library for Python3.
It is known to work with CPython3 and
`Pycopy <https://github.com/pfalcon/pycopy>`_ (Unix version is
officially supported for the latter), but should work with any
Python3 implementation which allows to access stdin/stdout file
descriptors.

You can learn more about it with the help of a virtual Q&A session:

Q: There're a few TUI libraries for Python, why yet another one?

A: Urwid is one well-known such TUI library. Here's an entry from its
FAQ: "How do I create drop-downs, floating windows, and scroll bars? -
You need to start writing some fairly complex widgets. This
functionality hasn't been added to Urwid yet." So, Urwid is a
widget library which doesn't have dropdowns. Version 0.8.0 of
Urwid was imported into SVN (and later Git) in 2004. Urwid doesn't
have dropdowns and stuff for 10+ years.

Q: Hey, but you cut off the answer from Urwid FAQ. It says: "but if you
are willing to write it, we do accept patches". Why didn't you implement
those widgets for Urwid and contribute them?

A: Why didn't you? No, wait, that's not productive. I didn't implement
them for Urwid because I don't like its architecture and the fact that
its widget set is rather weak (so it's hard to write new widgets - there
are not enough examples to start from). And don't get me wrong, but the
fact that nobody wrote those widgets for Urwid during 10+ years, got to
mean something. However, I tried to hack on another, less, but still
known Python TUI library - Npyscreen. Its widget set is much more
advanced and usable. But - it still has some architectural choices
which makes extending it and overriding some behaviors problematic.
I also found its project management a bit unresponsive. So, after making
a dozen of commits to my fork, I thought it's time to get some breath and
started picotui.

Q: So, sun must shine bright in the picotui land, and it must be the best
library out there?

A: Alas, no. Let me start with the fact that most TUI libraries are based
on ``curses`` library for terminal screen management. It makes sure that if
you update a screen, only the minimal set of updates is made. This was
very important at the era of 300 baud serial connections. Let's count:
300 baud is about 30 bytes/s, and the standard VT100 screen is 80*24 = ~2K.
Double that for attributes. So, transferring a complete screen to show
to user would take 2 mins. If you draw the same screen twice (no changes in
content), it would take 4 mins. ``curses`` library cuts that back to mere 2
mins. So, alas, ``picotui`` doesn't use curses. That's based on the fact
that picotui wants to be compatible with Pycopy, and its philosophy
is minimalism - if it's possible to do screen output without ``curses``,
let's do just that. It's also grounded in the fact that nobody uses
300 baud modems any longer, most apps are run in a local terminal emulator
with instant updates, most of the remaining are run over LANs which
also offer fast updates. The modern basic serial connection speed is
115200 which is still too slow for real-time fullscreen updates though.
That's why I say "alas". Beyond the optimized screen updates, ``picotui``
lacks many other things too: e.g., double-buffering (so redrawing the
previous screen content behind pop-ups is up to you), it lacks geometry
managers, so calculating coordinates is up to you, etc. Yes, just like
that - I lacked widgets the most, and that's what I implemented. The rest
is just KISS.

Q: But that's really sad!

A: Indeed, it is. The only good news is that now you have a choice: if
you want your app work well with 300 baud modems, you can use other
libraries, and if you want widgets, you can use `picotui`.

Q: So many words, where's a mandatory screenshot?

A: Sure:

.. image:: https://raw.githubusercontent.com/pfalcon/picotui/master/picotui.png

Documentation
-------------

.. tip:: Try the new Sphinx `docs build`_!

.. _docs build: https://sarnold.github.io/picotui/


Picotui is an experimental WIP project, and the best documentation currently
is the source code (https://github.com/pfalcon/picotui/tree/master/picotui)
and examples (see below).

Examples
--------

* example_widgets.py - Shows repertoire of widgets, inside a dialog.
* example_menu.py - Shows a "fullscreen" application with a main menu.
* example_dialogs.py - Shows some standard dialogs.
* examples/ - More assorted examples.

Known Issues
------------

Pay attention to what Unicode font you use in your console. Some Linux
distributions, e.g. Ubuntu, are known to have a broken Unicode font
installed by default, which causes various visual artifacts (specifically,
Ubuntu Mono font isn't really monospace - many Unicode pseudographic
characters have double (or so) width, box-drawing symbols have gaps, etc.)

SBOM and license info
=====================

Licensed under the `MIT License`_ as documented in ``REUSE.toml``.

This project is now compliant with the REUSE Specification Version 3.3,
and the corresponding license information for all files can be found in
the ``REUSE.toml`` configuration file with license text(s) in the
``LICENSES/`` folder.

Related metadata can be (re)generated with the following tools and
command examples.

* reuse-tool_ - REUSE_ compliance linting and sdist (source files) SBOM generation
* sbom4python_ - generate SBOM with full dependency chain

Commands
--------

Use tox to create the environment and run the lint command::

  $ tox -e reuse                      # to run reuse lint   --or--
  $ tox -e reuse -- spdx > sbom.txt   # generate sdist files sbom

Note you can pass any of the other reuse commands after the ``--`` above.

Use the above environment to generate the full SBOM in text format::

  $ source .tox/reuse/bin/activate
  $ sbom4python --system --use-pip -o <file_name>.txt

Be patient; the last command above may take several minutes. See the
doc links above for more detailed information on the tools and
specifications.

.. _reuse-tool: https://github.com/fsfe/reuse-tool
.. _REUSE: https://reuse.software/spec-3.3/
.. _sbom4python: https://github.com/anthonyharrison/sbom4python
.. _MIT License: LICENSES/


.. |ci| image:: https://github.com/sarnold/picotui/actions/workflows/ci.yml/badge.svg
    :target: https://github.com/sarnold/picotui/actions?query=workflow:CI
    :alt: CI Status

.. |wheels| image:: https://github.com/sarnold/picotui/workflows/Wheels/badge.svg
    :target: https://github.com/sarnold/picotui/actions?query=workflow:Wheels
    :alt: Wheel Status

.. |conda| image:: https://github.com/sarnold/picotui/workflows/Conda/badge.svg
    :target: https://github.com/sarnold/picotui/actions?query=workflow:Conda
    :alt: Conda Status

.. |coverage| image:: https://github.com/sarnold/picotui/actions/workflows/coverage.yml/badge.svg
    :target: https://github.com/sarnold/picotui/actions/workflows/coverage.yml
    :alt: Coverage Status

.. |release| image:: https://github.com/sarnold/picotui/workflows/Release/badge.svg
    :target: https://github.com/sarnold/picotui/actions?query=workflow:Release
    :alt: Release Status

.. |cov| image:: https://raw.githubusercontent.com/sarnold/picotui/badges/master/test-coverage.svg
    :target: https://github.com/sarnold/picotui/actions/workflows/coverage.yml
    :alt: Test coverage

.. |pylint| image:: https://raw.githubusercontent.com/sarnold/picotui/badges/master/pylint-score.svg
    :target: https://github.com/sarnold/picotui/actions/workflows/pylint.yml
    :alt: Pylint Score

.. |reuse| image:: https://api.reuse.software/badge/git.fsfe.org/reuse/api
    :target: https://api.reuse.software/info/git.fsfe.org/reuse/api
    :alt: REUSE status

.. |license| image:: https://img.shields.io/pypi/l/picotui?color=blue
    :target: https://github.com/sarnold/picotui/blob/master/LICENSE
    :alt: License

.. |tag| image:: https://img.shields.io/github/v/tag/sarnold/picotui?color=blue&include_prereleases&label=latest%20release
    :target: https://github.com/sarnold/picotui/releases
    :alt: GitHub tag (latest SemVer, including pre-release)

.. |python| image:: https://img.shields.io/badge/python-3.6+-blue.svg
    :target: https://www.python.org/downloads/
    :alt: Python

.. |pre| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit

.. |contributors| image:: https://img.shields.io/github/contributors/sarnold/picotui
   :target: https://github.com/sarnold/picotui
   :alt: Contributors
