import os
from flask import Flask, render_template, make_response

app = Flask(__name__,)

frettir = [
    ["0","Má rannsaka innihald farsíma",
     "Dómi Héraðsdóms Vest­ur­lands, þess efn­is að lög­reglu­stjór­an­um á Vest­ur­landi væri óheim­ilt að rann­saka ra­f­rænt inni­hald farsíma sem embættið tel­ur að geti varpað ljósi á meinta lík­ams­árás, var snúið við í Lands­rétti fyr­ir helgi þar sem rann­sókn­in var heim­iluð. "
     "Fuad@tskoli.is"],
    ["1","RÚV sektað fyrir Golfið",
     "RÚV hef­ur verið gert að greiða eina millj­ón krón­ur í stjórn­valds­sekt vegna brota á lög­um um Rík­is­út­varpið, að því er kem­ur fram í ákvörðun Fjöl­miðlanefnd­ar vegna kost­un­ar Golf­sam­bands Íslands á þáttaröðinni Golfið sem var á dag­skrá RÚV síðasta sum­ar."
     "Fuad@tskoli.is"],
    ["2","Segir af­reksíþróttafólk í áhættuhópi",
     "Íþrótta­sam­fé­lagið og sér­fræðing­ar í barna­vernd­ar­mál­um þurfa að vinna bet­ur sam­an að því að skapa ör­uggt um­hverfi fyr­ir börn og ung­menni í íþrótt­um en 22,8% af­reksíþrótta­manna hafa átt í kyn­ferðis­legu sam­bandi við aðila sem er vald­meiri í íþrótt­inni en viðkom­andi."
     "Fuad@tskoli.is"]
    ]

@app.route('/')
@app.route("/")
def Homepage():
    return render_template('index.tpl', frettir=frettir)

@app.route('/frett/<int:id>')
def newspage(id):
    return render_template('frett.tpl', frett=frettir[id], nr=id)

@app.route('/about')
def About():
    return render_template('about.tpl')

@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.tpl'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp

if __name__ == '__main__':
    app.run()
    #app.run(debug=True, use_reloader=True)
