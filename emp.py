class person:
	def __init__(self,name,age):
		self.name =name
		self.age=age
		
	def display(self):
		print(f"Name: {self.name}, Age :{self.age}")
		
class employee(person):
	def __init_-(self,name,age,employee):
		super().__init__(name,age)
		self.employee_id=employee_id 
		
	def display_employee(self):

		self.display_person()
		print(f"Employee Id:{self.employee_id}")
		
class manager(employee):
	def __init__(self,name,age,employee_id,team_size):
		self.team_size=team_size
	def display_manager(self):
		self.display_employee()
		print(f"team size {self.team_size}")

e=employee("MTHL",30,"1234","sales")
e.display_employee()

m=manager("jane",40,"456","marketing",10)
m.display_manager()
