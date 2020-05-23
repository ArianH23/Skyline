# Generated from Skyline.g by ANTLR 4.7.2
from skyline import *
from antlr4 import *
from .SkylineLexer import SkylineLexer
from .SkylineParser import SkylineParser
from .SkylineVisitor import *
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
else:
    from SkylineParser import SkylineParser


import pickle


class EvalVisitor(SkylineVisitor):
    def __init__(self, ts, id):
        self.ts = ts
        self.id = id

    def visitRoot(self, ctx: SkylineParser.RootContext):
        res = self.visit(ctx.statement())

        img = res.saveImage()
        height = res.get_height()
        area = res.get_area()

        return img, height, area

    def visitIdent(self, ctx: SkylineParser.IdentContext):
        id = ctx.ID().getText()
        return id

    def visitAssignment(self, ctx: SkylineParser.AssignmentContext):
        ident = self.visit(ctx.ident())
        sky = self.visit(ctx.expr())

        self.ts[ident] = sky

        pickle_out = open("Data/" + self.id + "/data.dict", "wb")
        pickle.dump(self.ts, pickle_out)
        pickle_out.close()

        # print(self.ts)
        # img = sky.saveImage()
        return sky

    def visitExprValue(self, ctx: SkylineParser.ExprValueContext):
        res = self.visitChildren(ctx)


        return res

    def visitExprIdent(self, ctx: SkylineParser.ExprIdentContext):
        id = self.visit(ctx.ident())

        if id in self.ts:
            sky = self.ts.get(id)
            print(id)
            return sky

        else:
            return "Error"

    def visitSkyCreation(self, ctx: SkylineParser.SkyContext):
        # Creacio de skyline compost
        if ctx.LB():

            listOfSkylineValues = []

            for sky in ctx.sky():
                listOfSkylineValues.append(int(sky.integerValue(0).getText()))
                listOfSkylineValues.append(int(sky.integerValue(1).getText()))
                listOfSkylineValues.append(int(sky.integerValue(2).getText()))

            sky = Skyline(listOfSkylineValues, 0, type="complex")

            return sky

        # Creacio de Skyline simple
        elif ctx.sky(0):
            return self.visitSky(ctx.sky(0))

        # Creacio de Skyline random
        elif ctx.LC():
            buildings = self.visit(ctx.integerValue(0))
            height = self.visit(ctx.integerValue(1))
            width = self.visit(ctx.integerValue(2))
            xmin = self.visit(ctx.integerValue(3))
            xmax = self.visit(ctx.integerValue(4))
            
            sky = Skyline(buildings, height, width, xmin, xmax, type="random")

            return sky

    # Visit a parse tree produced by SkylineParser#sky.

    def visitSky(self, ctx: SkylineParser.SkyContext):
        val0 = self.visit(ctx.integerValue(0))
        val1 = self.visit(ctx.integerValue(1))
        val2 = self.visit(ctx.integerValue(2))

        return Skyline(val0, val1, val2)

    def visitSkylineValue(self, ctx: SkylineParser.SkylineValueContext):
        # print("why hello there")
        return self.visitSkyCreation(ctx.skyCreation())

    # Visit a parse tree produced by SkylineParser#parenthesis.

    def visitParenthesis(self, ctx: SkylineParser.ParenthesisContext):
        return self.visit(ctx.expr())

    # Visit a parse tree produced by SkylineParser#interRepli.

    def visitInterRepli(self, ctx: SkylineParser.InterRepliContext):
        sky = self.visit(ctx.expr(0))
        val = self.visit(ctx.expr(1))

        ret = sky * val
        return ret

    # Visit a parse tree produced by SkylineParser#integerVal.

    def visitPosIntegerValue(self, ctx: SkylineParser.PosIntegerValueContext):
        value = int(ctx.INTVAL().getText())

        return value

    # Visit a parse tree produced by SkylineParser#negIntegerValue.
    def visitNegIntegerValue(self, ctx:SkylineParser.NegIntegerValueContext):
        value = int(ctx.INTVAL().getText())

        return -value


    def visitUnionOffset(self, ctx: SkylineParser.UnionOffsetContext):

        sky = self.visit(ctx.expr(0))
        val = self.visit(ctx.expr(1))
        
        if ctx.PLUS():
            ret = sky + val
            return ret
        elif ctx.MINUS():
            ret = sky - val
            return ret

        return "Error"

    # Visit a parse tree produced by SkylineParser#mirror.

    def visitMirror(self, ctx: SkylineParser.MirrorContext):
        sky = self.visit(ctx.expr())

        if not isinstance(sky, Skyline):
            return "Error"

        return -sky
