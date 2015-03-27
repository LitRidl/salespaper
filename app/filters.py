import jinja2
import flask
import babel
import re

from jinja2 import evalcontextfilter, Markup, escape


mod = flask.Blueprint('filters', __name__)


@mod.app_template_filter('datetime')
def format_datetime(value, format='dd.MM.yyyy HH:mm'):
    return babel.dates.format_datetime(value, format)


_paragraph_re = re.compile(r'(?:\r\n|\r|\n){2,}')


@mod.app_template_filter('nl2br')
@evalcontextfilter
def nl2br(eval_ctx, value):
    result = u'\n\n'.join(u'<p>%s</p>' % p.replace('\n', '<br>\n') for p in _paragraph_re.split(escape(value)))
    if eval_ctx.autoescape:
        result = Markup(result)
    return result
