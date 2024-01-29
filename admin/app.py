from typing import cast

from flask import Flask

from db.base import sync_session
from db.models.language import Individual
from flask_admin import Admin, AdminIndexView


def create_app() -> Flask:
    app = Flask(__name__)

    app.config['FLASK_ADMIN_SWATCH'] = 'Cosmo'
    app.secret_key = 'kek'

    admin = Admin(app, name='2 НДФЛ', index_view=AdminIndexView(name='📃', url='/'), template_mode='bootstrap4')

    from admin.views.individual import IndividualView

    admin.add_view(IndividualView(Individual, sync_session, name='Физлицо'))

    return cast(Flask, admin.app)


if __name__ == '__main__':

    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
