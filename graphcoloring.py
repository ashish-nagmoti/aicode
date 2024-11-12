# O(m^n) m->color abd n->vertices and o(n)
def is_safe(graph, color, vertex, c):
    for i in range(len(graph)):
        if graph[vertex][i] == 1 and color[i] == c:
            return False
    return True

def graph_coloring(graph, m, color, vertex, color_names):
    if vertex == len(graph):
        print("Solution:", [color_names[c-1] for c in color])
        return True

    for c in range(1, m + 1):
        if is_safe(graph, color, vertex, c):
            color[vertex] = c
            if graph_coloring(graph, m, color, vertex + 1, color_names):
                return True
            color[vertex] = 0

    return False


graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]
m = 3  
color = [0] * len(graph)
color_names = ["Red", "Green", "Blue"]  

if not graph_coloring(graph, m, color, 0, color_names):
    print("No solution exists")