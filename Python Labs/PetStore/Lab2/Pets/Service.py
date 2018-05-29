from flask import Flask, jsonify, abort, make_response, request
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:11335577@localhost:3306/iot-test-db'
db = SQLAlchemy(app)





class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    type = db.Column(db.String(45))
    price = db.Column(db.Integer)


@app.route('/pets', methods=['GET'])
def get_all_pets():
    pets = []
    all_pets = Pet.query.all()
    for pt in all_pets:
        pet = {
            'name': pt.name,
            'type': pt.type,
            'price': pt.price
        }
        pets.append(pet)
    db.session.commit()
    return jsonify({'pets': pets})


@app.route('/pets/<int:pet_id>', methods=['GET'])
def get_pet(pet_id):
    pt = Pet.query.filter_by(id=pet_id).first()
    pet = {
        'name': pt.name,
        'type': pt.type,
        'price': pt.price
    }
    db.session.commit()
    return jsonify({'pet': pet})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/pets', methods=['POST'])
def add_pet():
    # if not request.json or not 'name' in request.json:
    #     abort(400)
    new_pet = Pet()
    new_pet.iD = request.json['id']
    new_pet.name = request.json['name']
    new_pet.type = request.json.get('type', "")
    new_pet.price = request.json.get('price', 0)

    db.session.add(new_pet)
    db.session.commit()
    return jsonify('Successful')


@app.route('/pets/<int:pet_id>', methods=['PUT'])
def update_pet(pet_id):
    pet = Pet.query.get(pet_id)

    pet.name = request.json['name']
    pet.type = request.json['type']
    pet.price = request.json.get('price', pet.price)
    db.session.commit()
    return jsonify('Successful')


@app.route('/pets/<int:pet_id>', methods=['DELETE'])
def delete_pet(pet_id):
    pt = Pet.query.filter_by(id=pet_id).first()
    db.session.delete(pt)
    db.session.commit()
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True)
