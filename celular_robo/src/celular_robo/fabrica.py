# Factory — criar_robo_coletor, criar_robo_configurado — enunciado, Seção 2.3.
# (Ver fabrica_base.py — genérico do curso, não editar: criar_robo("RoboColetor",
# ...) já funciona, pode chamar direto ou usar como modelo.)
#
# TODO: implemente aqui. criar_robo_coletor(tipo_nome, ...) a partir do
# _registro (Seção 2.2); criar_robo_configurado combina isso com a validação do
# modelo de features (Seção 2.4).
#
# Contrato mínimo exigido por tests/test_00_fornecido.py (não altere a
# assinatura abaixo sem também atualizar aquele arquivo):
#
#   criar_robo_configurado(tipo_nome, nome, estrategia_nome=..., area_nome=...)

from src.celular_robo.robo import RoboColetor
from src.celular_robo.excecoes import *
from src.celular_robo.base.robo_base import Robo

def criar_robo_coletor(tipo_nome,nome, estrategia_nome,area_nome,**kwargs):
    if area_nome == "area_quarentena" and estrategia_nome == "direta":
        raise ConfiguracaoInvalida("Combinação de area e rota não permitida")
    return RoboColetor(nome,**kwargs)

def criar_robo_configurado(tipo_nome,nome,estrategia_nome="Padrao",area_nome="Padrao",**kwargs):
    match(tipo_nome):
        case "RoboColetor":
            return criar_robo_coletor(tipo_nome,nome,estrategia_nome,area_nome,**kwargs)
        case "Robo":
            return Robo(nome)
        case _:
            raise ConfiguracaoInvalida("Tipo de robo invalido")
