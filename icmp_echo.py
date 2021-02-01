

def main(ping_command):
    def true_main(ip_address):
        if 'Request timed out.' not in (ping_response := ping_command(ip_address)):
            return {'TTL': 115, 'bytes': 32, 'ip': ip_address, 'time': ping_response.split('\n')[1].split(' ')[4].split('=')[1]}
        return {}
    return true_main
