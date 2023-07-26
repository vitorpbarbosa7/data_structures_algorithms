import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])

# Add edges to form disjoint trees
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'C')])
G.add_edges_from([('D', 'E'), ('E', 'F'), ('F', 'G')])
G.add_edges_from([('H', 'H')])  # Isolated vertex

# Plot the forest
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_weight='bold')

# Display the graph
plt.axis('off')
plt.show()
