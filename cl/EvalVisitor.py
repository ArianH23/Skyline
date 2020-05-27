# Generated from Skyline.g by ANTLR 4.7.2
from skyline import *
import pickle
from .SkylineLexer import SkylineLexer
from .SkylineParser import SkylineParser
from .SkylineVisitor import *
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser


class EvalVisitor(SkylineVisitor):
    def __init__(self, ts, id):
        self.ts = ts
        self.id = id
        self.pathOfUserData = "Data/" + self.id + "/data.dict"

    def visitRoot(self, ctx: SkylineParser.RootContext):
        res = self.visit(ctx.statement())

        # Si s'ha detectat algun error, retorna'l:
        if isinstance(res, str):
            return res, -1, -1

        img = res.saveImage()
        height = res.get_height()
        area = res.get_area()

        return img, height, area

    def visitAssignment(self, ctx: SkylineParser.AssignmentContext):
        ident = self.visit(ctx.ident())
        sky = self.visit(ctx.expr())

        # Comproba si sky és un error:
        if isinstance(sky, str):
            return sky

        self.ts[ident] = sky

        pickle_out = open(self.pathOfUserData, "wb")
        pickle.dump(self.ts, pickle_out)
        pickle_out.close()

        return sky

    def visitExprValue(self, ctx: SkylineParser.ExprValueContext):
        res = self.visitChildren(ctx)

        return res

    def visitParenthesis(self, ctx: SkylineParser.ParenthesisContext):
        return self.visit(ctx.expr())

    def visitMirror(self, ctx: SkylineParser.MirrorContext):
        sky = self.visit(ctx.expr())

        # Comprobació de si sky és un error.
        if isinstance(sky, str):
            return sky

        return -sky

    def visitInterRepli(self, ctx: SkylineParser.InterRepliContext):
        sky = self.visit(ctx.expr(0))
        val = self.visit(ctx.expr(1))

        # Comprobació de si un dels dos valor visitats és un error.
        if isinstance(sky, str):
            return sky

        elif isinstance(val, str):
            return val

        ret = sky * val
        return ret

    def visitUnionOffset(self, ctx: SkylineParser.UnionOffsetContext):

        sky = self.visit(ctx.expr(0))
        val = self.visit(ctx.expr(1))

        # Comprobació de si un dels dos valor visitats és un error.
        if isinstance(sky, str):
            return sky

        elif isinstance(val, str):
            return val

        if ctx.PLUS():
            ret = sky + val
            return ret

        elif ctx.MINUS():
            ret = sky - val
            return ret

    def visitSkylineValue(self, ctx: SkylineParser.SkylineValueContext):

        return self.visit(ctx.skyCreation())

    def visitExprIdent(self, ctx: SkylineParser.ExprIdentContext):
        id = self.visit(ctx.ident())

        if id in self.ts:
            sky = self.ts.get(id)
            print(id)
            return sky

        else:
            return "ID \'" + id + "\' no trobat"

    def visitIdent(self, ctx: SkylineParser.IdentContext):
        id = ctx.ID().getText()
        return id

    def visitSkyCreation(self, ctx: SkylineParser.SkyContext):
        # Creacio de Skyline compost
        if ctx.LB():

            listOfSkylineValues = []

            for sky in ctx.sky():
                xmin = self.visit(sky.integerValue(0))
                height = self.visit(sky.integerValue(1))
                xmax = self.visit(sky.integerValue(2))

                # Comprobació d'errors de xmin i xmax.
                if xmin >= xmax:
                    return "ERROR: El valor de xmin és major o igual que xmax en un dels edificis que vols crear, que no és vàlid."

                # Comprobació d'errors de height.
                if height < 0:
                    return "ERROR: L'alçada dels edificis que vols crear es negativa, que no és vàlid."

                listOfSkylineValues.append([xmin, height, xmax])

            sky = Skyline(listOfSkylineValues, type="complex")

            return sky

        # Creacio de Skyline random
        elif ctx.LC():

            buildings = self.visit(ctx.integerValue(0))
            height = self.visit(ctx.integerValue(1))
            width = self.visit(ctx.integerValue(2))
            xmin = self.visit(ctx.integerValue(3))
            xmax = self.visit(ctx.integerValue(4))

            # Comprobació d'errors de xmin i xmax.
            if xmin >= xmax:
                return "ERROR: El valor de xmin és major o igual que xmax en un dels edificis que vols crear, que no és vàlid."

            # Comprobació d'errors de height.
            if height < 0:
                return "ERROR: L'alçada dels edificis que vols crear es negativa, que no és vàlid."

            sky = Skyline(buildings, height, width, xmin, xmax, type="random")

            return sky

        # Creacio de Skyline simple
        elif ctx.sky(0):
            return self.visitSky(ctx.sky(0))

    def visitSky(self, ctx: SkylineParser.SkyContext):
        xmin = self.visit(ctx.integerValue(0))
        height = self.visit(ctx.integerValue(1))
        xmax = self.visit(ctx.integerValue(2))

        # Comprobació d'errors de xmin i xmax.
        if xmin >= xmax:
            return "ERROR: El valor de xmin és major o igual que xmax en un dels edificis que vols crear, que no és vàlid."

        # Comprobació d'errors de height.
        if height < 0:
            return "ERROR: L'alçada dels edificis que vols crear es negativa, que no és vàlid."

        return Skyline(xmin, height, xmax)

    def visitPosIntegerValue(self, ctx: SkylineParser.PosIntegerValueContext):
        value = int(ctx.INTVAL().getText())

        return value

    def visitNegIntegerValue(self, ctx: SkylineParser.NegIntegerValueContext):
        value = int(ctx.INTVAL().getText())

        return -value
