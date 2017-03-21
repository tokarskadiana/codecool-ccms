from flask import url_for, render_template
from controller.decorators import login_required
import os
from app import app


@app.context_processor
def override_url_for():
    """Overrides url_for with additional values on end (cache prevent)"""
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    """Add on end to static files a int value(time)  """
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


@app.errorhandler(404)
@login_required
def page_not_found(e):
    return render_template('404.html'), 404
