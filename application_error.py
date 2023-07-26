import random

def process_data(data):
    if random.choice([True, False]):
        raise Exception("Error: Processing data failed.")
    else:
        print("Data processed successfully.")


if __name__ == "__main__":
    data = "Sample data"
    try:
        process_data(data)
    except Exception as e:
        print(e)
