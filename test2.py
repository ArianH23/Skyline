import sys
from antlr4 import *
from SkylineLexer import SkylineLexer
from SkylineParser import SkylineParser
from SkylineVisitor import SkylineVisitor
from EvalVisitor import EvalVisitor
map = {}
visitor = EvalVisitor(map)

while True:
    input_stream = InputStream(input('? '))


    lexer = SkylineLexer(input_stream)

    token_stream = CommonTokenStream(lexer)

    parser = SkylineParser(token_stream)

    tree = parser.root()

   
    print(type(visitor.visit(tree)))