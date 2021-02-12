import tkinter as tk
from PIL import ImageTk, Image
# from auto_entry import import_stuff, end_func
from csv import DictReader
from selenium import webdriver
import time
import pandas as pd
from codes_stuff import codes_list
from datetime import datetime, timedelta, date

HEIGHT = 590
WIDTH = 590


def date_tranform(radio_inpt, *args):
    if radio_inpt == 1:
        date_to_work = datetime.today().strftime("%d/%m/%Y")
        label['text'] = ''
        return date_to_work
    elif radio_inpt == 2:
        date_to_work = date.today() - timedelta(days=1)
        label['text'] = ''
        return date_to_work
    elif radio_inpt == 3:
        label['text'] = ''
        for x in args:
            if not x.isdigit():
                label['text'] = "Моля въведете само цифри"
                return None
            elif len(x) > 2:
                label['text'] = "Моля въведете само по две цифри на поле"
        if int(args[0]) > 31:
            label['text'] = "Невалидна дата (ден)"
        if int(args[1]) > 12:
            label['text'] = "Невалидна дата (месец)"
        date_to_work = f"{args[0]}/{args[1]}/20{args[2]}"
        return date_to_work


def import_stuff():
    id1 = 0
    with open("C:/Users/pmite/Google Drive/ML_scan_project/code/Archive/individual_info.csv") as file:
        csv_reader = DictReader(file)
        entry_info = next(csv_reader)
        try:
            while entry_info["Submitted"]:
                entry_info = next(csv_reader)
                id1 += 1
        except StopIteration:
            label['text'] = 'Всички карти са подадени'
            return None
        code_enter = entry_info["Code"]
        eik_enter = entry_info["EIK"]
        amnt = entry_info["Koli4estvo"]
        card_date = entry_info["Data"]

    df = pd.read_csv("C:/Users/pmite/Google Drive/ML_scan_project/code/Archive/individual_info.csv",
                     dtype={'Submitted': str})
    df.at[id1, "Submitted"] = 'Podadeno'
    df.to_csv('C:/Users/pmite/Google Drive/ML_scan_project/code/Archive/individual_info.csv', index=False)

    web = webdriver.Chrome()
    web.get('file:///C:/Users/pmite/Google%20Drive/ML_scan_project/code/NisoWebApp_whited2.html')

    time.sleep(2)

    # code_name = one.a.code_extract()
    last = web.find_element_by_xpath(
        '/html/body/ngb-modal-window/div/div/div[2]/ngb-tabset/div/div/form/div[1]/app-fi-select-dropdown/div/div/ng-select/div/div/div[3]/input')
    last.send_keys(code_enter)

    eik_ent = 'Юридическо лице / Едноличен търговец'
    last = web.find_element_by_xpath(
        '/html/body/ngb-modal-window/div/div/div[2]/ngb-tabset/div/div/form/div[3]/app-fi-select-dropdown/div/div/ng-select/div/div/div[3]/input')
    last.send_keys(eik_ent)

    time.sleep(2)

    # eik_ent = one.a.direction()
    last = web.find_element_by_xpath(
        '/html/body/ngb-modal-window/div/div/div[2]/ngb-tabset/div/div/form/div[4]/app-fi-select-dropdown/div/div/ng-select/div/div/div[2]/input')
    last.send_keys(eik_enter)

    amount = web.find_element_by_xpath(
        '/html/body/ngb-modal-window/div/div/div[2]/ngb-tabset/div/div/form/div[6]/app-fi-input-float/div/div/input')
    amount.send_keys(amnt)


def storage_import():
    id1 = 0
    with open("C:/Users/pmite/Google Drive/ML_scan_project/code/Archive/suhranenie.csv") as file:
        csv_reader = DictReader(file)
        entry_info = next(csv_reader)
        try:
            while entry_info["Submitted"]:
                entry_info = next(csv_reader)
                id1 += 1
        except StopIteration:
            label['text'] = 'Всичко е подадено'
            return None
        code_enter = entry_info["Code"]
        eik_enter = '112106418'
        amnt = entry_info["Koli4estvo_obshto"]

    df = pd.read_csv("C:/Users/pmite/Google Drive/ML_scan_project/code/Archive/suhranenie.csv",
                     dtype={'Submitted': str})
    df.at[id1, "Submitted"] = 'Podadeno'
    df.to_csv('C:/Users/pmite/Google Drive/ML_scan_project/code/Archive/suhranenie.csv', index=False)

    web = webdriver.Chrome()
    web.get('file:///C:/Users/pmite/Google%20Drive/ML_scan_project/code/NisoWebApp_whited_sum.html')

    time.sleep(2)

    # code_name = one.a.code_extract()
    last = web.find_element_by_xpath(
        '/html/body/ngb-modal-window/div/div/div[2]/ngb-tabset/div/div/form/div[1]/app-fi-select-dropdown/div/div/ng-select/div/div/div[3]/input')
    last.send_keys(code_enter)

    eik_ent = 'Юридическо лице / Едноличен търговец'
    last = web.find_element_by_xpath(
        '/html/body/ngb-modal-window/div/div/div[2]/ngb-tabset/div/div/form/div[3]/app-fi-select-dropdown/div/div/ng-select/div/div/div[3]/input')
    last.send_keys(eik_ent)

    time.sleep(2)

    # eik_ent = one.a.direction()
    last = web.find_element_by_xpath(
        '/html/body/ngb-modal-window/div/div/div[2]/ngb-tabset/div/div/form/div[4]/app-fi-select-dropdown/div/div/ng-select/div/div/div[2]/input')
    last.send_keys(eik_enter)

    amount = web.find_element_by_xpath(
        '/html/body/ngb-modal-window/div/div/div[2]/ngb-tabset/div/div/form/div[6]/app-fi-input-float/div/div/input')
    amount.send_keys(amnt)


