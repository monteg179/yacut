from flask import (
    flash,
    redirect,
    render_template,
    Response,
    url_for,
)

from yacut import app, db
from yacut.forms import URLMapForm
from yacut.models import URLMap


@app.route("/", methods=("GET", "POST"))
def index_view() -> str:
    form = URLMapForm()
    if not form.validate_on_submit():
        print(form.original_link.errors)
        print(form.custom_id.errors)
        return render_template("index.html", form=form)
    custom_id = form.custom_id.data
    if custom_id and URLMap.short_exist(custom_id):
        flash('Предложенный вариант короткой ссылки уже существует.')
        return render_template('index.html', form=form)
    instance = URLMap(
        original=form.original_link.data,
        short=custom_id,
    )
    db.session.add(instance)
    db.session.commit()
    form.custom_id.data = None
    url = url_for('mapping_redirect', short=instance.short, _external=True)
    flash(url, 'short')
    return render_template('index.html', form=form)


@app.route("/<string:short>", strict_slashes=False)
def mapping_redirect(short: str) -> Response:
    url = URLMap.query.filter_by(short=short).first_or_404().original
    return redirect(url)
