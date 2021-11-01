import json
import random

import falcon
from falcon import API

from Tienda_de_Mascotas.Infraestructura.PersistenciaPerro import \
    PersistenciaPerro


class HolaMundo():

    def on_get(self, req, resp, uuid):
        db=PersistenciaPerro()
        gui=db.load_json(uuid+'.json')
        mensajes = ['Hola Mindo','Hola Que hace', 'Adio', 'Ciao','2+2=4']
        resp.body = json.dumps(gui)
        resp.status =falcon.HTTP_OK


def iniciar() ->  API:
    api = API()
    api.add_route("/perro/{uuid}",HolaMundo())

    return api

app=iniciar()


