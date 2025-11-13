import io, sys
from tasks.task2 import solve

def run_io_fun(input_data):
    sys.stdin = io.StringIO(input_data)
    sys.stdout = io.StringIO()
    solve()
    return sys.stdout.getvalue().strip()

def test_samples():
    assert run_io_fun("Codeforces\n") == ".c.d.f.r.c.s"
    assert run_io_fun("Ba\n") == ".b"
