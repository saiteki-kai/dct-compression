import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class HeaderBar(Gtk.Box):
    def __init__(self, on_image_changed, on_compress_clicked):
        Gtk.Box.__init__(self, spacing=8, margin=16)

        self.on_image_changed = on_image_changed
        self.on_compress_clicked = on_compress_clicked

        self.F = 10
        self.d = 7

        label_img = Gtk.Label(label="Choose an image")
        self.add(label_img)

        self.file_chooser = Gtk.FileChooserButton(title="Choose an image")
        self.file_chooser.set_hexpand(True)
        self.file_chooser.connect("file-set", self.on_file_changed)
        self.add(self.file_chooser)

        label_F = Gtk.Label(label="F")
        self.add(label_F)

        entry_F = Gtk.SpinButton(adjustment=Gtk.Adjustment(10, 0, 1000, 1, 0, 0))
        entry_F.connect("value-changed", self.F_selected)
        self.add(entry_F)

        label_d = Gtk.Label(label="d")
        self.add(label_d)

        entry_d = Gtk.SpinButton(adjustment=Gtk.Adjustment(7, 0, 1000, 1, 0, 0))
        entry_d.connect("value-changed", self.d_selected)
        self.add(entry_d)

        btn_compress = Gtk.Button(label="Compress")
        btn_compress.connect("clicked", self.on_compress)
        self.add(btn_compress)

    def on_file_changed(self, _):
        filename = self.file_chooser.get_filename()
        self.on_image_changed(filename)

    def F_selected(self, entry):
        self.F = entry.get_value_as_int()

    def d_selected(self, entry):
        self.d = entry.get_value_as_int()

    def on_compress(self, _):
        self.on_compress_clicked(self.F, self.d)
