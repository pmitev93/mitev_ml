import os
import shutil
from datetime import date
from os import listdir
from os.path import isfile, join


def move_scans():
    today = date.today()

    # day_week = date.today().strftime('%A')
    d1 = today.strftime("%Y%m%d")

    file_names = [f for f in listdir('C:/Users/pmite/Google Drive/ML_scan_project/code/Scans_M') if isfile(join('C:/Users/pmite/Google Drive/ML_scan_project/code/Scans_M', f))]
    file_names_final = [f for f in file_names if f.endswith('.pdf') and f.startswith(f'Scan_{d1}')]

    dir1 = os.path.join(f"C:/Users/pmite/Google Drive/ML_scan_project/code/Archive/{d1}")
    if not os.path.exists(dir1):
        os.mkdir(dir1)

    for name in file_names_final:
        # if name.endswith('.pdf') and name.startswith(f'Scan_{d1}'):
        try:
            os.rename(f"C:/Users/pmite/Google Drive/ML_scan_project/code/Scans_M/{name}",
                      f"{dir1}/{name}")
            shutil.move(f"C:/Users/pmite/Google Drive/ML_scan_project/code/Scans_M/{name}",
                        f"{dir1}/win_scan200_yellow-Copy.pdf")
            os.replace(f"C:/Users/pmite/Google Drive/ML_scan_project/code/Scans_M/{name}",
                       f"{dir1}/win_scan200_yellow-Copy.pdf")

        except FileNotFoundError:
            pass

move_scans()
