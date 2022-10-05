visit = []
trajectory = []

globCity = ''

def visitas(objcostos, strCurrentCity, temp2, start, end): #strDestiny
    global visit, trajectory, globCity

    print("IMPRIMIENDO VISIT\n", visit)
    print("IMPRIMIENDO TRAJECTORY\n", trajectory)
    print("IMPRIMIENDO GLOBCITY\n", globCity)
    visit.append(strCurrentCity) #La ciudad actual se añade a la lista de visitados.
    for i in objcostos.nodes: # El ciclo sirve para recorrer la lista de los nodos que son adyacentes.
        #print("ENTRAMOS AL PRIMER FOR\n")
        if(i.ciudad == strCurrentCity): # Si la ciudad de la lista es la misma a la que se le está pasando en la función entra al otro ciclo for
            #print("ENTRAMOS AL PRIMER IF\n")
            for j in i.adjacent_Nodes: # Se busca el costo de los nodos vecinos a la ciudad actual por ejemplo SIBIU = FAG,RIMNI,ARAD, 0RAD
                #print("ENTRAMOS AL SEGUNDO FOR\n")
                if(str( list(j.keys())[0] ) in visit):  #Si los vecinos del nuevo nodo ya están en visitados no se vuelven a agregar.
                    #print("ENTRAMOS AL SEGUNDO IF\n")   
                    continue                
                else: #Caso contrario los vecinos que no se han marcado como visitados se tienen que agregar en el diccionario.
                    #print("ENTRAMOS AL ELSE\n")
                    tmp_city = str( list(j.keys())[0] ) # Se guarda temporalmente la ciudad vecina.
                    tmp_city += '/'  + globCity #Se actualiza la trayectoria.
                    tmp_distance = (int( list(j.values())[0])) + temp2
                    print('\ntmp_distance: ', tmp_distance)
                    print('\ntemp', temp2)
                    tmp_total = tmp_distance
                    tmp_total += objcostos.straight_Cost.get(str(list(j.keys())[0]))
                    trajectory.append({tmp_total:tmp_city})

    '''
    Comentar para mostrar solo la trayectoria:
    '''

    print("Ciudades visitadas \n", visit)
    print('\nNodos y distancias: ', trajectory)

    for i in visit: #Se verifica si ya se llegó al destino.
        indice = 0
        if(end in visit[indice]):
            print('Trayectoria: ', end)
            print('El costo total es: 0')
            return
        indice += 1

    for j in trajectory:
        if(end in str( list(j.values())[0])):
            print('Trayectoria: ', list(j.values())[0] + start)
            print('El costo total es: ', list(j.keys())[0])
            return
    
    globCity, min_distance = minimum() #Se regresa el valor más pequeño de la lista junto con su ciudad.
    print('\nFUNCION RETURN 1: ', min_distance)
    #print('\nFUNCION RETURN 2: ', globCity)
    trajectory.remove({min_distance:globCity}) #Se borra la ciudad y su costo de la lista por que ya no pertece a la lista de nodos y distancias.
    min_city = globCity.split('/')[0] #Se obtiene únicamente la ciudad de menor distancia, no toda la trayectoria.
    #print('\nFUNCION RETURN 2: ', min_city)
    #print('\nNodos y distancias: ', trajectory)
    print('\nTMP_DISTANCE ANTES DE LA RECURS.: ', tmp_distance)
    min_distance -= objcostos.straight_Cost.get(min_city)

    visitas(objcostos, min_city, min_distance, start, end) #Se llama recursivo.


def minimum():
    global trajectory

    strTmp = []
    intTmp = []
    for i in trajectory:
        intTmp.append(int( list(i.keys())[0] ))
        strTmp.append(str( list(i.values())[0] ))

    #print('\nMINIMO INT: ', intTmp)
    #print('\nMINIMO STR: ', strTmp)

    for j in trajectory:
        if(j.get(min(intTmp)) != None):
            #print('\nRETURN: ', j.get(min(intTmp)))
            return j.get(min(intTmp)), min(intTmp)
