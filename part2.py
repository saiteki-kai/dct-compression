#!env/bin/python3
import sys
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

from app.views.main_window import MainWindow


class App(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MainWindow(self)
        win.show_all()

    def do_startup(self):
        self.load_css()
        Gtk.Application.do_startup(self)

    def load_css(self):
        style_provider = Gtk.CssProvider()
        style_provider.load_from_path("./app/style.css")
        screen = Gdk.Screen.get_default()
        Gtk.StyleContext.add_provider_for_screen(screen, style_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)


app = App()
sys.exit(app.run(sys.argv))
