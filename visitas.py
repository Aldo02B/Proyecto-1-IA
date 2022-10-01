
visit = []
trayectory = []

globCity = ''

def visitas(objcostos, strCurrentCity, strDestiny, minDistance, strStart):
    global visit, trayectory, globCity

    visit.append(strCurrentCity) #Se añade la ciudad a visitados.
    for i in objcostos.nodes:
        if(i.ciudad == strCurrentCity):
            for j in i.adjacent_Nodes:
                if(str( list(j.keys())[0] ) in visit):  #Si los vecinos del nuevo nodo ya están en visitados
                    continue                            #no se vuelven a agregar.

                else: #Se añaden los vecinos a la trayectoria.
                    tmp_city = str( list(j.keys())[0] )
                    tmp_city += '/'  + globCity #Se actualiza la trayectoria.
                    tmp_distance = int( list(j.values())[0] )
                    tmp_distance += minDistance #Se actualizan las distancias
                    trayectory.append({tmp_distance:tmp_city})

    '''
    Comentar para mostrar solo la trayectoria:
    '''

    print('Ciudades visitadas: ', visit)
    print('Nodos y distancias: ', trayectory)
    print()




    for i in trayectory: #Se verifica si ya se llegó al destino.
        if(strDestiny in str( list(i.values())[0] )):
            print('La Taryectoría es: ', list(i.values())[0] + strStart)
            print('El costo total es de: ', list(i.keys())[0])

            return


    globCity, min_distance = minimum() #Se obtiene el menor en la lista.
    trayectory.remove({min_distance:globCity}) #Se actualiza la lista.
    min_city = globCity.split('/')[0] #Se obtiene únicamente la ciudad de menor distancia, no toda la trayectoria.

    visitas(objcostos, min_city, strDestiny, min_distance, strStart) #Se llama recursivo.


def minimum():
    global trayectory

    strTmp = []
    intTmp = []
    for i in trayectory:
        intTmp.append(int( list(i.keys())[0] ))
        strTmp.append(str( list(i.values())[0] ))

    for j in trayectory:
        if(j.get(min(intTmp)) != None):
            return j.get(min(intTmp)), min(intTmp)
