import io, sys
from tasks.task8 import solve

def run_io_fun(input_data):
    sys.stdin = io.StringIO(input_data)
    sys.stdout = io.StringIO()
    solve()
    return sys.stdout.getvalue().strip()

def test_samples():
    assert run_io_fun("1\n2\n3\n") == "#010203"
    assert run_io_fun("0\n255\n10\n") == "#00FF0A"
    assert run_io_fun("75\n0\n130\n") == "#4B0082"
    assert run_io_fun("143\n0\n255\n") == "#8F00FF"
