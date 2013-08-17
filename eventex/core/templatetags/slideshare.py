# coding: utf-8

from django import template
from django.template import (Context, Template, Node)


TEMPLATE = """ <iframe src="//www.slideshare.net/slideshow/embed_code/{{ id }}?rel=0" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="max-width:427px;border:1px solid #CCC;border-width:1px 1px 0;margin-bottom:5px" allowfullscreen webkitallowfullscreen mozallowfullscreen> </iframe> """


def do_slide(parser, token):
    try:
        tag_name, id_ = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires 1 argument" % token.contents.split()[0]
    return SlideShareNode(id_)


class SlideShareNode(Node):
    def __init__(self, id_):
        self.id = template.Variable(id_)

    def render(self, context):
        try:
            actual_id = self.id.resolve(context)
        except template.VariableDoesNotExist:
            actual_id = self.id

        t = Template(TEMPLATE)
        c = Context({'id': actual_id}, autoescape=context.autoescape)
        return t.render(c)


register = template.Library()
register.tag('slideshare', do_slide)