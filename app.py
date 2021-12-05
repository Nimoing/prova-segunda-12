from  flask import Flask #importa

from api.conta import conta #importa1
from api.lista_conta import listaconta #importa2
from api.delet_nova import deletnova #importa3
from api.info import info #importa4
from api.salario import salario #importa5
app= Flask(__name__)

#criar um endpoint
app.register_blueprint(conta,url_prefix='/api/conta/')
app.register_blueprint(listaconta,url_prefix='/api/listaconta/')
app.register_blueprint(deletnova,url_prefix='/api/deletnova/')
app.register_blueprint(info,url_prefix='/api/info/')
app.register_blueprint(salario,url_prefix='/api/salario/')

#xy.com/alguma coisa que vc decide
@app.route("/")#aqui<<
def hello():
    return "API controle de conta"

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)#quando for posta tira debug
