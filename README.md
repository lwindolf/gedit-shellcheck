ShellCheck plugin for Gedit
===========================
<!---
[![start with why](https://img.shields.io/badge/start%20with-why%3F-brightgreen.svg?style=flat)](http://www.ted.com/talks/simon_sinek_how_great_leaders_inspire_action)
--->
[![GitHub release](https://img.shields.io/github/release/lwindolf/gedit-shellcheck/all.svg?maxAge=1)](https://GitHub.com/lwindolf/gedit-shellcheck/releases/)
[![GitHub tag](https://img.shields.io/github/tag/lwindolf/gedit-shellcheck.svg)](https://GitHub.com/lwindolf/gedit-shellcheck/tags/)
[![GitHub license](https://img.shields.io/github/license/lwindolf/gedit-shellcheck.svg)](https://github.com/lwindolf/gedit-shellcheck/blob/master/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/lwindolf/gedit-shellcheck.svg)](https://GitHub.com/lwindolf/gedit-shellcheck/issues/)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/lwindolf/gedit-shellcheck.svg)](https://GitHub.com/lwindolf/gedit-shellcheck/issues?q=is%3Aissue+is%3Aclosed)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/lwindolf/gedit-shellcheck/issues)
[![GitHub contributors](https://img.shields.io/github/contributors/lwindolf/gedit-shellcheck.svg)](https://GitHub.com/lwindolf/gedit-shellcheck/graphs/contributors/)
[![Github All Releases](https://img.shields.io/github/downloads/lwindolf/gedit-shellcheck/total.svg)](https://github.com/lwindolf/gedit-shellcheck)

This software is a plugin for the text editor [Gedit](https://wiki.gnome.org/Apps/Gedit). It allows to check shell scripts using the [ShellCheck](https://www.shellcheck.net/) linter.


![Screenshot](https://lzone.de/images/gedit-shellcheck.png)

## Contributors

- This plugin is derived from the JSHint Gedit plugin by [Xavier Gendre](https://github.com/Meseira/gedit-jshint)
- Live checking and matching improvements by [Jürgen Key](https://github.com/elbosso)

## Requirements

Requires Gedit 3.14+ and ShellCheck being installed. On Debian-based distros install it using

    apt install shellcheck

## Installation

You might want to install the plugin using the [Gedit Plugin Installer](https://github.com/lwindolf/gedit-plugininstaller) or using these manual steps

    git clone https://github.com/lwindolf/gedit-shellcheck.git
    mkdir -p ~/.local/share/gedit/plugins/
    cp -r gedit-shellcheck/shellcheck.plugin gedit-shellcheck/shellcheck/ ~/.local/share/gedit/plugins/

Ensure to restart Gedit and activate the plugin in the preferences.

## Usage

When a shell source code file is active, you can check it

- editing and moving the cursor to the next line
- or by selecting menu option `Tools > Check with ShellCheck`

The results are automatically displayed in the bottom panel.
