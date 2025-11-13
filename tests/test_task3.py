import io, sys
from tasks.task3 import solve

def run_io_fun(input_data):
    sys.stdin = io.StringIO(input_data)
    sys.stdout = io.StringIO()
    solve()
    return sys.stdout.getvalue().strip()

def test_samples():
    assert run_io_fun("translate russian to english\ntranslate\nenglish\n") == "True"
    assert run_io_fun("translate russian to english\ntranslate\nSH\n") == "False"
    assert run_io_fun("TRanSlate russian to english\nTRa\nlish\n") == "True"
