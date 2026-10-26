class Buku:

  def _init_(self, isbn, judul, penulis, stok):
    self.isbn = isbn
    self.judul = judul
    self.penulis = penulis
    self.stok = stok

  def _str_(self):
    return f"[{self.isbn}] {self.judul} - {self.penulis} (Stok: {self.stok})"