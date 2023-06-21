import pandas as pd
import numpy as np


# student_data = pd.DataFrame({
#     'StudentID': [101, 102, 103, 104, 105],
#     'Name': ['John', 'Alice', 'Mike', 'Emily', 'David'],
#     'Grades': [[80, 65, 90], [90, 92, 88], [75, 80, 82], [95, 88, 92], [85, 90, 88]]
# })

# student_data['Grade Average']=student_data['Grades'].apply(lambda x: np.asarray(x).mean())

# student_data_filtered=student_data[student_data['Grades'].apply(lambda x: np.sum(np.asarray(x) < 80) > 0)]
# print(student_data)
# print('##########')
# print(student_data_filtered)

#### DATA CLEANING #####
# employee_data = pd.DataFrame({
#     'Name': ['John Doe', 'Alice Smith', 'Mike Johnson', 'Emily Brown', 'David'],
#     'Age': [35, 28, None, '30s', 40],
#     'Salary': ['$60,000', '70000', '85,000', None, '100000'],
#     'Email': ['johndoe@example.com', 'alice.smith@example.com', 'mike.johnson@example.com', 'emily.brown@example.com', 'dave.brown@example.com']
# })
# # employee_data.dropna(inplace=True)
# employee_data['Age'] = pd.to_numeric(employee_data['Age'], errors='coerce')
# employee_data['Salary'] = employee_data['Salary'].str.replace(',', '').str.replace('$', '').astype(float)
# #convert all names to lower case
# employee_data['Name']=employee_data['Name'].str.title()
# # split at the @ sign and select the first bit!
# employee_data['Username'] = employee_data['Email'].str.split('@',expand=True)[0]



# print(employee_data)


# product_data = pd.DataFrame({
#     'Name': ['Apple', 'Banana', 'Orange', 'Mango'],
#     'Price': ['$0.99', '$1.25', '$0.75', '$1.50']
# })

# # remove dollar signs from price and convert to floats
# product_data['Price']=product_data['Price'].str.replace('$','').astype(float)
# # Create a new column called 'Price Range' that categorizes the products as 'Low', 'Medium', or 'High' based on their prices. Assume the following price ranges: 'Low' for prices below $1.00, 'Medium' for prices between $1.00 and $1.50 (inclusive), and 'High' for prices above $1.50.
# product_data['Price Range'] = product_data['Price'].apply(lambda x: 'Low' if x < 1.0 else 'High' if x > 1.5 else 'Medium')


# print(product_data)
# print(product_data.describe())
# print(product_data.info())

# # create a new column with true values for any Name that has an 'a' in it
# product_data['Has an A'] = product_data['Name'].apply(lambda x: 'True' if 'a' in x else 'False')

# sales_data = pd.DataFrame({
#     'Product': ['A', 'B', 'C', 'A', 'B', 'C'],
#     'Quantity': [5, 10, 3, 8, 12, 4],
#     'Revenue': [100, 200, 150, 80, 240, 100]
# })

# # Create a new column called 'Total Revenue' that represents the total revenue for each product, calculated as the product of quantity sold and revenue per unit.
# sales_data['Total Revenue'] = sales_data['Quantity'] * sales_data['Revenue']

# # Find the product with the highest total revenue.
# print(sales_data.groupby('Product').sum().sort_values('Total Revenue', ascending=False).head(1))

# # Calculate the average quantity sold for each product.
# print(sales_data.groupby('Product').mean())

# # Sort the DataFrame by the average quantity sold in descending order.
# sales_data.sort_values('Quantity', ascending=False, inplace=True)

# write a while loop that iteratively removes values from a list that are not within 3 standard deviations of the mean of the list. The loop should terminate when all remaining values in the list are within 3 standard deviations of the mean.
def remove_outliers(data, n_std=3):
    # clean the data to make sure they are all numbers. if they are not, replace with np.nan
    data = [x if isinstance(x, (int, float)) else np.nan for x in data]
    # remove all np.nan values
    data = [x for x in data if str(x) != 'nan']
    while True:
        mean = np.mean(data)
        std = np.std(data)
        if np.max(data) < mean + n_std * std and np.min(data) > mean - n_std * std:
            break
        data = [x for x in data if x > mean - n_std * std and x < mean + n_std * std]
    return data

print(remove_outliers([2, 2, 3, 2, 5, 3, 5.2, 6,6.2,7.3,7.8,5,6,9,3,5, 43, 70],3))



