from jinja2 import Environment
from demo.templatetags.poll_extras import  lower
def environment(**options):
    env=Environment(**options)
    env.filters['allen_lower']=lower
    return env