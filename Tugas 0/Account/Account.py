class Account:
	# Constructor untuk akun
	def __init__(self, initial_balance):
		self._initial_balance = initial_balance
		if self._initial_balance < 0:
			raise ValueError("Saldo awal harus lebih besar atau sama dengan 0")

	# Getter untuk akun
	@property
	def initial_balance(self):
		return self._initial_balance

	# Untuk tambah saldo
	def credit(self, input_balance):
		if input_balance <= 0:
			raise ValueError("Nilai masukanmu harus lebih besar dari 0")
		self._initial_balance += input_balance
		print("Penambahan saldo sukses")
		print("Saldomu sekarang", self.initial_balance)

	# Untuk tarik tunai
	def debit(self, input_balance):
		if input_balance > self._initial_balance:
			raise ValueError("Nilai ambilmu harus lebih kecil dari saldomu")
		self._initial_balance -= input_balance
		print("Pengambilan saldo sukses")
		print("Saldomu sekarang", self.initial_balance)

