from flask import Flask, request, url_for
from db import noticias

layout = u"""
  <html>
  <head>
      <title>{title}</title>
  </head>
  <body>
     {body}
  </body>
  </html>
"""

@app.route("/noticias/cadastro/")
def cadastro():
    if request.method == "POST":
        dados_do_form = request.form.to_dict()


#Inicialmente não vamos nos preocupar com segurança, csrf ou login, mas nos próximos capítulos desta série iremos evoluir este pequeno app.
#http://pythonclub.com.br/what-the-flask-pt-1-introducao-ao-desenvolvimento-web-com-python.html#o_que_e_flask