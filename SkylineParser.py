# Generated from Skyline.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("S\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5\3\27\n\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4#\n\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\7\4+\n\4\f\4\16\4.\13\4\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\7\6\67\n\6\f\6\16\6:\13\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6I\n\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\2\3\6\b\2\4\6\b\n\f\2\3\4\2\7\7\t")
        buf.write("\t\2V\2\16\3\2\2\2\4\26\3\2\2\2\6\"\3\2\2\2\b/\3\2\2\2")
        buf.write("\nH\3\2\2\2\fJ\3\2\2\2\16\17\5\4\3\2\17\20\7\2\2\3\20")
        buf.write("\3\3\2\2\2\21\22\5\b\5\2\22\23\7\6\2\2\23\24\5\6\4\2\24")
        buf.write("\27\3\2\2\2\25\27\5\6\4\2\26\21\3\2\2\2\26\25\3\2\2\2")
        buf.write("\27\5\3\2\2\2\30\31\b\4\1\2\31\32\7\n\2\2\32\33\5\6\4")
        buf.write("\2\33\34\7\13\2\2\34#\3\2\2\2\35\36\7\t\2\2\36#\5\6\4")
        buf.write("\b\37#\5\n\6\2 #\7\16\2\2!#\5\b\5\2\"\30\3\2\2\2\"\35")
        buf.write("\3\2\2\2\"\37\3\2\2\2\" \3\2\2\2\"!\3\2\2\2#,\3\2\2\2")
        buf.write("$%\f\7\2\2%&\7\b\2\2&+\5\6\4\b\'(\f\6\2\2()\t\2\2\2)+")
        buf.write("\5\6\4\7*$\3\2\2\2*\'\3\2\2\2+.\3\2\2\2,*\3\2\2\2,-\3")
        buf.write("\2\2\2-\7\3\2\2\2.,\3\2\2\2/\60\7\17\2\2\60\t\3\2\2\2")
        buf.write("\61I\5\f\7\2\62\63\7\f\2\2\638\5\f\7\2\64\65\7\5\2\2\65")
        buf.write("\67\5\f\7\2\66\64\3\2\2\2\67:\3\2\2\28\66\3\2\2\289\3")
        buf.write("\2\2\29;\3\2\2\2:8\3\2\2\2;<\7\r\2\2<I\3\2\2\2=>\7\3\2")
        buf.write("\2>?\7\16\2\2?@\7\5\2\2@A\7\16\2\2AB\7\5\2\2BC\7\16\2")
        buf.write("\2CD\7\5\2\2DE\7\16\2\2EF\7\5\2\2FG\7\16\2\2GI\7\4\2\2")
        buf.write("H\61\3\2\2\2H\62\3\2\2\2H=\3\2\2\2I\13\3\2\2\2JK\7\n\2")
        buf.write("\2KL\7\16\2\2LM\7\5\2\2MN\7\16\2\2NO\7\5\2\2OP\7\16\2")
        buf.write("\2PQ\7\13\2\2Q\r\3\2\2\2\b\26\"*,8H")
        return buf.getvalue()


