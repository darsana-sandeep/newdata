import datetime
from operator import gt

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_excel('DATA SET & RULES - MOTOR TESTINdemo.xlsx',engine='openpyxl') # only for xlsx files



p=pd.DataFrame(df)
start_date = datetime.datetime.strptime('2021-05-16',"%Y-%m-%d").date()
end_date = datetime.datetime.strptime('2021-05-17',"%Y-%m-%d").date()
for item in p['Unnamed: 0'][5:]:
    #print(str(item))

    data = datetime.datetime.strptime(str(item),'%Y-%m-%d %H:%M:%S.%f')
    mask = (data.date() >= start_date) and (data.date() < end_date)
    print(mask)
    # plt.plot(mask, 20)
    # plt.title('Input V Indicator')
    # # specifying horizontal line type
    # plt.axhline(y=458, label='Upper Limit-458', color='r', linestyle='-')
    # plt.axhline(y=455, label='Tolerance-455', color='g', linestyle='-')
    # plt.axhline(y=452, label='Lower Limit-452', color='r', linestyle='-')
    # plt.legend(loc='upper right')
    #
    # plt.xlabel("Time")
    # plt.ylabel("Input V")
    # plt.show()
