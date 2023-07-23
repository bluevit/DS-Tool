import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from statistics import mean
import numpy as np
from datetime import datetime
from prettytable import PrettyTable




data = pd.read_csv('data1.csv')
price_date = data['Date']
#price_date = pd.to_datetime(data['Date'])
price_close = data['Close']


#price_date_str = price_date.dt.strftime('%m/%d/%Y')



#print("Enter a choice 1-8")

#fig = plt.figure()

#plt.subplot(2,2,1)
#plt.plot_date(price_date, price_close, linestyle='solid')
#plt.show()


#plt.subplot(2,2,2)
#plt.plot_date(price_date, price_close,'go')
#plt.tight_layout()
#plt.show()

def bubbleSort(array):
    
  # loop to access each array element
  for i in range(len(array)):

    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp

def bubble(array):
    bubbleSort(array)
    print('Minimum=',array[0])
    print('Maximum=',array[len(array)-1])


def linearSearch(array):
    key=float(input("Enter a Precised Value to Search"))
    for x in range(len(array)):
        if array[x]==key:
            place=x+1
            print(place)
            break
    else:
        print("Not Found")

def Mean(array):
    a=mean(array)
    print(round(a,1))
    
def outlier(arry):
   bubbleSort(arry)
   q1, q3= np.percentile(arry,[25,75])
   iqr = q3 - q1
   lower_bound = q1 -(1.5 * iqr) 
   upper_bound = q3 +(1.5 * iqr) 
   #print(lower_bound,upper_bound)
   # Create a larger figure and axis
   fig, ax = plt.subplots(figsize=(6, 5))  # Adjust the figsize as per your preference

    # Create the boxplot horizontally
   ax.boxplot(arry, vert=False)

    # Set the x-axis limits using the lower_bound and upper_bound
   ax.set_xlim(lower_bound - 1, upper_bound + 1)  # Adjust the values to decrease the distance

# Plot lower_bound and upper_bound as dots
   ax.plot(lower_bound, 1, 'ro', label=f'Lower Bound: {lower_bound}')
   ax.plot(upper_bound, 1, 'go', label=f'Upper Bound: {upper_bound}')
   ax.plot(q1, 1, 'bo', label=f'First Quartile: {q1}')
   ax.plot(q3, 1, 'yo', label=f'Third Quartile: {q3}')

   ax.set_title('Anything before Lower and after Upper Bounds is Outlier')

    # Display legend
   ax.legend()

    # Display the plot
   plt.show()

def Median(array):
    bubbleSort(array)
    n=len(array)
    print(array)
    if n%2==0:
        f=n//2
        s=(n+2)//2
        a=(array[f]+array[s])/2
        print('Median=',a)
    else:
        place=(n+1)/2
        a=array[place]
        print('Median=',a)
    return a
    

def comparision(price_date,price_close):
    fig = plt.figure()

# Subplot 1
    plt.subplot(2, 2, 3)
    plt.plot_date(mdates.date2num(price_date), price_close, linestyle='solid')
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d'))

    bubbleSort(price_close)
# Subplot 2
    plt.subplot(2, 2, 4)
    plt.plot_date(mdates.date2num(price_date), price_close, linestyle='solid')
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d'))

# Adjust the spacing between subplots
    plt.tight_layout()

# Add the month and year in the title
    title_date = datetime.strptime(price_date[0], '%Y-%m-%d').strftime('%B %Y')
    fig.suptitle(f'Comparision between Unsorted and Sorted Figures for ({title_date})')


# Display the figure
    plt.show()


columns = ["Choice", "Action"]

myTable = PrettyTable()
myTable.add_column(columns[0], ["1", "2", "3","4", "5", "6", "7", "8"])
myTable.add_column(columns[1], ["Unsorted vs Sorted Comparision (Time Series Chart)", "Sorted Figures of DataSet", "Minimum & Maximum value of DataSet", "Search a value in DataSet", "Mean of DataSet", "Median of DataSet", "Fencing DataSet (Boxplot)","Exit"])
myTable.title = "Welcome to DS Tool"
print(myTable)

while True:
    choice=input("Enter a choice 1-8\n")
    match choice:
        case "1":
            comparision(price_date,price_close)
        case "2":
            bubbleSort(price_close)
            print(price_close)
        case "3":
            bubble(price_close)
        case "4":
            linearSearch(price_close)#needed attention
        case "5":
            Mean(price_close)
        case "6":
            Median(price_close)
        case "7":
            outlier(price_close)
    if choice == "8":
        print("\nThank you for using DS Tool,\nKeep Analyzing!!!")
        break


