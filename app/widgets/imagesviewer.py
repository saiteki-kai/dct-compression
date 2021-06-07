import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from app.widgets.imagebox import ImageBox


class ImagesViewer(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self, spacing=8, margin=16, homogeneous=True)

        self.original_box = ImageBox(label="Original")
        self.add(self.original_box)

        self.compressed_box = ImageBox(label="Compressed")
        self.add(self.compressed_box)

    def set_original_image(self, filename):
        self.original_box.set_image(filename)

    def set_compressed_image(self, filename):
        self.compressed_box.set_image(filename)
