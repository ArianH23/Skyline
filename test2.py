import sys
from antlr4 import *
from SkylineLexer import SkylineLexer
from SkylineParser import SkylineParser
from SkylineVisitor import SkylineVisitor

map = {}

while True:
    input_stream = InputStream(input('? '))


    lexer = SkylineLexer(input_stream)

    token_stream = CommonTokenStream(lexer)

    parser = SkylineParser(token_stream)

    tree = parser.root() 

    visitor = SkylineVisitor()
    visitor.visit(tree)