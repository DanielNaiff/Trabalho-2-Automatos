class DFA:
    def __init__(self, states, input_symbols, transitions, initial_state, final_states):
        self.states = states
        self.input_symbols = input_symbols
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = final_states

    def accepts_input(self, input_string):
        current_state = self.initial_state
        for symbol in input_string:
            if symbol not in self.input_symbols:
                return False
            current_state = self.transitions.get(current_state, {}).get(symbol)
            if current_state is None:
                return False
        return current_state in self.final_states

# a) (ab*c*)*
dfa_a = DFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'a', 'b', 'c'},
    transitions={
        'q0': {'a': 'q1'},
        'q1': {'b': 'q1', 'c': 'q2'},  # 'b*' and 'c*'
        'q2': {'c': 'q2', 'a': 'q1'},  # Transition back to allow repeating (ab*c*)*
    },
    initial_state='q0',
    final_states={'q0', 'q2'}
)

# b) aaa(b | c)* | (b | c)* aaa
dfa_b = DFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5'},
    input_symbols={'a', 'b', 'c'},
    transitions={
        'q0': {'a': 'q1'},
        'q1': {'a': 'q2'},
        'q2': {'a': 'q3'},
        'q3': {'b': 'q3', 'c': 'q3', 'a': 'q4'},  # Loop for (b|c)*
        'q4': {'b': 'q5', 'c': 'q5'},
        'q5': {'b': 'q5', 'c': 'q5'},
    },
    initial_state='q0',
    final_states={'q3', 'q5'}
)

# c) a*b | ab*
dfa_c = DFA(
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': 'q1', 'b': 'q3'},
        'q1': {'a': 'q1', 'b': 'q2'},
        'q2': {'b': 'q2'},
        'q3': {}
    },
    initial_state='q0',
    final_states={'q1', 'q2', 'q3'}
)

# d) a*b* (a | ac*)
dfa_d = DFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4'},
    input_symbols={'a', 'b', 'c'},
    transitions={
        'q0': {'a': 'q1'},  # Transition to a
        'q1': {'a': 'q1', 'b': 'q2'},  # Loop for a* and transition to b*
        'q2': {'b': 'q2', 'a': 'q3'},  # Loop for b* and transition to a
        'q3': {'a': 'q3', 'c': 'q4'},  # Transition to a or ac*
        'q4': {'c': 'q4'},  # Loop for c*
    },
    initial_state='q0',
    final_states={'q2', 'q4'}
)

# Função para testar os autômatos
def test_dfa(dfa, test_strings):
    print(f"Testing DFA: {dfa}\n")
    for string in test_strings:
        result = dfa.accepts_input(string)
        print(f"Input: '{string}' -> {'Accepted' if result else 'Rejected'}")

# Testando as linguagens com algumas strings
test_strings_a = ['ab', 'abc', 'aabbcc', '']
test_strings_b = ['aaab', 'aaac', 'bbbaaa', 'abc']
test_strings_c = ['a', 'b', 'aa', 'ab', 'abb', 'aaa']
test_strings_d = ['ab', 'a', 'aac', 'aaac']

print("Language a:")
test_dfa(dfa_a, test_strings_a)
print("\nLanguage b:")
test_dfa(dfa_b, test_strings_b)
print("\nLanguage c:")
test_dfa(dfa_c, test_strings_c)
print("\nLanguage d:")
test_dfa(dfa_d, test_strings_d)
