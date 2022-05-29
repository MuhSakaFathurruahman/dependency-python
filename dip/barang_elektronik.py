from abc import ABC, abstractmethod

class BarangElektronik(ABC):
    
    @abstractmethod
    def beroprasi(self):
        pass
    
    @abstractmethod
    def berhenti(self):
        pass