// Generated from /home/arian/Uni/LP/BotTelegram/Skyline/Skyline.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class SkylineLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		LC=1, RC=2, COMMA=3, ASSIGN=4, PLUS=5, MULT=6, MINUS=7, LP=8, RP=9, LB=10, 
		RB=11, INTVAL=12, ID=13, WS=14;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"LC", "RC", "COMMA", "ASSIGN", "PLUS", "MULT", "MINUS", "LP", "RP", "LB", 
		"RB", "INTVAL", "ID", "WS"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'{'", "'}'", "','", "':='", "'+'", "'*'", "'-'", "'('", "')'", 
		"'['", "']'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "LC", "RC", "COMMA", "ASSIGN", "PLUS", "MULT", "MINUS", "LP", "RP", 
		"LB", "RB", "INTVAL", "ID", "WS"
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


	public SkylineLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Skyline.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20L\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3"+
		"\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\5"+
		"\r8\n\r\3\r\6\r;\n\r\r\r\16\r<\3\16\3\16\7\16A\n\16\f\16\16\16D\13\16"+
		"\3\17\6\17G\n\17\r\17\16\17H\3\17\3\17\2\2\20\3\3\5\4\7\5\t\6\13\7\r\b"+
		"\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\3\2\4\5\2C\\aac|\6\2\62;"+
		"C\\aac|\2O\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2"+
		"\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27"+
		"\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\3\37\3\2\2\2\5!\3\2\2"+
		"\2\7#\3\2\2\2\t%\3\2\2\2\13(\3\2\2\2\r*\3\2\2\2\17,\3\2\2\2\21.\3\2\2"+
		"\2\23\60\3\2\2\2\25\62\3\2\2\2\27\64\3\2\2\2\31\67\3\2\2\2\33>\3\2\2\2"+
		"\35F\3\2\2\2\37 \7}\2\2 \4\3\2\2\2!\"\7\177\2\2\"\6\3\2\2\2#$\7.\2\2$"+
		"\b\3\2\2\2%&\7<\2\2&\'\7?\2\2\'\n\3\2\2\2()\7-\2\2)\f\3\2\2\2*+\7,\2\2"+
		"+\16\3\2\2\2,-\7/\2\2-\20\3\2\2\2./\7*\2\2/\22\3\2\2\2\60\61\7+\2\2\61"+
		"\24\3\2\2\2\62\63\7]\2\2\63\26\3\2\2\2\64\65\7_\2\2\65\30\3\2\2\2\668"+
		"\7/\2\2\67\66\3\2\2\2\678\3\2\2\28:\3\2\2\29;\4\62;\2:9\3\2\2\2;<\3\2"+
		"\2\2<:\3\2\2\2<=\3\2\2\2=\32\3\2\2\2>B\t\2\2\2?A\t\3\2\2@?\3\2\2\2AD\3"+
		"\2\2\2B@\3\2\2\2BC\3\2\2\2C\34\3\2\2\2DB\3\2\2\2EG\7\"\2\2FE\3\2\2\2G"+
		"H\3\2\2\2HF\3\2\2\2HI\3\2\2\2IJ\3\2\2\2JK\b\17\2\2K\36\3\2\2\2\7\2\67"+
		"<BH\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}