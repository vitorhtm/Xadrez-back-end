from class_tab import Tabuleiro
import unittest


class TestMovimentoCavalo(unittest.TestCase):
#1
    def test_movimento_frente_valido_branco(self):
        tab = Tabuleiro()
        tab.mover_cavalo(0,1,2,0)        
        
        assert tab.xadrez[0][1]['peca'] == ""
        assert tab.xadrez[2][0]['peca'] == "Cavalo"
#2
    def test_movimento_frente_valido_preto(self):
        tab = Tabuleiro()
        tab.mover_cavalo(0,1,2,0)        
        
        assert tab.xadrez[0][1]['peca'] == ""
        assert tab.xadrez[2][0]['peca'] == "Cavalo"
#3
    def test_movimento_frente_valido_matar_peca_inimiga_lado_branco(self):
        tab = Tabuleiro()
        tab.mover_cavalo(0,1,2,0)        
        tab.mover_peao(6,1,4,1)
        tab.mover_cavalo(2,0,4,1) 

        tab.exibir()
        assert tab.xadrez[2][0]['peca'] == ""
        assert tab.xadrez[4][1]['peca'] == "Cavalo"
#4
    def test_movimento_frente_valido_matar_peca_inimiga_lado_preto(self):
        tab = Tabuleiro()
        tab.mover_cavalo(0,1,2,0)
        tab.mover_cavalo(2,0,3,2)
        tab.mover_cavalo(3,2,4,4)
        tab.mover_cavalo(4,4,5,2)                 
        tab.mover_cavalo(7,1,5,0)
        tab.mover_cavalo(5,0,3,1)
        tab.mover_cavalo(3,1,5,2)  
          

        assert tab.xadrez[3][1]['peca'] == ""
        assert tab.xadrez[5][2]['peca'] == "Cavalo"
#5
    def test_movimento_invalido_mover_para_casa_ocupada_pelo_mesmo_time_lado_branco(self):
        tab = Tabuleiro()
        tab.mover_cavalo(0,6,1,4)         

        assert tab.xadrez[0][6]['peca'] == "Cavalo"
        assert tab.xadrez[1][4]['peca'] == "Peao"
#6
    def test_movimento_invalido_mover_para_casa_ocupada_pelo_mesmo_time_lado_preto(self):
        tab = Tabuleiro()
        tab.mover_cavalo(7,6,6,4)         

        assert tab.xadrez[7][6]['peca'] == "Cavalo"
        assert tab.xadrez[6][4]['peca'] == "Peao"
#7
    def test_movimento_invalido_matar_peca_inimiga_de_um_jeito_nao_permitido_lado_branco(self):
        tab = Tabuleiro()         
        tab.mover_cavalo(0,1,2,0)
        tab.mover_peao(6,0,4,0)
        tab.mover_peao(4,0,3,0)
        tab.mover_cavalo(2,0,3,0)

        assert tab.xadrez[2][0]['peca'] == "Cavalo"
        assert tab.xadrez[3][0]['peca'] == "Peao"
#8
    def test_movimento_invalido_matar_peca_inimiga_de_um_jeito_nao_permitido_lado_preto(self):
        tab = Tabuleiro()         
        tab.mover_cavalo(7,1,5,0)
        tab.mover_peao(1,0,3,0)
        tab.mover_peao(3,0,4,0)
        tab.mover_cavalo(5,0,4,0)

        assert tab.xadrez[5][0]['peca'] == "Cavalo"
        assert tab.xadrez[4][0]['peca'] == "Peao"
#9
    def test_movimento_invalido_mover_pra_uma_posicao_invalida_lado_branco(self):
        tab = Tabuleiro()         
        tab.mover_cavalo(0,1,4,1)

        assert tab.xadrez[0][1]['peca'] == "Cavalo"
        assert tab.xadrez[4][1]['peca'] == ""
#10
    def test_movimento_invalido_mover_pra_uma_posicao_invalida_lado_preto(self):
        tab = Tabuleiro()         
        tab.mover_cavalo(7,1,5,1)

        assert tab.xadrez[7][1]['peca'] == "Cavalo"
        assert tab.xadrez[5][1]['peca'] == ""