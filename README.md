ShellCheck plugin for Gedit
===========================

This software is a plugin for the text editor [Gedit][1]. It allows to check bash scripts with [ShellCheck][2].

This plugin is derived from the JSHint Gedit plugin by Xavier Gendre [3]

Requirements
------------

This plugin is for Gedit 3 and is **not compatible with Gedit 2**. It requires ShellCheck being installed. On Debian-based distros install it using

```
apt install shellcheck
```

Installation
------------

You might want to install the plugin using these steps

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
