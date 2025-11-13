# tasks/task2.py

def solve():
# Ниже пишите решение задачи
    s=input().lower()
    s=s.replace('a','').replace('o','').replace('y','').replace('e','').replace('u','').replace('i','')
    s=s.replace('','.')
    print(s[:-1])

    
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()