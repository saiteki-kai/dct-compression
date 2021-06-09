import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf

import math


class ImageBox(Gtk.Box):
    def __init__(self, label):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL, expand=True)

        self.temp_height = 0
        self.temp_width = 0
        self.pixbuf = None

        self.img = Gtk.Image()
        self.img.set_name("image-box")
        self.img.set_vexpand(True)

        self.scrolled_window = Gtk.ScrolledWindow()
        self.scrolled_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        self.scrolled_window.add_with_viewport(self.img)
        self.scrolled_window.connect("size-allocate", self.window_resized)
        self.add(self.scrolled_window)

        lbl = Gtk.Label(label=label)
        self.add(lbl)

    def set_image(self, filename):
        pixbuf = GdkPixbuf.Pixbuf.new_from_file(filename)
        self.img.set_from_pixbuf(pixbuf)
        self.pixbuf = pixbuf
        self.window_resized(self.scrolled_window, force_update=True)

    # https://github.com/cvzi/MinimalImageViewer/blob/078a1dfffc9eaf572c950538bd4552512d815533/MinimalImageViewer.py#L214-L249
    def window_resized(self, widget, force_update=False):
        allocation = widget.get_allocation()
        box_h = allocation.height - 4
        box_w = allocation.width - 4

        if force_update or self.temp_height != box_h or self.temp_width != box_w:
            self.temp_height = box_h
            self.temp_width = box_w

            if self.pixbuf is None:
                # print("self.pixbuf is None")
                return

            img_h = self.pixbuf.get_height()
            img_w = self.pixbuf.get_width()

            w = float(img_w)
            h = float(img_h)
            totalscale = 1.0

            if h > box_h:
                scale = box_h / h
                w *= scale
                h *= scale
                totalscale *= scale

            if w > box_w:
                scale = box_w / w
                w *= scale
                h *= scale
                totalscale *= scale

            w = int(math.floor(w))
            h = int(math.floor(h))
            totalscale = math.ceil(totalscale * 100.0)

            # Update image
            if (w != img_w or h != img_h) and w > 0 and h > 0:
                pixbuf = self.pixbuf.scale_simple(w, h, GdkPixbuf.InterpType.BILINEAR)
                self.img.set_from_pixbuf(pixbuf)
