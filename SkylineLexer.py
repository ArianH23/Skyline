# Generated from Skyline.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("C\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\7")
        buf.write("\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\5\r")
        buf.write("\66\n\r\3\r\6\r9\n\r\r\r\16\r:\3\16\3\16\7\16?\n\16\f")
        buf.write("\16\16\16B\13\16\2\2\17\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\3\2\4\5\2C\\aac|\6\2")
        buf.write("\62;C\\aac|\2E\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3")
        buf.write("\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2")
        buf.write("\2\2\2\33\3\2\2\2\3\35\3\2\2\2\5\37\3\2\2\2\7!\3\2\2\2")
        buf.write("\t#\3\2\2\2\13&\3\2\2\2\r(\3\2\2\2\17*\3\2\2\2\21,\3\2")
        buf.write("\2\2\23.\3\2\2\2\25\60\3\2\2\2\27\62\3\2\2\2\31\65\3\2")
        buf.write("\2\2\33<\3\2\2\2\35\36\7}\2\2\36\4\3\2\2\2\37 \7\177\2")
        buf.write("\2 \6\3\2\2\2!\"\7.\2\2\"\b\3\2\2\2#$\7<\2\2$%\7?\2\2")
        buf.write("%\n\3\2\2\2&\'\7-\2\2\'\f\3\2\2\2()\7,\2\2)\16\3\2\2\2")
        buf.write("*+\7/\2\2+\20\3\2\2\2,-\7*\2\2-\22\3\2\2\2./\7+\2\2/\24")
        buf.write("\3\2\2\2\60\61\7]\2\2\61\26\3\2\2\2\62\63\7_\2\2\63\30")
        buf.write("\3\2\2\2\64\66\7/\2\2\65\64\3\2\2\2\65\66\3\2\2\2\668")
        buf.write("\3\2\2\2\679\4\62;\28\67\3\2\2\29:\3\2\2\2:8\3\2\2\2:")
        buf.write(";\3\2\2\2;\32\3\2\2\2<@\t\2\2\2=?\t\3\2\2>=\3\2\2\2?B")
        buf.write("\3\2\2\2@>\3\2\2\2@A\3\2\2\2A\34\3\2\2\2B@\3\2\2\2\6\2")
        buf.write("\65:@\2")
        return buf.getvalue()


class SkylineLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LB = 1
    RB = 2
    COMMA = 3
    ASSIGN = 4
    PLUS = 5
    MULT = 6
    MINUS = 7
    LP = 8
    RP = 9
    LC = 10
    RC = 11
    INTVAL = 12
    ID = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{'", "'}'", "','", "':='", "'+'", "'*'", "'-'", "'('", "')'", 
            "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "LB", "RB", "COMMA", "ASSIGN", "PLUS", "MULT", "MINUS", "LP", 
            "RP", "LC", "RC", "INTVAL", "ID" ]

    ruleNames = [ "LB", "RB", "COMMA", "ASSIGN", "PLUS", "MULT", "MINUS", 
                  "LP", "RP", "LC", "RC", "INTVAL", "ID" ]

    grammarFileName = "Skyline.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


