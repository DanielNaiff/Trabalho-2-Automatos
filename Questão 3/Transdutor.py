def Mealy(estados, sigma, delta, transicao, transducao, q0, cadeia):
     qTs = q0
     sTd = ''
     ss = ''
     for s in cadeia:
          ss = ss + s
          if ss == '25' or ss == '50' or ss == '100':
               sTd = sTd + transducao[(qTs, ss)]
               qTs = transicao[(qTs, ss)]
               ss = ''
     return sTd

estados = ['q0', 'q1', 'q2', 'q3']

sigma = ['25', '50', '100']

delta = '1'

q0 = 'q0'

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

print(Mealy(estados, sigma, delta, transicao, transducao, q0, '252550100502550252525502510025'))