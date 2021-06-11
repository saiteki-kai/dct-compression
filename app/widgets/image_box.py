import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf

import os
import math
from humanize import naturalsize


class ImageBox(Gtk.Box):
    def __init__(self, label):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL, expand=True)

        self.__temp_height = 0
        self.__temp_width = 0
        self.__pixbuf = None

        self.__img = Gtk.Image()
        self.__img.set_name("image-box")
        self.__img.set_vexpand(True)

        self.__scrolled_window = Gtk.ScrolledWindow()
        self.__scrolled_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        self.__scrolled_window.add_with_viewport(self.__img)
        self.__scrolled_window.connect("size-allocate", self.window_resized)
        self.add(self.__scrolled_window)

        __lbl_title = Gtk.Label(label=label)
        self.add(__lbl_title)

        self.__lbl_descr = Gtk.Label()
        self.add(self.__lbl_descr)

    def set_image(self, filename):
        if filename:
            pixbuf = GdkPixbuf.Pixbuf.new_from_file(filename)
            self.__img.set_from_pixbuf(pixbuf)
            self.__pixbuf = pixbuf
            self.window_resized(self.__scrolled_window, force_update=True)

            bytes = os.path.getsize(filename)
            dims = str(pixbuf.get_width()) + "x" + str(pixbuf.get_height())
            size = naturalsize(bytes, format="%.2f")

            self.__lbl_descr.set_label(dims + "\t" + size)

    def clear_image(self):
        self.__img.clear()
        self.__pixbuf = None
        self.__lbl_descr.set_label("")

    # https://github.com/cvzi/MinimalImageViewer/blob/078a1dfffc9eaf572c950538bd4552512d815533/MinimalImageViewer.py#L214-L249
    def window_resized(self, widget, force_update=False):
        allocation = widget.get_allocation()
        box_h = allocation.height - 4
        box_w = allocation.width - 4

        if force_update or self.__temp_height != box_h or self.__temp_width != box_w:
            self.__temp_height = box_h
            self.__temp_width = box_w

            if self.__pixbuf is None:
                # print("self.pixbuf is None")
                return

            img_h = self.__pixbuf.get_height()
            img_w = self.__pixbuf.get_width()

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
                pixbuf = self.__pixbuf.scale_simple(w, h, GdkPixbuf.InterpType.BILINEAR)
                self.__img.set_from_pixbuf(pixbuf)
