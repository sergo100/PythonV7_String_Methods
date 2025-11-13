import io, sys
from tasks.task6 import solve

def run_io_fun(input_data):
    sys.stdin = io.StringIO(input_data)
    sys.stdout = io.StringIO()
    solve()
    return sys.stdout.getvalue().strip()

def test_samples():
    assert run_io_fun("ABRACADABRA\n") == "True"
    assert run_io_fun("This Good\n") == "False"
