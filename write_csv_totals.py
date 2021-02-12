from one import Card
from archive import file_names_final, today
from csv import DictWriter
import os.path


file_exists = os.path.isfile('total_info.csv')

card_name = Card(file_names_final[0])
# print(card_name.name)


with open("total_info.csv", "a", newline='') as file:
	headers = ["EIK", "Amounts", "Date"]
	if not file_exists:
		csv_writer = DictWriter(file, fieldnames=headers)
		csv_writer.writeheader()
	csv_writer = DictWriter(file, fieldnames=headers)
	csv_writer.writerow({
		"EIK": card_name.direction(),
		"Amounts": "",
		"Date": today
	})
