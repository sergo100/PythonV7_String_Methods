# tasks/task8.py

def solve():
# Ниже пишите решение задачи
    
     s1=hex(int(input())).upper()
     s2=hex(int(input())).upper()
     s3=hex(int(input())).upper()
     print((s1.lstrip('0X').zfill(2)+s2.lstrip('0X').zfill(2)+s3.lstrip('0X').zfill(2)).rjust(7,'#'))
     
   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()