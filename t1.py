# import os
# os.system('cd C:/Users/pmite/Google Drive/ML_scan_project/code')
# os.system('python write_csv_totals.py > files_list.csv')


# new = df.loc[df["Added_to_Sum"]=="11"]
# print(new.empty)
# new_row = {'name':'Geo', 'physics':87, 'chemistry':92, 'algebra':97}
# mydataframe = mydataframe.append(new_row, ignore_index=True)


# df.to_csv('C:/Users/pmite/Google Drive/ML_scan_project/code/Archive/individual_info.csv', index=False)

# if not pd.isna(a):
#     print(type(a))

# ss = df.loc[df['Data']== '09/02/2021'].loc[df["Submitted"]=="x"]
# b = ss.sum(axis=0)
# print(b["Koli4estvo_obshto"])
# df['Total1'] = df.iloc[:, 4:10].sum(axis=1)

# from time import sleep
# from selenium import webdriver
# url = 'https://nwms.eea.government.bg/app/base/home'
# web = webdriver.Chrome()
# web.get(url)
# sleep(15)
# a = web.find_element_by_xpath('/html/body/app-root/app-home-main-page/app-home-page/div/div[2]/div/div[2]/div/div[1]/div[1]')
# from pyautogui import *
#
# sleep(5)
# moveTo(x=1175, y=114)
# click()
# press("Delete"),press("M"), press("L"), press("6"), press("3"), press("1"), press("0"), press("b"), press("g"), press("Enter")
#

# from tkinter import *
# def both(slctn, gt):
#     def eik_from():
#         if slctn == "one":
#             print (12121)
#         if slctn == "two":
#             print('233')
#         if slctn == "three":
#             print('333')
#
#     def box():
#         if gt:
#             print('Clicked')
#         else:
#             print("not clicked")
#     eik_from()
#     box()
#
# from codes_stuff import codes_list
#
# master = Tk()
# canvas = Canvas(master, height=800, width=800)
# canvas.pack()
#
# variable = StringVar(master)
# variable.set(codes_list[0]) # default value
#
# w = OptionMenu(master, variable, *codes_list)
# w.place(relx=0, relheight=0.5, relwidth=0.3)
#
# i = BooleanVar()
# i.set(True)
# c = Checkbutton(master, text = "Python", variable=i)
# c.place(relx=0, relheight=0.2, relwidth=0.3)
#
# button_sum = Button(master, text='Подай\n (Унищожение)', bg='#155fbf', fg='white', font='Courier, 12',
#                        command=lambda: both(variable.get(), i.get()))
# button_sum.place(relx=0.7, relheight=1, relwidth=0.3)

#
# mainloop()
# import tkinter as tk
#
# def test_f(a):
#     if a==0 :
#         print(f"the value is 1")
#     elif a==10:
#         print("two")
#
#
# master = tk.Tk()
# canvas = tk.Canvas(master, height=400, width=400)
# canvas.pack()
# var = tk.IntVar()
# var.set(3)
# bt = tk.Radiobutton(canvas, text="Option 1", variable=var, value=3,
#                   command=lambda: print("hello"))
#
# bt2 = tk.Radiobutton(canvas, text="Option 2", variable=var, value=10,
#                   command=lambda: test_f(var.get()))
# bt.pack()
# bt2.pack()
#
#
#
#
# tk.mainloop()

