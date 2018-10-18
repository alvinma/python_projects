"""Simple application to calculate the average of provided values"""
import pandas as pd

true = 1
sum = 0

# Open text file to write and store values to find overall average.
file = open("Number_file.txt","w")

while(true):
    n = input("Enter the number you want to save in file. leave blank to escape :")
    if n == '':
        true = 0
    elif not n.isdigit():
        print ("Please enter a valid input")
    else:
        file.write(n)
        file.write("\n")

file.close()

# Re-Open text file and extract data points from file.
file = open("Number_file.txt","r")
element_list = file.readlines()
file.close()

for element in element_list:                           #calculating mean by sum and divide method
    sum += element

mean1 = sum/len(element_list) 

# Create readable list of data points
l2 = list(map(lambda x : int(x), l2))
dataframe = pd.DataFrame(l2)

sd = dataframe.values.std(ddof=1)                      #calculating standard deviation
mean = dataframe[0].mean()                             #calculating mean using pandas library