#
# @database_connection.py Copyright (c) 2023 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
#
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#


import pymysql

class DatabaseConnection:
    """Defines the connection to the database"""

    try:
        conexion = pymysql.connect(host='127.0.0.1',
                                   user='root',
                                   password='',
                                   db='converter_db')
        print("Successful connection")
        
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("An error occurred while connecting: ", e)
