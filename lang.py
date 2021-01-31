from inspect import signature

def P(S):
    T = set()
    for i in range(1 << len(S)):
        T.add(frozenset(list(S)[s] for s in range(len(S)) if (i & (1 << s))))
    return T

class L:
    def __init__(self, M):
        self.__w = ''
        self._M = tuple()
        self.__name__ = type(self).__name__
        if type(M) in {tuple}:
            if len(M) == 4:
                if type(M[0]) in {set}:
                    if len(M[0]) > 0:
                        V = True
                        for A in M[0]:
                            if type(A) not in {str}:
                                V = False
                                break
                            elif len(A) == 0:
                                V = False
                                break
                        if V:
                            if type(M[1]) in {set}:
                                if len(M[1]) > 0:
                                    locals()['\u03a3'] = True
                                    for l in M[1]:
                                        if type(l) not in {str}:
                                            locals()['\u03a3'] = False
                                            break
                                        elif len(l) != 1:
                                            locals()['\u03a3'] = False
                                            break
                                    if locals()['\u03a3']:
                                        if len(M[0] & M[1]) == 0:
                                            if type(M[2]) in {dict}:
                                                if len(M[2]) > 0:
                                                    for A in M[0]:
                                                        if A not in M[2].keys():
                                                            V = False
                                                            break
                                                    if V:
                                                        R = True
                                                        for A in M[2]:
                                                            if A not in M[0]:
                                                                V = False
                                                                break
                                                            elif type(M[2][A]) not in {set}:
                                                                V = False
                                                                break
                                                            elif len(M[2][A]) == 0:
                                                                V = False
                                                                break
                                                            if V:
                                                                for u in M[2][A]:
                                                                    if len(u) > 0:
                                                                        for l in u.split('\u0000'):
                                                                            if l not in M[0] | M[1]:
                                                                                R = False
                                                                                break
                                                        if R:
                                                            if M[3] in M[0]:
                                                                pda = dict()
                                                                q = 1
                                                                pda[q] = dict()
                                                                for a in M[1] | {''}:
                                                                    pda[q][a] = dict()
                                                                    for b in M[0] | M[1] | {'$', ''}:
                                                                        pda[q][a][b] = set()
                                                                        if a == '' and b == '':
                                                                            pda[q][a][b].add((q + 1, '$'))
                                                                q += 1
                                                                pda[q] = dict()
                                                                for a in M[1] | {''}:
                                                                    pda[q][a] = dict()
                                                                    for b in M[0] | M[1] | {'$', ''}:
                                                                        pda[q][a][b] = set()
                                                                        if a == '' and b == '':
                                                                            pda[q][a][b].add((q + 1, M[3]))
                                                                q += 1
                                                                pda[q] = dict()
                                                                for a in M[1] | {''}:
                                                                    pda[q][a] = dict()
                                                                    for b in M[0] | M[1] | {'$', ''}:
                                                                        pda[q][a][b] = set()
                                                                        if a in M[1] and b == a:
                                                                            pda[q][a][b].add((q, ''))
                                                                        if a == '' and b in M[0]:
                                                                            for u in M[2][b]:
                                                                                if len(u) == 0:
                                                                                    pda[q][a][b].add((q, ''))
                                                                                elif len(u.split('\u0000')) == 1:
                                                                                    pda[q][a][b].add((q, u.split('\u0000')[0]))
                                                                                else:
                                                                                    pda[q][a][b].add((max(pda.keys()) + 1, u.split('\u0000')[-1]))
                                                                                    tmp = dict()
                                                                                    l = -2
                                                                                    while l > -len(u.split('\u0000')):
                                                                                        tmp[max(pda.keys())-l-1] = dict()
                                                                                        for x in M[1] | {''}:
                                                                                            tmp[max(pda.keys())-l-1][x] = dict()
                                                                                            for y in M[0] | M[1] | {'$', ''}:
                                                                                                tmp[max(pda.keys())-l-1][x][y] = set()
                                                                                                if x == '' and y == '':
                                                                                                    tmp[max(pda.keys())-l-1][x][y].add((max(pda.keys()) - l, u.split('\u0000')[l]))
                                                                                        l -= 1
                                                                                    tmp[max(pda.keys())-l-1] = dict()
                                                                                    for x in M[1] | {''}:
                                                                                        tmp[max(pda.keys())-l-1][x] = dict()
                                                                                        for y in M[0] | M[1] | {'$', ''}:
                                                                                            tmp[max(pda.keys())-l-1][x][y] = set()
                                                                                            if x == '' and y == '':
                                                                                                tmp[max(pda.keys())-l-1][x][y].add((q, u.split('\u0000')[l]))
                                                                                    pda.update(tmp)
                                                                pda[q]['']['$'].add((max(pda.keys()) + 1, ''))
                                                                q = max(pda.keys()) + 1
                                                                pda[q] = dict()
                                                                for a in M[1] | {''}:
                                                                    pda[q][a] = dict()
                                                                    for b in M[0] | M[1] | {'$', ''}:
                                                                        pda[q][a][b] = set()
                                                                self._M = (set(pda.keys()), M[1], M[0] | M[1] | {'$'}, lambda q, a, b: pda[q][a][b], min(pda.keys()), {max(pda.keys())})
                                                                self.__name__ = 'CFL'
            elif len(M) == 5:
                if type(M[0]) in {set}:
                    if len(M[0]) > 0:
                        if type(M[1]) in {set}:
                            if len(M[1]) > 0:
                                locals()['\u03a3'] = True
                                for l in M[1]:
                                    if type(l) not in {str}:
                                        locals()['\u03a3'] = False
                                        break
                                    elif len(l) != 1:
                                        locals()['\u03a3'] = False
                                        break
                                if locals()['\u03a3']:
                                    if M[3] in M[0]:
                                        if type(M[4]) in {set}:
                                            if M[4] <= M[0]:
                                                if callable(M[2]):
                                                    if len(signature(M[2]).parameters) == 2:
                                                        if [M[2](q, l) in M[0] for q in M[0] for l in M[1]] == [True] * (len(M[0]) * len(M[1])):
                                                            self._M = M
                                                            self.__name__ = 'REG'
                                                        elif [type(M[2](q, l)) for q in M[0] for l in M[1] | {''}] == [set] * (len(M[0]) * len(M[1] | {''})):
                                                            if [M[2](q, l) <= M[0] for q in M[0] for l in M[1] | {''}] == [True] * (len(M[0]) * len(M[1] | {''})):
                                                                Q = P(M[0])
                                                                q0 = {M[3]}
                                                                for q in M[2](M[3], ''):
                                                                    q0.add(q)
                                                                q0 = frozenset(q0)
                                                                dfa = dict()
                                                                for R in Q:
                                                                    dfa[R] = dict()
                                                                    if R == frozenset():
                                                                        for l in M[1]:
                                                                            dfa[R][l] = frozenset()
                                                                    else:
                                                                        for r in R:
                                                                            for l in M[1]:
                                                                                E = set()
                                                                                if l not in dfa[R].keys():
                                                                                    dfa[R][l] = frozenset()
                                                                                for q in M[2](r, l):
                                                                                    E.add(q)
                                                                                    for locals()['q\''] in M[2](q, ''):
                                                                                        E.add(locals()['q\''])
                                                                                dfa[R][l] = dfa[R][l] | frozenset(E)
                                                                F = set()
                                                                for R in Q:
                                                                    if set(R) & M[4] != set():
                                                                        F.add(R)
                                                                self._M = (Q, M[1], lambda R, l: dfa[R][l], q0, F)
                                                                self.__name__ = 'REG'
            elif len(M) == 6:
                if type(M[0]) in {set}:
                    if len(M[0]) > 0:
                        if type(M[1]) in {set}:
                            if len(M[1]) > 0:
                                locals()['\u03a3'] = True
                                for l in M[1]:
                                    if type(l) not in {str}:
                                        locals()['\u03a3'] = False
                                        break
                                    elif len(l) != 1:
                                        locals()['\u03a3'] = False
                                        break
                                if locals()['\u03a3']:
                                    if type(M[2]) in {set}:
                                        if len(M[2]) > 0:
                                            locals()['\u0393'] = True
                                            for l in M[2]:
                                                if type(l) not in {str}:
                                                    locals()['\u0393'] = False
                                                    break
                                                elif len(l) != 1:
                                                    locals()['\u0393'] = False
                                                    break
                                            if locals()['\u0393']:
                                                if M[4] in M[0]:
                                                    if type(M[5]) in {set}:
                                                        if M[5] <= M[0]:
                                                            if callable(M[3]):
                                                                if len(signature(M[3]).parameters) == 3:
                                                                    if [type(M[3](q, a, b)) for q in M[0] for a in M[1] | {''} for b in M[2] | {''}] == [set] * (len(M[0]) * len(M[1] | {''}) * len(M[2] | {''})):
                                                                        if [M[3](q, a, b) <= {(locals()['q\''], l) for locals()['q\''] in M[0] for l in M[2] | {''}} for q in M[0] for a in M[1] | {''} for b in M[2] | {''}] == [True] * (len(M[0]) * len(M[1] | {''}) * len(M[2] | {''})):
                                                                            self._M = M
                                                                            self.__name__ = 'CFL'
            elif len(M) == 7:
                if type(M[0]) in {set}:
                    if len(M[0]) > 0:
                        if type(M[1]) in {set}:
                            if len(M[1]) > 0:
                                locals()['\u03a3'] = True
                                for l in M[1]:
                                    if type(l) not in {str}:
                                        locals()['\u03a3'] = False
                                        break
                                    elif len(l) != 1:
                                        locals()['\u03a3'] = False
                                        break
                                if locals()['\u03a3']:
                                    if ' ' not in M[1]:
                                        if type(M[2]) in {set}:
                                            if len(M[2]) > 0:
                                                locals()['\u0393'] = True
                                                for l in M[2]:
                                                    if type(l) not in {str}:
                                                        locals()['\u0393'] = False
                                                        break
                                                    elif len(l) != 1:
                                                        locals()['\u0393'] = False
                                                        break
                                                if locals()['\u0393']:
                                                    if ' ' in M[2]:
                                                        if M[1] <= M[2]:
                                                            if {M[4], M[5], M[6]} <= M[0]:
                                                                if M[5] != M[6]:
                                                                    if callable(M[3]):
                                                                        if len(signature(M[3]).parameters) == 2:
                                                                            if [M[3](q, l) in {(locals()['q\''], locals()['l\''], locals()['\u0394']) for locals()['q\''] in M[0] for locals()['l\''] in M[2] for locals()['\u0394'] in {'L', 'R'}} for q in M[0] - {M[5], M[6]} for l in M[2]] == [True] * (len(M[0] - {M[5], M[6]}) * len(M[2])):
                                                                                self._M = M
                                                                                self.__name__ = 'TMR'
    def __contains__(self, w):
        try:
            if len(self._M) == 5:
                q = self._M[3]
                for l in w:
                    q = self._M[2](q, l)
                return q in self._M[4]
            elif len(self._M) == 6:
                queue = [(self._M[4], 0, '')]
                while len(queue) > 0:
                    q = queue.pop(0)
                    a = q[1]
                    b = ''
                    stack = q[2].split('\u0000') if len(q[2]) > 0 else list(q[2])
                    q = q[0]
                    if a == len(w) and len(stack) == 0:
                        if q in self._M[5]:
                            return True
                        else:
                            if len(stack) > 0:
                                b = stack.pop()
                            for i in range(len(self._M[3](q, '', b))):
                                queue.append((list(self._M[3](q, '', b))[i][0], a, '\u0000'.join(stack + ([list(self._M[3](q, '', b))[i][1]] if list(self._M[3](q, '', b))[i][1] != '' else list()))))
                            if b != '':
                                stack.append(b)
                                b = ''
                                for i in range(len(self._M[3](q, '', b))):
                                    queue.append((list(self._M[3](q, '', b))[i][0], a, '\u0000'.join(stack + ([list(self._M[3](q, '', b))[i][1]] if list(self._M[3](q, '', b))[i][1] != '' else list()))))
                    else:
                        if a < len(w):
                            if len(stack) > 0:
                                b = stack.pop()
                            for i in range(len(self._M[3](q, w[a], b))):
                                queue.append((list(self._M[3](q, w[a], b))[i][0], a + 1, '\u0000'.join(stack + ([list(self._M[3](q, w[a], b))[i][1]] if list(self._M[3](q, w[a], b))[i][1] != '' else list()))))
                            for i in range(len(self._M[3](q, '', b))):
                                queue.append((list(self._M[3](q, '', b))[i][0], a, '\u0000'.join(stack + ([list(self._M[3](q, '', b))[i][1]] if list(self._M[3](q, '', b))[i][1] != '' else list()))))
                            if b != '':
                                stack.append(b)
                                b = ''
                                for i in range(len(self._M[3](q, w[a], b))):
                                    queue.append((list(self._M[3](q, w[a], b))[i][0], a + 1, '\u0000'.join(stack + ([list(self._M[3](q, w[a], b))[i][1]] if list(self._M[3](q, w[a], b))[i][1] != '' else list()))))
                                for i in range(len(self._M[3](q, '', b))):
                                    queue.append((list(self._M[3](q, '', b))[i][0], a, '\u0000'.join(stack + ([list(self._M[3](q, '', b))[i][1]] if list(self._M[3](q, '', b))[i][1] != '' else list()))))
                        elif len(stack) > 0:
                            b = stack.pop()
                            for i in range(len(self._M[3](q, '', b))):
                                queue.append((list(self._M[3](q, '', b))[i][0], a, '\u0000'.join(stack + ([list(self._M[3](q, '', b))[i][1]] if list(self._M[3](q, '', b))[i][1] != '' else list()))))
                            if b != '':
                                stack.append(b)
                                b = ''
                                for i in range(len(self._M[3](q, '', b))):
                                    queue.append((list(self._M[3](q, '', b))[i][0], a, '\u0000'.join(stack + ([list(self._M[3](q, '', b))[i][1]] if list(self._M[3](q, '', b))[i][1] != '' else list()))))
                return False
            else:
                s = list(w) if len(w) > 0 else [' ']
                l = 0
                q = self._M[4]
                while q != self._M[5] and q != self._M[6]:
                    q = self._M[3](q, s[l])
                    s[l] = q[1]
                    if q[2] == 'R':
                        l += 1
                    else:
                        l -= 1
                    if l >= len(s):
                        s += [' ']
                    elif l < 0:
                        s = [' '] + s
                        l = 0
                    q = q[0]
                return q == self._M[5]
        except KeyError as err:
            return False
    def __iter__(self):
        return self
    def __next__(self):
        return self.next()
    def next(self):
        while len(self.__w) <= 2 ** 8 - 1:
            w = self.__w
            locals()['\u0393'] = sorted(self._M[1] | {''})
            b = len(locals()['\u0393'])
            n = locals()['\u0393'].index(self.__w[-1]) if len(self.__w) > 0 else 0
            self.__w = list(self.__w) if len(self.__w) > 0 else ['']
            if locals()['\u0393'].index(self.__w[-1]) < b - 1:
                n += 1
                self.__w[-1] = locals()['\u0393'][n]
            else:
                n = 1
                for i in range(-1, -len(self.__w), -1):
                    if locals()['\u0393'].index(self.__w[i]) == b - 1:
                        self.__w[i] = locals()['\u0393'][n]
                    else:
                        self.__w[i] = locals()['\u0393'][locals()['\u0393'].index(self.__w[i])+1]
                        self.__w[i-1] = locals()['\u0393'][locals()['\u0393'].index(self.__w[i-1])-1]
                if locals()['\u0393'].index(self.__w[0]) == b - 1:
                    self.__w[0] = locals()['\u0393'][n]
                    self.__w = [locals()['\u0393'][n]] + self.__w
                else:
                    self.__w[0] = locals()['\u0393'][locals()['\u0393'].index(self.__w[0])+1]
            self.__w = ''.join(self.__w)
            if w in self:
                return w
        raise StopIteration()
    def __eq__(self, other):
        for w in self:
            if w not in other:
                return False
        for w in other:
            if w not in self:
                return False
        return True
    def __ne__(self, other):
        for w in self:
            if w not in other:
                return True
        for w in other:
            if w not in self:
                return True
        return False
    def __lt__(self, other):
        for w in self:
            if w not in other:
                return False
        return self != other
    def __le__(self, other):
        return self < other or self == other
    def __gt__(self, other):
        for w in other:
            if w not in self:
                return False
        return self != other
    def __ge__(self, other):
        return self > other or self == other
    def __key(self):
        if len(self._M) == 5:
            return (frozenset(self._M[0]), frozenset(self._M[1]), self._M[2], self._M[3], frozenset(self._M[4]))
        elif len(self._M) == 6:
            return (frozenset(self._M[0]), frozenset(self._M[1]), frozenset(self._M[2]), self._M[3], self._M[4], frozenset(self._M[5]))
        else:
            return (frozenset(self._M[0]), frozenset(self._M[1]), frozenset(self._M[2]), self._M[3], self._M[4], self._M[5], self._M[6])
    def __hash__(self):
        return hash(self.__key())
