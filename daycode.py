from turtle import clear


date=int(input("please enter the date ex : xx\t "))
month=(input("please enter the month ex:xx \t "))
year=(input("please enter year ex: xxxx \t"))
mc={"01":1, "02":4 ,"03":4,"04":0,"05":2,"06":5,"07":0,"08":3,"09":6,"10":1,"11":4,"12":6}
mc1=mc.get(month,"please enter correct month")
years=int(year[0:2])
year2=int(years)%4
yc={0:6 , 1:4 , 2:2 , 3:0}
yc1=yc.get(year2,"None")
yc2=int(year[2:4])
leafc=yc2//4
sum1=date+mc1+yc1+yc2+leafc
sum=sum1-1 if int(year)%4==0 and int(month)<=2  else sum1
rem=sum%7
days={1:"sun",2:"mon",3:"tus",4:"wed",5:"thus",6:"fri",0:"sat"}
print(days.get(rem))





