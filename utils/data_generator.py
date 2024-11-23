import json
import random

def generate_synthetic_data(num_users=1000, num_messages=10000):
    users = [f"user_{i}" for i in range(num_users)]
    data = []
    
    for _ in range(num_messages):
        sender = random.choice(users)
        receiver = random.choice(users)
        timestamp = random.randint(1609459200, 1640995200)  # Random timestamp within 2021
        message = f"Message from {sender} to {receiver}"
        data.append({"sender": sender, "receiver": receiver, "timestamp": timestamp, "message": message})
    
    return data

def save_data(data, filename='data/synthetic_data.json'):
    with open(filename, 'w') as f:
        json.dump(data, f)

if __name__ == '__main__':
    data = generate_synthetic_data()
    save_data(data)
