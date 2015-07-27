'''
Created on Jul 26, 2015

@author: avinav
'''
import igraph as ig

graph = ig.Graph()
graph.add_vertices(2)
# graph.add_edges([(0,1),(1,2)])
graph.vs["name"] = ["avinav","sharan"]
graph.vs["idf"] = [2,3]
# graph.es["weight"] = [2,3]
# print graph
# print graph.vs[0].index,graph.es[0].source,graph.es[1].target

kwds = {'idf':2, 'count' : 4}
g = ig.Graph(directed=False)
# g.add_vertex(name='hello',count = 4, idf =6)
# g.add_vertex(name = 'world',count = 3, idf=9)
# g.add_vertex(name = 'avinav',count = 3, idf=9)
# g.add_vertex(name = 'sharan',count = 3, idf=9)
g.add_vertices(4)
# print g.vs.select('name'=='world')[0].index, g.vs.select('name'=='hello')[0].index
# print graph.vs.attributes(), g.vs.attributes()
# print g.vs.select([0,1])["name"]
# print  g.vs.select(name_eq='hello')["name"]
# vs = g.vs.select(lambda vertex: vertex["name"] in ('hello','world'))
# g.add_edge(vs[0],vs[1])
g.add_edges([(0,1),(1,2),(2,3)])
print g
print g.es.select(_between=([2],[1]))[0].index
print len(g.es.select(_from=1, _to=0))