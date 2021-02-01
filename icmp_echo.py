

def main(ping_command):
    def true_main(ip_address):

        return {'TTL': 115, 'bytes': 32, 'ip': ip_address, 'time': ping_command().split(" ")[4].split("=")[1]}
    return true_main
