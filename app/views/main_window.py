import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import cv2
from os import path

from app.widgets.header_bar import HeaderBar
from app.widgets.images_viewer import ImagesViewer

from dct.compress import compress_image


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="Part2", application=app)
        self.set_default_size(800, 500)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, expand=True)

        header = HeaderBar(self.on_image_changed, self.on_compress_clicked)
        box.add(header)

        self.viewer = ImagesViewer()
        box.add(self.viewer)

        self.add(box)

    def on_image_changed(self, filename):
        self.viewer.set_original_image(filename)
        self.viewer.clear_compressed_image()

        # preload image for compression
        self.img = cv2.imread(filename, 0)

    def show_message(self, message):
        def dialog_response(widget, _):
            widget.destroy()

        messagedialog = Gtk.MessageDialog(
            parent=self,
            flags=Gtk.DialogFlags.MODAL,
            type=Gtk.MessageType.ERROR,
            buttons=Gtk.ButtonsType.CLOSE,
            message_format=message,
        )
        messagedialog.connect("response", dialog_response)
        messagedialog.show()

    def on_compress_clicked(self, filename, F, d):
        if not filename:
            self.show_message("No image selected!")
            return

        if F < 0:
            self.show_message("F must be greater than 0")
            return

        if d < 0 or d > 2 * F - 2:
            self.show_message("d must be between 0 and 2F-2")
            return

        self.viewer.clear_compressed_image()

        img = self.img
        if img is None:
            img = cv2.imread(filename, 0)

        out = compress_image(img, F, d)

        basename = path.basename(filename)
        out_filename = path.join("output", "part2", "F_%s_d_%s_%s" % (F, d, basename))

        cv2.imwrite(out_filename, out)
        self.viewer.set_compressed_image(out_filename)
