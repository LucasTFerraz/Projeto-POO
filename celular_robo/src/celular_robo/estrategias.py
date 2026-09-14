# Strategy — RotaDireta, RotaComDuplaConferencia — enunciado, Seção 2.3.
# (Não confundir com estrategias_base.py — genérico do curso, não editar. Ao
# contrário de Command/Observer/State, aqui você NÃO herda de `Estrategia`:
# escreva sua própria base, ver TODO abaixo — motivo em estrategias_base.py.)
#
# TODO: implemente aqui. Considere uma base comum (RotaColeta) com
# __init_subclass__ registrando cada rota, ver Seção 2.2 (metaprogramação
# aplicada a uma segunda hierarquia).
from abc import ABC,abstractmethod
from celular_robo.src.celular_robo.base.estrategias_base import EstrategiaEsquiva,EstrategiaPadrao,EstrategiaZigzag
from celular_robo.src.celular_robo.base.robo_base import Robo,Direcao
from celular_robo.src.celular_robo.robo import QuantidadeValida
from celular_robo.src.celular_robo.excecoes import QualidadeBaixa,ErroColeta

class RotaColeta(ABC):
    _registro_rotas = {}
    @abstractmethod
    def mover(self, robo:Robo,):...
    def depositar(self,robo): self.carga = []
    def __init_subclass__(cls, categoria="geral", **kwargs):
        super().__init_subclass__(**kwargs)
        RotaColeta._registro_rotas[cls.__name__] = cls
        cls.categoria = categoria
    def __init__(self,inicio:tuple,fim:tuple,qualM):
        self.qualidadeMinima = qualM if isinstance(qualM,QuantidadeValida) else qualM
        self.est = EstrategiaPadrao()
        self.desvios = []
        self.carga = []
        self._dx =fim[0]
        self._dy =fim[1]
        self._direcaoX = Direcao(-1 if fim[0] - inicio[0]<0 else 1,0) if fim[0] - inicio[0]!=0 else None
        self._direcaoY = Direcao(0,-1 if fim[1] - inicio[1]<0 else 1) if fim[1] - inicio[1]!=0 else None
        self._inicio = inicio
        self._destino = fim
    @property
    def direX(self): return self._direcaoX
    @property
    def direY(self): return self._direcaoY
    @property
    def dx(self): return self._dx
    @property
    def dy(self): return self._dy
    @property
    def inicio(self): return self._inicio
    @property
    def dest(self): return self._destino
    @abstractmethod
    def coletar(self,objetos):
        ...

class RotaDireta (RotaColeta):
    # def coletar(self,objetos):
    #     self.carga = objetos
    #     return []
    def mover(self, robo:Robo):
        robo.girar_ate(self._direcaoX)
        while(robo.posicao[0]<self._dx):
            if not self.est.mover(robo): raise ErroColeta("Rota Impossivel")
        robo.girar_ate(self._direcaoY)
        while(robo.posicao[0]<self._dy):
            if not self.est.mover(robo): raise ErroColeta("Rota Impossivel")
    def depositar(self,robo): 
        self.carga = []
        return 0

class RotaComDuplaConferencia (RotaColeta):
    def mover(self, robo:Robo):
        robo.girar_ate(self._direcaoX)
        while(robo.posicao[0]<self._dx):
            if not self.est.mover(robo):
                self.desvios.append(robo.posicao)
                self.est = EstrategiaEsquiva()
                if self.est.mover(robo): 
                    
                    self.est = EstrategiaPadrao()
                else: raise ErroColeta("Rota Impossivel")
                robo.girar_ate(self._direcaoX)
        robo.girar_ate(self._direcaoY)
        while(robo.posicao[1]<self._dy):
            if not self.est.mover(robo):
                self.desvios.append(robo.posicao)
                self.est = EstrategiaEsquiva()
                if self.est.mover(robo): 
                    self.est = EstrategiaPadrao()
                else: raise ErroColeta("Rota Impossivel")
                robo.girar_ate(self._direcaoX)
    def depositar(self,robo:Robo): 
        fails = 0
        while (len(self.carga)>0):
            o = self.carga.pop(0)
            try:self.qualidadeMinima.checarQualidade(o)
            except QualidadeBaixa as e: 
                fails+=1
                robo.notificar("Object quality fail")
            except ValueError as e:
                fails+=1
                robo.notificar("Object invalid quality")
        self.carga 

class ObstaculoDuplaConferencia(RotaComDuplaConferencia):
    pass
    # def mover(self, robo:Robo):
    #     robo.girar_ate(self._direcaoX)
    #     while(robo.posicao[0]<self._dx):
    #         if not self.est.mover(robo):
    #             self.desvios.append(robo.posicao)
    #             self.est = EstrategiaEsquiva()
    #             if self.est.mover(robo): 
                    
    #                 self.est = EstrategiaPadrao()
    #             else: raise ErroColeta("Rota Impossivel")
    #             robo.girar_ate(self._direcaoX)
    #     robo.girar_ate(self._direcaoY)
    #     while(robo.posicao[1]<self._dy):
    #         if not self.est.mover(robo):
    #             self.desvios.append(robo.posicao)
    #             self.est = EstrategiaEsquiva()
    #             if self.est.mover(robo): 
    #                 self.est = EstrategiaPadrao()
    #             else: raise ErroColeta("Rota Impossivel")
    #             robo.girar_ate(self._direcaoX)
    #     #if robo.esta_na_borda
    #     EstrategiaPadrao