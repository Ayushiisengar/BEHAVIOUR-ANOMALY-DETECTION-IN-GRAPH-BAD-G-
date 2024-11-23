# Behavioral Anomaly Detection in Graphs (BAD-G)

This project provides a web application that visualizes a graph and performs anomaly detection on its nodes. The graph represents a social network of users, and the anomalies in the network are highlighted through color-coded nodes.

## Features

- **Graph Visualization**: Visualizes the graph using Plotly, where nodes represent users and edges represent relationships between them.
- **Anomaly Detection**: Nodes are color-coded to highlight anomalies (10% of the nodes are randomly marked as anomalous for demonstration purposes).
- **User Details**: Clicking on a node shows user-specific data (name, email, role, etc.) using Flask routes.
- **Graph Sampling**: Allows sampling of the graph to reduce its size for faster rendering (5% of the nodes are displayed by default).

## Project Structure

project/ 
├── app.py
├── data/ 
│ ├── synthetic_data.json 
│ ├── processed_graph.json 
├── templates/ 
│ ├── index.html
│ ├── graph.html 
│ ├── user_details.html 
├── static/ 
│ ├── styles.css
└── utils/ 
├── data_generator.py 
├── graph_builder.py
├── anomaly_detector.py


## Setup Instructions

### Prerequisites
- Python 3.x
- Flask
- NetworkX
- Plotly
- JSON

### Step 1: Install Dependencies

Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate

## Install the required packages:

bash
Copy code
pip install flask networkx plotly
### Step 2: Prepare the Graph Data
Make sure that your graph data is available in data/processed_graph.json. If you don't have this file, you can generate the graph using the data_generator.py and graph_builder.py scripts.

### Step 3: Run the Flask Application
To start the Flask server, run the following command:

bash
Copy code
python app.py
This will start the application at http://127.0.0.1:5000/.

### Step 4: Interact with the Application
Homepage: The homepage (index.html) shows an introduction to the project.
Graph Visualization: Navigate to /graph to see the graph visualization, where nodes are color-coded to distinguish normal and anomalous nodes.
User Details: Click on a node to view detailed information about the user (name, email, role).
Customization
Node Color Scheme: The nodes are colored randomly for demonstration purposes (anomalous nodes are red and normal nodes are green). You can update the logic to implement actual anomaly detection.
Sampling: The graph is sampled to display a fraction (5% by default) of the nodes for faster rendering.






