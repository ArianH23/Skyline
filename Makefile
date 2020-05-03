default:
	python3 bot.py
antlrv	:
	antlr4 -Dlanguage=Python3 -no-listener -visitor Skyline.g

clean	:
	rm Skyline.interp
	rm Skyline.tokens
	rm SkylineLexer*
	rm SkylineP*