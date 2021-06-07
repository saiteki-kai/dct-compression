import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from app.widgets.headerbar import HeaderBar
from app.widgets.imagesviewer import ImagesViewer


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="Part2", application=app)
        self.set_default_size(800, 600)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, expand=True)

        header = HeaderBar(self.on_image_changed, self.on_compress_clicked)
        box.add(header)

        self.viewer = ImagesViewer()
        box.add(self.viewer)

        self.add(box)

    def on_image_changed(self, image):
        self.image = image
        self.viewer.set_original_image(image)

    def on_compress_clicked(self, F, d):
        if "image" not in self or not self.image:
            return

        print(f"F: {F}, d: {d}, image: {self.image}")

        # do stuff with opencv

        # set image
        # self.viewer.set_compressed_image(compressed)
