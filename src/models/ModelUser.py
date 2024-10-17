from .entities.User import User

class ModelUser():

    # @Classmethod es un decorador que permite llamar a un método de la clase sin necesidad de instanciarla, tal como se hace en User.check_password
    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, username, password, fullname FROM users
                WHERE username= %s"""
            cursor.execute(sql, (user.username,)) # Ejecuta la consulta y retorna una tupla
            row = cursor.fetchone() # Obtiene la primera fila de la consulta o None si no hay filas
            if row != None:
                user = User(row[0], row[1], User.check_password(row[2], user.password), row[3]) # se accede a los valores de la tupla
                return user
            else:
                return None

        except Exception as ex:
            raise Exception(ex)