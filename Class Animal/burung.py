from animals import *

class burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_bulu, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis_bulu =jenis_bulu
        self.bunyi = bunyi

    def cetak_burung(self):
        super().cetak()
        print(f'hewan ini berbulu {self.jenis_bulu}, dan hewan ini berbunyi {self.bunyi}')

beo = burung('burung beo', 'biji-bijian', 'udara', 'bertelur', 'blue dan orange', 'kamu jelek')
beo.cetak_burung() 
kakatua = burung('burung kakatua', 'umbi', 'udara', 'bertelur', 'putih','keras dan melengking')
kakatua.cetak_burung()
perkutut = burung('perkutut', 'buah-buahan', 'udara', 'bertelur', 'coklat', 'berdengkur')
perkutut.cetak_burung()