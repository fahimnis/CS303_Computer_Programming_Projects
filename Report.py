#  File: Report.py
#  Description: Hw8
#  Student's Name: Fahim Noor Islam
#  Student's UT EID: fni66
#  Course Name: CS 303E 
#  Unique Number: 50180
#
#  Date Created:
#  Date Last Modified:



# input data
companyName = "Lone Star Corporation"
date = "March 5, 2020"
cash = 7505.54
acctsRec = 502.21
supplies = 313.89
land = 6456.23
buildings = 81598.00
machAndEquip = 8329.99
patents = 2000.00
acctsPay = 93569.23
stock = 88100.00

assets = cash + acctsRec + supplies + land + buildings + machAndEquip + patents
liability = acctsPay + stock


print(""*80)

print(format(companyName.upper(),"^80s"))
print(format('Balance Sheet',"^80s"))
print(format(date,"^80s"))
print(format('',"^80"))

print(format('Liabilities and' , ">58s"))
print('{:<46s}{:<34s}'.format("Assets", "Stockholders' Equity"))

print('-'*80)

#I divided the 80 sapces into 4 columnds and specified the maximum number of fields each column can take. Then I just added some extra indentation to make the columns line up

print('{:<31s}{:>9.2f}{:<31s}{:>9.2s}'.format('   Cash',cash,'   Liabilities:'," "))
print('{:<31s}{:>9.2f}{:<31s}{:>9.2f}'.format('   Accounts Receivable',acctsRec,'      Accounts Payable',acctsPay))
print('{:<31s}{:>9.2f}{:<31s}{:>9.2s}'.format('   Supplies',supplies,' ',""))
print('{:<31s}{:>9.2f}{:<31s}{:>9.2s}'.format('   Land',land,' ',""))
print('{:<31s}{:>9.2f}{:<31s}{:>9.2s}'.format('   Buildings',buildings,"      Stockholders' Equity:",""))
print('{:<31s}{:>9.2f}{:<31s}{:>9.2f}'.format('   Machines and Equipment',machAndEquip,'         Capital Stock',stock))
print('{:<31s}{:>9.2f}{:<31s}{:>9.2s}'.format('   Patents',patents,"",""))
print(""*80)
print('{:<31s}{:>9.2f}{:<31s}{:>9.2s}'.format('Total Assets',assets,'   Total Liabilities and',""))
print('{:<31s}{:>9.2s}{:<31s}{:>9.2f}'.format('','',"      Stockholders' Equity",liability))
print(""*80)










