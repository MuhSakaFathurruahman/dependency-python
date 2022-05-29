from barang_elektronik import BarangElektronik

class Lampu(BarangElektronik):
    
    def beroprasi(self):
        print("Lampu menyala")
    
    def berhenti(self):
        print("Lampu berhenti menyala")