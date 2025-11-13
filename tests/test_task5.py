import io, sys
from tasks.task5 import solve

def run_io_fun(input_data):
    sys.stdin = io.StringIO(input_data)
    sys.stdout = io.StringIO()
    solve()
    return sys.stdout.getvalue().strip()

def test_samples():
    assert run_io_fun("99\n") == "0000000099"
    assert run_io_fun("6873621\n") == "0006873621"
