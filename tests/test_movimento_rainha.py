from class_tab import Tabuleiro
import unittest


class TestMovimentoRainha(unittest.TestCase):
#1
    def test_movimento_frente_valido_branco(self):
        tab = Tabuleiro()
        tab.mover_peao(1,3,3,3)
        tab.mover_rainha(0,3,1,3)        
        
        tab.exibir()
        assert tab.xadrez[0][3]['peca'] == ""
        assert tab.xadrez[1][3]['peca'] == "Rainha"
#2
    def test_movimento_frente_valido_preto(self):
        tab = Tabuleiro()
        tab.mover_peao(6,3,4,3)
        tab.mover_rainha(7,3,6,3)        
        
        tab.exibir()
        assert tab.xadrez[7][3]['peca'] == ""
        assert tab.xadrez[6][3]['peca'] == "Rainha"
#3
    def test_movimento_valido_matar_peca_inimiga_lado_branco(self):
        tab = Tabuleiro()
        tab.mover_peao(1,4,2,4)
        tab.mover_rainha(0,3,2,5)
        tab.mover_rainha(2,5,6,5)        
        
        tab.exibir()
        assert tab.xadrez[2][5]['peca'] == ""
        assert tab.xadrez[6][5]['peca'] == "Rainha"
#4
    def test_movimento_valido_matar_peca_inimiga_lado_preto(self):
        tab = Tabuleiro()
        tab.mover_peao(6,4,4,4)
        tab.mover_rainha(7,3,5,5)
        tab.mover_rainha(5,5,1,5)        
        
        tab.exibir()
        assert tab.xadrez[5][5]['peca'] == ""
        assert tab.xadrez[1][5]['peca'] == "Rainha"
#5
    def test_movimento_invalido_mover_para_uma_posicao_do_mesmo_time_lado_branco(self):
        tab = Tabuleiro()
        tab.mover_rainha(0,3,0,4)        
        
        tab.exibir()
        assert tab.xadrez[0][3]['peca'] == "Rainha"
        assert tab.xadrez[0][4]['peca'] == "REI"
#6
    def test_movimento_invalido_mover_para_uma_posicao_do_mesmo_time_lado_preto(self):
        tab = Tabuleiro()
        tab.mover_rainha(7,3,7,4)        
        
        tab.exibir()
        assert tab.xadrez[7][3]['peca'] == "Rainha"
        assert tab.xadrez[7][4]['peca'] == "REI"
#7
    def test_movimento_invalido_tentar_pular_peca_do_mesmo_time_branco(self):
        tab = Tabuleiro()
        tab.mover_rainha(0,3,2,3)        
        
        tab.exibir()
        assert tab.xadrez[0][3]['peca'] == "Rainha"
        assert tab.xadrez[2][3]['peca'] == ""
#8
    def test_movimento_invalido_tentar_pular_peca_do_mesmo_time_preto(self):
        tab = Tabuleiro()
        tab.mover_peao(6,3,4,3)
        tab.mover_rainha(7,3,5,3)        
        
        tab.exibir()
        assert tab.xadrez[7][3]['peca'] == ""
        assert tab.xadrez[5][3]['peca'] == "Rainha"
#9 
    def test_movimento_invalido_matar_inimigo_com_uma_jogada_nao_permitida_lado_branco(self):
        tab = Tabuleiro()
        tab.mover_peao(1,4,2,4)
        tab.mover_rainha(0,3,2,5)
        tab.mover_rainha(2,5,4,5)
        tab.mover_rainha(4,5,6,6)        
        
        tab.exibir()
        assert tab.xadrez[4][5]['peca'] == "Rainha"
        assert tab.xadrez[6][6]['peca'] == "Peao"
#10/11/12 (foi testado ela andar em um movimento que ela não pode fazer.)
    def test_movimento_invalido_matar_inimigo_com_uma_jogada_nao_permitida_lado_preto(self):
        tab = Tabuleiro()
        tab.mover_peao(6,4,5,4)
        tab.mover_rainha(7,3,5,5)
        tab.mover_rainha(5,5,3,5)
        tab.mover_rainha(3,5,1,6)        
        
        tab.exibir()
        assert tab.xadrez[3][5]['peca'] == "Rainha"
        assert tab.xadrez[1][6]['peca'] == "Peao"
