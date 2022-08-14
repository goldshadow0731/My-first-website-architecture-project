from base_api import app, db, mail_app
from common import *
from configs import *

from apis import api_bp


app.register_blueprint(api_bp)

Log.init_log()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True, load_dotenv=True)
