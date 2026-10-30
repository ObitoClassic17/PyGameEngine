class Matrix4x4:
    def __init__(self,numbers):
        self.m = []
        height = 4
        width = 4 
        for row in range(height):
            start = row * width
            self.m.append(numbers[start:start + width])
    def Identity(self):
        height = 4
        width = 4
        self.m = []
        for i in range(height):
            row = ([0]*width)
            row[i] = 1
            self.m.append(row)
    def multiply(self,other):
        height = 4
        width = 4
        result = []
        for i in range(height):
            row = []
            for j in range(width):
                total = 0 
                for k in range(width):
                    total += self.m[i][k] * other.m[k][j]
                row.append(total)
            result.append(row)
        flat = []
        for row in result:
            for number in row:
                flat.append(number)
        return Matrix4x4(flat)
    
a = Matrix4x4([1,2,3,4, 5,6,7,8, 9,10,11,12, 13,14,15,16])
b = Matrix4x4([0]*16)
b.Identity()
c = a.multiply(b)
print(type(c))                       # Matrix4x4
print(c.m)                           # صفوف a نفسها
print(a.multiply(a).m[0][0])         # 90
print(a.multiply(b).multiply(b).m)   # صفوف a نفسها
