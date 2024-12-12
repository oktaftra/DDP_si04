from animals import *

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_ular, jenis_ular):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna_ular
        self.jenis = jenis_ular

    def cetak_Ular(self):
        super().cetak()
        print(f'warna ular ini {self.warna} dan jenis ular ini adalah {self.jenis}')

sanca = Ular('sanca', 'ayam', 'darat', 'bertelur', 'hitam', 'pembelit')
sanca.cetak_Ular()
sawah = Ular('sawah', 'tikus', 'darat', 'bertelur', 'coklat', 'ngelilit')
sawah.cetak_Ular()
cobra = Ular('cobra', 'daging', 'darat', 'bertelur', 'abu-abu', 'berbisa')
cobra.cetak_Ular()