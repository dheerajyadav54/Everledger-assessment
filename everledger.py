'''Write a python program to 
- parse the attached employee.csv file
- Normalize the date fields into a standard format
- group the employee list based on the field "Quarter of Joining" and sorted by the field "Date of Birth" and print as follows:
{
	"Q1": ["<emp_name_1>", "<emp_name_2>", "<emp_name_3>", "<emp_name_4>", ...],
	"Q2": ["<emp_name_8>", "<emp_name_7>", "<emp_name_6>", "<emp_name_5>",...], 
	...
}'''

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
#from pandas.compat import StringIO
oo = pd.read_excel('employee__1_.xls', parse_dates=['Date of Birth', 'Date of Joining'])

oo = oo.sort_values(by = ['Date of Birth'])

oo["Name"] = oo["First Name"] + " " + oo["Last Name"]

print(oo.groupby('Quarter of Joining').agg({'Name': lambda x: x.tolist()})['Name'].to_dict())
