from werkzeug.security import check_password_hash, generate_password_hash

class User():

    def __init__(self, id, username, password, fullname="") -> None:
        self.id = id
        self.username = username
        self.password = password
        self.fullname = fullname

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)
        # check_password_hash se le  ingresa la contraseña hasheada y la contraseña en texto plano
        # y retorna True si son iguales y False si no lo son

# print(generate_password_hash("Clave Encriptada"))