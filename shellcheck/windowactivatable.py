# -*- coding: utf-8 -*-
#    ShellCheck plugin for Gedit
#    Copyright (C) 2016 Xavier Gendre <gendre.reivax@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import GObject, Gedit, Gio, PeasGtk

from .shellcheck import ShellCheck
from .outputpanel import OutputPanel

class WindowActivatable(GObject.Object, Gedit.WindowActivatable):
    __gtype_name__ = "ShellCheckWindowActivatable"

    window = GObject.property(type=Gedit.Window)
    map={}

    def __init__(self):
        GObject.Object.__init__(self)

        self._action = None
        self._config_panel = None
        self._shellcheck = None
        self._output_panel = None

    def do_activate(self):
        #print('do_activate')
        self._action = Gio.SimpleAction(name="check-with-shellcheck")
        self._action.connect("activate", self._run_shellcheck)
        self.window.add_action(self._action)

        self._output_panel = OutputPanel(self.window)
        bottom_panel = self.window.get_bottom_panel()
        bottom_panel.add_titled(self._output_panel,
                "ShellCheckOutputPanel", "ShellCheck")
        self.window.connect('tab-added', self.on_window_activetabchanged_event)
        self.window.connect('tab-removed', self.on_window_tabremoved_event)


        self._shellcheck = ShellCheck()

    def on_window_activetabchanged_event(self, geditwindow,tab):
        #print("active tab changed")
        doc = tab.get_document()
        if doc not in self.map:
            handler_id=doc.connect('cursor-moved', self.on_textbuffer_cursormoved_event)
            self.map[doc] =handler_id
        pass

    def on_window_tabremoved_event(self, geditwindow,tab):
        #print("tab removed")
        doc = tab.get_document()
        if doc in self.map:
            doc.disconnect(self.map[doc])
            self.map.pop(doc)
        pass

    def on_textbuffer_cursormoved_event(self, document):
        #print("cursor moved")
        #print(document.get_language())
        if(document.get_language() is not None):
            if(document.get_language().get_name() == 'sh'):
                self._run_shellcheck(None)
        pass

    def do_deactivate(self):
        #print('do_deactivate')
        self._shellcheck = None
        self._output_panel = None

        self.window.remove_action("check-with-shellcheck")
        self._action = None

    def do_update_state(self):
        doc = self.window.get_active_document()
        state = False

        if doc:
            lang = doc.get_language()
            # Only for JavaScript
            if lang and lang.get_id() == "sh":
                state = True

        self._action.set_enabled(state)
        if state:
            self._output_panel.show()
        else:
            self._output_panel.hide()

    def _run_shellcheck(self, action, data=None):
        doc = self.window.get_active_document()
        if doc:
            # Show ShellCheck panel if not visible
            bottom_panel = self.window.get_bottom_panel()
            if not bottom_panel.is_visible():
                bottom_panel.set_visible(True)
            if bottom_panel.get_visible_child() != self._output_panel:
                bottom_panel.set_visible_child(self._output_panel)

            # Update the panel
            report = self._shellcheck.run(self.window.get_active_document())
            self._output_panel.update(report)
