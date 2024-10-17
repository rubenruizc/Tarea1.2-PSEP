from flask import *
from .personas.personas import personasBP
from .moviles.moviles import movilesBP

app = Flask(__name__)

app.register_blueprint(personasBP,url_prefix='/personas')
app.register_blueprint(movilesBP,url_prefix='/moviles')