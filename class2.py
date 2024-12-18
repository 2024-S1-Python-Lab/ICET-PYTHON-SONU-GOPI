class Student:
    def get(self):
        self.rlno=int(input("Enter Roll Number:"))
        self.name=input("Enter Name:")
        self.totalmark=float(input("Enter total Marks:"))
    def disp(self):
        print("\nStudent Details")
        print(f"Roll Number:{self.rlno}")
        print(f"Name:{self.name}")
        print(f"Total Marks:{self.totalmark}")
stud1=Student()
stud1.get()
stud1.disp()
