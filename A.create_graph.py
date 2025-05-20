import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes
nodes = [0, 1, 2, 3]
G.add_nodes_from(nodes)

# Add edges based on the relation R
edges = [(1, 2), (2, 1), (1, 3), (3, 1)]
G.add_edges_from(edges)

# Define the layout for the graph
pos = nx.spring_layout(G, seed=42)  # For consistent layout

# Draw the graph
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=12, font_weight='bold', arrowsize=20)
plt.title('Directed Graph of Relation R')

# Save the graph to a file
plt.savefig('relation_graph.png')