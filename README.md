ShellCheck plugin for Gedit
===========================
<!---
[![start with why](https://img.shields.io/badge/start%20with-why%3F-brightgreen.svg?style=flat)](http://www.ted.com/talks/simon_sinek_how_great_leaders_inspire_action)
--->
[![GitHub release](https://img.shields.io/github/release/elbosso/gedit-shellcheck/all.svg?maxAge=1)](https://GitHub.com/elbosso/gedit-shellcheck/releases/)
[![GitHub tag](https://img.shields.io/github/tag/elbosso/gedit-shellcheck.svg)](https://GitHub.com/elbosso/gedit-shellcheck/tags/)
[![GitHub license](https://img.shields.io/github/license/elbosso/gedit-shellcheck.svg)](https://github.com/elbosso/gedit-shellcheck/blob/master/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/elbosso/gedit-shellcheck.svg)](https://GitHub.com/elbosso/gedit-shellcheck/issues/)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/elbosso/gedit-shellcheck.svg)](https://GitHub.com/elbosso/gedit-shellcheck/issues?q=is%3Aissue+is%3Aclosed)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/elbosso/gedit-shellcheck/issues)
[![GitHub contributors](https://img.shields.io/github/contributors/elbosso/gedit-shellcheck.svg)](https://GitHub.com/elbosso/gedit-shellcheck/graphs/contributors/)
[![Github All Releases](https://img.shields.io/github/downloads/elbosso/gedit-shellcheck/total.svg)](https://github.com/elbosso/gedit-shellcheck)
[![Website elbosso.github.io](https://img.shields.io/website-up-down-green-red/https/elbosso.github.io.svg)](https://elbosso.github.io/)


This software is a plugin for the text editor [Gedit][1]. It allows to check shell scripts using the [ShellCheck][2] linter.

![Screenshot](https://lzone.de/images/gedit-shellcheck.png)

This plugin is derived from the JSHint Gedit plugin by [Xavier Gendre][3]

Requirements
------------

Requires Gedit 3.14+ and ShellCheck being installed. On Debian-based distros install it using

```
apt install shellcheck
```

Installation
------------

You might want to install the plugin using the [Gedit Plugin Installer](https://github.com/lwindolf/gedit-plugininstaller) or using these manual steps

    git clone https://github.com/lwindolf/gedit-shellcheck.git
    mkdir -p ~/.local/share/gedit/plugins/
    cp -r gedit-shellcheck/shellcheck.plugin gedit-shellcheck/shellcheck/ ~/.local/share/gedit/plugins/

Ensure to restart Gedit and activate the plugin in the preferences.

Usage
-----

When a JavaScript source code file is active, you can check it with `Tools > Check with ShellCheck` or with the accelerator `Ctrl+J`. The results are automatically displayed in the bottom panel.


  [1]: https://wiki.gnome.org/Apps/Gedit
  [2]: https://www.shellcheck.net/
  [3]: https://github.com/Meseira/gedit-jshint
