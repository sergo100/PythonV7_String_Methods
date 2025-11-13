# tasks/task3.py

def solve():
# Ниже пишите решение задачи
    s=input()
    prefix=input()
    postfix=input()
    print(s.startswith(prefix) and s.endswith(postfix))


# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()