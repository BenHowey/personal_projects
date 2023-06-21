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
employee_data = pd.DataFrame({
    'Name': ['John Doe', 'Alice Smith', 'Mike Johnson', 'Emily Brown', 'David'],
    'Age': [35, 28, None, '30s', 40],
    'Salary': ['$60,000', '70000', '85,000', None, '100000'],
    'Email': ['johndoe@example.com', 'alice.smith@example.com', 'mike.johnson@example.com', 'emily.brown@example.com', 'dave.brown@example.com']
})
# employee_data.dropna(inplace=True)
employee_data['Age'] = pd.to_numeric(employee_data['Age'], errors='coerce')
employee_data['Salary'] = employee_data['Salary'].str.replace(',', '').str.replace('$', '').astype(float)
#convert all names to lower case
employee_data['Name']=employee_data['Name'].str.title()
# split at the @ sign and select the first bit!
employee_data['Username'] = employee_data['Email'].str.split('@',expand=True)[0]



print(employee_data)


product_data = pd.DataFrame({
    'Name': ['Apple', 'Banana', 'Orange', 'Mango'],
    'Price': ['$0.99', '$1.25', '$0.75', '$1.50']
})

# remove dollar signs from price and convert to floats
product_data['Price']=product_data['Price'].str.replace('$','').astype(float)
# Create a new column called 'Price Range' that categorizes the products as 'Low', 'Medium', or 'High' based on their prices. Assume the following price ranges: 'Low' for prices below $1.00, 'Medium' for prices between $1.00 and $1.50 (inclusive), and 'High' for prices above $1.50.
product_data['Price Range'] = product_data['Price'].apply(lambda x: 'Low' if x < 1.0 else 'High' if x > 1.5 else 'Medium')


print(product_data)
print(product_data.describe())
print(product_data.info())
