import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from app.widgets.image_box import ImageBox


class ImagesViewer(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self, spacing=8, margin=16, homogeneous=True)

        self.__original_box = ImageBox(label="Original")
        self.add(self.__original_box)

        self.__compressed_box = ImageBox(label="Compressed")
        self.add(self.__compressed_box)

    def set_original_image(self, filename):
        self.__original_box.set_image(filename)

    def set_compressed_image(self, filename):
        self.__compressed_box.set_image(filename)

    def clear_compressed_image(self):
        self.__compressed_box.clear_image()
