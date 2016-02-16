# -*- coding: utf8 -*-
import json
import codecs
import sys
import csv
#with codecs.open(filename,'r',encoding='utf8') as f:
#Va = u'\u221220'
#float(a.replace(u'\N{MINUS SIGN}', '-'))
#a = u'\u221220'
#float(a.replace(u'\N{MINUS SIGN}', '-'))
#writer = csv.writer(open("/path/to/my/csv/file", 'w'))
#f = open('_Installation.json','r+b')
csv_file=[]
data_total=[]
location_total=[]
#location_by_country=[]
location=[]
#location=[]
cnt = 0
with codecs.open('../data/OctagonExcel_csv.csv','r') as f:
	reader = csv.reader(f)
	for i in reader:
		csv_file.append(i)
	print(csv_file)
		#print(data[j])




