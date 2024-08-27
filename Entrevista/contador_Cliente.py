def now ():
    return

S_IN_MS = 1000
clientes = {
    # id llave
    #{ contqdor, epoch}
}

class cliente :
    contador = 0
    epoch = now()
    TPS = 100

class throttle :
    def registrar(self, id, TPS):
        clientes[id] = {
            "contador" : 0,
            "epoch" : now(),
            "TPS" : TPS
        }
    def deregistrar(self, id):
        del clientes[id]

    def checar(self, id):
        if (id in clientes.keys()):
            if(clientes[id]["epoch"] + S_IN_MS >= now()):
                clientes[id]["epoch"] = now()
                clientes[id]["contador"] = 1
                return True
            else:
                clientes[id]["contador"] += 1
                if clientes[id]["contador"] < clientes[id]["TPS"]:
                    return True
        return False