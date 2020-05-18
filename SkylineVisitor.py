# Generated from Skyline.g4 by ANTLR 4.7.2
from skyline import *
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
else:
    from SkylineParser import SkylineParser

# This class defines a complete generic visitor for a parse tree produced by SkylineParser.

class SkylineVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SkylineParser#root.
    def visitRoot(self, ctx:SkylineParser.RootContext):
        print("KAPPACHINO")
        res = self.visit(ctx.statement())
        return res


    # Visit a parse tree produced by SkylineParser#exprVal.
    def visitExprVal(self, ctx:SkylineParser.ExprValContext):
        res = self.visitChildren(ctx)
        
        img = res.saveImage()
        
        return img


    # Visit a parse tree produced by SkylineParser#unionOffset.
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
        
        if not isinstance(sky,Skyline):
            return "Error"

        return -sky


    # Visit a parse tree produced by SkylineParser#skylineValue.
    def visitSkylineValue(self, ctx: SkylineParser.SkylineValueContext):
        print("why hello there")
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
    def visitIntegerVal(self, ctx: SkylineParser.IntegerValContext):
        value = int(ctx.INTVAL().getText())
        return value


    # Visit a parse tree produced by SkylineParser#ident.
    def visitIdent(self, ctx: SkylineParser.IdentContext):
        id = ctx.ID().getText()
        return id


    # Visit a parse tree produced by SkylineParser#skyCreation.
    def visitSkyCreation(self, ctx: SkylineParser.SkyContext):
        
        if ctx.sky(0):
            return self.visitSky(ctx.sky(0))

        if ctx.INTVAL(0):
            print("we trying")
            buildings = int(ctx.INTVAL(0).getText())
            height =int(ctx.INTVAL(1).getText())
            width = int(ctx.INTVAL(2).getText())
            xmin = int(ctx.INTVAL(3).getText())
            xmax =int(ctx.INTVAL(4).getText())

            sky = Skyline(buildings,height,width,xmin,xmax,type="random")

            return sky


    # Visit a parse tree produced by SkylineParser#sky.
    def visitSky(self, ctx: SkylineParser.SkyContext):
        
        val0 = int(ctx.INTVAL(0).getText())
        val1 = int(ctx.INTVAL(1).getText())
        val2 = int(ctx.INTVAL(2).getText())

        return Skyline(val0, val1, val2)



del SkylineParser