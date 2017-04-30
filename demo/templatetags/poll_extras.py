from django import template

from datetime import datetime
register=template.Library()

# class AllenDateNode(template.Node):
#     def __init__(self,format_string,asvar):
#         self.format_string=format_string
#         self.asvar=asvar
#
#     def render(self, context):
#         now=datetime.now().strftime(self.format_string)
#         if self.asvar:
#             context[self.asvar]=now
#             return ""
#         else:
#             return now
# @register.tag()
# def dateAllen(parse,token):
#     args=token.split_contents()
#     asvar=None
#     if len(args)==4 and args[-2]=='as':
#         asvar=args[-1]
#     elif len(args)!=2:
#         raise template.TemplateSyntaxError('invalid args error')
#     return AllenDateNode(args[1][1:-1],asvar)
# register.tag(name='dateAllen',compile_function=dateAllen)
@register.assignment_tag()
def get_current_time(format_string):
    return datetime.now().strftime(format_string)