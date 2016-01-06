#!/usr/bin/env python
import os
import jinja2
import webapp2
import random

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        self.render_template("index.html")

class lotoHandler(BaseHandler):
    def get(self):
        def osemStevilk():
            seznamStevilk = []
            stevecStevilk = 0
            while stevecStevilk != 8:
                nakljucnoSt = random.randint(1,50)
                if nakljucnoSt not in seznamStevilk:
                    seznamStevilk.append(nakljucnoSt)
                    stevecStevilk +=1
                else:
                    continue
            return seznamStevilk

        def dodatniStevilki():
            seznamDodatnih = []
            stevecDodatnih = 0
            while stevecDodatnih != 2:
                    nakljucnoSt = random.randint(1,8)
                    if nakljucnoSt not in seznamDodatnih:
                        seznamDodatnih.append(nakljucnoSt)
                        stevecDodatnih +=1
                    else:
                        continue
            return seznamDodatnih



        vsebina = str(osemStevilk()) + " " + str(dodatniStevilki())
        params = {"sporocilo": vsebina}
        self.render_template("loto.html", params=params)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/loto', lotoHandler),


], debug=True)
