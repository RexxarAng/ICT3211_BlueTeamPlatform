import json
import os
import dotenv
from pyvis.network import Network
import networkx as nx
import requests
from requests.auth import HTTPDigestAuth


def retrieve_arkime_var():
    dotenv_file = dotenv.find_dotenv(".arkime")
    dotenv.load_dotenv(dotenv_file, override=True)  # Take environment variables from .arkime

    return {
        "arkime_user": os.environ["ARKIME_USER"],
        "arkime_password": os.environ["ARKIME_PASSWORD"]}


# URL of the API endpoint
url = "http://127.0.0.1:8005/api/connections"

arkime_cred = retrieve_arkime_var()

# Send a GET request to the API endpoint
response = requests.get(url,
                        auth=HTTPDigestAuth(arkime_cred["arkime_user"], arkime_cred["arkime_password"]),
                        verify=False)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract the JSON data from the response
    data = response.json()

    # Save the JSON data to a file
    with open("connections.json", "w") as file:
        json.dump(data, file)

    print("JSON file downloaded successfully.")
else:
    print("Failed to download JSON file.")

# Read the graph data from the JSON file
with open("connections.json", "r") as file:
    graph_data = json.load(file)

nodes = graph_data["nodes"]
links = graph_data["links"]

# Create a NetworkX graph
G = nx.Graph()

# Create a Network object from the NetworkX graph
net = Network(height="1000px", width="100%", select_menu=True, filter_menu=True)
net.from_nx(G)
net.show_buttons(filter_=['nodes', 'edges'])

# Add nodes with their respective attributes
for node in nodes:
    node_id = node["id"]
    node_attributes = node.copy()
    node_attributes.pop("id")
    net.add_node(node_id, label=node_id, **node_attributes)

# Add edges based on source and target IDs, filtered by node type
for link in links:
    source_id = nodes[link["source"]]["id"]
    target_id = nodes[link["target"]]["id"]
    link_attributes = link.copy()
    link_attributes.pop("source")
    link_attributes.pop("target")
    if source_id in net.get_nodes() and target_id in net.get_nodes():
        net.add_edge(source_id, target_id, **link_attributes)

# Generate the HTML code manually
nodes_json = json.dumps(nodes)
links_json = json.dumps(links)

net.write_html("network_graph_dynamic_data.html")
