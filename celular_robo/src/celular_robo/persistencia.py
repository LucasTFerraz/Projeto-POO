# Configuração e persistência — enunciado, Seção 2.6.
#
# TODO: implemente aqui. montar_robo_de_config(config) e
# montar_pedido_de_json(caminho) — mesmo par de funções do capstone do curso
# (montar_robo_de_config/montar_frota_de_json), adaptado: um arquivo
# configura o robô (tipo, estratégia, área), outro traz o pedido de coleta.

import json
from src.celular_robo.excecoes import ConfiguracaoInvalida
from src.celular_robo.base.robo_base import Robo
from src.celular_robo.robo import RoboColetor

def montar_pedido_de_json(caminho):
    with open(caminho) as f:
        fileData = json.loads(f)

def montar_robo_de_config(caminho):
    with open(caminho) as f:
        fileData = json.loads(f)
    if isinstance(fileData,Robo):
        return fileData
    elif isinstance(fileData,dict):
        if any(k not in fileData for k in [""]):
            raise ConfiguracaoInvalida("Falta Informações para criar o robo")