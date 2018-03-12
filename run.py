# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)
an = search.GPSProblem('A', 'N', search.romania)
no = search.GPSProblem('N', 'O', search.romania)

print "Trayecto A-B:"
print "Busqueda en anchura: ",search.breadth_first_graph_search(ab).path()
print "Busqueda en profundidad: ",search.depth_first_graph_search(ab).path()
print "Busqueda por Ramificacion y Acotacion: ",search.ram_acot_graph_search(ab).path()
print "Busqueda por Ramificacion y Acotacion con subestimacion: ",search.ram_acot_sub_graph_search(ab).path()

print "\nTrayecto A-N:"
print "Busqueda en anchura: ", search.breadth_first_graph_search(an).path()
print "Busqueda en profundidad: ",search.depth_first_graph_search(an).path()
print "Busqueda por Ramificacion y Acotacion: ",search.ram_acot_graph_search(an).path()
print "Busqueda por Ramificacion y Acotacion con subestimacion: ",search.ram_acot_sub_graph_search(an).path()

print "\nTrayecto N-O:"
print "Busqueda en anchura: ",search.breadth_first_graph_search(no).path()
print "Busqueda en profundidad: ",search.depth_first_graph_search(no).path()
print "Busqueda por Ramificacion y Acotacion: ",search.ram_acot_graph_search(no).path()
print "Busqueda por Ramificacion y Acotacion con subestimacion: ",search.ram_acot_sub_graph_search(no).path()

#print search.iterative_deepening_search(ab).path()
#print search.depth_limited_search(ab).path()

#print search.astar_search(ab).path()

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
