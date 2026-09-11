# Observer — EquipeDeTestes, RegistroAuditoria — enunciado, Seção 2.3.
#
# Herde de `Observador` (observadores_base.py — ABC com registro automático):
#
#   from celular_robo.observadores_base import Observador
#
# TODO: implemente aqui. EquipeDeTestes(Observador) reage a "bandeja_pronta";
# RegistroAuditoria(Observador) loga todo evento (coleta, bandeja pronta,
# pedido rejeitado), pensando em trilha de auditoria, não só depuração.
from celular_robo.src.celular_robo.base.observadores_base import Observador


class EquipeDeTestes(Observador):
    def atualizar(self, evento, **dados):
        pass

class RegistroAuditoria (Observador):
    def atualizar(self, evento, **dados):
        pass

