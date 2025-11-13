import io, sys
from tasks.task7 import solve

def run_io_fun(input_data):
    sys.stdin = io.StringIO(input_data)
    sys.stdout = io.StringIO()
    solve()
    return sys.stdout.getvalue().strip()

def test_samples():
    assert run_io_fun("-----Hello----\n") == "-----Hello"
    assert run_io_fun("!!!World?????????\n") == "!!!World"
    assert run_io_fun("___________Зачет!!!!!!!!\n") == "___________Зачет"
