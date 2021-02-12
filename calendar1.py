from datetime import datetime,timedelta, date
import pandas as pd





def diff_month(card_date):
    todays_date = datetime.today().strftime("%d-%m-%Y")
    td = int(todays_date.split("-")[2])
    cd = int(card_date.split("/")[2])
    td_m = int(todays_date.split("-")[1])
    cd_m = int(card_date.split("/")[1])
    print(td,cd,td_m,cd_m)
    return ((td - cd) * 12) + td_m - cd_m


df = pd.read_csv("C:/Users/pmite/Google Drive/ML_scan_project/code/Archive/individual_info.csv",
                     dtype={'Submitted': str})

card_date = (df.at[0, 'Data'])

print(card_date)
print(diff_month(card_date))



# print(diff_month(datetime(2010,10,1), datetime(2010,9,1)))

