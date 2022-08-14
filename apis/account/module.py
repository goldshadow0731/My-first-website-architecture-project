from common import *
from configs import *
from DB.account import db, UserProfile
from tasks import send_mail


logger = logging.getLogger(__name__)


class User():
    @staticmethod
    def register(payload):
        username = payload.get("username")
        email = payload.get("email")
        password = payload.get("password")
        if username in [None, '', []]:
            return gen_result_format(status=1, message="Username should not be empty.")
        elif UserProfile.query.filter_by(name=username).first():
            logger.info("user has been registered")
            return gen_result_format(status=1, message="The username has been registered.")
        else:
            logger.info("new user register")
            user = UserProfile(name=username, email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            send_mail.delay("Register check",
                            "%s/apis/register-check?uuid=%s" % (
                                DOMAIN_URL, user.uuid),
                            email)
            return gen_result_format()

    @staticmethod
    def register_check(user_uuid):
        user = UserProfile.query.filter_by(uuid=user_uuid).first()
        if user is None:
            return gen_result_format(status=1, message="UUID not found.")
        elif user.verified:
            return gen_result_format(status=1, message="User has verified.")
        else:
            user.verified = True
            db.session.commit()
            return gen_result_format()

    @staticmethod
    def change_password(payload):
        user = UserProfile.query.filter_by(
            name=payload.get("username")).first()
        if not user.verify_password(payload.get("old_password")):
            return gen_result_format(status=1, message="password error")
        else:
            user.set_password(payload.get("new_password"))
            db.session.add(user)
            db.session.commit()
            return gen_result_format(status=0)
