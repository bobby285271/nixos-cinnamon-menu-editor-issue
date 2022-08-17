#!/usr/bin/env python3

import gi

gi.require_version("Gtk", "3.0")
gi.require_version('XApp', '1.0')

from gi.repository import Gtk, Gio, XApp


class MyApplication(Gtk.Application):

    def __init__(self, application_id, flags):
        Gtk.Application.__init__(self, application_id=application_id, flags=flags)
        self.connect("activate", self.activate)

    def activate(self, application):
        window = MainWindow(self)
        self.add_window(window.window)
        window.window.show()


class MainWindow():

    def __init__(self, application):
        self.application = application
        self.builder = Gtk.Builder()
        self.builder.add_from_file("editor.ui")
        self.window = self.builder.get_object("editor")
        self.window.show()


if __name__ == "__main__":
    application = MyApplication("top.bobby285271.nixos-cinnamon-menu-editor-issue",
                                Gio.ApplicationFlags.FLAGS_NONE)
    application.run()
