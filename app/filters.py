import jinja2
import flask
import babel

mod = flask.Blueprint('filters', __name__)


@mod.app_template_filter('datetime')
def format_datetime(value, format='dd.MM.yyyy HH:mm'):
    return babel.dates.format_datetime(value, format)


@jinja2.contextfilter
@mod.app_template_filter()
def filter2(context, value):
    return 2