def new_arch():
    df = pd.read_csv("C:/Users/pmite/Google Drive/ML_scan_project/code/Archive/individual_info.csv",
                     dtype={"Added_to_Sum": str, 'Submitted': str})
    df_suh = pd.read_csv("C:/Users/pmite/Google Drive/ML_scan_project/code/Archive/suhranenie.csv",
                         dtype={'Submitted': str})
    not_submitted = df.loc[df["Added_to_Sum"] != "s"]

    list_dates = not_submitted["Data"].tolist()
    list_dates = list(set(list_dates))

    for date in list_dates:
        date_f = not_submitted.loc[not_submitted["Data"] == date]
        for code in codes_list:
            to_enter = date_f.loc[date_f["Code"] == code]
            if not to_enter.empty:
                sum_to_add = to_enter.sum(axis=0)["Koli4estvo"]
                # print(to_enter.iloc[0,1])
                fin_df = df_suh.loc[df_suh["Data"] == date].loc[df_suh["Code"] == code]
                indx = df_suh.loc[df_suh["Data"] == date].loc[df_suh["Code"] == code].index
                if not fin_df.empty:
                    final_sum = fin_df.sum(axis=0)["Koli4estvo_obshto"] + sum_to_add
                    df_suh.at[indx, "Koli4estvo_obshto"] = final_sum
                else:
                    new_row = {'EIK': '112106418', 'Koli4estvo_obshto': sum_to_add, 'Code': code, 'Data': date,
                               "Submitted": ""}
                    df_suh = df_suh.append(new_row, ignore_index=True)

    df.loc[df['Added_to_Sum'] != 's', 'Added_to_Sum'] = 's'
    df.to_csv('C:/Users/pmite/Google Drive/ML_scan_project/code/Archive/individual_info.csv', index=False)
    df_suh.to_csv('C:/Users/pmite/Google Drive/ML_scan_project/code/Archive/suhranenie.csv', index=False)
    label['text'] = 'Сумирането извършено'
    return None


root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

img = ImageTk.PhotoImage(Image.open('geometry-background.png'))
background_label = tk.Label(root, image=img)
background_label.place(relheight=1, relwidth=1)

frame = tk.Frame(root, bg='#11bed9')
frame.place(relx=0.5, rely=0.02, relwidth=0.9, relheight=0.15, anchor='n')

button = tk.Button(frame, text='Подай\n (Индивидуални)', bg='#155fbf', fg='white', font='Courier, 15',
                   command=lambda: import_stuff())
button.place(relx=0, relheight=1, relwidth=0.32)

button_arch = tk.Button(frame, text='Обнови', bg='#155fbf', fg='white', font='Courier, 15',
                        command=lambda: new_arch())
button_arch.place(relx=0.34, relheight=1, relwidth=0.32)

button_sum = tk.Button(frame, text='Подай\n (Съхранение)', bg='#155fbf', fg='white', font='Courier, 15',
                       command=lambda: storage_import())
button_sum.place(relx=0.68, relheight=1, relwidth=0.32)

lower_frame = tk.Frame(root, bg='#155fbf', bd=10)
lower_frame.place(relx=0.5, rely=0.2, relwidth=0.885, relheight=0.15, anchor='n')

label = tk.Label(lower_frame, font='Courier, 16', anchor='center', justify='center', bd=4)
label.place(relwidth=1, relheight=1)

fin_frame = tk.Frame(root, bg='#155fbf', bd=10)
fin_frame.place(relx=0.5, rely=0.39, relwidth=0.885, relheight=0.58, anchor='n')

# entry_EIK = tk.Entry(fin_frame, font='Courier, 12',)
# entry_EIK.place(relwidth=0.5, rely=0, relheight=0.2)
T = tk.Text(fin_frame, height=2, width=30)
T.insert(tk.END, "Товарополучател: ")
T.config(bg="#155fbf", font='Courier, 17', bd=0, fg='white')
T.place(relx=0.02, relwidth=0.4, rely=0.025, relheight=0.15)

