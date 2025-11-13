import io, sys
from tasks.task4 import solve

def run_io_fun(input_data):
    sys.stdin = io.StringIO(input_data)
    sys.stdout = io.StringIO()
    solve()
    return sys.stdout.getvalue().strip()

def test_samples():
    assert run_io_fun("Макгрегор\n") == "___Макгрегор___"
    assert run_io_fun("Конор\n") == "_____Конор_____"
