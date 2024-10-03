def mealy(estados, alfabeto_entrada, alfabeto_saida, transicao, transducao, estado_inicial, cadeia):
     qTs = estado_inicial
     sTd = ''
     ss = ''
     for s in cadeia:
          ss = ss + s
          if ss == '25' or ss == '50' or ss == '100':
               sTd = sTd + transducao[(qTs, ss)]
               qTs = transicao[(qTs, ss)]
               ss = ''
     return sTd

def testar_cadeias(estados, alfabeto_entrada, alfabeto_saida, transicao, transducao, estado_inicial, vetor_cadeias):
     for c in vetor_cadeias:
          print(f'{c} = {mealy(estados, alfabeto_entrada, alfabeto_saida, transicao, transducao, estado_inicial, c)}')


estados = ['q0', 'q1', 'q2', 'q3']

alfabeto_entrada = ['25', '50', '100']

alfabeto_saida = '1'

estado_inicial = 'q0'

transicao = {('q0', '25'): 'q1', 
             ('q0', '50'): 'q2', 
             ('q0', '100'): 'q0', 
             ('q1', '25'): 'q2', 
             ('q1', '50'): 'q3',
             ('q1', '100'): 'q1',
             ('q2', '25'): 'q3',
             ('q2', '50'): 'q0', 
             ('q2', '100'): 'q2', 
             ('q3', '25'): 'q0', 
             ('q3', '50'): 'q1', 
             ('q3', '100'): 'q3'}

transducao = {('q0', '25'): '', 
             ('q0', '50'): '', 
             ('q0', '100'): '1', 
             ('q1', '25'): '', 
             ('q1', '50'): '',
             ('q1', '100'): '1',
             ('q2', '25'): '',
             ('q2', '50'): '1', 
             ('q2', '100'): '1', 
             ('q3', '25'): '1', 
             ('q3', '50'): '1', 
             ('q3', '100'): '1'}

vetor_cadeias = ['25', # ''
                 '2550', # ''
                 '505050', # '1'
                 '100100', # '11'
                 '2550502525505025', # '111'
                 '25100251002510025', # '1111'
                 '505050505050', # '111'
                 '2525252525252525252525252525' # '111'
                 ]

testar_cadeias(estados, alfabeto_entrada, alfabeto_saida, transicao, transducao, estado_inicial, vetor_cadeias)