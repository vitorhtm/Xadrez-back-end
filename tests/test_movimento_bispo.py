from class_tab import Tabuleiro
import unittest


class TestMovimentoBispo(unittest.TestCase):
#1
    def test_movimento_frente_valido_branco(self):
        tab = Tabuleiro()
        tab.mover_peao(1,1,2,1)
        tab.mover_bispo(0,2,2,0)        
        
        assert tab.xadrez[0][2]['peca'] == ""
        assert tab.xadrez[2][0]['peca'] == "Bispo"
#2
    def test_movimento_frente_valido_preto(self):
        tab = Tabuleiro()
        tab.mover_peao(6,1,5,1)
        tab.mover_bispo(7,2,5,0)        
        
        assert tab.xadrez[7][2]['peca'] == ""
        assert tab.xadrez[5][0]['peca'] == "Bispo"
#3
    def test_movimento_valido_matar_peca_inimiga_branco(self):
        tab = Tabuleiro()
        tab.mover_peao(1,1,2,1)
        tab.mover_bispo(0,2,2,0)
        tab.mover_bispo(2,0,6,4)
        
        assert tab.xadrez[2][0]['peca'] == ""
        assert tab.xadrez[6][4]['peca'] == "Bispo"
#4
    def test_movimento_valido_matar_peca_inimiga_preto(self):
        tab = Tabuleiro()
        tab.mover_peao(6,1,5,1)
        tab.mover_bispo(7,2,5,0)
        tab.mover_bispo(5,0,1,4)
        
        assert tab.xadrez[5][0]['peca'] == ""
        assert tab.xadrez[1][4]['peca'] == "Bispo"
#5  
    def test_movimento_invalido_jogar_na_mesma_posicao_do_meu_time_branco(self):
        tab = Tabuleiro()
        tab.mover_bispo(0,2,1,1)
        
        assert tab.xadrez[0][2]['peca'] == "Bispo"
        assert tab.xadrez[1][1]['peca'] == "Peao"
#6
    def test_movimento_invalido_jogar_na_mesma_posicao_do_meu_time_preto(self):
        tab = Tabuleiro()
        tab.mover_bispo(7,2,6,1)
        
        assert tab.xadrez[7][2]['peca'] == "Bispo"
        assert tab.xadrez[6][1]['peca'] == "Peao"
#7
    def test_movimento_invalido_jogar_pulando_peca_do_mesmo_time_lado_branco(self):
        tab = Tabuleiro()
        tab.mover_bispo(0,2,2,0)
        
        assert tab.xadrez[0][2]['peca'] == "Bispo"
        assert tab.xadrez[2][0]['peca'] == ""
#8    
    def test_movimento_invalido_jogar_pulando_peca_do_mesmo_time_lado_preto(self):
        tab = Tabuleiro()
        tab.mover_bispo(7,2,5,0)
        
        tab.exibir()
        assert tab.xadrez[7][2]['peca'] == "Bispo"
        assert tab.xadrez[5][0]['peca'] == ""
#9
    def test_movimento_invalido_matar_peca_inimiga_de_um_jeito_nao_permitido_branco(self):
        tab = Tabuleiro()
        tab.mover_peao(1,1,2,1) 
        tab.mover_bispo(0,2,2,0)
        tab.mover_bispo(2,0,5,3)
        tab.mover_bispo(5,3,6,3)

        assert tab.xadrez[5][3]['peca'] == "Bispo"
        assert tab.xadrez[6][3]['peca'] == "Peao"
#10
    def test_movimento_invalido_matar_peca_inimiga_de_um_jeito_nao_permitido_preto(self):
        tab = Tabuleiro()
        tab.mover_peao(6,1,5,1) 
        tab.mover_bispo(7,2,5,0)
        tab.mover_bispo(5,0,2,3)
        tab.mover_bispo(2,3,1,3)

        assert tab.xadrez[2][3]['peca'] == "Bispo"
        assert tab.xadrez[1][3]['peca'] == "Peao"
#11
    def test_movimento_invalido_mover_pra_uma_posicao_que_a_peca_nao0_pode_ir_lado_branco(self):
        tab = Tabuleiro()
        tab.mover_peao(1,1,2,1) 
        tab.mover_bispo(0,2,2,0)
        tab.mover_bispo(2,0,4,2)
        tab.mover_bispo(4,2,4,1)

        tab.exibir()
        assert tab.xadrez[4][2]['peca'] == "Bispo"
        assert tab.xadrez[4][1]['peca'] == ""
#12
    def test_movimento_invalido_mover_pra_uma_posicao_que_a_peca_nao0_pode_ir_lado_preto(self):
        tab = Tabuleiro()
        tab.mover_peao(6,1,5,1) 
        tab.mover_bispo(7,2,5,0)
        tab.mover_bispo(5,0,4,1)
        tab.mover_bispo(4,1,4,2)

        tab.exibir()
        assert tab.xadrez[4][1]['peca'] == "Bispo"
        assert tab.xadrez[4][2]['peca'] == ""