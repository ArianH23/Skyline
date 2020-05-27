default:
	python3 bot.py
antlrv	:
	antlr4 -Dlanguage=Python3 -no-listener -visitor cl/Skyline.g4

clean	:
	rm Skyline.interp
	rm Skyline.tokens
	rm SkylineLexer*
	rm SkylineP*
tar:
	rm -rf Data/*
	tar -zcvf practica.tar cl/S* cl/EvalVisitor.py compromis.pdf bot.py README.md requirements.txt skyline.py Data

