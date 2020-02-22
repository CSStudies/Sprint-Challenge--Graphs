from util import Stack, Queue

class Search:
    """
    
    """
    def __init__(self):
        # stack for unassigned to component
        # stack for is_diff_component? verts
        # counter for verticies 
        self.unassigned = Stack()
        self.is_diff = Stack()
        self.counter = 0

    def dfs_recursive(self, starting_vertex,  target_value, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        count = 0 

        if visited is None:
            visited = set()
        if path is None:
            path = []
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        if starting_vertex == target_value:
            return path
        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                new_path = self.dfs_recursive(child_vert, target_value, visited, path)
                if new_path:
                    return new_path
        return None

        def SCC(self, starting_vertex):
            
            count = 0
            visited= set()
            unassiged = Stack()
            unknown = Stack()

            preorders= {}
            preorders[starting_vertex] = count

            unassiged.push(starting_vertex)
            unknown.push(starting_vertex)

            for edge in neighbors:
                if edge not in preorders:
                    dft(edge)
                else if


