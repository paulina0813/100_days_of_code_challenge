'''
003. Lists
- Grouped pieces of data
- They use []
- They can store strings, ints, booleans, etc
- They have an order determined by the list
'''
#order in which the states joined the union
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
                     "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
                     "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky",
                     "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama",
                     "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa",
                     "Wisconsin", "Calfornia", "Minnesota", "Oregon", "Kansas", "West Virginia",
                     "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana",
                     "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona",
                     "Alaska", "Hawaii"]

print(states_of_america[0]) #Print the first item of the list

#If you increase the number, it goes through the list in the order that it was saved
print(states_of_america[1]) #prints Pennsylvania
print(states_of_america[2]) #prints New Jersey
print(states_of_america[3]) #prints Georgia
print(len(states_of_america)) #shows you the length of the list

#If you use a negative index, it starts counting from the back
print(states_of_america[-1]) #prints Hawaii
print(states_of_america[-2]) #prints Alaska
print(states_of_america[-3]) #prints Arizona

#Edit the list
states_of_america[1] = "Pencilvania" #edits the entry in that index to "Pencilvania"
print(states_of_america) #look at the changes

#Add to the list

#Append adds a single value
states_of_america.append("Angelaland") #adds Angelaland to the end of the list
print(states_of_america) #look at the changes

#extend adds several values
states_of_america.extend(["Jack Bauer Land", "Lalaland"])
print(states_of_america) #look at the changes