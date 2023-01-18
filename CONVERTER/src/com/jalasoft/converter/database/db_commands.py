#
# @db_commands.py Copyright (c) 2022 Jalasoft.
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


from database.database_connection import DatabaseConnection as db

mycursor = db.conexion.cursor()

class CRUD:
    """"Defines Create, Read, Update and Delete functions"""

    def create_table(tablename):
        """Creates a table"""

        with mycursor:
            mycursor.execute("""SELECT COUNT(*) FROM information_schema.tables WHERE table_name = '{0}' """.format(tablename.replace('\'', '\'\'')))
            if mycursor.fetchone()[0] == 1:
                print("Table already created")
                db.conexion.close()
                return
            mycursor.execute("CREATE TABLE "+tablename+" (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), checksum VARCHAR(255), route VARCHAR(155))")
            print("Table created")
            db.conexion.close()
            return

    def check_table_exists(tablename):
        """Checks if table exists"""

        mycursor.execute("""
            SELECT COUNT(*)
            FROM information_schema.tables
            WHERE table_name = '{0}'
            """.format(tablename.replace('\'', '\'\'')))
        if mycursor.fetchone()[0] == 1:
            mycursor.close()
            return True
        mycursor.close()
        return False
    
    def insert_data( name, checksum, route):
        """Inserts data"""
      
        query = "INSERT INTO media (name, checksum, route) VALUES (%s, %s, %s)"    
        mycursor.execute(query, (name, checksum, route))
        print("Data inserted")
        db.conexion.close()
    
    def read_all_data():
        """Reads all data"""
    
        query = "SELECT name, checksum, route FROM media"
        mycursor.execute(query)
        datos = mycursor.fetchall()
        for dato in datos:
            print(dato)
        print("Data read")
        db.conexion.close()

    def read_specific_data(name):
        """Reads data searching by its name"""
    
        query = "SELECT name, checksum, route FROM person WHERE name = %s"    
        mycursor.execute(query,(name))
        datos = mycursor.fetchall()
        for dato in datos:
            print(dato)
        print("Data read")
        db.conexion.close()

    def update_data(newName,id):
        """Updates data"""
    
        query = "UPDATE media SET name = %s  WHERE id = %s"
        mycursor.execute(query, (newName, id))
        print("Data updated")
        db.conexion.close()


    def delete_data(id):
        """Deletes data"""
    
        query = "DELETE FROM media WHERE id = %s"
        mycursor.execute(query, (id))
        print("Data deleted")
        db.conexion.close()
