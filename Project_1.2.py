import csv

"""
Which brand is most popular in each region?
"""

def categorical_dict_creator(column_name): #Creates a dictionary with the categories in a column as the key and the number of occurrences as the value
    with open("EV.csv", "r") as file:
        data = list(csv.reader(file))
    
    column_dict = {}

    for i in range(len(data[0])): #Assigns the column number based on the column name provided
        if data[0][i] == str(column_name):
            column_num = i
            
    for row in data[1:]: #Assigns keys and values to the dictionary
        if row[column_num] not in column_dict:
            column_dict[row[column_num]] = 1
        else:
            column_dict[row[column_num]] += 1
    
    return column_dict
    file.close()


def dict_print(Dict): #This function prints the dictionary in a readable format
    bold_start = '\033[1m'
    bold_end = '\033[0m'
    
    for key, value in Dict.items():
        nested_sum = sum(value.values())  # Sum the values in the nested dictionary
        print(bold_start + key + ":" + bold_end, value, bold_start 
                + "| Total:" + bold_end, bold_start + str(nested_sum) + bold_end)
        print('\n')
    

def print_answer(Dict):
    bold_start = '\033[1m'
    bold_end = '\033[0m'

    for key, value in Dict.items():
        nested_sum = sum(value.values())  # Sum the values in the nested dictionary
        """
        Of the [num] EV's sold in [region], the brand [brand] was the most popular, selling [num] units.
        """
        print("Of the ", bold_start + str(nested_sum) + bold_end, " EV's sold in ", bold_start + key + bold_end,
              ", the brand ", bold_start + str(max(value, key=value.get)) + bold_end, " was the most popular, selling ", 
              bold_start + str(value[max(value, key=value.get)]) + bold_end, " units.")
        print('\n')
        

def region_brand_units_sold():
    with open("EV.csv", "r") as file:
        data = list(csv.reader(file))

    column1_dict = categorical_dict_creator("Region")

    Region_column = columnNum_assignment("Region")
    Brand_column = columnNum_assignment("Brand") 
    UnitsSold_column = columnNum_assignment("Units_Sold") 

    return_dict = {}
    for key1 in column1_dict.keys(): # Iterate over unique values in column1
        return_dict[key1] = {} #Assigns the regions as main keys and each region has an empty value
        for row in data[1:]: #iterates over all rows in the dataset, skipping the header row 
            if row[Region_column] == key1: #If the value in the row matches the key in the dictionary
                Brand_value = row[Brand_column] #Assigns the value in the row to the key in the dictionary
                if Brand_value not in return_dict[key1]: # If the value in the row is not in the dictionary it creates a new key

                    return_dict[key1][Brand_value] = 0 
                else:
                    return_dict[key1][Brand_value] += int(row[UnitsSold_column]) 
  
    return return_dict
    file.close()
    
def columnNum_assignment(column_name): #This function assigns the column number based on the column name provided
    with open("EV.csv", "r") as file:
        data = list(csv.reader(file))
    
    for i in range(len(data[0])):
        if data[0][i] == str(column_name):
            column_num = i
    return column_num
    file.close()


print("\n")
print('\033[1m' + "Which brand is most popular in each region?\n" + '\033[0m')
dict_print(region_brand_units_sold())
print("_" * 100)
print("\n")
print_answer(region_brand_units_sold())



