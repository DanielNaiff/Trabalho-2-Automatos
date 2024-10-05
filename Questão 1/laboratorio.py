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
        'q0': {'a': 'q1'},
        'q1': {'b': 'q1', 'c': 'q2'},
        'q2': {'c': 'q2', 'a': 'q1'},
    },
    estado_inicial='q0',
    estados_finais={'q0', 'q2'}
)

# b) aaa(b | c)* | (b | c)* aaa
automato_b = AFD(
    estados={'q0', 'q1', 'q2', 'q3', 'q4', 'q5'},
    simbolos_entrada={'a', 'b', 'c'},
    transicoes={
        'q0': {'a': 'q1'},
        'q1': {'a': 'q2'},
        'q2': {'a': 'q3'},
        'q3': {'b': 'q3', 'c': 'q3', 'a': 'q4'},
        'q4': {'b': 'q5', 'c': 'q5'},
        'q5': {'b': 'q5', 'c': 'q5'},
    },
    estado_inicial='q0',
    estados_finais={'q3', 'q5'}
)

# c) a*b | ab*
automato_c = AFD(
    estados={'q0', 'q1', 'q2', 'q3'},
    simbolos_entrada={'a', 'b'},
    transicoes={
        'q0': {'a': 'q1', 'b': 'q3'},
        'q1': {'a': 'q1', 'b': 'q2'},
        'q2': {'b': 'q2'},
        'q3': {}
    },
    estado_inicial='q0',
    estados_finais={'q1', 'q2', 'q3'}
)

# d) a*b* (a | ac*)
automato_d = AFD(
    estados={'q0', 'q1', 'q2', 'q3', 'q4'},
    simbolos_entrada={'a', 'b', 'c'},
    transicoes={
        'q0': {'a': 'q1'},
        'q1': {'a': 'q1', 'b': 'q2'},
        'q2': {'b': 'q2', 'a': 'q3'},
        'q3': {'a': 'q3', 'c': 'q4'},
        'q4': {'c': 'q4'},
    },
    estado_inicial='q0',
    estados_finais={'q2', 'q4'}
)

def testar_automato(automato, strings_teste):
    print(f"Testando Autômato:\n")
    for string in strings_teste:
        resultado = automato.aceita_entrada(string)
        print(f"Entrada: '{string}' -> {'Aceita' if resultado else 'Rejeitada'}")

strings_teste_a = ['ab', 'abc', 'aabbcc', '']
strings_teste_b = ['aaab', 'aaac', 'bbbaaa', 'abc']
strings_teste_c = ['a', 'b', 'aa', 'ab', 'abb', 'aaa']
strings_teste_d = ['ab', 'a', 'aac', 'aaac']

print("Linguagem a:")
testar_automato(automato_a, strings_teste_a)
print("\nLinguagem b:")
testar_automato(automato_b, strings_teste_b)
print("\nLinguagem c:")
testar_automato(automato_c, strings_teste_c)
print("\nLinguagem d:")
testar_automato(automato_d, strings_teste_d)