variable = tk.StringVar(fin_frame)
variable.set("МЛ")
entry_EIK = tk.OptionMenu(fin_frame, variable, "МЛ България", "Екосейф", "ПУДООС")
entry_EIK.config(bg="#155fbf", font='Courier, 16', anchor='c', fg='white')
entry_EIK.place(relx=0.5, relwidth=0.5, rely=0, relheight=0.15)
entry_EIK["menu"].config(bg="#155fbf", font='Courier, 16', fg='white')

# entry_code = tk.Entry(fin_frame, font='Courier, 12')
# entry_code.place(relwidth=0.5, rely=0.25, relheight=0.2)
Cd = tk.Text(fin_frame, height=2, width=30)
Cd.insert(tk.END, "Код: ")
Cd.config(bg="#155fbf", font='Courier, 17', bd=0, fg='white')
Cd.place(relx=0.02, relwidth=0.4, rely=0.225, relheight=0.15)

variable_cd = tk.StringVar(fin_frame)
variable_cd.set(codes_list[0])  # default value

codes_entry = tk.OptionMenu(fin_frame, variable_cd, *codes_list)
codes_entry.config(bg="#155fbf", font='Courier, 16', anchor='c', fg='white')
codes_entry['menu'].config(bg="#155fbf", font='Courier, 16', fg='white')
codes_entry.place(relx=0.5, relwidth=0.5, rely=0.2, relheight=0.15)

Dt = tk.Text(fin_frame, height=2, width=30)
Dt.insert(tk.END, "Дата: ")
Dt.config(bg="#155fbf", font='Courier, 17', bd=0, fg='white')
Dt.place(relx=0.02, relwidth=0.13, rely=0.43, relheight=0.15)

var = tk.IntVar()
var.set(1)
bt = tk.Radiobutton(fin_frame, text="Днес", variable=var, value=1)
bt.config(bg="#155fbf", font='Courier, 16', bd=0, fg='white', padx=0, selectcolor='#155fbf')

bt2 = tk.Radiobutton(fin_frame, text="Пред. \nраб. ден", variable=var, value=2)
bt2.config(bg="#155fbf", font='Courier, 16', bd=0, fg='white', padx=0, selectcolor='#155fbf')

bt3 = tk.Radiobutton(fin_frame, text="Друга \nдата:", variable=var, value=3)
bt3.config(bg="#155fbf", font='Courier, 16', bd=0, fg='white', selectcolor='#155fbf')

bt.place(relx=0.16, rely=0.4, relheight=0.15)
bt2.place(relx=0.35, rely=0.40, relheight=0.15)
bt3.place(relx=0.6, rely=0.4, relheight=0.15)
bt.select()
bt2.deselect()
bt3.deselect()

Dtd = tk.Text(fin_frame, height=2, width=3)
Dtd.insert(tk.END, "дд")
Dtd.config(bg="#155fbf", font='Courier, 15', bd=0, fg='white', )
Dtd.place(relx=0.802, rely=0.36, relheight=0.1)
entry_data_d = tk.Entry(fin_frame, font='Courier, 16', width=2)
entry_data_d.place(relx=0.8, rely=0.45, relheight=0.1)

Dtm = tk.Text(fin_frame, height=2, width=3)
Dtm.insert(tk.END, "мм")
Dtm.config(bg="#155fbf", font='Courier, 15', bd=0, fg='white', )
Dtm.place(relx=0.87, rely=0.36, relheight=0.1)
entry_data_m = tk.Entry(fin_frame, font='Courier, 16', width=2)
entry_data_m.place(relx=0.87, rely=0.45, relheight=0.1)

Dtg = tk.Text(fin_frame, height=2, width=3)
Dtg.insert(tk.END, "гг")
Dtg.config(bg="#155fbf", font='Courier, 15', bd=0, fg='white', )
Dtg.place(relx=0.952, rely=0.36, relheight=0.1)
entry_data_y = tk.Entry(fin_frame, font='Courier, 16', width=2)
entry_data_y.place(relx=0.94, rely=0.45, relheight=0.1)

Kol = tk.Text(fin_frame, height=2, width=30)
Kol.insert(tk.END, "Количество (т.) : ")
Kol.config(bg="#155fbf", font='Courier, 17', bd=0, fg='white')
Kol.place(relx=0.02, relwidth=0.4, rely=0.625, relheight=0.15)

entry_kol = tk.Entry(fin_frame, font='Courier, 16')  #.configure(state='disabled'/'normal)
entry_kol.place(relx=0.5, relwidth=0.5, rely=0.6, relheight=0.15)

button_sum = tk.Button(fin_frame, text='Подай\n (Унищожение)', bg='#155fbf', fg='white', font='Courier, 17',
                       command=lambda: date_tranform(var.get(), entry_data_d.get(), entry_data_m.get(),
                                                     entry_data_y.get()))
button_sum.place(relx=0, rely=0.8, relheight=0.2, relwidth=1)

root.mainloop()
