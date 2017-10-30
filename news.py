# coding: utf-8

from werkzeug import secure_filename
from flask import Flask, request, url_for, current_app, send_from_directory, render_template
from db import noticias
import os
#from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


app = Flask(__name__, static_folder='assets')
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
app.config['MEDIA_ROOT'] = os.path.join(PROJECT_ROOT, 'media_files')


@app.route("/noticias/cadastrar/", methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":

        dados_do_form = request.form.to_dict()
        imagem = request.files.get('imagem')

        if imagem:
            filename = secure_filename(imagem.filename)
            path = os.path.join(current_app.config['MEDIA_ROOT'], filename)
            imagem.save(path)
            dados_do_form['imagem'] = filename

        id_nova_noticia = noticias.insert(dados_do_form)
        return render_template(
            'cadastro_sucesso.html',
            id_nova_noticia=id_nova_noticia
        )

    return render_template(
        'cadastro.html',
        title=u"Inserir nova noticia"
    )

@app.route('/noticias/remover/<int:noticia_id>')
def remover(noticia_id):
    noticia = noticias.delete(id=noticia_id)

    return render_template(
        'noticia_removida.html',
        noticia_id=noticia_id
    )

@app.route("/noticias/listagem/")
def index():
    todas_as_noticias = list(noticias.all())

    PER_PAGE = 12

    page = request.args.get('page', 1)

    paginator = Paginator(todas_as_noticias, PER_PAGE)
    try:
        lista_noticias = paginator.page(page)
    except PageNotAnInteger:
        lista_noticias = paginator.page(1)
    except EmptyPage:
        lista_noticias = paginator.page(paginator.num_pages)

    return render_template(
        'index.html',
        itens=lista_noticias,
        title=u"Todas as notícias",
    )

@app.route("/noticia/visualizar/<int:noticia_id>")
def noticia(noticia_id):
    noticia = noticias.find_one(id=noticia_id)

    return render_template(
        'noticia.html',
        noticia=noticia
    )

@app.route("/media/<path:filename>")
def media(filename):
     return send_from_directory(current_app.config.get('MEDIA_ROOT'), filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, use_reloader=True)