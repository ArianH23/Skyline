# Generated from Skyline.g by ANTLR 4.7.2
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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#replication.
    def visitReplication(self, ctx:SkylineParser.ReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#mirror.
    def visitMirror(self, ctx:SkylineParser.MirrorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#offset.
    def visitOffset(self, ctx:SkylineParser.OffsetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#assignment.
    def visitAssignment(self, ctx:SkylineParser.AssignmentContext):

        ident = self.visit(ctx.ident())
        print("el ident es " + ident)
        sky = self.visit(ctx.expr())

        # print("xdddd")
        # return sky.saveImage()
        sky.saveImage()

        return sky


    # Visit a parse tree produced by SkylineParser#skylineValue.
    def visitSkylineValue(self, ctx:SkylineParser.SkylineValueContext):
        print("soy val")
        return self.visit(ctx.sky())


    # Visit a parse tree produced by SkylineParser#exprIdent.
    def visitExprIdent(self, ctx:SkylineParser.ExprIdentContext):
        return self.visit(ctx.ident())



    # Visit a parse tree produced by SkylineParser#instersection.
    def visitInstersection(self, ctx:SkylineParser.InstersectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#union.
    def visitUnion(self, ctx:SkylineParser.UnionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#parenthesis.
    def visitParenthesis(self, ctx:SkylineParser.ParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#ident.
    def visitIdent(self, ctx:SkylineParser.IdentContext):
        id = ctx.ID().getText()
        return id


    # Visit a parse tree produced by SkylineParser#sky.
    def visitSky(self, ctx:SkylineParser.SkyContext):
        print ("holas")
        val0 = int(ctx.INTVAL(0).getText())
        val1 = int(ctx.INTVAL(1).getText())
        val2 = int(ctx.INTVAL(2).getText())
        print ("dew")
        return  Skyline("a", val0, val1, val2)
        return self.visitChildren(ctx)



del SkylineParser