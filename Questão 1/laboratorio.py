class AutomaFinito:
    def __init__(self, estados, simbolos_entrada, transicoes, estado_inicial, estados_finais):
        self.estados = estados  # Conjunto de estados do autômato
        self.simbolos_entrada = simbolos_entrada  # Conjunto de símbolos de entrada
        self.transicoes = transicoes  # Dicionário de transições entre estados
        self.estado_inicial = estado_inicial  # Estado inicial do autômato
        self.estados_finais = estados_finais  # Conjunto de estados finais

    def aceita_entrada(self, string_entrada):
        estado_atual = self.estado_inicial  # Começa no estado inicial
        for simbolo in string_entrada:  # Itera sobre cada símbolo da entrada
            if simbolo not in self.simbolos_entrada:  # Verifica se o símbolo é válido
                return False  # Rejeita se o símbolo não está nos símbolos de entrada
            estado_atual = self.transicoes.get(estado_atual, {}).get(simbolo)  # Transição para o próximo estado
            if estado_atual is None:  # Verifica se a transição é válida
                return False  # Rejeita se não houver transição válida
        return estado_atual in self.estados_finais  # Aceita se o estado atual for um estado final

# a) (ab*c*)*
automa_a = AutomaFinito(
    estados={'q0', 'q1', 'q2'},  # Estados do autômato
    simbolos_entrada={'a', 'b', 'c'},  # Símbolos de entrada
    transicoes={
        'q0': {'a': 'q1'},  # Transição de q0 para q1 com 'a'
        'q1': {'b': 'q1', 'c': 'q2'},  # Loop em q1 para 'b' e transição para q2 com 'c'
        'q2': {'c': 'q2', 'a': 'q1'},  # Permite voltar a q1 para repetir (ab*c*)*
    },
    estado_inicial='q0',  # Estado inicial
    estados_finais={'q0', 'q2'}  # Estados finais
)

# b) aaa(b | c)* | (b | c)* aaa
automa_b = AutomaFinito(
    estados={'q0', 'q1', 'q2', 'q3', 'q4', 'q5'},  # Estados do autômato
    simbolos_entrada={'a', 'b', 'c'},  # Símbolos de entrada
    transicoes={
        'q0': {'a': 'q1'},  # Transição de q0 para q1 com 'a'
        'q1': {'a': 'q2'},  # Transição de q1 para q2 com 'a'
        'q2': {'a': 'q3'},  # Transição de q2 para q3 com 'a'
        'q3': {'b': 'q3', 'c': 'q3', 'a': 'q4'},  # Loop em q3 para 'b' ou 'c', ou transição para q4 com 'a'
        'q4': {'b': 'q5', 'c': 'q5'},  # Transição para q5 com 'b' ou 'c'
        'q5': {'b': 'q5', 'c': 'q5'},  # Loop em q5 para 'b' ou 'c'
    },
    estado_inicial='q0',  # Estado inicial
    estados_finais={'q3', 'q5'}  # Estados finais
)

# c) a*b | ab*
automa_c = AutomaFinito(
    estados={'q0', 'q1', 'q2', 'q3'},  # Estados do autômato
    simbolos_entrada={'a', 'b'},  # Símbolos de entrada
    transicoes={
        'q0': {'a': 'q1', 'b': 'q3'},  # Transição de q0 para q1 com 'a' ou para q3 com 'b'
        'q1': {'a': 'q1', 'b': 'q2'},  # Loop em q1 para 'a' e transição para q2 com 'b'
        'q2': {'b': 'q2'},  # Loop em q2 para 'b'
        'q3': {}  # Estado final sem transições
    },
    estado_inicial='q0',  # Estado inicial
    estados_finais={'q1', 'q2', 'q3'}  # Estados finais
)

# d) a*b* (a | ac*)
automa_d = AutomaFinito(
    estados={'q0', 'q1', 'q2', 'q3', 'q4'},  # Estados do autômato
    simbolos_entrada={'a', 'b', 'c'},  # Símbolos de entrada
    transicoes={
        'q0': {'a': 'q1'},  # Transição de q0 para q1 com 'a'
        'q1': {'a': 'q1', 'b': 'q2'},  # Loop em q1 para 'a' e transição para q2 com 'b'
        'q2': {'b': 'q2', 'a': 'q3'},  # Loop em q2 para 'b' e transição para q3 com 'a'
        'q3': {'a': 'q3', 'c': 'q4'},  # Transição para q3 com 'a' ou para q4 com 'c'
        'q4': {'c': 'q4'},  # Loop em q4 para 'c'
    },
    estado_inicial='q0',  # Estado inicial
    estados_finais={'q2', 'q4'}  # Estados finais
)

# Função para testar os autômatos
def testar_automa(automa, strings_teste):
    print(f"Testando Autômato:\n")
    for string in strings_teste:
        resultado = automa.aceita_entrada(string)
        print(f"Entrada: '{string}' -> {'Aceita' if resultado else 'Rejeitada'}")

# Testando as linguagens com algumas strings
strings_teste_a = ['ab', 'abc', 'aabbcc', '']
strings_teste_b = ['aaab', 'aaac', 'bbbaaa', 'abc']
strings_teste_c = ['a', 'b', 'aa', 'ab', 'abb', 'aaa']
strings_teste_d = ['ab', 'a', 'aac', 'aaac']

print("Linguagem a:")
testar_automa(automa_a, strings_teste_a)
print("\nLinguagem b:")
testar_automa(automa_b, strings_teste_b)
print("\nLinguagem c:")
testar_automa(automa_c, strings_teste_c)
print("\nLinguagem d:")
testar_automa(automa_d, strings_teste_d)
