#!/usr/bin/env python
# -*- conding: utf-8 -*- 

class TerminalExpression:
    def interpret(self, context):
        name  = context.get_name()

        if name == 'a':
            return 'I' 
        elif name == 'b':
            return 'II' 
        else:
            return ''

class NonterminalExpression:
    def interpret(self, context):
        name = context.get_name()

        if name == 'a':
            return 1 
        elif name == 'b':
            return 2 
        else:
            return ''

class Context:
    def __init__(self, name='context'):
        self.name = name 
    
    def get_name(self):
        return self.name

if __name__ == '__main__':
    context_1 = Context('a')
    context_2 = Context('b')
    array = []

    array.append(NonterminalExpression())
    array.append(TerminalExpression())
    array.append(TerminalExpression())
    array.append(NonterminalExpression())
    array.append(NonterminalExpression())

    for expression in array:
        print(expression.interpret(context_1))
        print(expression.interpret(context_2))


