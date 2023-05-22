from pyvis.network import Network
import networkx as nx

g = nx.Graph()

g.add_node(1, label="Node 1")
g.add_node(2, label="Node 2")
g.add_node(3, label="Node 3")
g.add_node(4, label="Node 4")
g.add_node(5, label="Node 5")

g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(1,4)
g.add_edge(1,5)
g.remove_node(4)

# Set the options for the button filter
net = Network(height='400px', width='50%',select_menu=True, filter_menu=True)

net.from_nx(g)

net.show_buttons(filter_=['nodes', 'edges'])

net.show("network_graph.html")