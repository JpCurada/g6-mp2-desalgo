
items = [

    {"weight": 3, "value":4},
    {"weight":4, "value":5},
    {"weight": 2, "value": 6},
]

capacity = 7
number_of_items = 3

best_value = 0
best_selection = 0
best_weight = 0


#For checking the combination
selection = 0 

    #Looping through all the combinations
while selection < 2 ** number_of_items:
    total_weight = 0
    total_value = 0
    index = 0

    #Check each item in the selection combination
    while index < number_of_items:
        if selection & (1 <<index):
            total_weight += items[index]["weight"]
            total_value += items[index]["value"]
        index += 1 


#Checking if the total of combination is better than the previous 
    if total_weight <= capacity and total_value > best_value:
            best_value = total_value
            best_selection = selection
            best_weight = total_weight
        
    selection += 1
        
    #Printing of the Results

print("\nThe Capacity of knapsack", capacity)
print("Best estimation of the knapsack problem", best_weight)
print("Best value of the knapsack problem", best_value)
print("" * 10 + "Items Chosen:    ")
index = 0

while index < number_of_items:
        if best_selection & (1 << index):
            print("   - Item", index + 1,
                  "Weight:", items[index]["weight"],
                  "Value:-", items[index]["value"])
        
        index += 1
 