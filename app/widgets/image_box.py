import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf


class ImageBox(Gtk.Box):
    def __init__(self, label):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL, expand=True)

        self.img = Gtk.Image()
        self.img.set_name("image-box")
        self.img.set_vexpand(True)
        self.add(self.img)

        lbl = Gtk.Label(label=label)
        self.add(lbl)

    def set_image(self, filename):
        screen = self.get_allocation()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file(filename)
        pixbuf = pixbuf.scale_simple(screen.width, screen.height, GdkPixbuf.InterpType.BILINEAR)
        self.img.set_from_pixbuf(pixbuf)
