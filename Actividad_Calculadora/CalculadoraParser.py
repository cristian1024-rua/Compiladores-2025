# Generated from Calculadora.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,10,40,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,3,1,19,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        5,1,30,8,1,10,1,12,1,33,9,1,1,2,1,2,1,2,1,2,1,2,1,2,0,1,2,3,0,2,
        4,0,2,1,0,3,4,2,0,1,1,5,5,42,0,6,1,0,0,0,2,18,1,0,0,0,4,34,1,0,0,
        0,6,7,3,2,1,0,7,8,5,0,0,1,8,1,1,0,0,0,9,10,6,1,-1,0,10,19,3,4,2,
        0,11,12,5,1,0,0,12,19,3,2,1,6,13,14,5,6,0,0,14,15,3,2,1,0,15,16,
        5,7,0,0,16,19,1,0,0,0,17,19,5,9,0,0,18,9,1,0,0,0,18,11,1,0,0,0,18,
        13,1,0,0,0,18,17,1,0,0,0,19,31,1,0,0,0,20,21,10,5,0,0,21,22,5,2,
        0,0,22,30,3,2,1,6,23,24,10,4,0,0,24,25,7,0,0,0,25,30,3,2,1,5,26,
        27,10,3,0,0,27,28,7,1,0,0,28,30,3,2,1,4,29,20,1,0,0,0,29,23,1,0,
        0,0,29,26,1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,3,
        1,0,0,0,33,31,1,0,0,0,34,35,5,8,0,0,35,36,5,6,0,0,36,37,3,2,1,0,
        37,38,5,7,0,0,38,5,1,0,0,0,3,18,29,31
    ]

class CalculadoraParser ( Parser ):

    grammarFileName = "Calculadora.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'-'", "'^'", "'*'", "'/'", "'+'", "'('", 
                     "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "NUMBER", "WS" ]

    RULE_prog = 0
    RULE_expresion = 1
    RULE_funcion = 2

    ruleNames =  [ "prog", "expresion", "funcion" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    ID=8
    NUMBER=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,0)


        def EOF(self):
            return self.getToken(CalculadoraParser.EOF, 0)

        def getRuleIndex(self):
            return CalculadoraParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = CalculadoraParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.expresion(0)
            self.state = 7
            self.match(CalculadoraParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalculadoraParser.RULE_expresion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NumeroContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(CalculadoraParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumero" ):
                listener.enterNumero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumero" ):
                listener.exitNumero(self)


    class AddSubContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)


    class ParentesisContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self):
            return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentesis" ):
                listener.enterParentesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentesis" ):
                listener.exitParentesis(self)


    class PotenciaContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPotencia" ):
                listener.enterPotencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPotencia" ):
                listener.exitPotencia(self)


    class CallFunctionContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def funcion(self):
            return self.getTypedRuleContext(CalculadoraParser.FuncionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallFunction" ):
                listener.enterCallFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallFunction" ):
                listener.exitCallFunction(self)


    class NegativoContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self):
            return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegativo" ):
                listener.enterNegativo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegativo" ):
                listener.exitNegativo(self)


    class MultDivContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultDiv" ):
                listener.enterMultDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultDiv" ):
                listener.exitMultDiv(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CalculadoraParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expresion, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                localctx = CalculadoraParser.CallFunctionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 10
                self.funcion()
                pass
            elif token in [1]:
                localctx = CalculadoraParser.NegativoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 11
                self.match(CalculadoraParser.T__0)
                self.state = 12
                self.expresion(6)
                pass
            elif token in [6]:
                localctx = CalculadoraParser.ParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 13
                self.match(CalculadoraParser.T__5)
                self.state = 14
                self.expresion(0)
                self.state = 15
                self.match(CalculadoraParser.T__6)
                pass
            elif token in [9]:
                localctx = CalculadoraParser.NumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 17
                self.match(CalculadoraParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 31
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 29
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = CalculadoraParser.PotenciaContext(self, CalculadoraParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 20
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 21
                        self.match(CalculadoraParser.T__1)
                        self.state = 22
                        self.expresion(6)
                        pass

                    elif la_ == 2:
                        localctx = CalculadoraParser.MultDivContext(self, CalculadoraParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 23
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 24
                        _la = self._input.LA(1)
                        if not(_la==3 or _la==4):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 25
                        self.expresion(5)
                        pass

                    elif la_ == 3:
                        localctx = CalculadoraParser.AddSubContext(self, CalculadoraParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 26
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 27
                        _la = self._input.LA(1)
                        if not(_la==1 or _la==5):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 28
                        self.expresion(4)
                        pass

             
                self.state = 33
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CalculadoraParser.ID, 0)

        def expresion(self):
            return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,0)


        def getRuleIndex(self):
            return CalculadoraParser.RULE_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncion" ):
                listener.enterFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncion" ):
                listener.exitFuncion(self)




    def funcion(self):

        localctx = CalculadoraParser.FuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_funcion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(CalculadoraParser.ID)
            self.state = 35
            self.match(CalculadoraParser.T__5)
            self.state = 36
            self.expresion(0)
            self.state = 37
            self.match(CalculadoraParser.T__6)
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
        self._predicates[1] = self.expresion_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




