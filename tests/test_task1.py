import io, sys
from tasks.task1 import solve

def run_io_fun(input_data):
    sys.stdin = io.StringIO(input_data)
    sys.stdout = io.StringIO()
    solve()
    return sys.stdout.getvalue().strip()

def test_samples():
    assert run_io_fun("what's up?\n") == "hat's up?"
    assert run_io_fun("i love zoo\n") == "i love oo"
