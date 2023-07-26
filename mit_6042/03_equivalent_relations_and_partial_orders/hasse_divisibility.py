import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph (DiGraph)
G = nx.DiGraph()

# Define the set of elements
elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Add nodes to the graph
G.add_nodes_from(elements)

# Add edges based on the divisibility relation
for i in elements:
    for j in elements:
        if i != j and j % i == 0:
            G.add_edge(i, j)

# Create the Hasse diagram
pos = {
    1: (0, 0),
    2: (-1, -1), 3: (1, -1),
    4: (-1.5, -2), 5: (-0.5, -2), 6: (0.5, -2), 7: (1.5, -2),
    8: (-1.5, -3), 9: (-0.5, -3), 10: (0.5, -3)
}

# Get the edges to be drawn (only the direct divisibility relations)
edges_to_draw = [(i, j) for (i, j) in G.edges() if j % i == 0]

nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightblue', font_weight='bold', font_size=10, arrowstyle='->', arrowsize=15, edgelist=edges_to_draw)

# Display the Hasse diagram
plt.axis('off')
plt.show()

