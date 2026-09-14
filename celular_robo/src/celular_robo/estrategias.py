# Strategy — RotaDireta, RotaComDuplaConferencia — enunciado, Seção 2.3.
# (Não confundir com estrategias_base.py — genérico do curso, não editar. Ao
# contrário de Command/Observer/State, aqui você NÃO herda de `Estrategia`:
# escreva sua própria base, ver TODO abaixo — motivo em estrategias_base.py.)
#
# TODO: implemente aqui. Considere uma base comum (RotaColeta) com
# __init_subclass__ registrando cada rota, ver Seção 2.2 (metaprogramação
# aplicada a uma segunda hierarquia).
from src.celular_robo.base.estrategias_base import Estrategia
from src.celular_robo.base.robo_base import Coordenada
class RotaColeta():    
    inicio = Coordenada()
    destino = Coordenada() 
    
    def __set_name__(self, owner, name):
        self.nome_publico = name
        self.nome = "_" + name
    def __init_subclass__(cls, categoria="geral", **kwargs):
        super().__init_subclass__(**kwargs)
        RotaColeta._registro_rotas[cls.__name__] = cls
        cls.categoria = categoria
    def __init__(self,inicio,fim,numero):
        self.numero = numero
        self.inicio = inicio
        self.destino = fim
class RotaDireta (Estrategia):
    def __init__(self):
        pass

class RotaComDuplaConferencia (Estrategia):
    def __init__(self):
        pass