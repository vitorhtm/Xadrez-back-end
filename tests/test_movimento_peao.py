from class_tab import Tabuleiro
import unittest


class TestMovimentoPeao(unittest.TestCase):
#1
    def test_movimento_frente_valido_peao_branco(self):
        tab = Tabuleiro()
        tab.mover_peao(1,0,2,0)        
        
        assert tab.xadrez[1][0]['peca'] == ""
        assert tab.xadrez[2][0]['peca'] == "Peao"
#2
    def test_movimento_frente_valido_peao_preto(self):
        tab = Tabuleiro()
        tab.mover_peao(6,0,5,0)        
        
        assert tab.xadrez[6][0]['peca'] == ""
        assert tab.xadrez[5][0]['peca'] == "Peao"
#3
    def test_movimento_invalido_posicao_com_peca_do_mesmo_time_branco(self):
        tab = Tabuleiro()
        tab.mover_cavalo(0,1,2,0)
        tab.mover_peao(1,0,2,0)        
        
        assert tab.xadrez[1][0]['peca'] == "Peao"
        assert tab.xadrez[2][0]['peca'] == "Cavalo" 
#4
    def test_movimento_frente_invalido_posicao_com_peca_do_mesmo_time_preto(self):
        tab = Tabuleiro()
        tab.mover_cavalo(7,1,5,0)
        tab.mover_peao(6,0,5,0)        
        
        assert tab.xadrez[6][0]['peca'] == "Peao"
        assert tab.xadrez[5][0]['peca'] == "Cavalo"
#5
    def test_movimento_invalido_pular_peca_do_mesmo_time_branco(self):
        tab = Tabuleiro()
        tab.mover_cavalo(0,1,2,0)
        tab.mover_peao(1,0,3,0)        
        
        tab.exibir()
        assert tab.xadrez[1][0]['peca'] == "Peao"
        assert tab.xadrez[2][0]['peca'] == "Cavalo"
#6
    def test_movimento_invalido_pular_peca_do_mesmo_time_preto(self):
        tab = Tabuleiro()
        tab.mover_cavalo(7,1,5,0)
        tab.mover_peao(6,0,5,0)        
        
        assert tab.xadrez[6][0]['peca'] == "Peao"
        assert tab.xadrez[5][0]['peca'] == "Cavalo"
#7
    def test_movimento_lado_invalido_casa_ocupada_mesmo_time_branco(self):
        tab = Tabuleiro()
        tab.mover_peao(1,0,1,1)        
        
        assert tab.xadrez[1][0]['peca'] == "Peao"
        assert tab.xadrez[1][1]['peca'] == "Peao"
#8
    def test_movimento_lado_invalido_casa_ocupada_mesmo_time_preto(self):
        tab = Tabuleiro()
        tab.mover_peao(6,0,6,1)        
        
        assert tab.xadrez[6][0]['peca'] == "Peao"
        assert tab.xadrez[6][1]['peca'] == "Peao"
#9
    def test_movimento_valido_lado_branco_matando_peca(self):
        tab = Tabuleiro()
        tab.mover_peao(1,0,3,0)
        tab.mover_peao(6,1,4,1)
        tab.mover_peao(3,0,4,1)                
        
        assert tab.xadrez[3][0]['peca'] == ""
        assert tab.xadrez[4][1]['peca'] == "Peao"
#10
    def test_movimento_valido_lado_preto_matando_peca(self):
        tab = Tabuleiro()
        tab.mover_peao(1,0,3,0)
        tab.mover_peao(6,1,4,1)
        tab.mover_peao(4,1,3,0)        
        
        assert tab.xadrez[4][1]['peca'] == ""
        assert tab.xadrez[3][0]['peca'] == "Peao"
 #11
    def test_movimento_invalido_andando_duas_casas_fora_da_posicao_permitida_branco(self):
        tab = Tabuleiro()
        tab.mover_peao(1,0,3,0)
        tab.mover_peao(3,0,5,0)
        
        assert tab.xadrez[3][0]['peca'] == "Peao"
        assert tab.xadrez[5][0]['peca'] == ""
#12
    def test_movimento_invalido_andando_duas_casas_fora_da_posicao_permitida_preto(self):
        tab = Tabuleiro()
        tab.mover_peao(6,0,4,0)
        tab.mover_peao(4,0,2,0)
        
        assert tab.xadrez[4][0]['peca'] == "Peao"
        assert tab.xadrez[2][0]['peca'] == ""
#13
    def test_movimento_diagonal_invalido_sem_matar_outra_peca_lado_branco(self):
        tab = Tabuleiro()
        tab.mover_peao(1,0,2,1)
        
        assert tab.xadrez[1][0]['peca'] == "Peao"
        assert tab.xadrez[2][1]['peca'] == ""
#14
    def test_movimento_diagonal_invalido_sem_matar_outra_peca_lado_preto(self):
        tab = Tabuleiro()
        tab.mover_peao(6,0,5,1)
        
        assert tab.xadrez[6][0]['peca'] == "Peao"
        assert tab.xadrez[5][1]['peca'] == ""
#15
    def test_movimento_invalido_peca_andando_pra_tras_lado_branco(self):
        tab = Tabuleiro()
        tab.mover_peao(1,0,3,0)
        tab.mover_peao(3,0,2,0)
        
        
        assert tab.xadrez[3][0]['peca'] == "Peao"
        assert tab.xadrez[2][0]['peca'] == ""
#16
    def test_movimento_invalido_peca_andando_pra_tras_lado_preto(self):
        tab = Tabuleiro()
        tab.mover_peao(6,0,4,0)
        tab.mover_peao(4,0,5,0)
        
        assert tab.xadrez[4][0]['peca'] == "Peao"
        assert tab.xadrez[5][0]['peca'] == ""
#17
    def test_movimento_invalido_matando_peca_inimiga_de_um_jeito_nao_permitido_lado_branco(self):
        tab = Tabuleiro()
        tab.mover_peao(1,0,3,0)
        tab.mover_peao(6,0,4,0)
        tab.mover_peao(3,0,4,0) 
        
        tab.exibir()
        assert tab.xadrez[3][0]['peca'] == "Peao"
        assert tab.xadrez[4][0]['peca'] == "Peao"
#18
    def test_movimento_invalido_matando_peca_inimiga_de_um_jeito_nao_permitido_lado_preto(self):
        tab = Tabuleiro()
        tab.mover_peao(1,0,3,0)
        tab.mover_peao(6,0,4,0)
        tab.mover_peao(4,0,3,0) 
        
        tab.exibir()
        assert tab.xadrez[4][0]['peca'] == "Peao"
        assert tab.xadrez[3][0]['peca'] == "Peao"