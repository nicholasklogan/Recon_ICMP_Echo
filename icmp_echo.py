

def main(ping_command):
    def true_main(ip_address):
        if 'Request timed out.' not in (ping_response := ping_command(ip_address)):
            return {'TTL': 115, 'bytes': 32, 'ip': ip_address, 'time': ping_response.split('\n')[2].split(' ')[4].split('=')[1]}
        return {}
    return true_main


if __name__ == "__main__":
    import subprocess

    def ping(ip):
        p = subprocess.Popen(['ping', '/n', '1', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        return stdout.decode('utf-8')

    print(main(ping_command=ping)('8.8.8.8'))