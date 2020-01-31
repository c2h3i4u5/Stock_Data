# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 21:43:21 2020

@author: c2h3i4u5
"""

import csv
import time
import Stock_Data
with open('output.csv', 'w', newline='\n') as csvfile:
  # 建立 CSV 檔寫入器
  writer = csv.writer(csvfile)
  
  
  while 1:
      
      writer.writerow([Stock_Data.Data_list[0],Stock_Data.Data_list[1],Stock_Data.Data_list[2],Stock_Data.Data_list[3],Stock_Data.Data_list[4],Stock_Data.Data_list[5],Stock_Data.Data_list[6],Stock_Data.Data_list[7],Stock_Data.Data_list[8],Stock_Data.Data_list[9],Stock_Data.Data_list[10],Stock_Data.Data_list[11],Stock_Data.Data_list[12]])
      time.sleep( 3 )

  
  csvfile.close
# writer.writerow([Stock_Data.Buy_price,Stock_Data.Buy_count,Stock_Data.Sell_price,Stock_Data.Sell_count,Stock_Data.Final_price,Stock_Data.Up_Down,Stock_Data.Vibration,Stock_Data.Final_Volume,Stock_Data.Open_price,Stock_Data.Highest_price,Stock_Data.Lowest_price,Stock_Data.Reference_price,Stock_Data.Time_step])

  # 寫入一列資料
#  writer.writerow([Stock_Data.Data_list])
#  writer.writerow(['姓名', '身高', '體重'])

#   寫入另外幾列資料
#  writer.writerow(['令狐沖', 175, 60])
#  writer.writerow(['岳靈珊', 165, 57])