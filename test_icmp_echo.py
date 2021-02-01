import pytest

import icmp_echo

@pytest.mark.parametrize(
    'ping_response,ip_address,expected_response',
    [
        pytest.param(
            'Reply from 8.8.8.8: bytes=32 time=33ms TTL=115',
            '8.8.8.8',
            {
                'ip': '8.8.8.8',
                'bytes': 32,
                'time': '33ms',
                'TTL': 115
            },
            id='Given an ip is provided, When main is called for icmp_echo, Then the system returns the ip, bytes, time, and TTL of the ping call.'
        ),
        pytest.param(
            'Reply from 4.4.4.4: bytes=32 time=33ms TTL=115',
            '4.4.4.4',
            {
                'ip': '4.4.4.4',
                'bytes': 32,
                'time': '33ms',
                'TTL': 115
            },
            id='Given a different ip is provided, When main is called for icmp_echo, Then the system returns the different ip, bytes, time, and TTL of the ping call.'
        ),
        pytest.param(
            'Reply from 8.8.8.8: bytes=32 time=330ms TTL=115',
            '8.8.8.8',
            {
                'ip': '8.8.8.8',
                'bytes': 32,
                'time': '330ms',
                'TTL': 115
            },
            id='Given a slower response from ping command, When main is called for icmp_echo, Then the system returns the ip, bytes,  and the slower response time, and TTL of the ping call.'
        ),
        pytest.param(
            'Request timed out.',
            '8.8.8.8',
            {},
            id='Given an ip address with no server responding to ping command, When main is called for icmp_echo, Then the system returns an empty dictionary.'
        ),
    ],
)
def test_icmp_on_windows(ping_response, ip_address, expected_response):
    # Test / Verify
    assert icmp_echo.main(lambda: ping_response)(ip_address) == expected_response
