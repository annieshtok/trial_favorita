# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
# Demo file for Spyder Tutorial
# Hans Fangohr, University of Southampton, UK

def hello():
    """Print "Hello World" and return None"""
    print("Hello World")
    df=pd.read_csv("C:/NewDay/Favorita/set/oil.csv",na_values='NaN')
    df['dcoilwtico'][0]=92
    df2=pd.DataFrame(df,columns=['date','dcoilwtico'])
    df2['date']=pd.to_datetime(df2['date'])
    df2['dcoilwtico']=pd.to_numeric(df2['dcoilwtico'],errors='ignore')
    df2=df2.interpolate()
    print(df2.mean())
    print(df2)
    plt.plot(df2.date, df2.dcoilwtico)
#
    plt.savefig("C:/NewDay/Favorita/set/oil2.png")
    plt.show()

    print(sum(df2['dcoilwtico']))

# main program starts here
hello()