from nodo import *
from costos import *
import visitas


def main():

    cities = [
    'Oradea', 'Zerind', 'Arad', 'Sibiu', 'Timisoara', 'Lugoj', 'Mehadia',
    'Dobreta', 'Craiova', 'Rimnicu Vilcea', 'Fagaras', 'Pitesti',
    'Bucharest', 'Giurgiu', 'Urziceni','Hirsova', 'Eforie', 'Vaslui',
    'Iasi', 'Neamt']

    print("\n ======= Ciudades Disponibles ======\n\n")
    print(cities)

    flag = False
    while(flag == False):
        print()
        start = input('Ingresa el punto de partida: ')
        end = "Bucharest"
        if(start in cities):
            flag = True
    print("\n")

    numNodes = len(cities)
    numEdges = 23
    directed = False
    cost = True
    straight_Cost = {'Arad':366, 'Bucharest':0, 'Craiova':160, 'Dobreta':242,
        'Eforie':161, 'Fagaras':178, 'Giurgiu':77, 'Hirsova':151, 'Iasi':226,
        'Lugoj':244, 'Mehadia':241, 'Neamt':234, 'Oradea':380, 'Pitesti':98,
        'Rimnicu Vilcea':193, 'Sibiu':253, 'Timisoara':329, 'Urziceni':80, 'Vaslui':199,
        'Zerind':374}

    Camino = costos(numNodes, numEdges, directed, cost, straight_Cost)
    Camino.start_costos(sorted(cities))

    visitas.visitas(Camino, start, 0, start ,end)


if __name__ == '__main__':
    main()
