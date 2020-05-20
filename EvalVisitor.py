# Generated from Skyline.g by ANTLR 4.7.2
from skyline import *
from antlr4 import *
from SkylineVisitor import *
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
else:
    from SkylineParser import SkylineParser
import pickle

class EvalVisitor(SkylineVisitor):
    def __init__(self, ts, id):
        self.ts = ts
        self.id = id

    def visitAssignment(self, ctx: SkylineParser.AssignmentContext):
        ident = self.visit(ctx.ident())

        sky = self.visit(ctx.expr())
        
        self.ts[ident] = sky

        pickle_out = open("Data/" + self.id + "/data.dict", "wb")
        pickle.dump(self.ts, pickle_out)
        pickle_out.close()
        
        print(self.ts)
        img = sky.saveImage()
        return img


    def visitExprIdent(self, ctx: SkylineParser.ExprIdentContext):
        id = self.visit(ctx.ident())

        if id in self.ts:
            sky = self.ts.get(id)
            print (id)
            return sky
        
        else:
            return "Error"