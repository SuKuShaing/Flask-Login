from flask import Flask
from config import config # Importa el diccionario de configuraciones

app = Flask(__name__)

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()