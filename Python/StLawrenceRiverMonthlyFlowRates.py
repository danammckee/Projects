# Program File Name: StLawrenceRiverMonthlyFlowRates.py
# Authors: Group 4 - Dana McKee, Korey Hayes, Riley Sweeney, Natalia Hrynko
# Date: November 30, 2020
# Description: The program is designed to read daily flow rates from a CSV file 
# and calculate the average monthly and yearly flow rates totals at a specific monitoring station, 
# St. Lawrence River, at Cornwall annd display data as a table and graph.

# Program Structure: Modules CSV and mathplotlib are imported.  Three functions are defined (plotGraph, Calcaverage, main). 
# CSV file is read. User input for year. Monthly and yearly flow rate average are calculated. Table with output values is produced.
# Graph with output values is produced. 

# Assumptions: None

# Limitations (Plans): Data is limited to the years 1958-1993 and only from the specific river,
# St. Lawernece River, at specific monitoring station, Cornwall

# Special Cases and Known Problems: 
# 1. 1958 cannot be run in the program due to no data being provided for the entire months of Jan-Jun. 
# This is handled by input statement and exception handler. 
# 2. If the user wants information for multiple years, they must restart the program due to limitations caused the matplotlib module.
# 3. The CSV file must be formatted so that  the year and the months are the only columns.

# Inputs: Year from user, Daily Discharge (m3/s) from CSV file
# Outputs: Average Monthly Discharge (m3/s), and Total Average Yearly Discharge (m3/s)

# References: Scatterplot and Matplotlib module - https://www.w3schools.com/python/python_ml_scatterplot.asp.
# https://matplotlib.org/tutorials/introductory/pyplot.html, CSV Module: Week 11 File Access_2020.pdf (Karen Whillans), 
# Table Formatting: Whale Mapping Version 2.2 Karen Whillans, https://www.educba.com/python-print-table/, 
# CSV Data File: https://wateroffice.ec.gc.ca/search/historical_e.html

# File: StLawrenceRiverMonthlyFlowRates.py
# Date: November 30, 2020

import csv                                  # csv used in week 12 for csv file reading/writing
import matplotlib                           # (available on college system as indicated on VDI)
def plotGraph(input_year, average, yearlyav):
    import matplotlib.pyplot as plt         # calls the module through plt
    yearlyav = str(round(yearlyav, 2))      # rounds the average
    Month= ["January","February","March","April","May","June","July","August","September","October","November","December"]
    plt.scatter(Month, average)             # creates a scatter plot with Month as the x-values and average as the y-values
    plt.ylabel('Average Discharge (m³/s)')  # creates a y-label
    plt.xlabel('Month')                     # creates an x-label
    plt.xticks(Month, rotation =45)         # formats the x-axis points to a 45 degree angle for viewing ease
    # sets the title of the graph
    plt.title('The Average Monthly Discharge of The St. Lawrence River \n At Cornwall Monitoring Station for the Year' + ' ' + input_year)
    # callout text for the yearly average at a specified point on the graph
    plt.text(Month[8], 7200, 'Yearly Avg ='+ ' ' + yearlyav, fontsize = 9)
    return plt.show()                       # returns the graph to print
    
def Calcaverage(month):
    # rounds the average calculated from the sum of the items in the month list and divides by the length of the list
    average=round(sum(month)/len(month), 2)
    return average

