from edge import Edge
class Vertex:
    def __init__(self, data2):
        self.data = data2
        self.incident_edges = []
        self.marked = False
    
    def add_incident_edge(self, edge):
        if edge not in self.incident_edges:
            self.incident_edges.append(edge)
    
    def get_data(self):
        return self.data
    
    def get_incident_edges(self):
        return self.incident_edges
    
    def is_marked(self):
        return self.marked
    
    def set_mark(self, val):
        self.marked = val
    
    def is_root(self):
        return len(self.incident_edges) == 0
    
    def __eq__(self, other):
        if isinstance(other, Vertex):
            return self.data == other.data
        # and self.incident_edges == other.incident_edges
        return False
    
    def copy(self):
        vertex = Vertex(self.data)
        for edge in self.incident_edges:
            vertex.incident_edges.append(Edge(vertex, edge.get_to()))
        return vertex
    
    def get_adjacent_vertex(self, edge):
        return edge.get_adjacent_vertex(self)
    
    def get_vertex_height(self):
        arr = self.data.split(":")
        height = 0
        for item in arr:
            height += int(item.split(" ")[1])
        return height
    
    def get_direct_generalizations(self, generalizations):
        for edge in self.incident_edges:
            v = edge.get_to()
            if (v in generalizations):
                continue
            generalizations.append(v)
        return generalizations
    
    def __str__(self):
        return self.get_data().strip()
