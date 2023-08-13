class Edge:
    def __init__(self, from_vertex, to_vertex):
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
    
    def get_adjacent_vertex(self, current):
        if self.to_vertex == current:
            return self.from_vertex
        if self.from_vertex == current:
            return self.to_vertex
        return None
    
    def __eq__(self, other):
        if not isinstance(other, Edge):
            return False
        return self.to_vertex == other.to_vertex and self.from_vertex == other.from_vertex
    
    def copy(self):
        return Edge(self.from_vertex.copy(), self.to_vertex.copy())
    
    def get_to(self):
        return self.to_vertex
    
    def get_from(self):
        return self.from_vertex
    
    def __str__(self):
        return str(self.from_vertex) + " -> " + str(self.to_vertex)
