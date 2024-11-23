import networkx as nx
import json
import random

def load_graph_from_json(filename='data/processed_graph.json'):
    with open(filename, 'r') as f:
        data = json.load(f)
    return nx.node_link_graph(data)

def generate_user_data(G):
    user_data = {}
    for node in G.nodes():
        user_data[node] = {
            "name": f"User {node}",
            "email": f"{node.lower()}@example.com",
            "role": random.choice(["Admin", "Moderator", "User"])
        }
    return user_data

def sample_graph(G, sample_fraction=0.05):
    all_nodes = list(G.nodes())
    sample_size = max(1, int(len(all_nodes) * sample_fraction))  # Ensure at least 1 node
    sampled_nodes = random.sample(all_nodes, sample_size)
    return G.subgraph(sampled_nodes)
