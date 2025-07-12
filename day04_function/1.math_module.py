import math #print(help(math))để xem module này có cung cấp những gì

#sqrt :  square root : hàm căn bật 2 
print(math.sqrt(4)) # kq =2 


from math import * #import all module
print(sqrt(9)) # lúc này k cần dùng math nữa


#isqrt : integer square root : cân bậc 2 sô nguyên
print(isqrt(10)) # kq = 3. mấy thì chỉ lấy 3 th 

#pow : power : lũy thừa 
print(pow(2,10)) # tức 2 mũ 10
print(pow(10,1/3)) # căn 10 mũ 1/3

#ceil : ceiling(trần nhà) : làm tròn lên
print(ceil(2.1)) # kq =3


#floor : floor(sàn nhà) : làm tròn xuống
print(floor(2.9)) #kq=2

#factorial : giai thừa : 1*2*3....
print(factorial(4)) #kq=24

#gcd(a,b) : tính ước chung số lớn nhất : greotest common divisor 
print(gcd(100,450)) #kq=50

#comb (n,k): tổ hợp 
print(comb(45,5))