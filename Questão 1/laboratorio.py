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



automato_a = AFD(
    estados={'q0', 'q1', 'q2'},
    simbolos_entrada={'a', 'b', 'c'},
    transicoes={
        'q0': {'a': 'q1'},        
        'q1': {'a': 'q1','b': 'q1', 'c': 'q2'},  
        'q2': {'c': 'q2', 'a': 'q1'},  
    },
    estado_inicial='q0',
    estados_finais={'q0', 'q1', 'q2'}  
)


automato_b = AFD(
    estados={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8'},
    simbolos_entrada={'a', 'b', 'c'},
    transicoes={
        'q0': {'a': 'q1', 'b': 'q5', 'c': 'q5'},   
        'q1': {'a': 'q2'},                         
        'q2': {'a': 'q3'},                         
        'q3': {'b': 'q4', 'c': 'q4'},              
        'q4': {'b': 'q4', 'c': 'q4'},              
        'q5': {'b': 'q5', 'c': 'q5', 'a': 'q6'},   
        'q6': {'a': 'q7'},                         
        'q7': {'a': 'q8'},                         
    },
    estado_inicial='q0',
    estados_finais={'q3', 'q4', 'q8'}  
)


automato_c = AFD(
    estados={'q0', 'q1', 'q2', 'q3'},
    simbolos_entrada={'a', 'b'},
    transicoes={
        'q0': {'a': 'q1', 'b': 'q2'},  
        'q1': {'a': 'q1', 'b': 'q3'},  
        'q2': {},                       
        'q3': {'b': 'q3'},             
    },
    estado_inicial='q0',
    estados_finais={'q1', 'q2', 'q3'}  
)


automato_d = AFD(
    estados={'q0', 'q1', 'q2', 'q3'},
    simbolos_entrada={'a', 'b', 'c'},
    transicoes={
        'q0': {'a': 'q1','b': 'q2'},               
        'q1': {'a': 'q3', 'b': 'q2', "c": "q5"},    
        'q2': {'a': 'q4','b': 'q2'},               
        'q3': {'a': 'q3',"b":"q2",'c': 'q5'},               
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








strings_teste_a = [
    'ab', 'abc', 'abcc', 'abbbbcccc', '', 'ac', 'a', 'b', 'c', 'abcx',   
    'abbbbb', 'accc', 'abac', 'abbccc', 'abbbbbcccccc', 'aabb',        
    'abbb', 'abcb', 'abccccc', 'a', 'abbbbbc', 'abcabc',                
]  


strings_teste_b = [
    'aaa', 'aaab', 'aaac', 'bbb', 'a', 'b', 'c', 'aac',                
    'aaaccc', 'bbbbaaa', 'aaabc', 'abcaaa', 'ccccaa', 'aaaaaa',       
    'ccaaaa', 'baaa', 'bbaaa', 'aaaaab', 'bbbcaaa', 'caaaaa',        
]  


strings_teste_c = [
    'a', 'aa', 'b', 'ab', 'ba', 'bba', 'c', 'abbc',                   
    'aaaab', 'aab', 'bbaa', 'aaab', 'abbbbb', 'aaaaa',                
    'abab', 'aaabbb', 'abbbbbbb', 'a', 'bb', 'aaaa',                 
]  


strings_teste_d = [
    'a', 'ab', 'aa', 'abbb', 'b', 'ac', 'aab', 'aaa',                 
    'aabbb', 'aaaaac', 'abbbbb', 'abac', 'aabc', 'accc',              
    'aaaac', 'acccccc', 'ababab', 'aac', 'aabbbb', 'bbaaa',          
]  



print("Linguagem a:")
testar_automato(automato_a, strings_teste_a)

print("\nLinguagem b:")
testar_automato(automato_b, strings_teste_b)

print("\nLinguagem c:")
testar_automato(automato_c, strings_teste_c)

print("\nLinguagem d:")
testar_automato(automato_d, strings_teste_d)
























































































































































