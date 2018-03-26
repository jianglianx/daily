#coding:utf-8
from __future__ import print_function
def prnmonth( year,month):
#	print "\t",getmonthname(name), " ",year
	print ();
        print ("         日历" ,year,month )
	print ("#"*28);
	print (' Sun Mon Tue Wed Thu Fri Sat');
#一号是星期几
	starday = whatday(year,month)
#当月有多少天
	numinmonth = howmanydays(year,month)
#输入当月的所有天数
	for i in range (0,starday):
		print ("    ",end="")
	for i in range(1,numinmonth+1):
		if i<10:
			tem='   %d' %i
		else:
			tem='  %d' %i
		print(tem, end="")
		if ((i + starday)%7==0):
			print ()
	print ()
 	print ('#'*28)
	print ()
	
	#每月的1日是星期几
def whatday(year,month):
	starday18000101 = 3
#总天数
	total = 0
	for y in range(1800,year):
		if isrunnian(y):
			total=366+total
		else :
			total=365+total
	for m in range (1,month):
		total=total+howmanydays(year,m)
	return (total+starday18000101)%7
			
	


#每月有多少天
def howmanydays(year,month):
	if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
		return 31
	if(month==4 or month==6 or month==8 or month==11 ):
		return 30
	if (month==2):
		if isrunnian(year):
			return 29
		else:
			return 28

#是否是闰年
def isrunnian(year):
	return (year%4==0 and year%100!=0)or year%400==0


def main():
	year =input('请输入年份： ')	
	month = input('请输入月份： ')
	return (prnmonth(year, month))
main()
