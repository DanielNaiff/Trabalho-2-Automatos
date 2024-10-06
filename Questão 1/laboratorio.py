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
    estados_finais={'q3', 'q4', 'q8'}  # 13, q4 e q8 são estados finais
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
# Testes unificados para todas as linguagens
# Testes para todas as linguagens

# Testes para todas as linguagens

# (ab*c*)*
strings_teste_a = [
    'ab', 'abc', 'abcc', 'abbbbcccc', '', 'ac', 'a', 'b', 'c', 'abcx',   
    'abbbbb', 'accc', 'abac', 'abbccc', 'abbbbbcccccc', 'aabb',        
    'abbb', 'abcb', 'abccccc', 'a', 'abbbbbc', 'abcabc',                
]  # Rejeitados a partir de 'abbb' (índice 16)

# aaa(b | c)* | (b | c)* aaa
strings_teste_b = [
    'aaa', 'aaab', 'aaac', 'bbb', 'a', 'b', 'c', 'aac',                # Casos aceitos (0 a 7)
    'aaaccc', 'bbbbaaa', 'aaabc', 'abcaaa', 'ccccaa', 'aaaaaa',       # Novos casos aceitos (8 a 13)
    'ccaaaa', 'baaa', 'bbaaa', 'aaaaab', 'bbbcaaa', 'caaaaa',        # Novos casos rejeitados (14 a 19)
]  # Rejeitados a partir de 'ccaaaa' (índice 14)

# a*b | ab*
strings_teste_c = [
    'a', 'aa', 'b', 'ab', 'ba', 'bba', 'c', 'abbc',                   # Casos aceitos (0 a 7)
    'aaaab', 'aab', 'bbaa', 'aaab', 'abbbbb', 'aaaaa',                # Novos casos aceitos (8 a 13)
    'abab', 'aaabbb', 'abbbbbbb', 'a', 'bb', 'aaaa',                 # Novos casos rejeitados (14 a 19)
]  # Rejeitados a partir de 'abab' (índice 14)

# a*b* (a | ac*)
strings_teste_d = [
    'a', 'ab', 'aa', 'abbb', 'b', 'ac', 'aab', 'aaa',                 # Casos aceitos (0 a 7)
    'aabbb', 'aaaaac', 'abbbbb', 'abac', 'aabc', 'accc',              # Novos casos aceitos (8 a 13)
    'aaaac', 'acccccc', 'ababab', 'aac', 'aabbbb', 'bbaaa',          # Novos casos rejeitados (14 a 19)
]  # Rejeitados a partir de 'aaaac' (índice 14)


# Executando os testes
print("Linguagem a:")
testar_automato(automato_a, strings_teste_a)

print("\nLinguagem b:")
testar_automato(automato_b, strings_teste_b)

print("\nLinguagem c:")
testar_automato(automato_c, strings_teste_c)

print("\nLinguagem d:")
testar_automato(automato_d, strings_teste_d)




# Exemplos para a Linguagem a: 
# (
# 𝑎
# 𝑏
# ∗
# 𝑐
# ∗
# )
# ∗
# (ab∗c∗)∗

# ab
# abc
# abcc
# abbbbcccc
# <empty>
# ac
# a
# b
# c
# abcx
# abbbbb
# accc
# abac
# abbccc
# abbbbbcccccc
# aabb
# abbb
# abcb
# abccccc
# a
# abbbbbc
# abcabc


# Exemplos para a Linguagem b: 
# 𝑎
# 𝑎
# 𝑎
# (
# 𝑏
# ∣
# 𝑐
# )
# ∗
# ∣
# (
# 𝑏
# ∣
# 𝑐
# )
# ∗
# 𝑎
# 𝑎
# 𝑎
# aaa(b∣c)∗∣(b∣c)∗aaa
# css
# Copiar código
# aaa
# aaab
# aaac
# bbb
# a
# b
# c
# aac
# aaaccc
# bbbbaaa
# aaabc
# abcaaa
# ccccaa
# aaaaaa
# ccaaaa
# baaa
# bbaaa
# aaaaab
# bbbcaaa
# caaaaa


# Exemplos para a Linguagem c: 
# 𝑎
# ∗
# 𝑏
# ∣
# 𝑎
# 𝑏


# ∗
# a∗b∣ab∗


# a
# aa
# b
# ab
# ba
# bba
# c
# abbc
# aaaab
# aab
# bbaa
# aaab
# abbbbb
# aaaaa
# abab
# aaabbb
# abbbbbbb
# a
# bb
# aaaa

# Exemplos para a Linguagem d: 
# 𝑎
# ∗
# 𝑏
# ∗
# (
# 𝑎
# ∣
# 𝑎
# 𝑐
# ∗
# )

# a∗b∗(a∣ac∗)

# a
# ab
# aa
# abbb
# b
# ac
# aab
# aaa
# aabbb
# aaaaac
# abbbbb
# abac
# aabc
# accc
# aaaac
# acccccc
# ababab
# aac
# aabbbb
# bbaaa