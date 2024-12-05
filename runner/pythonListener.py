# Generated from python.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .pythonParser import pythonParser
else:
    from pythonParser import pythonParser

# This class defines a complete listener for a parse tree produced by pythonParser.
class pythonListener(ParseTreeListener):

    # Enter a parse tree produced by pythonParser#start.
    def enterStart(self, ctx:pythonParser.StartContext):
        pass

    # Exit a parse tree produced by pythonParser#start.
    def exitStart(self, ctx:pythonParser.StartContext):
        pass


    # Enter a parse tree produced by pythonParser#line.
    def enterLine(self, ctx:pythonParser.LineContext):
        pass

    # Exit a parse tree produced by pythonParser#line.
    def exitLine(self, ctx:pythonParser.LineContext):
        pass


    # Enter a parse tree produced by pythonParser#assignment.
    def enterAssignment(self, ctx:pythonParser.AssignmentContext):
        pass

    # Exit a parse tree produced by pythonParser#assignment.
    def exitAssignment(self, ctx:pythonParser.AssignmentContext):
        pass


    # Enter a parse tree produced by pythonParser#expression.
    def enterExpression(self, ctx:pythonParser.ExpressionContext):
        pass

    # Exit a parse tree produced by pythonParser#expression.
    def exitExpression(self, ctx:pythonParser.ExpressionContext):
        pass


    # Enter a parse tree produced by pythonParser#ifStatement.
    def enterIfStatement(self, ctx:pythonParser.IfStatementContext):
        pass

    # Exit a parse tree produced by pythonParser#ifStatement.
    def exitIfStatement(self, ctx:pythonParser.IfStatementContext):
        pass


    # Enter a parse tree produced by pythonParser#if.
    def enterIf(self, ctx:pythonParser.IfContext):
        pass

    # Exit a parse tree produced by pythonParser#if.
    def exitIf(self, ctx:pythonParser.IfContext):
        pass


    # Enter a parse tree produced by pythonParser#elif.
    def enterElif(self, ctx:pythonParser.ElifContext):
        pass

    # Exit a parse tree produced by pythonParser#elif.
    def exitElif(self, ctx:pythonParser.ElifContext):
        pass


    # Enter a parse tree produced by pythonParser#else.
    def enterElse(self, ctx:pythonParser.ElseContext):
        pass

    # Exit a parse tree produced by pythonParser#else.
    def exitElse(self, ctx:pythonParser.ElseContext):
        pass


    # Enter a parse tree produced by pythonParser#while.
    def enterWhile(self, ctx:pythonParser.WhileContext):
        pass

    # Exit a parse tree produced by pythonParser#while.
    def exitWhile(self, ctx:pythonParser.WhileContext):
        pass


    # Enter a parse tree produced by pythonParser#for.
    def enterFor(self, ctx:pythonParser.ForContext):
        pass

    # Exit a parse tree produced by pythonParser#for.
    def exitFor(self, ctx:pythonParser.ForContext):
        pass


    # Enter a parse tree produced by pythonParser#value.
    def enterValue(self, ctx:pythonParser.ValueContext):
        pass

    # Exit a parse tree produced by pythonParser#value.
    def exitValue(self, ctx:pythonParser.ValueContext):
        pass


    # Enter a parse tree produced by pythonParser#val.
    def enterVal(self, ctx:pythonParser.ValContext):
        pass

    # Exit a parse tree produced by pythonParser#val.
    def exitVal(self, ctx:pythonParser.ValContext):
        pass


    # Enter a parse tree produced by pythonParser#array.
    def enterArray(self, ctx:pythonParser.ArrayContext):
        pass

    # Exit a parse tree produced by pythonParser#array.
    def exitArray(self, ctx:pythonParser.ArrayContext):
        pass


    # Enter a parse tree produced by pythonParser#operator.
    def enterOperator(self, ctx:pythonParser.OperatorContext):
        pass

    # Exit a parse tree produced by pythonParser#operator.
    def exitOperator(self, ctx:pythonParser.OperatorContext):
        pass


    # Enter a parse tree produced by pythonParser#operatorHP.
    def enterOperatorHP(self, ctx:pythonParser.OperatorHPContext):
        pass

    # Exit a parse tree produced by pythonParser#operatorHP.
    def exitOperatorHP(self, ctx:pythonParser.OperatorHPContext):
        pass


    # Enter a parse tree produced by pythonParser#operatorLP.
    def enterOperatorLP(self, ctx:pythonParser.OperatorLPContext):
        pass

    # Exit a parse tree produced by pythonParser#operatorLP.
    def exitOperatorLP(self, ctx:pythonParser.OperatorLPContext):
        pass


    # Enter a parse tree produced by pythonParser#conditionals.
    def enterConditionals(self, ctx:pythonParser.ConditionalsContext):
        pass

    # Exit a parse tree produced by pythonParser#conditionals.
    def exitConditionals(self, ctx:pythonParser.ConditionalsContext):
        pass


    # Enter a parse tree produced by pythonParser#function.
    def enterFunction(self, ctx:pythonParser.FunctionContext):
        pass

    # Exit a parse tree produced by pythonParser#function.
    def exitFunction(self, ctx:pythonParser.FunctionContext):
        pass


    # Enter a parse tree produced by pythonParser#bool.
    def enterBool(self, ctx:pythonParser.BoolContext):
        pass

    # Exit a parse tree produced by pythonParser#bool.
    def exitBool(self, ctx:pythonParser.BoolContext):
        pass


    # Enter a parse tree produced by pythonParser#number.
    def enterNumber(self, ctx:pythonParser.NumberContext):
        pass

    # Exit a parse tree produced by pythonParser#number.
    def exitNumber(self, ctx:pythonParser.NumberContext):
        pass


    # Enter a parse tree produced by pythonParser#term.
    def enterTerm(self, ctx:pythonParser.TermContext):
        pass

    # Exit a parse tree produced by pythonParser#term.
    def exitTerm(self, ctx:pythonParser.TermContext):
        pass



del pythonParser