import os
import time

def check_network_connectivity():
    while True:
        response = os.system("ping -c 1 www.google.com")
        if response == 0:
            print("Network is up and running!")
        else:
            print("Network is down!")
        time.sleep(5)

if __name__ == "__main__":
    check_network_connectivity()
