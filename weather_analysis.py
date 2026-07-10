import numpy as np
temps = np.array([32,34,33,35,31, 
30,36,38,41,
32,45,42,46,
29,27,43,44])
print(temps)
print(" Shape",temps.shape)
print("Size",temps.size)
print("Weather Analysis Report")
avg = np.mean(temps)
print("Average temperature",avg)
max = np.max(temps)
min = np.min(temps)
print("Maximum temperature",max)
print("Minimum temperature", min)
hday = np.argmax(temps)
print("Hottest day", hday)
cday = np.argmin(temps)
print("Coldest day", cday)
# day above average
above_average = temps[temps>avg]
print(above_average)
# count hot days above 35°C
count = temps[temps> 35]
print("No of hot days above 35°C :",len(count))

range_temps = max - min
print("Temperature range : ", range_temps)
# sort the temperatures
sort = np.sort(temps)
print("Sorted temperature",sort)
# print 5 hottest days
hottest_5 = print(" 5 hottest days",sort[-5: ])
# ptint 5 coldest days
coldest_5 = print(" 5 coldest days",sort[: 6])
print("Std = ", np.std(temps))

# count days below 32 °C
count = temps[temps< 32]
print("No of days below 32°C : ", len(count))
median = np.median(temps)
print("Median temperatures : ", median )

# 356 days of random temperatures
temps = np.random.randint(15,46, size = 365)
print(temps)
print("Season comparison report")
# creating summer and winter arrays
summer = np.random.randint(30,45,size = 10)
print("Summer Average : ",np.mean(summer))
winter = np.random.randint(10,15,size = 10)
print("Winter Average : ", np.mean(winter))
print("Temperature difference = ",np.mean(summer)- np.mean(winter))

# comparing which session is hotter
if (np.mean(summer)> np.mean(winter)) :
    print(" Summer is hotter than winter")
else :
    print( " Winter is hotter than summer")

