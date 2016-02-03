class FSM():
    """
        Learning Finite State Machine
        Current state transfer table only work for 'nano'
    """

    def __init__(self):
        print("Am I a real FSM?")

    def getNextState(self, state, change, fsm):
        if state in fsm.keys() and change in fsm[state].keys():
            nextSt = fsm[state][change]
        else:
            nextSt = ''
        return nextSt

    def match(self, p, t):
        fsm = {
            '': {'n':'n', 'a':'', 'o':''},
            'n': {'n':'n', 'a':'na', 'o':''},
            'na': {'n':'nan', 'a':'', 'o':''},
            'nan': {'n':'n', 'a':'na', 'o':'nano'},
            'nano': {'n':'nano', 'a':'nano', 'o':'nano'}
        }
        state = ''
        for char in t:
            state = self.getNextState(state, char, fsm)
            if state == p:
                return True
        return False

fst = FSM()
print(fst.match('nano', "lalsjlfajnanoaljlfaj"))
