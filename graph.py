from edge import Edge
class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []
    
    def get_vertices(self):
        return self.vertices
    
    def copy(self):
        graph = Graph()
        graph.vertices = self.vertices.copy()
        graph.edges = self.edges.copy()
        return graph
    
    def add_edge(self, x, y):
        edge = Edge(x, y)
        self.edges.append(edge)
        x.add_incident_edge(edge)
    
    def add_edge_obj(self, edge):
        if edge not in self.edges:
            self.edges.append(edge)
    
    def add_vertex(self, v):
        if v not in self.vertices:
            self.vertices.append(v)
    
    def get_vertex(self, index):
        return self.vertices[index]
    
    def print_out(self):
        for v in self.vertices:
            for e in v.get_incident_edges():
                adjacent_vertex = e.get_adjacent_vertex(v)
                print(v.get_data() + " -> " + adjacent_vertex.get_data())
            print()
    
    def has_vertex(self, v):
        for vertex in self.vertices:
            if vertex == v:
                return vertex
        return v
    
    def get_roots(self):
        roots = []
        for v in self.vertices:
            is_root = True
            for e in self.edges:
                if e.get_to() == v:
                    is_root = False
                    break
            if is_root:
                roots.append(v)
        return roots
