import flask
import pymongo
import ocr
from flask import request
import ocrutlis
from datetime import datetime

now = datetime.now()
app = flask.Flask(__name__)
app.config["DEBUG"] = True
dictionnary = {}
try:
    client = pymongo.MongoClient("mongo connection string here")
    db = client.API_Tickets
    T = db.ticketsData
except:
    print("cannot connect")

@app.route('/do', methods=['GET', 'POST'])

def home():
    if request.method == 'POST':
        p = request.form.get('url')
        user_nom = request.form.get('user_nom')
        user_prenom = request.form.get('user_prenom')
        user_email = request.form.get('user_email')
        user_date_naissance = request.form.get('user_date_naissance')
        user_genre = request.form.get('user_genre')
        userobj =  {"nom":user_nom,
                    "prenom":user_prenom,
                    "email":user_email,"date_naissance":user_date_naissance,"genre":user_genre}

        resultTraitement = ocr.traitement(p)
        if hash(resultTraitement) in dictionnary.keys():
            return ({"Error122":"Ticket is already scanned"})
        else:
            dictionnary.update({hash(resultTraitement): resultTraitement.marketid})
        resultTraitement.tup = ocrutlis.autocorrect(resultTraitement.tup)
        result = dict(name=resultTraitement.name, total=resultTraitement.total, products=resultTraitement.tup, date=resultTraitement.date, time=resultTraitement.time)
        try:
            T.insert_one({"name": resultTraitement.name,
                          "total": resultTraitement.total,
                          "products": resultTraitement.tup,
                          "date": resultTraitement.date,
                          "time": resultTraitement.time,
                          "ticket_image_url": p,
                          "userobj": userobj,
                          "extractiondate": now.strftime("%m/%d/%Y, %H:%M:%S")})

            print("insert success")
        except:
            print("coudnt insert object to mongodb atlas")
        return result

        return({"E0011":"verify ticket image (assure enough lightening and clear shot)"})

    if __name__ == '__main__':
        app.run(host='0.0.0.0', debug=True)

app.run(host='0.0.0.0')
