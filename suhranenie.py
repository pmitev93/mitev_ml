from datetime import date
from csv import DictWriter, DictReader
from os.path import isfile
from one import Card
from codes_stuff import get_codes

total_ML = 0
total_other = 0
kol = 1

today = date.today()
d1 = today.strftime("%Y%m%d")

all_codes = get_codes()
all_dict = dict.fromkeys(all_codes, 0)
ML_dict = dict.fromkeys(all_codes, 0)
other_dict = dict.fromkeys(all_codes, 0)
list_dates = []

ind_file_exists = isfile('C:/Users/pmite/Google Drive/ML_scan_project/code/Archive/individual_info.csv')
sum_suhranenie = isfile('C:/Users/pmite/Google Drive/ML_scan_project/code/Archive/suhranenie.csv')

with open("C:/Users/pmite/Google Drive/ML_scan_project/code/Archive/individual_info.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        s = float(row["Koli4estvo"])
        all_dict[row['Code']] += s


with open(f"C:/Users/pmite/Google Drive/ML_scan_project/code/Archive/suhranenie.csv", "a",
          newline='') as file:
    headers = ["EIK", "Koli4estvo_obshto", "Code", "Data", "Added"]
    if not sum_suhranenie:
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
    csv_writer = DictWriter(file, fieldnames=headers)
    for key in all_dict:
        if all_dict.get(key) != 0:
            csv_writer.writerow({
                "EIK": '112106418',
                "Koli4estvo_obshto": all_dict.get(key),
                "Code": key,
                "Data": today,
                "Added": "",
            })