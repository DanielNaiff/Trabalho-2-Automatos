class AutomatoFinito:
    def __init__(self, estados, alfabeto, transicoes, estado_inicial, estados_finais):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais

    def separarPalavras(self, entrada):
        # Remover apenas os pontos
        texto_sem_pontos = entrada.replace('.', '')
        return texto_sem_pontos.split()  # Retorna diretamente a lista de palavras

    def processar(self, entrada):
        palavras = self.separarPalavras(entrada)  # Captura a lista de palavras
        posicoes = []  
        
        # Manter a posição inicial na string original
        posicao_atual = 0
        
        for palavra in palavras:
            qa = self.estado_inicial  # Reinicia o estado para cada palavra
            for letra in palavra:  # Processa letra por letra
                if (qa, letra) in self.transicoes:
                    qa = self.transicoes[(qa, letra)]
                else:
                    qa = self.estado_inicial  # Reinicia se não houver transição
                    break  # Sai do loop se a transição falhar
            
            # Se chegou a um estado final, registra a posição da palavra na string original
            if qa in self.estados_finais:
                # Adiciona a posição da palavra na string original
                posicoes.append(entrada.find(palavra, posicao_atual))
            
            # Atualiza a posição atual (considerando a palavra e o espaço)
            posicao_atual += len(palavra) + 1  # +1 para o espaço

        return posicoes

estados = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10'}
alfabeto = {'c', 'o', 'm', 'p', 'u', 't', 'a', 'd', 'o', 'r'}
transicoes = {
    ('q0', 'c'): 'q1',
    ('q1', 'o'): 'q2',
    ('q2', 'm'): 'q3',
    ('q3', 'p'): 'q4',
    ('q4', 'u'): 'q5',
    ('q5', 't'): 'q6',
    ('q6', 'a'): 'q7',
    ('q7', 'd'): 'q8',
    ('q8', 'o'): 'q9',
    ('q9', 'r'): 'q10',
}
estado_inicial = 'q0'
estados_finais = {'q10'}

autômato = AutomatoFinito(estados, alfabeto, transicoes, estado_inicial, estados_finais)

entrada = """O computador é uma máquina capaz de variados tipos de tratamento automático de
informações ou processamento de dados. Entende-se por computador um sistema físico que
realiza algum tipo de computação. Assumiu-se que os computadores pessoais e laptops são
ícones da era da informação. O primeiro computador eletromecânico foi construído por
Konrad Zuse (1910–1995). Atualmente, um microcomputador é também chamado
computador pessoal ou ainda computador doméstico."""

posicoes = autômato.processar(entrada)

if posicoes:
    print("A palavra 'computador' foi encontrada nas seguintes posições:", posicoes)
else:
    print("A palavra 'computador' não foi encontrada no texto.")
