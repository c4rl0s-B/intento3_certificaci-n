from flask_app import app

#ACA NO SE NOS OLVIDE, DEBEMOS IMPORTAR LOS CONTROLADORES
#QUE CREEMOS

#-------------
from flask_app.controllers import usuarios
from flask_app.controllers import misiones


if __name__=="__main__": 

   app.run(debug=True)



