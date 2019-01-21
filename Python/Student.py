class Student: 
    def __init__(self):
        self._rollno=0
        self._Name=None
        self._marks=[]
        self._Grade=0.0
        
    def readData(self):
        self._rollno=int(input("Enter rollno"))
        self._Name=input("Enter name")
        self._marks=[int(x) for x in input().split()]
        self.calculate()
    def displayData(self):
        print(self._rollno,self._Name,self._marks)
    def calculate(self):
        print(sum(self._marks)/(len(self._marks)*100))

    def sortName(self,stu):
        for i in range(0,len(stu)):
            for j in range(i+1,len(stu)):
                if(stu[i]._Name > stu[j]._Name):
                    stu[i],stu[j]=stu[j],stu[i]
        for k in range(0,len(stu)):
            print(stu[k]._Name)
        
s1=Student()
s2=Student()
s3=Student()
s1.readData()
s2.readData()
s3.readData()
#s1.displayData()
stu=[s1,s2,s3]
s1.sortName(stu)

    
