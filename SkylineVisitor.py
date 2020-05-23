# Generated from Skyline.g4 by ANTLR 4.7.2
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


    # Visit a parse tree produced by SkylineParser#assignment.
    def visitAssignment(self, ctx:SkylineParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#exprVal.
    def visitExprVal(self, ctx:SkylineParser.ExprValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#unionOffset.
    def visitUnionOffset(self, ctx:SkylineParser.UnionOffsetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#mirror.
    def visitMirror(self, ctx:SkylineParser.MirrorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#skylineValue.
    def visitSkylineValue(self, ctx:SkylineParser.SkylineValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#exprIdent.
    def visitExprIdent(self, ctx:SkylineParser.ExprIdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#parenthesis.
    def visitParenthesis(self, ctx:SkylineParser.ParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#interRepli.
    def visitInterRepli(self, ctx:SkylineParser.InterRepliContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#integerVal.
    def visitIntegerVal(self, ctx:SkylineParser.IntegerValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#ident.
    def visitIdent(self, ctx:SkylineParser.IdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#skyCreation.
    def visitSkyCreation(self, ctx:SkylineParser.SkyCreationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#sky.
    def visitSky(self, ctx:SkylineParser.SkyContext):
        return self.visitChildren(ctx)



del SkylineParser