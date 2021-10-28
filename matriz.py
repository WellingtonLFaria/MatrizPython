class matriz():
    def GerarMatriz(self, linhas, colunas):
        self.linhas = linhas
        self.colunas = colunas
        self.matriz = []
        for c in range(self.linhas):
            self.matriz.append([])
            for d in range(self.colunas):
                while True:
                    try:
                        valor = float(input(f'Qual o valor do elemento {c+1}x{d+1} da matriz: '))
                        self.matriz[c].append(valor)
                        break
                    except:
                        print('\033[30;41mPor favor digite um valor válido.\033[m')
        return self.matriz

# MANUAL DE USO NO ARQUIVO "exemplo_de_uso.py"