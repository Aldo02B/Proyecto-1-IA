"""

NOSOTROS REALIZAMOS DOS CÓDIGOS, YA QUE EL QUE CORRESPONDE LINUX VA CON EL MÉTODO GRÁFICO, CREANDO
UN GRAFO PARA EL MAPA.

EL DE WINDOWS SOLO SE MUESTRA EN PANTALLA LAS CIUDADES EN LAS QUE SE PUEDE VIAJAR

"""



from nodo import *
from costos import *
import visitas




def main():

    cities = [
    'Oradea', 'Zerind', 'Arad', 'Sibiu',
                'Timisoara', 'Lugoj', 'Mehadia', 'Dobreta',
                'Craiova', 'Rimnicu Vilcea', 'Fagaras', 'Pitesti',
                'Bucharest', 'Giurgiu', 'Urziceni','Hirsova',
                'Eforie', 'Vaslui', 'Iasi', 'Neamt']

    print()
    print(" ======= Ciudades Disponibles ======")
    print()
    print(cities)


    flag = False
    while(flag == False):
        print()
        start = input('Ingresa el punto de partida: ')
        end = input('Ingresa el destino: ')
        if((start in cities) and (end in cities)):
            flag = True
    print()

    numNodes = len(cities)
    numEdges = 23
    directed = False
    cost = True

    Camino = costos(numNodes, numEdges, directed, cost)
    Camino.start_costos(sorted(cities))
    #Rumania.printcostos()

    visitas.visitas(Camino, start, end, 0, start)




if __name__ == '__main__':
    main()
