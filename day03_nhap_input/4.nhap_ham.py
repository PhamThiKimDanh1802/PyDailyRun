"""
nhập dữ liệu với hàm input" NHẬP NHIỀU SỐ"

b1: nhập cả dong bằng hàm input 
b2:dùng split để tách các sô trong xâu input ra 
b3: sử dụng map  để ép các xâu được tách ra trong input sang số int/float tủy theo đề bài


EX:
'10 20 30' --> ['10','20','30'] --> 10,20,30 --> GÁN a b c = 10,20,30
   input   -->    split       -->  map     --> 

"""

# bước 1 : input ( dạng chuỗi)
s = input( " nhập : ")

#bước 2 : split : tách các số ra ( sâu ký tụ)
a =s.split()

#bước 3 : map : ép thành int 
x,y,z=map(int, a)

print(x+y+z)

# gọn 
b,c,d = map(int ,input("nhâp:").split())