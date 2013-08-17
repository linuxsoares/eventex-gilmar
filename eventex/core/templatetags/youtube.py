# coding: utf-8

from django.template import (Context, Template, Node, TemplateSyntaxError,
                             Variable, VariableDoesNotExist, Library)

TEMPLATE = '<iframe width="420" height="315" src="//www.youtube.com/embed/{{ id }}" frameborder="0" allowfullscreen></iframe>'



def do_youtube(parser, token):
    try:
        tag_name, id_ = token.split_contents()
    except ValueError:
        raise TemplateSyntaxError, '%r Tag requires 1 argument' % token.contents.split()[0]

    return YoutubeNode(id_)

class YoutubeNode(Node):
    def __init__(self, id_):
        self.id = Variable(id_)

    def render(self, context):
        try:
            actual_id = self.id.resolve(context)
        except VariableDoesNotExist:
            actual_id = self.id

        t = Template(TEMPLATE)
        c = Context({'id': actual_id}, autoescape=context.autoescape)

        return t.render(c)

register = Library()
register.tag('youtube', do_youtube)