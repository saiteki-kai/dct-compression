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

    def on_compress_clicked(self, filename, F, d):
        if not filename:
            return

        if F < 0:
            return

        if d < 0 or d > 2 * F - 2:
            messagedialog = Gtk.MessageDialog(
                parent=self,
                flags=Gtk.DialogFlags.MODAL,
                type=Gtk.MessageType.WARNING,
                buttons=Gtk.ButtonsType.OK_CANCEL,
                message_format="Error",
            )
            # messagedialog.connect("response", self.dialog_response)
            messagedialog.show()
            return

        print(f"F: {F}, d: {d}, image: {filename}")

        self.viewer.clear_compressed_image()

        img = self.img
        if img is None:
            img = cv2.imread(filename, 0)

        out = compress_image(img, F, d)
        #out_filename = path.join("output", "part2", "out.bmp")
        out_filename = path.join("output", "part2", "F_"+str(F)+"_d_"+str(d)+"_"+(filename.split("/"))[-1])
        cv2.imwrite(out_filename, out)

        self.viewer.set_compressed_image(out_filename)