def main():
    try:
        flow = open(r"C:\PSP\Group4\group4psp\StLawrenceFlow.csv")          # opens the file required to read the input
        freader = list(csv.reader(flow))			# sets the file that is read to a list of lists					
        flow.close()								# closes the file once the reader is done
        x = 1									    # sets x to 1 because we don't want the first row of the csv
        janflow =[]                                 # create an empty list for each month of the year
        febflow =[]
        marflow =[]
        aprflow =[]
        mayflow =[]
        junflow =[]
        julflow =[]
        augflow =[]
        sepflow =[]
        octflow =[]
        novflow =[]
        decflow =[]

        # yearflow =[]                                # create an empty list for the flow of the whole year
        # year number index = 0, jan = 1, feb = 2, ...... , dec = 12
        print("Hello! \n Seems like you want to calculate flow rates!")
        print("What year would you like to calculate the flow rates for?")
        # allow the user to input the selected year between 1959 and 1993
        yearChoice = int(input("Please enter a year between 1959 and 1993:  "))
        # ensures the user input a number in the specified range
        if yearChoice <1959 or yearChoice >1993:
            while yearChoice <1959 or yearChoice >1993:
                print ("Year choice must be between 1959 and 1993")
                print("Please re-enter values")
                yearChoice = int(input("Please enter a REALISTIC number between 1959 and 1993:  "))
        # convert the choice to a string to be able to compare to the list items
        yearChoice = str(yearChoice)
        while x<1115:                               # cycle through all of the rows in the table
            if freader[x][0] == yearChoice:         # only append the lists if the item at this index = the inputted year
                if freader[x][1] != "":             # only append the list if there exists a value at this index
                    janflow.append(int(freader[x][1]))
                if freader[x][2] !="":
                    febflow.append(int(freader[x][2]))
                if freader[x][3] !="":
                    marflow.append(int(freader[x][3]))
                if freader[x][4] !="":
                    aprflow.append(int(freader[x][4]))
                if freader[x][5] !="":
                    mayflow.append(int(freader[x][5]))
                if freader[x][6] !="":
                    junflow.append(int(freader[x][6]))
                if freader[x][7] !="":
                    julflow.append(int(freader[x][7]))
                if freader[x][8] !="":
                    augflow.append(int(freader[x][8]))
                if freader[x][9] !="":
                    sepflow.append(int(freader[x][9]))
                if freader[x][10] !="":
                    octflow.append(int(freader[x][10]))
                if freader[x][11] !="":
                    novflow.append(int(freader[x][11]))
                if freader[x][12] !="":
                    decflow.append(int(freader[x][12]))
            x += 1
        # create a list of the monthly results
        monthlyflow=[janflow,febflow,marflow,aprflow,mayflow,junflow,julflow,augflow,sepflow,octflow,novflow,decflow]
        averagemonthlyflow=[]                       # create an empty list for average values
        for i in monthlyflow:                       # open a for loop to cycle through the index of the months
            average=Calcaverage(i)                  # call the average calculation function
            averagemonthlyflow.append(average)      # append the average list with the newly calculated value
        yearAvg = Calcaverage(averagemonthlyflow)   # get a yearly average from the calculated monthly averages
        print(averagemonthlyflow)
        print (yearAvg)
        print(plotGraph(yearChoice, averagemonthlyflow, yearAvg))

        # beginning of the end print statements
        print("---------------------------------------------------------------------------------")
        print()
        print("The Average Monthly Discharge (m³/s) of the St. Lawrence River \n at Cornwall Monitoring Station for the Year" + " " + yearChoice)
        print()
        # Display the columns headers and calculated averages
        print("January\t\t February\t March\t\t April\t\t June\t\t July")
        print(averagemonthlyflow[0],"\t", averagemonthlyflow[1],"\t", averagemonthlyflow[2],"\t", averagemonthlyflow[3],"\t", \
            averagemonthlyflow[5], "\t", averagemonthlyflow[6],"\n")
        # in two lines for easier viewing
        print("August\t\t September\t October\t November\t December\t Total Yearly Average")
        print(averagemonthlyflow[7],"\t", averagemonthlyflow[8],"\t", \
            averagemonthlyflow[9],"\t", averagemonthlyflow[10],"\t", averagemonthlyflow[11],"\t", yearAvg)
        print("---------------------------------------------------------------------------------")
    # exception handlers for those pesky users
    except TypeError:
        print("What are you trying to do here?")
    except ValueError: 
        print("You didn't enter a valid number, smart one")
    except RuntimeError: 
        print("You took too long, speedy one")
    except ZeroDivisionError:
        print("Stop trying to break the universe")
    except Exception as message:
        print(message)
if __name__ == '__main__':                          # call the main function if being called inside the script
    main()
