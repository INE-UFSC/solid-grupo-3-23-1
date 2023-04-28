"""
Interface Segregation Principle
Crie interfaces que são específicas. Clientes não devem depender de interfaces que eles não usarão
"""

from abc import ABC
"""
class IJanela(ABC):
    def maximizar(self):
        raise NotImplementedError
    
    def minimizar(self):
        raise NotImplementedError
    
    def mostrar_menu(self):
        raise NotImplementedError
        
    def fechar(self):
        raise NotImplementedError

class JanelaTamanhoFixo(IJanela):
    def maximizar(self):
        pass

    def minimizar(self):
        pass
    
    def mostrar_menu(self):
        pass
    
    def fechar(self):
        pass

class JanelaSemMenu(IJanela):
    def maximizar(self):
        pass

    def minimizar(self):
        pass
    
    def mostrar_menu(self):
        pass
    
    def fechar(self):
        pass
"""

class IJanela(ABC):
    def fechar(self):
        raise NotImplementedError
    
class IJanelaSemMenu(IJanela):
    def maximizar(self):
        raise NotImplementedError
    
    def minimizar(self):
        raise NotImplementedError
            

class IJanelaTamanhoFixo(IJanela):
    def mostrar_menu(self):
        raise NotImplementedError


class JanelaTamanhoFixo(IJanelaTamanhoFixo):
    def mostrar_menu(self):
        pass
    
    def fechar(self):
        pass

class JanelaSemMenu(IJanelaSemMenu):
    def maximizar(self):
        pass

    def minimizar(self):
        pass
    
    def fechar(self):
        pass
