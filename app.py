from flask import Flask, render_template, request
import brazilcep
from brazilcep.exceptions import CEPNotFound, InvalidCEP

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/address", methods=['POST'])
def address():
    # function to receive postal code.
    zip_code = request.form['address']

    try:
        data = brazilcep.get_address_from_cep(zip_code)
        street = data["street"]
        city = data["city"]
        uf = data["uf"]
        neighborhood = data["district"]     
        return render_template("address.html", zip_code=zip_code, street=street, city=city, uf=uf, neighborhood=neighborhood)
    except CEPNotFound:
        return "Cep não encontrado" # caso do cep passado em zip_code não ser encontrado
    except InvalidCEP:
        return "Cep inválido." # caso do cep passado em zip_code ser inváliodo.



if __name__ == "__main__":
    app.run(debug=True)
