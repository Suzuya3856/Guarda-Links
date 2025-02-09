from flask import Flask, render_template, url_for, request, redirect

lista_de_links = []

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("inicio.html")


@app.route("/lista")
def listar():

    return render_template("lista.html", lista=lista_de_links)


@app.route("/cad")
def cadastrar():
    return render_template("form_cad.html")


@app.route("/cad", methods=["POST"])
def inserir():
    nome = request.form.get("nome")
    link = request.form.get("link")

    novo_link = {"nome": nome, "link": link}

    lista_de_links.append(novo_link)

    return redirect("/")


if __name__ == "__main__":

    app.run(debug=True)
