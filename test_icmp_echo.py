import icmp_echo


def test_icmp_success_on_windows():
    """
    Given nothing,
    When main is called for icmp_echo,
    Then the system returns the ip, bytes, time, and TTL of the ping call.
    """
    # Test / Verify
    assert icmp_echo.main() == (
        {
            'ip': '8.8.8.8',
            'bytes': 32,
            'time': '33ms',
            'TTL': 115
        }
    )
