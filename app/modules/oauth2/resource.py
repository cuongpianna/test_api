from flask_restful import Resource

from app.modules.oauth2.models import OAuthSignIn


class OAuth2Resource(Resource):
    def get(self, provider):
        oauth = OAuthSignIn.get_provider(provider)
        social_id, username, email = oauth.callback()
        return 1



