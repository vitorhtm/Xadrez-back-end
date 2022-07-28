from tabulate import tabulate


class Tabuleiro:
    xadrez = {}
    jogadas_branco = 0
    jogadas_preto = 0
    contador_rei = 0

    def __init__(
        self,
    ):
        self.montar_xadrez()
        self.cavalos()
        self.torre()
        self.peao()
        self.bispo()
        self.rainha()
        self.rei()

    def montar_xadrez(self):
        self.xadrez[0] = self.colunas_da_linha()
        self.xadrez[1] = self.colunas_da_linha()
        self.xadrez[2] = self.colunas_da_linha()

        for linha in range(0, 8):
            self.xadrez[linha] = self.colunas_da_linha()

    def colunas_da_linha(self):
        colunas = {}
        for key in range(0, 8):
            colunas[key] = {"peca": "", "cor": ""}

        return colunas

    def posiciona_peca(self, linha, coluna, peca, cor):
        self.xadrez[linha][coluna].update(
            {
                "peca": peca,
                "cor": cor,
            }
        )

    def cavalos(self):
        self.posiciona_peca(linha=0, coluna=1, peca="Cavalo", cor="Branco")
        self.posiciona_peca(linha=0, coluna=6, peca="Cavalo", cor="Branco")

        self.posiciona_peca(linha=7, coluna=1, peca="Cavalo", cor="Preto")
        self.posiciona_peca(linha=7, coluna=6, peca="Cavalo", cor="Preto")

    def torre(self):
        self.posiciona_peca(linha=0, coluna=0, peca="Torre", cor="Branco")
        self.posiciona_peca(linha=0, coluna=7, peca="Torre", cor="Branco")

        self.posiciona_peca(linha=7, coluna=0, peca="Torre", cor="Preto")
        self.posiciona_peca(linha=7, coluna=7, peca="Torre", cor="Preto")

    def peao(self):
        def add_peao(linha, cor):
            for coluna in range(0, 8):
                self.posiciona_peca(
                    linha=linha,
                    coluna=coluna,
                    peca="Peao",
                    cor=cor,
                )

        add_peao(linha=1, cor="Branco")
        add_peao(linha=6, cor="Preto")

    def bispo(self):
        self.posiciona_peca(linha=0, coluna=2, peca="Bispo", cor="Branco")
        self.posiciona_peca(linha=0, coluna=5, peca="Bispo", cor="Branco")

        self.posiciona_peca(linha=7, coluna=2, peca="Bispo", cor="Preto")
        self.posiciona_peca(linha=7, coluna=5, peca="Bispo", cor="Preto")

    def rainha(self):
        self.posiciona_peca(linha=0, coluna=3, peca="Rainha", cor="Branco")

        self.posiciona_peca(linha=7, coluna=3, peca="Rainha", cor="Preto")

    def rei(self):
        self.posiciona_peca(
            linha=0,
            coluna=4,
            peca="REI",
            cor="Branco",
        )

        self.posiciona_peca(
            linha=7,
            coluna=4,
            peca="REI",
            cor="Preto",
        )

    def mover_peao(self, linha_atual, coluna_atual, futura_linha, futura_coluna):
        peca = self.xadrez[linha_atual][coluna_atual]["peca"]

        if peca == "Peao":
            dife_linha = self.comparar_linhas(linha_atual, futura_linha)

            peca_cor = self.xadrez[linha_atual][coluna_atual]["cor"]
            cor_peca_futura = self.xadrez[futura_linha][futura_coluna]["cor"]

            dife_coluna = self.validar_coluna_peao(
                dife_linha, coluna_atual, futura_coluna
            )

            jogada = self.comparar_jogada_p(
                linha_atual, dife_linha, dife_coluna, peca_cor, cor_peca_futura
            )
            if jogada == 0:
                print("jogada invalida")
                return
            validar_movimento = self.validar_movimento(
                linha_atual, futura_linha, coluna_atual, futura_coluna
            )
            if validar_movimento == 1:
                self.comparar_cor(
                    linha_atual, futura_linha, coluna_atual, futura_coluna
                )

            else:
                print("jogada invalida")

    def mover_cavalo(self, linha_atual, coluna_atual, futura_linha, futura_coluna):

        peca = self.xadrez[linha_atual][coluna_atual]["peca"]

        if peca == "Cavalo":
            dife_linha = self.comparar_linhas(linha_atual, futura_linha)

            if dife_linha == 2 or dife_linha == 1:
                dife_coluna = self.comparar_colunas(coluna_atual, futura_coluna)
                if dife_coluna == 0:
                    return

                validar_jogadas = self.comparar_jogada_c(dife_linha, dife_coluna)
                if validar_jogadas == 0:
                    print("jogada invalida")
                    return
                self.comparar_cor(
                    linha_atual, futura_linha, coluna_atual, futura_coluna
                )

            else:
                print("jogada invalida")

    def mover_bispo(self, linha_atual, coluna_atual, futura_linha, futura_coluna):

        peca = self.xadrez[linha_atual][coluna_atual]["peca"]
        if peca == "Bispo":
            dife_linha = self.comparar_linhas(linha_atual, futura_linha)

            lista = list(range(8))
            if dife_linha == lista.index(dife_linha):

                dife_coluna = self.comparar_colunas(coluna_atual, futura_coluna)
                if dife_coluna == 0:
                    return

                if dife_coluna == lista.index(dife_coluna):
                    jogada = self.comparar_jogadas_b(dife_linha, dife_coluna)
                    if jogada == 0:
                        return

                    validar_movimento = self.validar_movimento_b_r(
                        linha_atual, futura_linha, coluna_atual, futura_coluna
                    )
                    if validar_movimento == 1:
                        self.comparar_cor(
                            linha_atual, futura_linha, coluna_atual, futura_coluna
                        )

                else:
                    print("jogada invalida")

    def pegar_peca(self, linha, coluna):
        return self.xadrez[linha][coluna]

    def mover_torre(self, linha_atual, coluna_atual, futura_linha, futura_coluna):
        peca = self.xadrez[linha_atual][coluna_atual]["peca"]

        if peca == "Torre":
            dife_linha = self.comparar_linhas(linha_atual, futura_linha)

            lista = list(range(0, 8))
            if dife_linha == lista.index(dife_linha):

                dife_coluna = self.comparar_colunas(coluna_atual, futura_coluna)
                if dife_coluna == 10:
                    return

                if dife_coluna == lista.index(dife_coluna):
                    validar_jogada = self.comparar_jogadas_t(dife_linha, dife_coluna)
                    if validar_jogada == 0:
                        return

                    validar_movimento = self.validar_movimento(
                        linha_atual, futura_linha, coluna_atual, futura_coluna
                    )
                    if validar_movimento == 1:
                        self.comparar_cor(
                            linha_atual, futura_linha, coluna_atual, futura_coluna
                        )

            else:
                print("jogada invalida")

    def mover_rei(self, linha_atual, coluna_atual, futura_linha, futura_coluna):

        peca_atual = self.pegar_peca(linha_atual, coluna_atual)
        if peca_atual["peca"] == "REI":
            dife_linha = self.comparar_linhas(linha_atual, futura_linha)

            if dife_linha == 1 or dife_linha == 0:
                dife_coluna = self.comparar_colunas(coluna_atual, futura_coluna)
                if dife_coluna == 10:
                    return

                def mov():
                    self.comparar_cor(
                        linha_atual,
                        futura_linha,
                        coluna_atual,
                        futura_coluna,
                    )
                    self.comparar_cor(
                        linha_atual,
                        futura_linha,
                        coluna_atual,
                        futura_coluna,
                    )

                if self.contador_rei == 0:
                    if dife_linha == 0 and dife_coluna == 2:

                        if coluna_atual > futura_coluna:
                            if peca_atual["cor"] == "Branco":
                                self.mover_torre(0, 0, 0, 3)
                                mov()

                            if peca_atual["cor"] == "Preto":
                                self.mover_torre(7, 0, 7, 3)
                                mov()

                        if coluna_atual < futura_coluna:
                            if peca_atual["cor"] == "Branco":
                                self.mover_torre(0, 7, 0, 5)
                                mov()

                            if peca_atual["cor"] == "Preto":
                                self.mover_torre(7, 7, 7, 5)
                                mov()
                        return

                print("aki")
                if dife_linha == 1 and dife_coluna == 1:
                    self.contador_rei = self.contador_rei + 1
                    self.comparar_cor(
                        linha_atual, futura_linha, coluna_atual, futura_coluna
                    )

                validar_jogada = self.comparar_jogadas_r(dife_linha, dife_coluna)
                if validar_jogada == 0:
                    return

                self.contador_rei = self.contador_rei + 1
                self.comparar_cor(
                    linha_atual, futura_linha, coluna_atual, futura_coluna
                )
            else:
                print("jogada invalida")

    def mover_rainha(self, linha_atual, coluna_atual, futura_linha, futura_coluna):

        peca = self.xadrez[linha_atual][coluna_atual]["peca"]

        if peca == "Rainha":
            dife_linha = self.comparar_linhas(linha_atual, futura_linha)

            lista = list(range(8))
            if dife_linha <= 7:
                dife_coluna = self.comparar_colunas(coluna_atual, futura_coluna)
                if dife_coluna == 10:
                    return

                if dife_coluna == lista.index(dife_coluna):

                    if dife_linha == dife_coluna:
                        validar_movimento_b_r = self.validar_movimento_b_r(
                            linha_atual, futura_linha, coluna_atual, futura_coluna
                        )
                        if validar_movimento_b_r == 1:
                            self.comparar_cor(
                                linha_atual, futura_linha, coluna_atual, futura_coluna
                            )

                    jogada = self.comparar_jogadas_ra(dife_linha, dife_coluna)
                    if jogada == 0:
                        return

                    if linha_atual < futura_linha:
                        if coluna_atual == futura_coluna:
                            validar_movimento = self.validar_movimento(
                                linha_atual, futura_linha, coluna_atual, futura_coluna
                            )
                            if validar_movimento == 1:
                                self.comparar_cor(
                                    linha_atual,
                                    futura_linha,
                                    coluna_atual,
                                    futura_coluna,
                                )

                    if linha_atual > futura_linha:
                        if coluna_atual == futura_coluna:
                            validar_movimento = self.validar_movimento(
                                linha_atual, futura_linha, coluna_atual, futura_coluna
                            )
                            if validar_movimento == 1:
                                self.comparar_cor(
                                    linha_atual,
                                    futura_linha,
                                    coluna_atual,
                                    futura_coluna,
                                )

                else:
                    print("jogada invalida")

    def comparar_cor(self, linha_atual, futura_linha, coluna_atual, futura_coluna):
        peca_atual = self.pegar_peca(linha_atual, coluna_atual)
        peca_futura = self.pegar_peca(futura_linha, futura_coluna)

        if peca_atual["cor"] == "Branco":
            if peca_futura["cor"] == "Preto":
                self.posiciona_peca(
                    linha=futura_linha,
                    coluna=futura_coluna,
                    peca=peca_atual["peca"],
                    cor=peca_atual["cor"],
                )
                self.posiciona_peca(
                    linha=linha_atual, coluna=coluna_atual, peca="", cor=""
                )
                return

            if not peca_futura["peca"]:
                self.posiciona_peca(
                    linha=futura_linha,
                    coluna=futura_coluna,
                    peca=peca_atual["peca"],
                    cor=peca_atual["cor"],
                )
                self.posiciona_peca(
                    linha=linha_atual, coluna=coluna_atual, peca="", cor=""
                )
                return

            if ["cor"] == "Branco":

                return 1

        if peca_atual["cor"] == "Preto":
            if peca_futura["cor"] == "Branco":
                self.posiciona_peca(
                    linha=futura_linha,
                    coluna=futura_coluna,
                    peca=peca_atual["peca"],
                    cor=peca_atual["cor"],
                )
                self.posiciona_peca(
                    linha=linha_atual, coluna=coluna_atual, peca="", cor=""
                )
                return

            if not peca_futura["peca"]:
                self.posiciona_peca(
                    linha=futura_linha,
                    coluna=futura_coluna,
                    peca=peca_atual["peca"],
                    cor=peca_atual["cor"],
                )
                self.posiciona_peca(
                    linha=linha_atual, coluna=coluna_atual, peca="", cor=""
                )
                return

            else:
                print("Jogada invalida, mesmo time")
                return

    def comparar_jogadas_ra(self, dife_linha, dife_coluna):

        if dife_linha != 0 and dife_coluna != 0:
            print("jogada invalida")
            return 0

        return

    def comparar_jogadas_r(self, dife_linha, dife_coluna):

        if dife_linha == 0 and dife_coluna != 1:
            print("jogada invalida")
            return 0

        if dife_linha == 1 and dife_coluna != 0:
            print("jogada invalida")
            return 0
        return

    def comparar_jogadas_t(self, dife_linha, dife_coluna):
        if dife_linha == dife_coluna:
            return 0

        if dife_linha != 0 and dife_coluna != 0:
            return 0

        return

    def comparar_jogadas_b(self, dife_linha, dife_coluna):
        if dife_linha != dife_coluna:
            print("jogada invalida")
            return 0
        return

    def comparar_jogada_c(self, dife_linha, dife_coluna):
        if dife_linha == 2 and dife_coluna != 1:
            return 0
        if dife_coluna == 2 and dife_linha != 1:
            return 0
        if dife_coluna == 1 and dife_linha == 1:
            return 0
        else:
            return

    def comparar_jogada_p(
        self, linha_atual, dife_linha, dife_coluna, peca_cor, cor_peca_futura
    ):

        if dife_linha == 2 or dife_linha == 1:
            if linha_atual == 6 or linha_atual == 1:
                if dife_linha == 2:
                    if dife_coluna == 0:
                        return

            if dife_linha == 1:
                if dife_coluna == 0:
                    return

            if dife_linha == 1:
                if dife_coluna == 1:
                    if peca_cor == "Branco":
                        if cor_peca_futura == "Preto":
                            return

            if dife_linha == 1:
                if dife_coluna == 1:
                    if peca_cor == "Preto":
                        if cor_peca_futura == "Branco":
                            return

            else:
                return 0

        return 0

    def validar_coluna_peao(self, dife_linha, coluna_atual, futura_coluna):

        if dife_linha == 2 or dife_linha == 1:
            if futura_coluna > coluna_atual:
                dife_coluna = futura_coluna - coluna_atual
                return dife_coluna

            if futura_coluna == coluna_atual:
                dife_coluna = coluna_atual - futura_coluna
                return dife_coluna

            else:
                dife_coluna = coluna_atual - futura_coluna
                return dife_coluna

        else:
            print("jogada invalida")

    def comparar_linhas(self, linha_atual, futura_linha):
        if linha_atual > futura_linha:
            dife_linha = linha_atual - futura_linha
            return dife_linha
        if futura_linha > linha_atual:
            dife_linha = futura_linha - linha_atual
            return dife_linha
        if futura_linha == linha_atual:
            dife_linha = futura_linha - linha_atual
            return dife_linha
        if linha_atual == futura_linha:
            dife_linha = linha_atual - futura_linha
            return dife_linha

    def comparar_colunas(self, coluna_atual, futura_coluna):
        dife_coluna = None
        if coluna_atual > futura_coluna:
            dife_coluna = coluna_atual - futura_coluna
            return dife_coluna

        if futura_coluna > coluna_atual:
            dife_coluna = futura_coluna - coluna_atual
            return dife_coluna

        if coluna_atual == futura_coluna:
            dife_coluna = coluna_atual - futura_coluna
            return dife_coluna

        if not dife_coluna:
            return 10

    def validar_movimento_b_r(
        self, linha_atual, futura_linha, coluna_atual, futura_coluna
    ):
        lista_linha = range(linha_atual, futura_linha + 1)
        lista_coluna = range(coluna_atual, futura_coluna + 1)

        lista_linha_reverse = range(linha_atual, futura_linha - 1, -1)
        lista_coluna_reverse = range(coluna_atual, futura_coluna - 1, -1)

        peca_a_ser_movida = self.pegar_peca(linha_atual, coluna_atual)

        if linha_atual < futura_linha:
            if coluna_atual > futura_coluna:
                for indice in range(0, len(lista_linha)):
                    peca_frente = self.pegar_peca(
                        lista_linha[indice], lista_coluna_reverse[indice]
                    )

                    if peca_frente.get("peca") == peca_a_ser_movida["peca"]:
                        continue

                    if peca_frente.get("cor") == "Preto":
                        return

                    if peca_frente.get("cor") == "Branco":
                        return

                    else:
                        return 1

        if linha_atual < futura_linha:
            if coluna_atual < futura_coluna:
                for indice in range(0, len(lista_linha)):
                    peca_frente = self.pegar_peca(
                        lista_linha[indice], lista_coluna[indice]
                    )

                    if peca_frente.get("peca") == peca_a_ser_movida["peca"]:
                        continue

                    if peca_frente.get("cor") == "Preto":
                        return

                    if peca_frente.get("cor") == "Branco":
                        return

                    else:
                        return 1

        if linha_atual > futura_linha:
            if coluna_atual > futura_coluna:
                for indice in range(0, len(lista_linha_reverse)):
                    peca_frente = self.pegar_peca(
                        lista_linha_reverse[indice], lista_coluna_reverse[indice]
                    )

                    if peca_frente.get("peca") == peca_a_ser_movida["peca"]:
                        continue

                    if peca_frente.get("cor") == "Preto":
                        return

                    if peca_frente.get("cor") == "Branco":
                        return

                    else:
                        return 1

        if linha_atual > futura_linha:
            if coluna_atual < futura_coluna:
                for indice in range(0, len(lista_linha_reverse)):
                    peca_frente = self.pegar_peca(
                        lista_linha_reverse[indice], lista_coluna[indice]
                    )

                    if peca_frente.get("peca") == peca_a_ser_movida["peca"]:
                        continue

                    if peca_frente.get("cor") == "Preto":
                        return

                    if peca_frente.get("cor") == "Branco":
                        return

                    else:
                        return 1

    def validar_movimento(self, linha_atual, futura_linha, coluna_atual, futura_coluna):
        lista_linha = range(linha_atual, futura_linha + 1)
        lista_coluna = range(coluna_atual, futura_coluna + 1)

        lista_linha_reverse = range(linha_atual, futura_linha - 1, -1)
        lista_coluna_reverse = range(coluna_atual, futura_coluna - 1, -1)

        peca_a_ser_movida = self.pegar_peca(linha_atual, coluna_atual)

        if linha_atual <= futura_linha:
            for linha in lista_linha:
                peca_frente = self.pegar_peca(linha, coluna_atual)

                if peca_a_ser_movida.get("peca") == "Peao":
                    if peca_a_ser_movida.get("cor") == "Preto":
                        if futura_linha > linha_atual:
                            return

                if peca_frente.get("peca") == "Peao":
                    if peca_a_ser_movida.get("peca") == "Peao":
                        if peca_frente.get("cor") == "Preto":
                            if peca_a_ser_movida.get("cor") == "Branco":
                                return

                if peca_frente["peca"] == peca_a_ser_movida["peca"]:
                    continue

                if peca_frente.get("cor") == peca_a_ser_movida.get("cor"):
                    print(
                        f"invalido, na linha:{linha}, coluna:{coluna_atual}, tem peca do mesmo time"
                    )
                    return

                if peca_frente.get("cor") == "Preto":
                    if futura_coluna == 0:
                        return

                if futura_coluna == 0:
                    if peca_frente.get("cor") == "Branco":
                        return
                else:
                    return 1

        if coluna_atual <= futura_coluna:
            for coluna in lista_coluna:
                peca_frente = self.pegar_peca(linha_atual, coluna)

                if not peca_frente.get("peca"):
                    continue

                if peca_frente["peca"] == peca_a_ser_movida["peca"]:
                    continue

                if peca_frente.get("cor") == peca_a_ser_movida.get("cor"):
                    print(
                        f"invalido, na linha:{linha_atual}, coluna:{coluna}, tem peca do mesmo time"
                    )
                    return

        if linha_atual >= futura_linha:
            for linha in lista_linha_reverse:
                peca_frente = self.pegar_peca(linha, coluna_atual)

                if peca_a_ser_movida.get("peca") == "Peao":
                    if peca_a_ser_movida.get("cor") == "Branco":
                        if futura_linha < linha_atual:
                            return

                if peca_frente.get("peca") == "Peao":
                    if peca_a_ser_movida.get("peca") == "Peao":
                        if peca_frente.get("cor") == "Branco":
                            if peca_a_ser_movida.get("cor") == "Preto":
                                return

                if not peca_frente.get("peca") and linha == futura_linha:
                    return 1

                if peca_frente["peca"] == peca_a_ser_movida["peca"]:
                    continue

                if peca_frente.get("cor") == peca_a_ser_movida.get("cor"):
                    print(
                        f"invalido, na linha:{linha}, coluna:{coluna_atual}, tem peca do mesmo time"
                    )
                    return

        if coluna_atual >= futura_coluna:
            for coluna in lista_coluna_reverse:
                peca_frente = self.pegar_peca(linha_atual, coluna)

                if not peca_frente.get("peca"):
                    continue

                if peca_frente["peca"] == peca_a_ser_movida["peca"]:
                    continue

                if peca_frente.get("cor") == peca_a_ser_movida.get("cor"):
                    print(
                        f"invalido, na linha:{linha_atual}, coluna:{coluna}, tem peca do mesmo time"
                    )
                    return

        return 1

    def exibir(self, mostrarcor=False):
        valores = []
        for linha in self.xadrez:
            valores_da_linha = []
            for coluna in self.xadrez[linha]:
                peca = self.xadrez[linha][coluna]
                show = f"{peca['peca']}({peca['cor']})"
                if mostrarcor:
                    valores_da_linha.append(show)
                else:
                    valores_da_linha.append(peca["peca"])
            valores.append(valores_da_linha)

        print(tabulate(valores, [], tablefmt="fancy_grid"))
        return tabulate(valores, [], tablefmt="html")

    def jogar(self, linha_atual, coluna_atual, futura_linha, futura_coluna):
        peca = self.xadrez[linha_atual][coluna_atual]

        if peca.get("cor") == "Branco":
            if self.jogadas_branco == self.jogadas_preto:
                self.jogadas_branco = self.jogadas_branco + 1

                if peca.get("peca") == "Peao":
                    self.mover_peao(
                        linha_atual, coluna_atual, futura_linha, futura_coluna
                    )

                if peca.get("peca") == "Torre":
                    self.mover_torre(
                        linha_atual, coluna_atual, futura_linha, futura_coluna
                    )

                if peca.get("peca") == "Cavalo":
                    self.mover_cavalo(
                        linha_atual, coluna_atual, futura_linha, futura_coluna
                    )

                if peca.get("peca") == "Bispo":
                    self.mover_bispo(
                        linha_atual, coluna_atual, futura_linha, futura_coluna
                    )

                if peca.get("peca") == "Rainha":
                    self.mover_rainha(
                        linha_atual, coluna_atual, futura_linha, futura_coluna
                    )

                if peca.get("peca") == "REI":
                    self.mover_rei(
                        linha_atual, coluna_atual, futura_linha, futura_coluna
                    )
            else:
                print("to aqui")
                return

        if peca.get("cor") == "Preto":
            if self.jogadas_preto != self.jogadas_branco:
                self.jogadas_preto = self.jogadas_preto + 1

                if peca.get("peca") == "Peao":
                    self.mover_peao(
                        linha_atual, coluna_atual, futura_linha, futura_coluna
                    )

                if peca.get("peca") == "Torre":
                    self.mover_torre(
                        linha_atual, coluna_atual, futura_linha, futura_coluna
                    )

                if peca.get("peca") == "Cavalo":
                    self.mover_cavalo(
                        linha_atual, coluna_atual, futura_linha, futura_coluna
                    )

                if peca.get("peca") == "Bispo":
                    self.mover_bispo(
                        linha_atual, coluna_atual, futura_linha, futura_coluna
                    )

                if peca.get("peca") == "Rainha":
                    self.mover_rainha(
                        linha_atual, coluna_atual, futura_linha, futura_coluna
                    )

                if peca.get("peca") == "REI":
                    self.mover_rei(
                        linha_atual, coluna_atual, futura_linha, futura_coluna
                    )

            else:
                print("to aqui")
                return