class SkylineParser ( Parser ):

    grammarFileName = "Skyline.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "','", "':='", "'+'", "'*'", 
                     "'-'", "'('", "')'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "LB", "RB", "COMMA", "ASSIGN", "PLUS", 
                      "MULT", "MINUS", "LP", "RP", "LC", "RC", "INTVAL", 
                      "ID" ]

    RULE_root = 0
    RULE_statement = 1
    RULE_expr = 2
    RULE_ident = 3
    RULE_skyCreation = 4
    RULE_sky = 5

    ruleNames =  [ "root", "statement", "expr", "ident", "skyCreation", 
                   "sky" ]

    EOF = Token.EOF
    LB=1
    RB=2
    COMMA=3
    ASSIGN=4
    PLUS=5
    MULT=6
    MINUS=7
    LP=8
    RP=9
    LC=10
    RC=11
    INTVAL=12
    ID=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(SkylineParser.StatementContext,0)


        def EOF(self):
            return self.getToken(SkylineParser.EOF, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = SkylineParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.statement()
            self.state = 13
            self.match(SkylineParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SkylineParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignmentContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ident(self):
            return self.getTypedRuleContext(SkylineParser.IdentContext,0)

        def ASSIGN(self):
            return self.getToken(SkylineParser.ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(SkylineParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)


    class ExprValContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(SkylineParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprVal" ):
                return visitor.visitExprVal(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = SkylineParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 20
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = SkylineParser.AssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.ident()
                self.state = 16
                self.match(SkylineParser.ASSIGN)
                self.state = 17
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = SkylineParser.ExprValContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SkylineParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class UnionOffsetContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.ExprContext)
            else:
                return self.getTypedRuleContext(SkylineParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(SkylineParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(SkylineParser.MINUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnionOffset" ):
                return visitor.visitUnionOffset(self)
            else:
                return visitor.visitChildren(self)


    class MirrorContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(SkylineParser.MINUS, 0)
        def expr(self):
            return self.getTypedRuleContext(SkylineParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMirror" ):
                return visitor.visitMirror(self)
            else:
                return visitor.visitChildren(self)


    class SkylineValueContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def skyCreation(self):
            return self.getTypedRuleContext(SkylineParser.SkyCreationContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSkylineValue" ):
                return visitor.visitSkylineValue(self)
            else:
                return visitor.visitChildren(self)


    class ExprIdentContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ident(self):
            return self.getTypedRuleContext(SkylineParser.IdentContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprIdent" ):
                return visitor.visitExprIdent(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesisContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LP(self):
            return self.getToken(SkylineParser.LP, 0)
        def expr(self):
            return self.getTypedRuleContext(SkylineParser.ExprContext,0)

        def RP(self):
            return self.getToken(SkylineParser.RP, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesis" ):
                return visitor.visitParenthesis(self)
            else:
                return visitor.visitChildren(self)


    class InterRepliContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.ExprContext)
            else:
                return self.getTypedRuleContext(SkylineParser.ExprContext,i)

        def MULT(self):
            return self.getToken(SkylineParser.MULT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterRepli" ):
                return visitor.visitInterRepli(self)
            else:
                return visitor.visitChildren(self)


    class IntegerValContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INTVAL(self):
            return self.getToken(SkylineParser.INTVAL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntegerVal" ):
                return visitor.visitIntegerVal(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SkylineParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = SkylineParser.ParenthesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 23
                self.match(SkylineParser.LP)
                self.state = 24
                self.expr(0)
                self.state = 25
                self.match(SkylineParser.RP)
                pass

            elif la_ == 2:
                localctx = SkylineParser.MirrorContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 27
                self.match(SkylineParser.MINUS)
                self.state = 28
                self.expr(6)
                pass

            elif la_ == 3:
                localctx = SkylineParser.SkylineValueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 29
                self.skyCreation()
                pass

            elif la_ == 4:
                localctx = SkylineParser.IntegerValContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 30
                self.match(SkylineParser.INTVAL)
                pass

            elif la_ == 5:
                localctx = SkylineParser.ExprIdentContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 31
                self.ident()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 42
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 40
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = SkylineParser.InterRepliContext(self, SkylineParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 34
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 35
                        self.match(SkylineParser.MULT)
                        self.state = 36
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = SkylineParser.UnionOffsetContext(self, SkylineParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 37
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 38
                        _la = self._input.LA(1)
                        if not(_la==SkylineParser.PLUS or _la==SkylineParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 39
                        self.expr(5)
                        pass

             
                self.state = 44
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class IdentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SkylineParser.ID, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_ident

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdent" ):
                return visitor.visitIdent(self)
            else:
                return visitor.visitChildren(self)




    def ident(self):

        localctx = SkylineParser.IdentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ident)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(SkylineParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SkyCreationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sky(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.SkyContext)
            else:
                return self.getTypedRuleContext(SkylineParser.SkyContext,i)


        def LC(self):
            return self.getToken(SkylineParser.LC, 0)

        def RC(self):
            return self.getToken(SkylineParser.RC, 0)

        def LB(self):
            return self.getToken(SkylineParser.LB, 0)

        def INTVAL(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.INTVAL)
            else:
                return self.getToken(SkylineParser.INTVAL, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.COMMA)
            else:
                return self.getToken(SkylineParser.COMMA, i)

        def RB(self):
            return self.getToken(SkylineParser.RB, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_skyCreation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSkyCreation" ):
                return visitor.visitSkyCreation(self)
            else:
                return visitor.visitChildren(self)




    def skyCreation(self):

        localctx = SkylineParser.SkyCreationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_skyCreation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SkylineParser.LP]:
                self.state = 47
                self.sky()
                pass
            elif token in [SkylineParser.LC]:
                self.state = 48
                self.match(SkylineParser.LC)
                self.state = 49
                self.sky()
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SkylineParser.COMMA:
                    self.state = 50
                    self.match(SkylineParser.COMMA)
                    self.state = 51
                    self.sky()
                    self.state = 56
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 57
                self.match(SkylineParser.RC)
                pass
            elif token in [SkylineParser.LB]:
                self.state = 59
                self.match(SkylineParser.LB)
                self.state = 60
                self.match(SkylineParser.INTVAL)
                self.state = 61
                self.match(SkylineParser.COMMA)
                self.state = 62
                self.match(SkylineParser.INTVAL)
                self.state = 63
                self.match(SkylineParser.COMMA)
                self.state = 64
                self.match(SkylineParser.INTVAL)
                self.state = 65
                self.match(SkylineParser.COMMA)
                self.state = 66
                self.match(SkylineParser.INTVAL)
                self.state = 67
                self.match(SkylineParser.COMMA)
                self.state = 68
                self.match(SkylineParser.INTVAL)
                self.state = 69
                self.match(SkylineParser.RB)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SkyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(SkylineParser.LP, 0)

        def INTVAL(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.INTVAL)
            else:
                return self.getToken(SkylineParser.INTVAL, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.COMMA)
            else:
                return self.getToken(SkylineParser.COMMA, i)

        def RP(self):
            return self.getToken(SkylineParser.RP, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_sky

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSky" ):
                return visitor.visitSky(self)
            else:
                return visitor.visitChildren(self)




    def sky(self):

        localctx = SkylineParser.SkyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_sky)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(SkylineParser.LP)
            self.state = 73
            self.match(SkylineParser.INTVAL)
            self.state = 74
            self.match(SkylineParser.COMMA)
            self.state = 75
            self.match(SkylineParser.INTVAL)
            self.state = 76
            self.match(SkylineParser.COMMA)
            self.state = 77
            self.match(SkylineParser.INTVAL)
            self.state = 78
            self.match(SkylineParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




