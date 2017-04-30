from django import template

from datetime import datetime
register=template.Library()

class AllenDateNode(template.Node):
    def __init__(self,format_string):
        self.format_string=format_string
    def render(self, context):
        now=datetime.now().strftime(self.format_string)
        context['mytime']=now
        return ""
@register.tag(name='dateAllen')
def dateAllen(parse,token):
    try:
        tag_name,format_string=token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires a single argument" % token.contents.split()[0])
    return AllenDateNode(format_string[1:-1])
# register.tag(name='dateAllen',compile_function=dateAllen)