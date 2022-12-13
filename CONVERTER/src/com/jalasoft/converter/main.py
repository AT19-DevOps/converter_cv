#
# @main.py Copyright (c) 2022 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from flask import Flask
from flask import request
from flask_restful import Resource
from flask_restful import Api
from werkzeug.utils import secure_filename
import os
import pandas as pd

PATH = 'CONVERTER/src/com/jalasoft/converter/'
UPLOAD_FOLDER = PATH + 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(file):
    file = file.split('.')
    if file[1] in ALLOWED_EXTENSIONS:
        return True
    return False

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
api = Api(app)


class RestAPI(Resource):
    """Defines RestAPI Commands CRUD"""
    def get(self):
        """GET method"""
        data = pd.read_csv(PATH + 'users.csv')
        data = data.to_dict()
        return {'data': data}, 200 

    def post(self):
        """POST method"""
        userId = request.form.get("userId")
        name = request.form.get("name")
        city = request.form.get("city")
        file = request.files['file']
        data = pd.read_csv(PATH + 'users.csv')
        if userId in list(data['userId']):
            return {
                'message': f"'{userId}' already exists."
            }, 401
        else:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            new_data = pd.DataFrame({
                'userId': [userId],
                'name': name,
                'city': city
            })
            data = data.append(new_data, ignore_index=True)
            data.to_csv('users.csv', index=False)
            return {'data': data.to_dict()}, 200

    def put(self):
        """PUT method"""
        userId = request.form.get("userId")
        name = request.form.get("name")
        city = request.form.get("city")
        data = pd.read_csv('users.csv')

        if userId in list(data['userId']):
            user_data = data[data['userId'] == userId]
            user_data['name'] = name
            user_data['city'] = city
            data[data['userId'] == userId] = user_data
            data.to_csv('users.csv', index=False)
            return {'data': data.to_dict()}, 200
        else:
            return {
                'message': f"'{userId}' user not found."
            }, 404

    def delete(self):
        """DELETE method"""
        userId = request.form.get("userId")
        data = pd.read_csv('users.csv')

        if userId in list(data['userId']):
            final_data = data.loc[data['userId'] != userId]
            final_data.to_csv('users.csv', index=False)
            return {'data': final_data.to_dict()}, 200
        else:
            return {
                'message': f"'{userId}' user not found."
            }, 404


api.add_resource(RestAPI, '/')


if __name__ == '__main__':
    app.run(debug=True)