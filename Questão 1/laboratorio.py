class AFD:
    def __init__(self, estados, simbolos_entrada, transicoes, estado_inicial, estados_finais):
        self.estados = estados
        self.simbolos_entrada = simbolos_entrada
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais

    def aceita_entrada(self, string_entrada):
        estado_atual = self.estado_inicial
        for simbolo in string_entrada:
            if simbolo not in self.simbolos_entrada:
                print(f"O símbolo '{simbolo}' não está na entrada.")
                return False
            estado_atual = self.transicoes.get(estado_atual, {}).get(simbolo)
            if estado_atual is None:
                return False
        return estado_atual in self.estados_finais


# a) (ab*c*)*
automato_a = AFD(
    estados={'q0', 'q1', 'q2'},
    simbolos_entrada={'a', 'b', 'c'},
    transicoes={
        'q0': {'a': 'q1'},        # a vai para q1
        'q1': {'a': 'q1','b': 'q1', 'c': 'q2'},  # b permanece em q1, c vai para q2
        'q2': {'c': 'q2', 'a': 'q1'},  # c permanece em q2, a retorna para q1
    },
    estado_inicial='q0',
    estados_finais={'q0', 'q1', 'q2'}  # q0, q1 e q2 são estados finais
)

# b) aaa(b | c)* | (b | c)* aaa
automato_b = AFD(
    estados={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8'},
    simbolos_entrada={'a', 'b', 'c'},
    transicoes={
        'q0': {'a': 'q1', 'b': 'q5', 'c': 'q5'},   # q0 pode ir para q1 com 'a', ou para q5 com 'b' ou 'c'
        'q1': {'a': 'q2'},                         # q1 vai para q2 com 'a'
        'q2': {'a': 'q3'},                         # q2 vai para q3 com 'a'
        'q3': {'b': 'q4', 'c': 'q4'},              # q3 vai para q4 com 'b' ou 'c'
        'q4': {'b': 'q4', 'c': 'q4'},              # q4 permanece em q4 com 'b' ou 'c'
        'q5': {'b': 'q5', 'c': 'q5', 'a': 'q6'},   # q5 permanece em q5 com 'b' ou 'c', e vai para q6 com 'a'
        'q6': {'a': 'q7'},                         # q6 vai para q7 com 'a'
        'q7': {'a': 'q8'},                         # q7 vai para q8 com 'a'
    },
    estado_inicial='q0',
    estados_finais={'q4', 'q8'}  # q4 e q8 são estados finais
)

# c) a*b | ab*
automato_c = AFD(
    estados={'q0', 'q1', 'q2', 'q3'},
    simbolos_entrada={'a', 'b'},
    transicoes={
        'q0': {'a': 'q1', 'b': 'q2'},  # a vai para q1, b vai para q2
        'q1': {'a': 'q1', 'b': 'q3'},  # a permanece em q1, b vai para q3
        'q2': {},                       # q2 é um estado final
        'q3': {'b': 'q3'},             # b permanece em q3
    },
    estado_inicial='q0',
    estados_finais={'q1', 'q2', 'q3'}  # estados finais são q1, q2 e q3
)

# d) a*b* (a | ac*)
automato_d = AFD(
    estados={'q0', 'q1', 'q2', 'q3'},
    simbolos_entrada={'a', 'b', 'c'},
    transicoes={
        'q0': {'a': 'q1','b': 'q2'},               # a vai para q1
        'q1': {'a': 'q3', 'b': 'q2'},    # a permanece em q1, b vai para q2
        'q2': {'a': 'q6','b': 'q2'},               # b vai para q2, a vai para q3
        'q3': {'a': 'q3','c': 'q5'},               # a ou c permanece em q3
        'q4': {'c': 'q5'},
        'q5': {'c': 'q5'},
    },
    estado_inicial='q0',
    estados_finais={'q1', 'q3', 'q5', 'q4'}
)

def testar_automato(automato, strings_teste):
    print(f"Testando Autômato:\n")
    for string in strings_teste:
        resultado = automato.aceita_entrada(string)
        print(f"Entrada: '{string}' -> {'Aceita' if resultado else 'Rejeitada'}")

# Testes
# a) (ab*c*)*
strings_teste_a_aceitos = ['ab', 'abc', 'abcc', 'abbbbcccc', '', 'ac']
strings_teste_a_nao_aceitos = ['a', 'b', 'c', 'abcx']

# b) aaa(b | c)* | (b | c)* aaa
strings_teste_b_aceitos = ['aaa', 'aaab', 'aaac', 'bbb']
strings_teste_b_nao_aceitos = ['a', 'b', 'c', 'aac']

# c) a*b | ab*
strings_teste_c_aceitos = ['a', 'aa', 'b', 'ab']
strings_teste_c_nao_aceitos = ['ba', 'bba', 'c', 'abbc']

# d) a*b* (a | ac*)
strings_teste_d_aceitos = ['a', 'ab', 'aa', 'abbb']
strings_teste_d_nao_aceitos = ['b', 'ac', 'aab', 'aaa']

# Executando os testes
print("Linguagem a:")
testar_automato(automato_a, strings_teste_a_aceitos)
testar_automato(automato_a, strings_teste_a_nao_aceitos)

print("\nLinguagem b:")
testar_automato(automato_b, strings_teste_b_aceitos)
testar_automato(automato_b, strings_teste_b_nao_aceitos)

print("\nLinguagem c:")
testar_automato(automato_c, strings_teste_c_aceitos)
testar_automato(automato_c, strings_teste_c_nao_aceitos)

print("\nLinguagem d:")
testar_automato(automato_d, strings_teste_d_aceitos)
testar_automato(automato_d, strings_teste_d_nao_aceitos)
