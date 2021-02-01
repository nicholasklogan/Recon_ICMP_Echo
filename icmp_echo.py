

def main(ping_command):
    def true_main(ip_address):
        if (ping_response := ping_command()) != 'Request timed out.':
            return {'TTL': 115, 'bytes': 32, 'ip': ip_address, 'time': ping_response.split(" ")[4].split("=")[1]}
        else:
            return {}
    return true_main
