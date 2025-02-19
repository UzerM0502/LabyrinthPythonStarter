def load_labyrinth(filename):
    
    with open(filename, "r") as f:
        lines = f.readlines()

    labyrinth = [list(line.strip()) for line in lines]
    return labyrinth

def dijkstra(labyrinth):
    path = []
    cost = 0
    return path, cost

labyrinth = load_labyrinth("labyrinth_5x5.txt")
print("Labyrinth loaded:")
print(labyrinth)
path, cost = dijkstra(labyrinth)
print(f"Shortest path has a cost of: {cost}")