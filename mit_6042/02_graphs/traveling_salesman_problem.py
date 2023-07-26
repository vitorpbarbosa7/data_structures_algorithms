import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Define the vertices
vertices = ['v0', 'v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9', 'v10', 'v11']

# Add the vertices to the graph
G.add_nodes_from(vertices)

# Define the edges and their weights
edges = [
    ('v0', 'v1', 2),
    ('v1', 'v2', 1),
    ('v2', 'v3', 1),
    ('v3', 'v4', 2),
    ('v3', 'v5', 1),
    ('v5', 'v6', 1),
    ('v6', 'v7', 2),
    ('v6', 'v8', 1),
    ('v8', 'v9', 1),
    ('v9', 'v10', 2),
    ('v9', 'v11', 1),
    ('v11', 'v1', 1)
]

# Add the edges to the graph with their respective weights
G.add_weighted_edges_from(edges)

# Draw the graph
pos = nx.spring_layout(G)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Display the graph
plt.axis('off')
plt.show()
