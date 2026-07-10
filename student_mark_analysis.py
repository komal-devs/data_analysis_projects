import numpy as np
# data with missing values
data = np.array([25,30,45, np.nan,40,np.nan,56])
print(data)
count= np.isnan(data)
print(count)
print("Missing values", sum(count))
mean_value = np.mean(data)
print(mean_value) # give nan as output
# printing mean with ignoring nan 
mean_value = np.nanmean(data)
print(mean_value)
data[np.isnan(data)] = mean_value # this concept is known as masking
print(data)
print("Summary Statistics")
print("Mean : ", np.mean(data))
print("Median : ", np.median(data))
print("Maximum : ",np.max(data))
print("Minimum : ",np.min(data))
print("Standard Deviation : ",np.std(data))

