import random

def connect_to_database():
    if random.choice([True, False]):
        raise ConnectionError("Failed to connect to database.")
    else:
        print("Connected to database successfully.")

if __name__ == "__main__":
    try:
        connect_to_database()
    except ConnectionError as e:
        print(e)

