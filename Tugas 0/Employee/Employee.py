class Employee:
	# Constructor untuk Employee
	def __init__(self, first_name, last_name, monthly_salary):
		self._first_name = first_name
		self._last_name = last_name
		self._monthly_salary = monthly_salary
		if monthly_salary < 0:
			self._monthly_salary = 0

	# Getter dan setter first_name
	@property
	def first_name(self):
		return self._first_name

	@first_name.setter
	def first_name(self, new_first_name):
		self._first_name = new_first_name

	# Getter dan setter last_name
	@property
	def last_name(self):
		return self._last_name

	@last_name.setter
	def last_name(self, new_last_name):
		self._last_name = new_last_name

	# Getter dan setter monthly_salary
	@property
	def monthly_salary(self):
		return self._monthly_salary

	@monthly_salary.setter
	def monthly_salary(self, new_monthly_salary):
		self._monthly_salary = new_monthly_salary

