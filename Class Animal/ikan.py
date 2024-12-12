from animals import *

class ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_ikan, jenis_ikan):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna_ikan
        self.jenis = jenis_ikan

    def cetak_ikan(self):
        super().cetak()
        print(f'warna ikan ini adalah warna {self.warna} dan hewan ini jenisnya ikan {self.jenis}')

nemo = ikan('ikan nemo', 'plakton', 'air', 'bertelur', 'orange', 'air laut')
nemo.cetak_ikan()
koi = ikan('ikan koi', 'pelet', 'air', 'bertelur', 'merah', 'air tawar')
koi.cetak_ikan()
arwana = ikan('ikan arwana', 'cacing', 'air', 'betelur', 'hijau', 'air sungai')
arwana.cetak_ikan()