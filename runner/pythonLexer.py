# Generated from python.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from pythonParser import pythonParser
from antlr4.Token import CommonToken
from antlr4.Token import Token
from pythonParser import pythonParser


def serializedATN():
    return [
        4,0,40,295,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,
        1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,
        11,1,12,1,12,1,13,1,13,1,14,1,14,1,14,1,15,1,15,1,15,1,16,1,16,1,
        16,1,17,1,17,1,18,1,18,1,18,1,19,3,19,130,8,19,1,19,1,19,5,19,134,
        8,19,10,19,12,19,137,9,19,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,22,
        1,22,1,22,1,22,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,25,1,25,
        1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,27,
        1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,30,1,30,
        5,30,186,8,30,10,30,12,30,189,9,30,1,30,1,30,1,30,5,30,194,8,30,
        10,30,12,30,197,9,30,1,30,3,30,200,8,30,1,31,1,31,5,31,204,8,31,
        10,31,12,31,207,9,31,1,32,1,32,1,33,4,33,212,8,33,11,33,12,33,213,
        1,34,3,34,217,8,34,1,34,4,34,220,8,34,11,34,12,34,221,1,34,1,34,
        4,34,226,8,34,11,34,12,34,227,1,35,3,35,231,8,35,1,35,1,35,1,36,
        1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,37,1,37,5,37,245,8,37,10,37,
        12,37,248,9,37,1,37,1,37,1,37,1,37,1,37,1,37,1,38,1,38,1,38,1,38,
        1,38,1,38,5,38,262,8,38,10,38,12,38,265,9,38,1,38,1,38,1,38,1,38,
        1,38,1,38,1,39,1,39,5,39,275,8,39,10,39,12,39,278,9,39,1,39,1,39,
        1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,41,1,41,1,41,1,41,1,41,1,41,
        1,41,4,187,195,246,263,0,42,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,
        9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,37,19,39,
        20,41,21,43,22,45,23,47,24,49,25,51,26,53,27,55,28,57,29,59,30,61,
        31,63,32,65,0,67,0,69,33,71,34,73,35,75,36,77,37,79,38,81,39,83,
        40,1,0,7,1,0,34,34,1,0,39,39,2,0,65,90,97,122,5,0,45,45,48,57,65,
        90,95,95,97,122,1,0,48,57,1,0,32,32,2,0,10,10,13,13,308,0,1,1,0,
        0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,
        0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,
        0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,
        0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,
        0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,
        0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,
        0,63,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,
        0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,1,85,1,0,0,0,
        3,87,1,0,0,0,5,89,1,0,0,0,7,91,1,0,0,0,9,93,1,0,0,0,11,96,1,0,0,
        0,13,98,1,0,0,0,15,100,1,0,0,0,17,102,1,0,0,0,19,104,1,0,0,0,21,
        106,1,0,0,0,23,108,1,0,0,0,25,110,1,0,0,0,27,112,1,0,0,0,29,114,
        1,0,0,0,31,117,1,0,0,0,33,120,1,0,0,0,35,123,1,0,0,0,37,125,1,0,
        0,0,39,129,1,0,0,0,41,138,1,0,0,0,43,142,1,0,0,0,45,145,1,0,0,0,
        47,149,1,0,0,0,49,152,1,0,0,0,51,157,1,0,0,0,53,162,1,0,0,0,55,166,
        1,0,0,0,57,172,1,0,0,0,59,177,1,0,0,0,61,199,1,0,0,0,63,201,1,0,
        0,0,65,208,1,0,0,0,67,211,1,0,0,0,69,216,1,0,0,0,71,230,1,0,0,0,
        73,234,1,0,0,0,75,238,1,0,0,0,77,255,1,0,0,0,79,272,1,0,0,0,81,281,
        1,0,0,0,83,288,1,0,0,0,85,86,5,61,0,0,86,2,1,0,0,0,87,88,5,40,0,
        0,88,4,1,0,0,0,89,90,5,41,0,0,90,6,1,0,0,0,91,92,5,58,0,0,92,8,1,
        0,0,0,93,94,5,105,0,0,94,95,5,110,0,0,95,10,1,0,0,0,96,97,5,91,0,
        0,97,12,1,0,0,0,98,99,5,44,0,0,99,14,1,0,0,0,100,101,5,93,0,0,101,
        16,1,0,0,0,102,103,5,47,0,0,103,18,1,0,0,0,104,105,5,37,0,0,105,
        20,1,0,0,0,106,107,5,42,0,0,107,22,1,0,0,0,108,109,5,43,0,0,109,
        24,1,0,0,0,110,111,5,45,0,0,111,26,1,0,0,0,112,113,5,60,0,0,113,
        28,1,0,0,0,114,115,5,60,0,0,115,116,5,61,0,0,116,30,1,0,0,0,117,
        118,5,61,0,0,118,119,5,61,0,0,119,32,1,0,0,0,120,121,5,62,0,0,121,
        122,5,61,0,0,122,34,1,0,0,0,123,124,5,62,0,0,124,36,1,0,0,0,125,
        126,5,33,0,0,126,127,5,61,0,0,127,38,1,0,0,0,128,130,5,13,0,0,129,
        128,1,0,0,0,129,130,1,0,0,0,130,131,1,0,0,0,131,135,5,10,0,0,132,
        134,5,9,0,0,133,132,1,0,0,0,134,137,1,0,0,0,135,133,1,0,0,0,135,
        136,1,0,0,0,136,40,1,0,0,0,137,135,1,0,0,0,138,139,5,97,0,0,139,
        140,5,110,0,0,140,141,5,100,0,0,141,42,1,0,0,0,142,143,5,111,0,0,
        143,144,5,114,0,0,144,44,1,0,0,0,145,146,5,110,0,0,146,147,5,111,
        0,0,147,148,5,116,0,0,148,46,1,0,0,0,149,150,5,105,0,0,150,151,5,
        102,0,0,151,48,1,0,0,0,152,153,5,101,0,0,153,154,5,108,0,0,154,155,
        5,115,0,0,155,156,5,101,0,0,156,50,1,0,0,0,157,158,5,101,0,0,158,
        159,5,108,0,0,159,160,5,105,0,0,160,161,5,102,0,0,161,52,1,0,0,0,
        162,163,5,102,0,0,163,164,5,111,0,0,164,165,5,114,0,0,165,54,1,0,
        0,0,166,167,5,119,0,0,167,168,5,104,0,0,168,169,5,105,0,0,169,170,
        5,108,0,0,170,171,5,101,0,0,171,56,1,0,0,0,172,173,5,84,0,0,173,
        174,5,114,0,0,174,175,5,117,0,0,175,176,5,101,0,0,176,58,1,0,0,0,
        177,178,5,70,0,0,178,179,5,97,0,0,179,180,5,108,0,0,180,181,5,115,
        0,0,181,182,5,101,0,0,182,60,1,0,0,0,183,187,5,34,0,0,184,186,8,
        0,0,0,185,184,1,0,0,0,186,189,1,0,0,0,187,188,1,0,0,0,187,185,1,
        0,0,0,188,190,1,0,0,0,189,187,1,0,0,0,190,200,5,34,0,0,191,195,5,
        39,0,0,192,194,8,1,0,0,193,192,1,0,0,0,194,197,1,0,0,0,195,196,1,
        0,0,0,195,193,1,0,0,0,196,198,1,0,0,0,197,195,1,0,0,0,198,200,5,
        39,0,0,199,183,1,0,0,0,199,191,1,0,0,0,200,62,1,0,0,0,201,205,3,
        65,32,0,202,204,3,67,33,0,203,202,1,0,0,0,204,207,1,0,0,0,205,203,
        1,0,0,0,205,206,1,0,0,0,206,64,1,0,0,0,207,205,1,0,0,0,208,209,7,
        2,0,0,209,66,1,0,0,0,210,212,7,3,0,0,211,210,1,0,0,0,212,213,1,0,
        0,0,213,211,1,0,0,0,213,214,1,0,0,0,214,68,1,0,0,0,215,217,5,45,
        0,0,216,215,1,0,0,0,216,217,1,0,0,0,217,219,1,0,0,0,218,220,7,4,
        0,0,219,218,1,0,0,0,220,221,1,0,0,0,221,219,1,0,0,0,221,222,1,0,
        0,0,222,223,1,0,0,0,223,225,5,46,0,0,224,226,7,4,0,0,225,224,1,0,
        0,0,226,227,1,0,0,0,227,225,1,0,0,0,227,228,1,0,0,0,228,70,1,0,0,
        0,229,231,5,45,0,0,230,229,1,0,0,0,230,231,1,0,0,0,231,232,1,0,0,
        0,232,233,7,4,0,0,233,72,1,0,0,0,234,235,7,5,0,0,235,236,1,0,0,0,
        236,237,6,36,0,0,237,74,1,0,0,0,238,239,5,39,0,0,239,240,5,39,0,
        0,240,241,5,39,0,0,241,246,1,0,0,0,242,245,3,75,37,0,243,245,9,0,
        0,0,244,242,1,0,0,0,244,243,1,0,0,0,245,248,1,0,0,0,246,247,1,0,
        0,0,246,244,1,0,0,0,247,249,1,0,0,0,248,246,1,0,0,0,249,250,5,39,
        0,0,250,251,5,39,0,0,251,252,5,39,0,0,252,253,1,0,0,0,253,254,6,
        37,0,0,254,76,1,0,0,0,255,256,5,34,0,0,256,257,5,34,0,0,257,258,
        5,34,0,0,258,263,1,0,0,0,259,262,3,77,38,0,260,262,9,0,0,0,261,259,
        1,0,0,0,261,260,1,0,0,0,262,265,1,0,0,0,263,264,1,0,0,0,263,261,
        1,0,0,0,264,266,1,0,0,0,265,263,1,0,0,0,266,267,5,34,0,0,267,268,
        5,34,0,0,268,269,5,34,0,0,269,270,1,0,0,0,270,271,6,38,0,0,271,78,
        1,0,0,0,272,276,5,35,0,0,273,275,8,6,0,0,274,273,1,0,0,0,275,278,
        1,0,0,0,276,274,1,0,0,0,276,277,1,0,0,0,277,279,1,0,0,0,278,276,
        1,0,0,0,279,280,6,39,0,0,280,80,1,0,0,0,281,282,5,105,0,0,282,283,
        5,110,0,0,283,284,5,100,0,0,284,285,5,101,0,0,285,286,5,110,0,0,
        286,287,5,116,0,0,287,82,1,0,0,0,288,289,5,100,0,0,289,290,5,101,
        0,0,290,291,5,100,0,0,291,292,5,101,0,0,292,293,5,110,0,0,293,294,
        5,116,0,0,294,84,1,0,0,0,17,0,129,135,187,195,199,205,213,216,221,
        227,230,244,246,261,263,276,1,6,0,0
    ]

class pythonLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    NL = 20
    AND = 21
    OR = 22
    NOT = 23
    IF = 24
    ELSE = 25
    ELIF = 26
    FOR = 27
    WHILE = 28
    TRUE = 29
    FALSE = 30
    STRING = 31
    TERM = 32
    FLOAT = 33
    DIGIT = 34
    WS = 35
    BLOCKCOMMENT = 36
    BLOCKCOMMENT2 = 37
    LINECOMMENT = 38
    INDENT = 39
    DEDENT = 40

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'('", "')'", "':'", "'in'", "'['", "','", "']'", "'/'", 
            "'%'", "'*'", "'+'", "'-'", "'<'", "'<='", "'=='", "'>='", "'>'", 
            "'!='", "'and'", "'or'", "'not'", "'if'", "'else'", "'elif'", 
            "'for'", "'while'", "'True'", "'False'", "'indent'", "'dedent'" ]

    symbolicNames = [ "<INVALID>",
            "NL", "AND", "OR", "NOT", "IF", "ELSE", "ELIF", "FOR", "WHILE", 
            "TRUE", "FALSE", "STRING", "TERM", "FLOAT", "DIGIT", "WS", "BLOCKCOMMENT", 
            "BLOCKCOMMENT2", "LINECOMMENT", "INDENT", "DEDENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "NL", "AND", 
                  "OR", "NOT", "IF", "ELSE", "ELIF", "FOR", "WHILE", "TRUE", 
                  "FALSE", "STRING", "TERM", "TERM_START", "TERM_FOLLOW", 
                  "FLOAT", "DIGIT", "WS", "BLOCKCOMMENT", "BLOCKCOMMENT2", 
                  "LINECOMMENT", "INDENT", "DEDENT" ]

    grammarFileName = "python.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    class DenterHelper(object):
        def __init__(self, nl_token, indent_token, dedent_token, should_ignore_eof):
            self.dents_buffer = []
            self.indentations = []
            self.nl_token = nl_token
            self.indent_token = indent_token
            self.dedent_token = dedent_token
            self.reached_eof = False
            self.should_ignore_eof = should_ignore_eof

        def next_token(self):
            self.init_if_first_run()
            if not self.dents_buffer:
                t = self.pull_token()
            else:
                t = self.dents_buffer.pop(0)
            if self.reached_eof:
                return t
            if t.type == self.nl_token:
                r = self.handle_newline_token(t)
            elif t.type == Token.EOF:
                r = self.apply(t)
            else:
                r = t
            return r
        
        def pull_token(self):
                """

                :rtype: CommonToken
                """
                pass

        def init_if_first_run(self):
            if not self.indentations:
                self.indentations.insert(0, 0)
                while True:
                    first_real_token = self.pull_token()
                    if first_real_token.type != self.nl_token:
                        break
                if first_real_token.column > 0:
                    self.indentations.insert(0, first_real_token.column)
                    self.dents_buffer.append(self.create_token(self.indent_token, first_real_token))
                self.dents_buffer.append(first_real_token)

        def handle_newline_token(self, t: Token):
            next_next = self.pull_token()
            while next_next.type == self.nl_token:
                t = next_next
                next_next = self.pull_token()
            if next_next.type == Token.EOF:
                return self.apply(next_next)
            nl_text = t.text
            indent = len(nl_text) - 1
            if indent > 0 and nl_text[0] == '\r':
                indent -= 1
            prev_indent = self.indentations[0]
            if indent == prev_indent:
                r = t
            elif indent > prev_indent:
                r = self.create_token(self.indent_token, t)
                self.indentations.insert(0, indent)
            else:
                r = self.unwind_to(indent, t)
            self.dents_buffer.append(next_next)
            return r

        def create_token(self, token_type, copy_from: CommonToken):
            if token_type == self.nl_token:
                token_type_str = 'newLine'
            elif token_type == self.indent_token:
                token_type_str = 'indent'
            elif token_type == self.dedent_token:
                token_type_str = 'dedent'
            else:
                token_type_str = None
            r = self.get_injected_token(copy_from, token_type_str)
            r.type = token_type
            return r
        
        def get_injected_token(self, copy_from: CommonToken, token_type_str):
            new_token = copy_from.clone()
            new_token.text = token_type_str
            return new_token

        def unwind_to(self, target_indent, copy_from : CommonToken):
            self.dents_buffer.append(self.create_token(self.nl_token, copy_from))
            while True:
                prev_indent = self.indentations.pop(0)
                if prev_indent == target_indent:
                    break
                if target_indent > prev_indent:
                    self.indentations.insert(0, prev_indent)
                    self.dents_buffer.append(self.create_token(self.indent_token, copy_from))
                    break
                self.dents_buffer.append(self.create_token(self.dedent_token, copy_from))
            self.indentations.insert(0, target_indent)
            return self.dents_buffer.pop(0)

        def apply(self, t: CommonToken):
            if self.should_ignore_eof:
                self.reached_eof = True
                return t
            else:
                if not self.indentations:
                    r = self.create_token(self.nl_token, t)
                    self.dents_buffer.append(t)
                else:
                    r = self.unwind_to(0, t)
                    self.dents_buffer.append(t)
                self.reached_eof = True
                return r

    class MyCoolDenter(DenterHelper):
        def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
            super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
            self.lexer: pythonLexer = lexer

        def pull_token(self):
            return super(pythonLexer, self.lexer).nextToken()

    denter = None

    def nextToken(self):
        if not self.denter:
            self.denter = self.MyCoolDenter(self, self.NL, pythonParser.INDENT, pythonParser.DEDENT, False)
        return self.denter.next_token()



