import icmp_echo


def test_icmp_success_on_windows():
    # Test / Verify
    assert icmp_echo.main() == (
        {
            'ip': '8.8.8.8',
            'bytes': 32,
            'time': '33ms',
            'TTL': 115
        }
    )
