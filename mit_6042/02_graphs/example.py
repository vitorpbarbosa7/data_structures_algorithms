import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
social_network = nx.Graph()

# Add nodes (users) to the graph
social_network.add_nodes_from(['Alice', 'Bob', 'Charlie', 'David', 'Eve'])

# Add edges (connections between users)
social_network.add_edges_from([('Alice', 'Bob'), ('Alice', 'Charlie'), ('Charlie', 'David'), ('Charlie', 'Eve')])

# Visualize the graph
pos = nx.spring_layout(social_network)
nx.draw_networkx(social_network, pos=pos, with_labels=True, node_color='lightblue', edge_color='gray')

# Display the plot
plt.title('Social Network')
plt.show()
