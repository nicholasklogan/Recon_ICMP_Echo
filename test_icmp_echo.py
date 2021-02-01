import icmp_echo


def test_icmp_success_on_windows():
    """
    Given an ip is provided,
    When main is called for icmp_echo,
    Then the system returns the ip, bytes, time, and TTL of the ping call.
    """
    # Test / Verify
    assert icmp_echo.main('8.8.8.8') == (
        {
            'ip': '8.8.8.8',
            'bytes': 32,
            'time': '33ms',
            'TTL': 115
        }
    )

def test_different_ip_address_icmp_success_on_windows_with_different_ip():
    """
    Given a different ip address is provided,
    When main is called for icmp_echo,
    Then the system returns the different ip, bytes, time, and TTL of the ping call.
    """
    # Test / Verify
    assert icmp_echo.main(lambda: "Reply from 4.4.4.4: bytes=32 time=33ms TTL=115")('4.4.4.4') == (
        {
            'ip': '4.4.4.4',
            'bytes': 32,
            'time': '33ms',
            'TTL': 115
        }
    )

def test_slower_response_icmp_success_on_windows_with_slow_response_recorded():
    """
    Given a slower response from ping command,
    When main is called for icmp_echo,
    Then the system returns the ip, bytes,  and the slower response time, and TTL of the ping call.
    """
    # Test / Verify
    assert icmp_echo.main(lambda: "Reply from 8.8.8.8: bytes=32 time=330ms TTL=115")('8.8.8.8') == (
        {
            'ip': '8.8.8.8',
            'bytes': 32,
            'time': '330ms',
            'TTL': 115
        }
    )