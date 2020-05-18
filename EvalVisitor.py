# Generated from Skyline.g by ANTLR 4.7.2
from skyline import *
from antlr4 import *
from SkylineVisitor import *
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
else:
    from SkylineParser import SkylineParser


class EvalVisitor(SkylineVisitor):
    def __init__(self, ts):
        self.ts = ts

    def visitAssignment(self, ctx: SkylineParser.AssignmentContext):
        ident = self.visit(ctx.ident())

        sky = self.visit(ctx.expr())
        
        self.ts[ident] = sky
        img = sky.saveImage()
        return img


    def visitExprIdent(self, ctx: SkylineParser.ExprIdentContext):
        id = self.visit(ctx.ident())
        print ("error")
        if id in self.ts:
            sky = self.ts.get(id)
            return sky
        
        else:
            return "Error"