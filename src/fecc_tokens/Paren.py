class Paren:
    def __init__(self, paren):
        if paren == '(':
            LParen()

    @staticmethod
    def getParen(paren):
        if paren == '(': return LParen()
        elif paren == ')': return RParen()
        elif paren == '{': return LBrace()
        elif paren == '}': return RBrace()

    def __str__(self):
        return 'Generic PAREN'


class LParen(Paren):
    def __init__(self):
        pass

    def __str__(self):
        return 'LPAREN'


class RParen(Paren):
    def __init__(self):
        pass

    def __str__(self):
        return 'RPAREN'


class LBrace(Paren):
    def __init__(self):
        pass

    def __str__(self):
        return 'LBRACE'


class RBrace(Paren):
    def __init__(self):
        pass

    def __str__(self):
        return 'RBrace'
