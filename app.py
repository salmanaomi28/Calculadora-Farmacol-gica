from distutils.log import debug
from flask import Flask
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/densidad/<string:volumen>/<string:masa>")
def get_datosD(volumen,masa):
    volumen = float(volumen)
    masa = float(masa)
    densidad = masa/volumen
    return jsonify({ "densidad" : densidad})


@app.route("/masa/<string:densidad>/<string:volumen>")
def get_datosM(volumen,densidad):
    volumen = float(volumen)
    densidad = float(densidad)
    masa = volumen*densidad
    return jsonify({ "masa" : masa})

@app.route("/volumen/<string:densidad>/<string:masa>")
def get_datosV(masa,densidad):
    masa = float(masa)
    densidad = float(densidad)
    volumen = masa/densidad
    return jsonify({ "volumen" : volumen})


if __name__ == '_main_':
    app.run(debug=True, port=4000)