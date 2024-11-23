import random

def identify_anomalous_users(graph, anomaly_fraction=0.1):
    anomalous_users = []
    for node in graph.nodes():
        if random.random() < anomaly_fraction:
            anomalous_users.append(node)
    return anomalous_users
