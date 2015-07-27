import igraph as ig

# igraph with vertex attributes as: (term_text, docfreq), edge attributes as: (weights)
class TweetGraph:
    def __init__(self, **kwargs):
        self.graph = ig.Graph(directed=True)
        if len(kwargs) == 2 and 'doc' in kwargs:
            doc = kwargs.get('doc')
            termMap = kwargs.get('termMap')
            self.id = doc.id
            self.create_graph(doc.term_list,termMap)
        elif len(kwargs) == 3 and 'term_list' in kwargs:
            term_list = kwargs.get('term_list')
            termMap = kwargs.get('termMap')
            self.id = kwargs.get('id')
            self.create_graph(term_list, termMap)
        else :
            raise Exception("Illegal number of arguments! can be 1 (id) or 2(doc,termMap)")
    
    def select_on_termList(self, term_list):
        term_set = set(term_list)
        return self.graph.vs.select(lambda vertex:vertex["name"] in term_set)
    
    def select_on_termTupList(self,termTupList):
        vseqList = [self.select_on_termList(termTup) for termTup in termTupList]
        vertexTupList = [(vseq[0],vseq[1]) for vseq in vseqList if len(vseq) == 2] 
        return vertexTupList
    
    # index.Term    
    def add_term_vertex(self, termObj):
        self.graph.add_vertex(name = termObj.term_text, df = termObj.docfreq)
    
    # [index.Term]
    def add_term_vertices(self, termObjList):
        m = self.graph.vcount()
        self.graph.add_vertices(len(termObjList))
        self.graph.vs[m:]["name"] = [termObj.term_text for termObj in termObjList]
        self.graph.vs[m:]["df"] = [termObj.docfreq for termObj in termObjList]
        
    def add_term_edge(self, term1, term2):
        vertices = self.select_on_termList([term1, term2])
        self.graph.add_edge(vertices[0],vertices[1])
    
    def add_term_edges(self, termTupList):
        vertexTupList = self.select_on_termTupList(termTupList)
        self.graph.add_edges(vertexTupList)
    
    def add_term_vertices_and_edges(self,termList,termMap):
        self.graph.add_vertices(len(termList))
        self.graph.vs["name"] = termList
        self.graph.vs["df"] = [termMap[term].docfreq if (term in termMap and termMap[term]) else None for term in termList]
        vertexTupList = [(i,i+1) for i in range(len(termList)-1)]
        self.graph.add_edges(vertexTupList)
    
    def create_graph(self, term_list, termMap):
        self.add_term_vertices_and_edges(term_list, termMap)
#         termObjList = [termMap[term] for term in term_list]
#         self.add_term_vertices(termObjList)
#         termTupList = [(term_list[i],term_list[i+1]) for i in range(len(term_list)-1)]
#         self.add_term_edges(termTupList)

    
            
        
    
        