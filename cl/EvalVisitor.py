# Generated from Skyline.g by ANTLR 4.7.2
from skyline import *
import pickle
from .SkylineLexer import SkylineLexer
from .SkylineParser import SkylineParser
from .SkylineVisitor import *
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
else:
    from SkylineParser import SkylineParser


class EvalVisitor(SkylineVisitor):
    def __init__(self, ts, id):
        self.ts = ts
        self.id = id
        self.pathOfUserData = "Data/" + self.id + "/data.dict"

    def visitRoot(self, ctx: SkylineParser.RootContext):
        res = self.visit(ctx.statement())
        print("final")
        #Si s'ha detectat algun error, retorna'l:
        # print(res.intervalos)
        # print(res.values)
        if isinstance(res,str):
            return res,-1,-1

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
        
        if isinstance(sky,str):
            return sky

        self.ts[ident] = sky

        pickle_out = open(self.pathOfUserData, "wb")
        pickle.dump(self.ts, pickle_out)
        pickle_out.close()

        # print(self.ts)
        # img = sky.saveImage()
        return sky

    def visitExprValue(self, ctx: SkylineParser.ExprValueContext):
        res = self.visitChildren(ctx)
        print("checking type")
        print(type(res))
        return res

    def visitExprIdent(self, ctx: SkylineParser.ExprIdentContext):
        id = self.visit(ctx.ident())

        if id in self.ts:
            sky = self.ts.get(id)
            print(id)
            return sky

        else:
            return "ID no trobat"

    def visitSkyCreation(self, ctx: SkylineParser.SkyContext):
        # Creacio de Skyline compost
        if ctx.LB():

            listOfSkylineValues = []

            for sky in ctx.sky():
                xmin = self.visit(sky.integerValue(0))
                height = self.visit(sky.integerValue(1))
                xmax = self.visit(sky.integerValue(2))

                #Comprobació d'errors de xmin i xmax.
                if xmin >= xmax:
                    return "El valor de xmin és major o igual que xmax en un dels edificis que vols crear, que no és vàlid."

                #Comprobació d'errors de height.
                if height <= 0:
                    return "L'alçada dels edificis que vols crear es inferior o igual a 0, que no és valid."

                listOfSkylineValues.append(xmin)
                listOfSkylineValues.append(height)
                listOfSkylineValues.append(xmax)
                print(type(xmin))
            print(listOfSkylineValues)
            print("creating compost")
            sky = Skyline(listOfSkylineValues, 0, type="complex")
            print("doneso")
            print("Done, type is "+ str(type(sky)))

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

            #Comprobació d'errors de xmin i xmax.

            if xmin >= xmax:
                return "El valor de xmin és major o igual que xmax en un dels edificis que vols crear, que no és vàlid."
            
            #Comprobació d'errors de height.
            if height <= 0:
                return "L'alçada dels edificis que vols crear es inferior o igual a 0, que no és valid."

            sky = Skyline(buildings, height, width, xmin, xmax, type="random")

            return sky

    # Visit a parse tree produced by SkylineParser#sky.

    def visitSky(self, ctx: SkylineParser.SkyContext):
        xmin = self.visit(ctx.integerValue(0))
        height = self.visit(ctx.integerValue(1))
        xmax = self.visit(ctx.integerValue(2))

        #Comprobació d'errors de xmin i xmax.
        if xmin >= xmax:
            return "El valor de xmin és major o igual que xmax en un dels edificis que vols crear, que no és vàlid."
        
        #Comprobació d'errors de height.
        if height <= 0:
            return "L'alçada dels edificis que vols crear es inferior o igual a 0, que no és valid."

        return Skyline(xmin, height, xmax)

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

        if isinstance(sky,str):
            return sky

        elif isinstance(val,str):
            return val

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
        
        if isinstance(sky,str):
            return sky

        elif isinstance(val,str):
            return val

        if ctx.PLUS():
            ret = sky + val
            return ret
        elif ctx.MINUS():
            ret = sky - val
            return ret

    # Visit a parse tree produced by SkylineParser#mirror.

    def visitMirror(self, ctx: SkylineParser.MirrorContext):
        sky = self.visit(ctx.expr())

        if isinstance(sky,str):
            return sky

        return -sky
