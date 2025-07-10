"""
toán từ logic trong Python
"""
#phép gán 
a=b=100
a , b, c = 10, 20, 30  # Gán giá trị cho a, b, c

# Toán tử học 
a = 1+1
b = 10-1
c = 5*5
d = 11/2 # Toán tử chia thập phân
e = 11//2  # Toán tử chia lấy nguyên
f = 11 % 2  # Toán tử chia lấy dư
g = 2 ** 3  # Toán tử lũy thừa

#toán tử so sánh
x = 1
y = 2 

print( a==b )




a = True
b = False

# Toán tử AND
c = a and b  # Kết quả là False

# Toán tử OR
d = a or b  # Kết quả là True

# Toán tử NOT
e = not a  # Kết quả là False

# In ra kết quả
print("Kết quả của a and b:", c)
print("Kết quả của a or b:", d)
print("Kết quả của not a:", e)
