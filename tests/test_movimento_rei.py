from class_tab import Tabuleiro
import unittest


class TestMovimentoBispo(unittest.TestCase):
    # 1
    def test_movimento_frente_valido_branco(self):
        tab = Tabuleiro()
        tab.mover_peao(1, 4, 3, 4)
        tab.mover_rei(0, 4, 1, 4)

        tab.exibir()
        assert tab.xadrez[0][4]["peca"] == ""
        assert tab.xadrez[1][4]["peca"] == "REI"

    # 2
    def test_movimento_frente_valido_preto(self):
        tab = Tabuleiro()
        tab.mover_peao(6, 4, 4, 4)
        tab.mover_rei(7, 4, 6, 4)

        tab.exibir()
        assert tab.xadrez[7][4]["peca"] == ""
        assert tab.xadrez[6][4]["peca"] == "REI"

    # 3
    def test_movimento_valido_matar_inimigo_branco(self):
        tab = Tabuleiro()
        tab.mover_peao(6, 4, 5, 4)
        tab.mover_peao(5, 4, 4, 4)
        tab.mover_peao(4, 4, 3, 4)
        tab.mover_peao(1, 4, 2, 4)
        tab.mover_rei(0, 4, 1, 4)
        tab.mover_rei(1, 4, 2, 5)
        tab.mover_rei(2, 5, 3, 4)

        tab.exibir()
        assert tab.xadrez[2][5]["peca"] == ""
        assert tab.xadrez[3][4]["peca"] == "REI"

    # 4
    def test_movimento_valido_matar_inimigo_preto(self):
        tab = Tabuleiro()
        tab.mover_peao(1, 4, 3, 4)
        tab.mover_peao(3, 4, 4, 4)
        tab.mover_peao(4, 4, 5, 4)
        tab.mover_peao(6, 5, 4, 5)
        tab.mover_rei(7, 4, 6, 5)
        tab.mover_rei(6, 5, 5, 4)

        tab.exibir()
        assert tab.xadrez[6][5]["peca"] == ""
        assert tab.xadrez[5][4]["peca"] == "REI"

    # 5
    def test_movimento_invalido_posicao_mesmo_time_branco(self):
        tab = Tabuleiro()
        tab.mover_rei(0, 4, 1, 4)

        tab.exibir()
        assert tab.xadrez[0][4]["peca"] == "REI"
        assert tab.xadrez[1][4]["peca"] == "Peao"

    # 6
    def test_movimento_invalido_posicao_mesmo_time_preto(self):
        tab = Tabuleiro()
        tab.mover_rei(7, 4, 6, 4)

        tab.exibir()
        tab.exibir()
        assert tab.xadrez[7][4]["peca"] == "REI"
        assert tab.xadrez[6][4]["peca"] == "Peao"

    # 7
    def test_movimento_invalido_matar_inimigo_de_um_jeito_nao_permitido_lado_branco(
        self,
    ):
        tab = Tabuleiro()
        tab = Tabuleiro()
        tab.mover_peao(6, 4, 5, 4)
        tab.mover_peao(5, 4, 4, 4)
        tab.mover_peao(4, 4, 3, 4)
        tab.mover_peao(1, 4, 2, 4)
        tab.mover_rei(0, 4, 1, 4)
        tab.mover_rei(1, 4, 3, 4)

        tab.exibir()
        assert tab.xadrez[1][4]["peca"] == "REI"
        assert tab.xadrez[3][4]["peca"] == "Peao"

    # 8
    def test_movimento_invalido_matar_inimigo_de_um_jeito_nao_permitido_lado_preto(
        self,
    ):
        tab = Tabuleiro()
        tab = Tabuleiro()
        tab.mover_peao(1, 4, 3, 4)
        tab.mover_peao(3, 4, 4, 4)
        tab.mover_peao(4, 4, 5, 4)
        tab.mover_peao(6, 5, 4, 5)
        tab.mover_rei(7, 4, 4, 5)

        tab.exibir()
        assert tab.xadrez[7][4]["peca"] == "REI"
        assert tab.xadrez[4][5]["peca"] == "Peao"

    # 9
    def test_movimento_invalido_posicao_nao_permitida_lado_branco(self):
        tab = Tabuleiro()
        tab.mover_peao(1, 4, 3, 4)
        tab.mover_rei(0, 4, 2, 4)

        tab.exibir()
        assert tab.xadrez[0][4]["peca"] == "REI"
        assert tab.xadrez[2][4]["peca"] == ""

    # 10
    def test_movimento_invalido_posicao_nao_permitida_lado_preto(self):
        tab = Tabuleiro()
        tab.mover_peao(6, 4, 4, 4)
        tab.mover_rei(7, 4, 5, 4)

        assert tab.xadrez[7][4]["peca"] == "REI"
        assert tab.xadrez[5][4]["peca"] == ""

    # 11
    def test_movimento_valido_rock_esquerda(self):
        tab = Tabuleiro()
        tab.mover_cavalo(0, 1, 2, 0)
        tab.mover_cavalo(7, 1, 5, 0)
        tab.mover_peao(1, 3, 3, 3)
        tab.mover_peao(6, 3, 4, 3)
        tab.mover_bispo(0, 2, 2, 4)
        tab.mover_bispo(7, 2, 5, 4)
        tab.mover_rainha(0, 3, 1, 3)
        tab.mover_rainha(7, 3, 6, 3)
        tab.mover_rei(0, 4, 0, 2)
        tab.mover_rei(7, 4, 7, 2)

        tab.exibir()
        assert tab.xadrez[7][4]["peca"] == ""
        assert tab.xadrez[7][2]["peca"] == "REI"

    # 12
    def test_movimento_valido_rock_direita(self):
        tab = Tabuleiro()
        tab.mover_cavalo(0, 6, 2, 7)
        tab.mover_cavalo(7, 6, 5, 7)
        tab.mover_peao(1, 4, 3, 4)
        tab.mover_peao(6, 4, 4, 4)
        tab.mover_bispo(0, 5, 2, 3)
        tab.mover_bispo(7, 5, 5, 3)
        tab.mover_rei(0, 4, 0, 6)
        tab.mover_rei(7, 4, 7, 6)

        tab.exibir()
        assert tab.xadrez[7][4]["peca"] == ""
        assert tab.xadrez[7][6]["peca"] == "REI"
