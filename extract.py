from archive import move_scans
from os import listdir
from os.path import isfile, join
from datetime import date
from csv import DictWriter, DictReader
from one import Card
from codes_stuff import get_codes

today = date.today()
d1 = today.strftime("%Y%m%d")

move_scans()

f_names = [f for f in listdir(f'C:/Users/pmite/Google Drive/ML_scan_project/code/Archive/{d1}') if
           isfile(join(f'C:/Users/pmite/Google Drive/ML_scan_project/code/Archive/{d1}', f))]

ind_file_exists = isfile('C:/Users/pmite/Google Drive/ML_scan_project/code/Archive/individual_info.csv')
sum_suhranenie = isfile('C:/Users/pmite/Google Drive/ML_scan_project/code/Archive/suhranenie.csv')
# sum_other_exists = isfile(f'C:/Users/pmite/Google Drive/ML_scan_project/code/Archive/{d1}/total_info_other.csv')

total_ML = 0
total_other = 0
kol = 1

all_codes = get_codes()
all_dict = dict.fromkeys(all_codes, 0)
ML_dict = dict.fromkeys(all_codes, 0)
other_dict = dict.fromkeys(all_codes, 0)

with open("C:/Users/pmite/Google Drive/ML_scan_project/code/Archive/individual_info.csv", "a",
          newline='') as file:
    headers = ["EIK", "Koli4estvo", "Data", "Code", "Added_to_Sum","Submitted"]
    if not ind_file_exists:
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
    for f in f_names:
        card_inp = Card(f)
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writerow({
            "EIK": card_inp.direction(),
            "Koli4estvo": kol,
            "Data": today,
            "Code": card_inp.code_extract(),
            "Added_to_Sum": "",
            "Submitted": ""
        })


with open("C:/Users/pmite/Google Drive/ML_scan_project/code/Archive/individual_info.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        s = float(row["Koli4estvo"])
        all_dict[row['Code']] += s

with open(f"C:/Users/pmite/Google Drive/ML_scan_project/code/Archive/suhranenie.csv", "a",
          newline='') as file:
    headers = ["EIK", "Koli4estvo_obshto", "Code", "Data", "Submitted"]
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
                "Submitted": "",
            })


# with open(f"C:/Users/pmite/Google Drive/ML_scan_project/code/Archive/{d1}/total_info_other.csv", "a",
#           newline='') as file:
#     headers = ["EIK", "Koli4estvo_obshto", "Code", "Data"]
#     if not sum_other_exists:
#         csv_writer = DictWriter(file, fieldnames=headers)
#         csv_writer.writeheader()
#     csv_writer = DictWriter(file, fieldnames=headers)
#     csv_writer.writerow({
#         "EIK": card_inp.direction(),
#         "Koli4estvo": total_other,
#         "Code": "",
#         "Data": today,
#     })
