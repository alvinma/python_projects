//This example demostrates the creation of objects for Student class

class Student:
   """Basic student object.
    
   Attributes:
       rollno: Roll id number of student.
       name: Name of student.
   """
   
   def __init__(self, rollno, name):
      """Inits for student object."""
      self.rollno = rollno  
      self.name = name
   
   def displayStudent(self):
      """Display roll number and student name."""
      print("rollno : ", self.rollno,  ", name: ", self.name)  


// object creation
emp1 = Student(121, "Ajeet")  
emp2 = Student(122, "Sonoo")  

emp1.displayStudent()  
emp2.displayStudent()  