from class_tab import Tabuleiro
import unittest


class TestMovimentoTorre(unittest.TestCase):
#1
    def test_movimento_frente_valido_peao_branco(self):
        tab = Tabuleiro()
        tab.mover_peao(1,0,3,0)
        tab.mover_torre(0,0,2,0)
        
        
        assert tab.xadrez[0][0]['peca'] == ""
        assert tab.xadrez[2][0]['peca'] == "Torre"
#2    
    def test_movimento_frente_valido_peao_preto(self):
        tab = Tabuleiro()
        tab.mover_peao(6,0,4,0)
        tab.mover_torre(7,0,5,0)
        
        
        assert tab.xadrez[7][0]['peca'] == ""
        assert tab.xadrez[5][0]['peca'] == "Torre"
#3    
    def test_movimento_invalido_posicao_com_peca_do_mesmo_time_preto(self):
        tab = Tabuleiro()
        tab.mover_torre(7,0,6,0)
        
        
        assert tab.xadrez[7][0]['peca'] == "Torre"
        assert tab.xadrez[6][0]['peca'] == "Peao"
#4
    def test_movimento_invalido_posicao_com_peca_do_mesmo_time_branco(self):
        tab = Tabuleiro()
        tab.mover_torre(0,0,1,0)
        
        
        assert tab.xadrez[0][0]['peca'] == "Torre"
        assert tab.xadrez[1][0]['peca'] == "Peao"
#5
    def test_movimento_invalido_peca_do_mesmo_time_na_frente_preto(self):
        tab = Tabuleiro()
        tab.mover_torre(7,0,5,0)
        
        
        assert tab.xadrez[7][0]['peca'] == "Torre"
        assert tab.xadrez[5][0]['peca'] == ""
#6    
    def test_movimento_invalido_peca_do_mesmo_time_na_frente_branco(self):
        tab = Tabuleiro()
        tab.mover_torre(0,0,2,0)
        
        
        assert tab.xadrez[0][0]['peca'] == "Torre"
        assert tab.xadrez[2][0]['peca'] == ""
#7    
    def test_movimento_lado_invalido_casa_ocupada_mesmo_time_preto(self):
        tab = Tabuleiro()
        tab.mover_torre(7,0,7,1)
        
        
        assert tab.xadrez[7][0]['peca'] == "Torre"
        assert tab.xadrez[7][1]['peca'] == "Cavalo"
#8
    def test_movimento_lado_invalido_casa_ocupada_mesmo_time_branco(self):
        tab = Tabuleiro()
        tab.mover_torre(0,0,0,1)
        
        
        assert tab.xadrez[0][0]['peca'] == "Torre"
        assert tab.xadrez[0][1]['peca'] == "Cavalo"
#9
    def test_movimento_lado_valido_ordem_crescente_branco(self):
        tab = Tabuleiro()
        tab.mover_peao(1,0,3,0)
        tab.mover_torre(0,0,2,0)
        tab.mover_torre(2,0,2,4)
        
        
        assert tab.xadrez[2][0]['peca'] == ""
        assert tab.xadrez[2][4]['peca'] == "Torre"
#10
    def test_movimento_lado_valido_ordem_crescente_preto(self):
        tab = Tabuleiro()
        tab.mover_peao(6,0,4,0)
        tab.mover_torre(7,0,5,0)
        tab.mover_torre(5,0,5,4)
        
        
        assert tab.xadrez[5][0]['peca'] == ""
        assert tab.xadrez[5][4]['peca'] == "Torre"
#11
    def test_movimento_valido_lado_ordem_decrescente_branco(self):    
        tab = Tabuleiro()
        tab.mover_peao(1,0,3,0)
        tab.mover_torre(0,0,2,0)
        tab.mover_torre(2,0,2,4)
        tab.mover_torre(2,4,2,0)
        
        
        assert tab.xadrez[2][4]['peca'] == ""
        assert tab.xadrez[2][0]['peca'] == "Torre"
#12    
    def test_movimento_valido_lado_ordem_decrescente_preto(self): 
        tab = Tabuleiro()
        tab.mover_peao(6,0,4,0)
        tab.mover_torre(7,0,5,0)
        tab.mover_torre(5,0,5,4)
        tab.mover_torre(5,4,5,0)
        
        
        assert tab.xadrez[5][4]['peca'] == ""
        assert tab.xadrez[5][0]['peca'] == "Torre"
#13
    def test_movimento_invalido_diagonal_branco(self):
        tab = Tabuleiro()
        tab.mover_peao(1,1,3,1)
        tab.mover_torre(0,0,1,1)        
        
        assert tab.xadrez[0][0]['peca'] == "Torre"
        assert tab.xadrez[1][1]['peca'] == ""
#14    
    def test_movimento_invalido_diagonal_preto(self):
        tab = Tabuleiro()
        tab.mover_peao(6,1,4,1)
        tab.mover_torre(7,0,6,1)        
        
        assert tab.xadrez[7][0]['peca'] == "Torre"
        assert tab.xadrez[6][1]['peca'] == ""
    