from Employee import Employee


def main():
	humans = [Employee("Raiden", "Kusumo", 5000000), Employee("Norman", "Kamaru", 10000000)]
	for human in humans:
		print("Gajimu perbulang sekarang adalah", human.monthly_salary)

	for human in humans:
		human.monthly_salary += human.monthly_salary * 10 / 100

	print()

	for human in humans:
		print("Gajimu perbulang sekarang adalah", human.monthly_salary)


if __name__ == "__main__":
	main()
