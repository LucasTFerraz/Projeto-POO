# TODO: seus testes de configuração/LPS — enunciado, Seção 2.7 (pytest.raises,
# @pytest.mark.parametrize cobrindo estratégia×área).

import pytest

from celular_robo.src.celular_robo.excecoes import ConfiguracaoInvalida
from celular_robo.src.celular_robo.fabrica import criar_robo_configurado



def test_robo_padrao_comeca_na_origem():
    robo_novo = criar_robo_configurado("RoboColetor", "Coletor-3",)
    robo_novo2 = criar_robo_configurado("RoboColetor", "Coletor-3",estrategia_nome="RotaObstaculoComDuplaConferencia")
    assert (robo_novo.x, robo_novo.y) == (0, 0)


def test_area_quarentena_exclui_rota_direta():
    with pytest.raises(ConfiguracaoInvalida):
        criar_robo_configurado(
            "RoboColetor", "Coletor-2",
            estrategia_nome="direta", area_nome="area 4",
        )