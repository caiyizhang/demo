from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/demo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.String(10), nullable=False)

    def to_dict(self):
        return {
            'uid': self.uid,
            'name': self.name,
            'gender': self.gender
        }

with app.app_context():
    db.create_all()
    print('Tables created successfully.')


@app.route('/get_user_list', methods=['GET'])
def get_user_list():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    new_user = User(name=data['name'], gender=data['gender'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

@app.route('/edit_user/<int:uid>', methods=['PUT'])
def edit_user(uid):
    user = User.query.get_or_404(uid)
    data = request.json
    user.name = data.get('name', user.name)
    user.gender = data.get('gender', user.gender)
    db.session.commit()
    return jsonify(user.to_dict())

if __name__ == '__main__':
    # db.create_all() # 创建表
    app.run(host='0.0.0.0', port=5000)