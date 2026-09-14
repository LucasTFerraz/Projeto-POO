# Command — ComandoColeta — enunciado, Seção 2.3.
#
# Herde de `Comando` (comandos_base.py — ABC com registro automático):
#
#   from celular_robo.comandos_base import Comando
#
# TODO: implemente aqui. ComandoColeta(Comando): __init__(codinome, posicao,
# quantidade), com .executar(robo) e .desfazer(robo) (remove o item da
# bandeja, decrementa a contagem coletada).
from abc import ABC

from celular_robo.src.celular_robo.base.comandos_base import Comando
from celular_robo.src.celular_robo.base.robo_base import Robo
from celular_robo.src.celular_robo.estrategias import RotaColeta


class ComandoColeta(Comando):
    def __init__(self,rota:RotaColeta,objetos:List):
        self.rota = rota
        self.obj = objetos
        self.rotaAlternativa = None
        super().__init__()
    def executar(self,robo:Robo):
        
        while(len(self.obj)>0):
            self.obj = self.rota.coletar(self.obj)
            self.rota.mover(robo)
            self.rota.depositar()
            self.rota.voltar(robo)