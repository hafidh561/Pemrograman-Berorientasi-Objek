from Invoice import Invoice


def main():
	items = [Invoice("RTX 2080", "VGA", 5, 10000000), Invoice("Intel i9 10900K", "Processor", 10, 8000000)]
	for item in items:
		print(item.part_num)
		print(item.part_desc)
		print(item.quantity)
		print(item.price)
		print("Total tagihanmu adalah", item.get_invoice_amount(), end="\n\n")


if __name__ == "__main__":
	main()
