from app.modules.oauth2.models import OAuthSignIn
from app.modules.oauth2 import bp


@bp.route('/authorize/<provider>')
def oauth_authorize(provider):
    # if not current_user.is_anonymous:
    #     return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()


@bp.route('/callback/<provider>')
def oauth_callback(provider):
    # if not current_user.is_anonymous:
    #     return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    social_id, username, email = oauth.callback()
    # if social_id is None:
    #     flash('Authentication failed.')
    #     return redirect(url_for('index'))
    # user = User.query.filter_by(social_id=social_id).first()
    # if not user:
    #     user = User(social_id=social_id, nickname=username, email=email)
    #     db.session.add(user)
    #     db.session.commit()
    # login_user(user, True)
    return 1
