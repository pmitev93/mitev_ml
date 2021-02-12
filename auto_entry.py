from selenium import webdriver
import time
# import one
from csv import DictReader
import pandas as pd

def import_stuff():
    id = 0
    with open("C:/Users/pmite/Google Drive/ML_scan_project/code/Archive/individual_info.csv") as file:
        csv_reader = DictReader(file)
        entry_info = next(csv_reader)
        try:
            while entry_info["Added_to_Sum"]:
                entry_info = next(csv_reader)
                id += 1
        except StopIteration:
            label['text'] = 'End'
            return None
        code_enter = entry_info["Code"]
        eik_enter = entry_info["EIK"]

    df = pd.read_csv("C:/Users/pmite/Google Drive/ML_scan_project/code/Archive/individual_info.csv", dtype={'Added_to_Sum': str})
    df.at[id, "Added_to_Sum"] = 'x'
    df.to_csv('C:/Users/pmite/Google Drive/ML_scan_project/code/Archive/individual_info.csv', index=False)

    web = webdriver.Chrome()
    web.get('file:///C:/Users/pmite/Google%20Drive/ML_scan_project/code/NisoWebApp_whited2.html')

    time.sleep(2)

    # code_name = one.a.code_extract()
    last = web.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/ngb-tabset/div/div/form/div[1]/app-fi-select-dropdown/div/div/ng-select/div/div/div[3]/input')
    last.send_keys(code_enter)

    eik_ent = 'Юридическо лице / Едноличен търговец'
    last = web.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/ngb-tabset/div/div/form/div[3]/app-fi-select-dropdown/div/div/ng-select/div/div/div[3]/input')
    last.send_keys(eik_ent)

    time.sleep(2)

    # eik_ent = one.a.direction()
    last = web.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/ngb-tabset/div/div/form/div[4]/app-fi-select-dropdown/div/div/ng-select/div/div/div[2]/input')
    last.send_keys(eik_enter)

def storage_import():
    id = 0
    with open("C:/Users/pmite/Google Drive/ML_scan_project/code/Archive/suhranenie.csv") as file:
        csv_reader = DictReader(file)
        entry_info = next(csv_reader)
        try:
            while entry_info["Added"]:
                entry_info = next(csv_reader)
                id += 1
        except StopIteration:
            label['text'] = 'End'
            return None
        code_enter = entry_info["Code"]
        eik_enter = entry_info["EIK"]

    df = pd.read_csv("C:/Users/pmite/Google Drive/ML_scan_project/code/Archive/suhranenie.csv", dtype={'Added': str})
    df.at[id, "Added"] = 'x'
    df.to_csv('C:/Users/pmite/Google Drive/ML_scan_project/code/Archive/suhranenie.csv', index=False)

    web = webdriver.Chrome()
    web.get('file:///C:/Users/pmite/Google%20Drive/ML_scan_project/code/NisoWebApp_whited2.html')

    time.sleep(2)

    # code_name = one.a.code_extract()
    last = web.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/ngb-tabset/div/div/form/div[1]/app-fi-select-dropdown/div/div/ng-select/div/div/div[3]/input')
    last.send_keys(code_enter)

    eik_ent = 'Юридическо лице / Едноличен търговец'
    last = web.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/ngb-tabset/div/div/form/div[3]/app-fi-select-dropdown/div/div/ng-select/div/div/div[3]/input')
    last.send_keys(eik_ent)

    time.sleep(2)

    # eik_ent = one.a.direction()
    last = web.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/ngb-tabset/div/div/form/div[4]/app-fi-select-dropdown/div/div/ng-select/div/div/div[2]/input')
    last.send_keys(eik_enter)