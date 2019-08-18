from gi.repository import GObject, Gedit


class ExamplePyViewActivatable(GObject.Object, Gedit.ViewActivatable):
    __gtype_name__ = "ExamplePyViewActivatable"

    view = GObject.property(type=Gedit.View)

    def __init__(self):
        GObject.Object.__init__(self)

    def do_activate(self):
        #print("Plugin created for", self.view)
        pass

    def do_deactivate(self):
        #print("Plugin stopped for", self.view)
        pass

    def do_update_state(self):
        # Called whenever the view has been updated
        #print("Plugin update for", self.view)
        pass
