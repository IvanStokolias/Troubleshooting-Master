def get_server_status():
    # Simulating misconfigured  server settings
    server_status = "Server is running, but the database is not connected."  
    return server_status

if __name__ == "__main__":
    status = get_server_status()
    print(status)
