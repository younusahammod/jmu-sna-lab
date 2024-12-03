import networkx as nx
import matplotlib.pyplot as plt

# Create a sample graph
G = nx.Graph()
G.add_weighted_edges_from([(0, 1, 1), (1, 2, 2), (2, 3, 1), (3, 4, 3)])

# Calculate shortest paths
shortest_paths = nx.shortest_path_length(G, source=0, weight='weight')

# Print shortest paths
print('Shortest paths from node 0:')
for node, distance in shortest_paths.items():
    print(f'Node {node}: Distance = {distance}')

# Visualize the graph
nx.draw(G, with_labels=True, node_color='lightblue', font_weight='bold')
plt.title('Graph Visualization')
plt.show()
