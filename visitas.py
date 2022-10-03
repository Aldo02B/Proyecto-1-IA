
visit = []
trajectory = []

globCity = ''

def visitas(objcostos, strCurrentCity, minDistance, strStart): #strDestiny
    global visit, trajectory, globCity

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
                    #tmp_distance += objcostos.straight_Cost.get(str(list(j.keys())[0]))
                    trajectory.append({tmp_distance:tmp_city})

    '''
    Comentar para mostrar solo la trayectoria:
    '''

    print("\nCiudades visitadas {} \n".format(visit))
    print('Nodos y distancias: ', trajectory)

    for i in trajectory: #Se verifica si ya se llegó al destino.
        if("Bucharest" in str( list(i.values())[0] )):
            print('Trayectoria: ', list(i.values())[0] + strStart)
            print('El costo total es: ', list(i.keys())[0])
            break

    globCity, min_distance = minimum() #Se obtiene el menor en la lista.
    trajectory.remove({min_distance:globCity}) #Se actualiza la lista.
    min_city = globCity.split('/')[0] #Se obtiene únicamente la ciudad de menor distancia, no toda la trayectoria.

    visitas(objcostos, min_city, min_distance, strStart) #Se llama recursivo.


def minimum():
    global trajectory

    strTmp = []
    intTmp = []
    for i in trajectory:
        intTmp.append(int( list(i.keys())[0] ))
        strTmp.append(str( list(i.values())[0] ))

    for j in trajectory:
        if(j.get(min(intTmp)) != None):
            return j.get(min(intTmp)), min(intTmp)
