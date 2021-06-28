from flask import Flask, jsonify, request, render_template, make_response, session
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_cors import CORS
from blog_view import blog
from blog_control.user_mgmt import User
import os

# https 만을 지원하는 기능을 HTTP 에서 테스트 할 때 필요한 설정
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__, static_url_path='/static')
CORS(app)

# 세션 정보 보전을 위해 일단 고정된 값
app.secret_key = 'dave_server1'
app.register_blueprint(blog.blog_abtest,url_prefix='/blog')

# login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'



# db 에서 해당 유저를 가지고 온다.
@login_manager.user_loader
def load_user(user_id):
    print(User.get(user_id))
    return User.get(user_id)

@app.before_request
def app_before_request():
    if 'client_id' not in session:
        session['client_id'] = request.environ.get('HTTP_X_REAL_IP',request.remote_addr)

@app.route('/test_A')
def test_A():
    # html file은 templates 폴더에 위치해야 함
    return render_template('blog_A.html')

@app.route('/test_B')
def test_B():
    # html file은 templates 폴더에 위치해야 함
    return render_template('blog_B.html')

@login_manager.unauthorized_handler
def unauthorized():
    return make_response(jsonify(success=False), 401)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)
