# -*- coding: utf-8 -*-


import requests

r = requests.get('https://info512.taifex.com.tw/Future/FusaQuote_Norl.aspx')
if r.status_code == requests.codes.ok:
    
# print(r.status_code)
 
 stock_URL = r.text
 
# TX_point_now = stock_URL.find("臺指期020")     # 當月份
 MTX_point_now = stock_URL.find("小臺指期020")  # 當月份
 
# TX_point_NextMonth = stock_URL.find("臺指期030")     # 下個月份
 MTX_point_NextMonth = stock_URL.find("小臺指期030")  # 下個月份
 
 MTX_length = MTX_point_NextMonth - MTX_point_now
 
 Split_MTX = stock_URL[MTX_point_now:MTX_point_NextMonth]
 
 MTX_startpoint = Split_MTX.find("</span>")
 MTX_endpoint = Split_MTX.find("</tr>")  
  
 Split_MTX = Split_MTX[MTX_startpoint+7:MTX_endpoint]
 
 
 Process_str = Split_MTX.replace(' ', '')
 
 Process_str = Process_str.replace('</font>', '')
 Process_str = Process_str.replace('</td>', '')
 Process_str = Process_str.replace('<td>', '')
 Process_str = Process_str.replace('<fontcolor="', '')
 
 Start_split_point = Process_str.find(">")
 num_str = Process_str[Start_split_point+1:len(Process_str)]  #開始分割數據
 End_split_point = num_str.find("#")

 Buy_price = num_str[0:End_split_point]     #買價
 Buy_price = Buy_price.replace(',', '')     #買價
 Buy_price = float(Buy_price)               #買價
 
 Start_split_point = num_str.find(">")
 num_str_2 = num_str[Start_split_point+1:len(num_str)]
 num_str = num_str_2
 End_split_point = num_str.find("#")
 
 Buy_count = num_str[0:End_split_point]   #買量
 Buy_count = float(Buy_count)             #買量
 
 Start_split_point = num_str.find(">")
 num_str_2 = num_str[Start_split_point+1:len(num_str)]
 num_str = num_str_2
 End_split_point = num_str.find("#")
 
 Sell_price = num_str[0:End_split_point]   #賣價  
 Sell_price = Sell_price.replace(',', '')  #賣價                              
 Sell_price = float(Sell_price)            #賣價      

 Start_split_point = num_str.find(">")
 num_str_2 = num_str[Start_split_point+1:len(num_str)]
 num_str = num_str_2
 End_split_point = num_str.find("#")        
                                
 Sell_count = num_str[0:End_split_point]   #賣量                               
 Sell_count = float(Sell_count)            #賣量

 Start_split_point = num_str.find(">")
 num_str_2 = num_str[Start_split_point+1:len(num_str)]
 num_str = num_str_2
 End_split_point = num_str.find("#")     
                                
 Final_price = num_str[0:End_split_point]   #成交價
 Final_price = Final_price.replace(',', '')  #成交價                              
 Final_price = float(Final_price)            #成交價          
 
 Start_split_point = num_str.find(">")
 num_str_2 = num_str[Start_split_point+1:len(num_str)]
 num_str = num_str_2
 End_split_point = num_str.find("#")
                                
 Up_Down = num_str[0:End_split_point]   #漲跌
 Up_Down = Up_Down.replace(',', '')     #漲跌                              
 Up_Down = float(Up_Down)               #漲跌                              
                                
 Start_split_point = num_str.find(">")
 num_str_2 = num_str[Start_split_point+1:len(num_str)]
 num_str = num_str_2
 End_split_point = num_str.find("#")                               
  
 Vibration = num_str[0:End_split_point]   #振幅%
 Vibration = Vibration.replace(',', '')   #振幅%                             
 Vibration = float(Vibration)             #振幅%                                     
                                
 Start_split_point = num_str.find(">")
 num_str_2 = num_str[Start_split_point+1:len(num_str)]
 num_str = num_str_2
 End_split_point = num_str.find("#")                               
  
 Final_Volume = num_str[0:End_split_point]      #成交量
 Final_Volume = Final_Volume.replace(',', '')   #成交量                             
 Final_Volume = float(Final_Volume)             #成交量         

 Start_split_point = num_str.find(">")
 num_str_2 = num_str[Start_split_point+1:len(num_str)]
 num_str = num_str_2
 End_split_point = num_str.find("#")                               
  
 Open_price = num_str[0:End_split_point]    #開盤價
 Open_price = Open_price.replace(',', '')   #開盤價                             
 Open_price = float(Open_price)             #開盤價     
                            
 Start_split_point = num_str.find(">")
 num_str_2 = num_str[Start_split_point+1:len(num_str)]
 num_str = num_str_2
 End_split_point = num_str.find("#")                               
  
 Highest_price = num_str[0:End_split_point]       #當日最高價
 Highest_price = Highest_price.replace(',', '')   #當日最高價                             
 Highest_price = float(Highest_price)             #當日最高價   

 Start_split_point = num_str.find(">")
 num_str_2 = num_str[Start_split_point+1:len(num_str)]
 num_str = num_str_2
 End_split_point = num_str.find("#")                               
  
 Lowest_price = num_str[0:End_split_point]       #當日最低價
 Lowest_price = Lowest_price.replace(',', '')    #當日最低價                             
 Lowest_price = float(Lowest_price)              #當日最低價  

 Start_split_point = num_str.find(">")
 num_str_2 = num_str[Start_split_point+1:len(num_str)]
 num_str = num_str_2
 End_split_point = num_str.find("#")                               
  
 Reference_price = num_str[0:End_split_point]          #參考價
 Reference_price = Reference_price.replace(',', '')    #參考價                             
 Reference_price = float(Reference_price)              #參考價  

 Start_split_point = num_str.find(">")
 num_str_2 = num_str[Start_split_point+1:len(num_str)]
 
 Time_step = num_str_2
 Time_step = Time_step.replace('\t', '')
 Time_step = Time_step.replace('\r', '')
 Time_step = Time_step.replace('\n', '')
# Hour = Time_step[0:2]
# Min = Time_step[3:5]
# Sec = Time_step[6:8]
# Hour = float(Hour)
# Min = float(Min)
# Sec = float(Sec)

 Data_list = [Buy_price,Buy_count,Sell_price,Sell_count,Final_price,Up_Down,Vibration,Final_Volume,Open_price,Highest_price,Lowest_price,Reference_price,Time_step]

 print(Data_list)













 
# s.strip()
# string = "python"
#print(string[3:5])
# 輸出為 ho
 
# print(stock_URL.find("FF0000"))
 
 
 
# print(stock_URL.find("臺指期020"))
# print(stock_URL.find("小臺指期020"))
 
# print(r.text)



