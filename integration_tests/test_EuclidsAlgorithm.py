def test_gcd_calculation(run_app):
    result = run_app("EuclidsAlgorithm", args=["48", "18"])

    assert result.returncode == 0
    assert "The greated common divisor of 48 and 18 is 6" in result.stdout

def test_missing_args(run_app):
    result = run_app("EuclidsAlgorithm", args=["20"])

    assert result.returncode == 1