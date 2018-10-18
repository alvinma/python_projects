class Employee:
    """Basic employee class.
    
    Attributes:
        name: Name of the employee.
        salary: Salary of the employee.
        empCount: Interger count for the number of employees entered
    """
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      """Inits for Employee."""
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     """Print total count of employees recorded."""
     print("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      """Print employee name and salary information."""
      print("Name : ", self.name,  ", Salary: ", self.salary)