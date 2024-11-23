from flask import Flask, render_template, jsonify
import networkx as nx
import plotly.graph_objects as go
import os
import random
from utils.graph_builder import load_graph_from_json

app = Flask(__name__)

# Function to load the graph
def load_graph():
    graph_path = "data/processed_graph.json"
    if os.path.exists(graph_path):
        try:
            G = load_graph_from_json(graph_path)
            print(f"Graph loaded with {len(G.nodes())} nodes and {len(G.edges())} edges.")
            return G
        except Exception as e:
            print(f"Error loading graph: {e}")
    else:
        print("Graph file does not exist.")
    return None

# Function to generate user data for each node
def generate_user_data(G):
    user_data = {}
    for node in G.nodes():
        # Simulating random user data
        user_data[node] = {
            "name": f"User {node}",
            "email": f"{node.lower()}@example.com",
            "role": random.choice(["Admin", "Moderator", "User"])
        }
    return user_data

# Sample the graph to reduce size
def sample_graph(G, sample_fraction=0.05):
    all_nodes = list(G.nodes())
    sample_size = max(1, int(len(all_nodes) * sample_fraction))  # Ensure at least 1 node
    sampled_nodes = random.sample(all_nodes, sample_size)
    return G.subgraph(sampled_nodes)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/graph')
def graph():
    G = load_graph()  # Load the graph from JSON or another source
    if not G:
        return jsonify({'error': 'Graph not found! Please generate or load the graph first.'})

    # Generate user data dynamically based on the graph
    user_data = generate_user_data(G)

    # Step 1: Sample the graph (reducing the size)
    G = sample_graph(G, sample_fraction=0.05)  # Use 5% of the graph

    # Step 2: Generate graph visualization with Plotly
    pos = nx.spring_layout(G)  # Layout for better readability (use spring layout)

    # Edge trace
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_y.append(y0)
        edge_y.append(y1)

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines'
    )

    # Node trace
    node_x = []
    node_y = []
    node_color = []  # Store node color
    node_text = []   # Store node hover text (used for click actions)

    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)

        # Assign random colors for normal/anomalous nodes as a placeholder
        if random.random() < 0.1:  # Simulate anomaly detection
            node_color.append('red')  # Anomalous nodes
        else:
            node_color.append('green')  # Normal nodes

        # Add the node name to hover text (user details)
        node_text.append(node)

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',  # Add hover info to show node details
        text=node_text,    # Text for each node (used for hover and click)
        marker=dict(
            color=node_color,
            size=10,
            opacity=0.8,
            showscale=False  # No color scale for simplicity
        )
    )

    # Create the figure with edge and node traces
    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        title='Social Graph Visualization',
                        titlefont_size=16,
                        showlegend=False,
                        hovermode='closest',
                        xaxis=dict(showgrid=False),
                        yaxis=dict(showgrid=False)
                    ))

    # Convert figure to HTML and pass it to the template
    graph_html = fig.to_html(full_html=False)
    return render_template('graph.html', graph_html=graph_html, user_data=user_data)



@app.route('/user_details/<node_name>')
def user_details(node_name):
    # Normalize the node name (e.g., make case-insensitive)
    normalized_name = node_name.strip().upper()  # Adjust as needed
    # Fetch the user data
    user_data = generate_user_data(load_graph())  # Generate user data dynamically based on graph
    if normalized_name in user_data:
        return jsonify(user_data[normalized_name])
    else:
        return jsonify({'error': f'User "{node_name}" not found'})


if __name__ == '__main__':
    app.run(debug=True)
