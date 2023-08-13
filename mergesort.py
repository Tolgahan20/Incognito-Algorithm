from copy import deepcopy
class MergeSort:
    def __init__(self) -> None:
        pass
    def sort(self, vertexes):
        if len(vertexes) <= 1:
            return vertexes
        temp_vertexes = deepcopy(vertexes)
        self.mergesort(temp_vertexes, 0, len(temp_vertexes) - 1)
        return temp_vertexes

    def mergesort(self, vertexes, low, high):
        if low < high:
            middle = (low + high) // 2
            self.mergesort(vertexes, low, middle)
            self.mergesort(vertexes, middle + 1, high)
            self.merge(vertexes, low, middle, high)

    def merge(self, vertexes, low, middle, high):
        temp_vertexes = deepcopy(vertexes)
        i = low
        j = middle + 1
        k = low
        while i <= middle and j <= high:
            if temp_vertexes[i].get_vertex_height() <= temp_vertexes[j].get_vertex_height():
                vertexes[k] = temp_vertexes[i]
                i += 1
            else:
                vertexes[k] = temp_vertexes[j]
                j += 1
            k += 1
        while i <= middle:
            vertexes[k] = temp_vertexes[i]
            i += 1
            k += 1
