#height = 4
#width = 4
#num = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#for i in range(0,height * width,4):
#    row=[]
#    for j in range(i,i+width,1):
#        row.append(num[j])
#    print(row)

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
    