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
    estados={'q0', 'q1', 'q2', 'q3'},
    simbolos_entrada={'a', 'b', 'c'},
    transicoes={
        'q0': {'a': 'q1'},      # a vai para q1
        'q1': {'b': 'q1', 'c': 'q2'},  # b fica em q1, c vai para q2
        'q2': {'c': 'q2', 'a': 'q1'},  # c fica em q2, a volta para q1
    },
    estado_inicial='q0',
    estados_finais={'q0', 'q2'}  # estados finais são q0 e q2
)

# b) aaa(b | c)* | (b | c)* aaa
automato_b = AFD(
    estados={'q0', 'q1', 'q2', 'q3', 'q4'},
    simbolos_entrada={'a', 'b', 'c'},
    transicoes={
        'q0': {'a': 'q1'},       # a vai para q1
        'q1': {'a': 'q2'},       # a vai para q2
        'q2': {'a': 'q3'},       # a vai para q3
        'q3': {'b': 'q3', 'c': 'q3'},  # b ou c fica em q3
        'q4': {'b': 'q4', 'c': 'q4'},  # b ou c fica em q4
    },
    estado_inicial='q0',
    estados_finais={'q3', 'q4'}  # estados finais são q3 e q4
)

# c) a*b | ab*
automato_c = AFD(
    estados={'q0', 'q1', 'q2', 'q3'},
    simbolos_entrada={'a', 'b'},
    transicoes={
        'q0': {'a': 'q1', 'b': 'q2'},  # a vai para q1, b vai para q2
        'q1': {'a': 'q1', 'b': 'q3'},  # a fica em q1, b vai para q3
        'q2': {},                       # q2 é final
        'q3': {'b': 'q3'},             # b fica em q3
    },
    estado_inicial='q0',
    estados_finais={'q1', 'q2', 'q3'}  # estados finais são q1, q2 e q3
)

# d) a*b* (a | ac*)
automato_d = AFD(
    estados={'q0', 'q1', 'q2', 'q3'},
    simbolos_entrada={'a', 'b', 'c'},
    transicoes={
        'q0': {'a': 'q1'},               # a vai para q1
        'q1': {'a': 'q1', 'b': 'q2'},    # a fica em q1, b vai para q2
        'q2': {'a': 'q3'},               # b vai para q2, a vai para q3
        'q3': {'c': 'q3'},               # a ou c fica em q3
    },
    estado_inicial='q0',
    estados_finais={'q2', 'q3'}  # estados finais são q2 e q3
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
