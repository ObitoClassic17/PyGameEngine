class  Matrix4x4:
    def __init__(self,numbers):
        height = 4
        width = 4
        self.m = []
        for i in range(0,height * width,4):
            row=[]
            for j in range(i,i+width,1):
                row.append(numbers[j])
            self.m.append(row)
            print(row)
    
    def Identity(self):
        height = 4
        width = 4
        self.m = []
        for i in range(0,height * width,4):
            row = [0,0,0,0]
            row[i//4] = 1
            self.m.append(row)

    def __repr__(self):
        s=self.m
        return str(s)

    def multiply(self,other):
        height = 4
        width = 4
        result_rows = []
        for i in range(height):
            row = []
            for j in range(width):
                total = 0
                for k in range(width):
                    total += self.m[i][k] * other.m[k][j]
                row.append(total)
            result_rows.append(row)
        return result_rows
