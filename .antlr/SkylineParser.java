// Generated from /home/arian/Uni/LP/BotTelegram/Skyline2/Skyline/Skyline.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class SkylineParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		LB=1, RB=2, COMMA=3, ASSIGN=4, PLUS=5, MULT=6, MINUS=7, LP=8, RP=9, LC=10, 
		RC=11, INTVAL=12, ID=13;
	public static final int
		RULE_root = 0, RULE_statement = 1, RULE_expr = 2, RULE_ident = 3, RULE_skyCreation = 4, 
		RULE_sky = 5;
	public static final String[] ruleNames = {
		"root", "statement", "expr", "ident", "skyCreation", "sky"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'{'", "'}'", "','", "':='", "'+'", "'*'", "'-'", "'('", "')'", 
		"'['", "']'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "LB", "RB", "COMMA", "ASSIGN", "PLUS", "MULT", "MINUS", "LP", "RP", 
		"LC", "RC", "INTVAL", "ID"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Skyline.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public SkylineParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class RootContext extends ParserRuleContext {
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public TerminalNode EOF() { return getToken(SkylineParser.EOF, 0); }
		public RootContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_root; }
	}

	public final RootContext root() throws RecognitionException {
		RootContext _localctx = new RootContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_root);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(12);
			statement();
			setState(13);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	 
		public StatementContext() { }
		public void copyFrom(StatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class AssignmentContext extends StatementContext {
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(SkylineParser.ASSIGN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public AssignmentContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class ExprValContext extends StatementContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ExprValContext(StatementContext ctx) { copyFrom(ctx); }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(20);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				_localctx = new AssignmentContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(15);
				ident();
				setState(16);
				match(ASSIGN);
				setState(17);
				expr(0);
				}
				break;
			case 2:
				_localctx = new ExprValContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(19);
				expr(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	 
		public ExprContext() { }
		public void copyFrom(ExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class UnionOffsetContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode PLUS() { return getToken(SkylineParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(SkylineParser.MINUS, 0); }
		public UnionOffsetContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class MirrorContext extends ExprContext {
		public TerminalNode MINUS() { return getToken(SkylineParser.MINUS, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public MirrorContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class SkylineValueContext extends ExprContext {
		public SkyCreationContext skyCreation() {
			return getRuleContext(SkyCreationContext.class,0);
		}
		public SkylineValueContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class ExprIdentContext extends ExprContext {
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public ExprIdentContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class ParenthesisContext extends ExprContext {
		public TerminalNode LP() { return getToken(SkylineParser.LP, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RP() { return getToken(SkylineParser.RP, 0); }
		public ParenthesisContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class InterRepliContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode MULT() { return getToken(SkylineParser.MULT, 0); }
		public InterRepliContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class IntegerValContext extends ExprContext {
		public TerminalNode INTVAL() { return getToken(SkylineParser.INTVAL, 0); }
		public IntegerValContext(ExprContext ctx) { copyFrom(ctx); }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 4;
		enterRecursionRule(_localctx, 4, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(32);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				{
				_localctx = new ParenthesisContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(23);
				match(LP);
				setState(24);
				expr(0);
				setState(25);
				match(RP);
				}
				break;
			case 2:
				{
				_localctx = new MirrorContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(27);
				match(MINUS);
				setState(28);
				expr(6);
				}
				break;
			case 3:
				{
				_localctx = new SkylineValueContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(29);
				skyCreation();
				}
				break;
			case 4:
				{
				_localctx = new IntegerValContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(30);
				match(INTVAL);
				}
				break;
			case 5:
				{
				_localctx = new ExprIdentContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(31);
				ident();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(42);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(40);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
					case 1:
						{
						_localctx = new InterRepliContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(34);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(35);
						match(MULT);
						setState(36);
						expr(6);
						}
						break;
					case 2:
						{
						_localctx = new UnionOffsetContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(37);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(38);
						_la = _input.LA(1);
						if ( !(_la==PLUS || _la==MINUS) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(39);
						expr(5);
						}
						break;
					}
					} 
				}
				setState(44);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class IdentContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(SkylineParser.ID, 0); }
		public IdentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ident; }
	}

	public final IdentContext ident() throws RecognitionException {
		IdentContext _localctx = new IdentContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_ident);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(45);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SkyCreationContext extends ParserRuleContext {
		public List<SkyContext> sky() {
			return getRuleContexts(SkyContext.class);
		}
		public SkyContext sky(int i) {
			return getRuleContext(SkyContext.class,i);
		}
		public TerminalNode LC() { return getToken(SkylineParser.LC, 0); }
		public TerminalNode RC() { return getToken(SkylineParser.RC, 0); }
		public TerminalNode LB() { return getToken(SkylineParser.LB, 0); }
		public List<TerminalNode> INTVAL() { return getTokens(SkylineParser.INTVAL); }
		public TerminalNode INTVAL(int i) {
			return getToken(SkylineParser.INTVAL, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(SkylineParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(SkylineParser.COMMA, i);
		}
		public TerminalNode RB() { return getToken(SkylineParser.RB, 0); }
		public SkyCreationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_skyCreation; }
	}

	public final SkyCreationContext skyCreation() throws RecognitionException {
		SkyCreationContext _localctx = new SkyCreationContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_skyCreation);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(70);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LP:
				{
				setState(47);
				sky();
				}
				break;
			case LC:
				{
				setState(48);
				match(LC);
				setState(49);
				sky();
				setState(54);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(50);
					match(COMMA);
					setState(51);
					sky();
					}
					}
					setState(56);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(57);
				match(RC);
				}
				break;
			case LB:
				{
				setState(59);
				match(LB);
				setState(60);
				match(INTVAL);
				setState(61);
				match(COMMA);
				setState(62);
				match(INTVAL);
				setState(63);
				match(COMMA);
				setState(64);
				match(INTVAL);
				setState(65);
				match(COMMA);
				setState(66);
				match(INTVAL);
				setState(67);
				match(COMMA);
				setState(68);
				match(INTVAL);
				setState(69);
				match(RB);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SkyContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(SkylineParser.LP, 0); }
		public List<TerminalNode> INTVAL() { return getTokens(SkylineParser.INTVAL); }
		public TerminalNode INTVAL(int i) {
			return getToken(SkylineParser.INTVAL, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(SkylineParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(SkylineParser.COMMA, i);
		}
		public TerminalNode RP() { return getToken(SkylineParser.RP, 0); }
		public SkyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sky; }
	}

	public final SkyContext sky() throws RecognitionException {
		SkyContext _localctx = new SkyContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_sky);
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(72);
			match(LP);
			setState(73);
			match(INTVAL);
			setState(74);
			match(COMMA);
			setState(75);
			match(INTVAL);
			setState(76);
			match(COMMA);
			setState(77);
			match(INTVAL);
			setState(78);
			match(RP);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 2:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 5);
		case 1:
			return precpred(_ctx, 4);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17S\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5\3"+
		"\27\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4#\n\4\3\4\3\4\3\4\3"+
		"\4\3\4\3\4\7\4+\n\4\f\4\16\4.\13\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\7\6\67"+
		"\n\6\f\6\16\6:\13\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3"+
		"\6\5\6I\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\2\3\6\b\2\4\6\b\n\f\2"+
		"\3\4\2\7\7\t\t\2V\2\16\3\2\2\2\4\26\3\2\2\2\6\"\3\2\2\2\b/\3\2\2\2\nH"+
		"\3\2\2\2\fJ\3\2\2\2\16\17\5\4\3\2\17\20\7\2\2\3\20\3\3\2\2\2\21\22\5\b"+
		"\5\2\22\23\7\6\2\2\23\24\5\6\4\2\24\27\3\2\2\2\25\27\5\6\4\2\26\21\3\2"+
		"\2\2\26\25\3\2\2\2\27\5\3\2\2\2\30\31\b\4\1\2\31\32\7\n\2\2\32\33\5\6"+
		"\4\2\33\34\7\13\2\2\34#\3\2\2\2\35\36\7\t\2\2\36#\5\6\4\b\37#\5\n\6\2"+
		" #\7\16\2\2!#\5\b\5\2\"\30\3\2\2\2\"\35\3\2\2\2\"\37\3\2\2\2\" \3\2\2"+
		"\2\"!\3\2\2\2#,\3\2\2\2$%\f\7\2\2%&\7\b\2\2&+\5\6\4\b\'(\f\6\2\2()\t\2"+
		"\2\2)+\5\6\4\7*$\3\2\2\2*\'\3\2\2\2+.\3\2\2\2,*\3\2\2\2,-\3\2\2\2-\7\3"+
		"\2\2\2.,\3\2\2\2/\60\7\17\2\2\60\t\3\2\2\2\61I\5\f\7\2\62\63\7\f\2\2\63"+
		"8\5\f\7\2\64\65\7\5\2\2\65\67\5\f\7\2\66\64\3\2\2\2\67:\3\2\2\28\66\3"+
		"\2\2\289\3\2\2\29;\3\2\2\2:8\3\2\2\2;<\7\r\2\2<I\3\2\2\2=>\7\3\2\2>?\7"+
		"\16\2\2?@\7\5\2\2@A\7\16\2\2AB\7\5\2\2BC\7\16\2\2CD\7\5\2\2DE\7\16\2\2"+
		"EF\7\5\2\2FG\7\16\2\2GI\7\4\2\2H\61\3\2\2\2H\62\3\2\2\2H=\3\2\2\2I\13"+
		"\3\2\2\2JK\7\n\2\2KL\7\16\2\2LM\7\5\2\2MN\7\16\2\2NO\7\5\2\2OP\7\16\2"+
		"\2PQ\7\13\2\2Q\r\3\2\2\2\b\26\"*,8H";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}