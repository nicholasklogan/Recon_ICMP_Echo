import pytest

import icmp_echo


@pytest.mark.parametrize(
    'expected_response',
    [
        pytest.param(
            {
                'ip': '8.8.8.8',
                'bytes': 32,
                'time': '33ms',
                'TTL': 115
            },
            id='Given an ip is provided,'
               ' When main is called for icmp_echo,'
               ' Then the system returns the ip, bytes, time, and TTL of the ping call.'
        ),
        pytest.param(
            {
                'ip': '4.4.4.4',
                'bytes': 32,
                'time': '33ms',
                'TTL': 115
            },
            id='Given a different ip is provided,'
               ' When main is called for icmp_echo,'
               ' Then the system returns the different ip, bytes, time, and TTL of the ping call.'
        ),
        pytest.param(
            {
                'ip': '8.8.8.8',
                'bytes': 32,
                'time': '330ms',
                'TTL': 115
            },
            id='Given a slower response from ping command, '
               'When main is called for icmp_echo,'
               ' Then the system returns the ip, bytes,  and the slower response time, and TTL of the ping call.'
        )
    ],
)
def test_icmp_on_windows(expected_response):
    # Setup
    def ping(ip):
        return f'''
Pinging {expected_response['ip']} with 32 bytes of data:
Reply from {expected_response['ip']}: bytes=32 time={expected_response['time']} TTL=115

Ping statistics for {expected_response['ip']}:
    Packets: Sent = 1, Received = 1, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 330ms, Maximum = 330ms, Average = 330ms'''
    # Test / Verify
    assert icmp_echo.main(ping_command=ping)(ip_address=expected_response['ip']) == expected_response


@pytest.mark.parametrize(
    'ip_address,expected_response',
    [
        pytest.param(
            '8.8.8.8',
            {},
            id='Given an ip address with no server responding to ping command, When main is called for icmp_echo, Then the system returns an empty dictionary.'
        ),
    ],
)
def test_failing_icmp_on_windows(ip_address, expected_response):
    # Setup
    def ping(ip):
        return f'''Pinging {ip} with 32 bytes of data:
Request timed out.

Ping statistics for {ip}:
    Packets: Sent = 1, Received = 0, Lost = 1 (100% loss),'''
    # Test / Verify
    assert icmp_echo.main(ping_command=ping)(ip_address=ip_address) == expected_response
