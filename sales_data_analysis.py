import numpy as np
# shop sells 4 poduct 7 days
# Each row = product
# Each column = day
sales = np.array([
    [10, 12, 15, 11, 14, 16, 18],
    [8, 10, 9, 11, 13, 12, 10],
    [20, 22, 25, 24, 26, 28, 30],
    [5, 7, 8, 6, 9, 10, 11]
])
# Total sales
print(np.sum(sales))
# Total sales of each product
print(np.sum(sales,axis = 1))
# Total sales per day
print(np.sum(sales,axis = 0))
# best selling product
product_totals = np.sum(sales,axis = 1)
best_product = np.argmax(product_totals)
print(best_product)
# Average sales
print("Average : ", np.mean(sales))
# highest sales
print("Highest sales : ", np.max(sales))
