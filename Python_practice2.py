### Membership Operator
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties")
else:
    print("El Paso is not in the list of counties")

### Logical Operator
counties = ["Arapahoe","Denver","Jefferson"]
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

### While Loop
x = 0
while x <= 5:
    print(x)
    x = x + 1

### for Loop
counties = ["Arapahoe","Denver","Jefferson"]
for county in counties:
    print(county)

numbers = [0, 1, 2, 3, 4,]
for num in numbers:
    print(num)
# the output will be the same if simplify the code by using the range() function
for num in range(5):
    print(num)

# Indexing can also by used to iterate through a list
# If the list contains string, will need to get the length of the list as an integer for the range() function.
for i in range(len(counties)):
    print(counties[i])

#Iterate Through a Dictionary
counties_dict = {"Arapahoe": 422829,"Denver":463353,"Jefferson":432438}
#Get the keys of a Dictionary
for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(county)
#Get the values of a Dictionary
for voters in counties_dict.values():
    print(voters)
for county in counties_dict:
    print(counties_dict[county])
for county in counties_dict:
    print(counties_dict.get(county))
#Get the Key-Value Pairs of a Dictionary
## for key, value in dictionary_name.items():
    #print(key, value)
for county, voters in counties_dict.items():
    print(county, voters)
# Skill Drill
for county, voters in counties_dict.items():
    print(str(county) + " county has", str(voters) + " registered voters.")

#Iterate Through a List of Dictionaries

##Get Each Dictionary in a List of Dictionaries
voting_data = [{"county":"Arapahoe","registered_voters": 422829},
               {"county":"Denver","registered_voters": 463353},
               {"county":"Jefferson","registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict)
# use range() to iterate over the list of dictionaries and prin tthe counties in voting_data
for i in range(len(voting_data)):
    print(voting_data[i])

# Get the Values from a List of Dictionaries
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
#retrieve the number of registered voters from each dictionary
for county_dict in voting_data:
    print(county_dict['registered_voters'])
#retrieve the county name from each dictionary
for county_dict in voting_data:
    print(county_dict['county'])

#Printing Formats
# 1. The print() Function
print("Hello World")
print("Your interest for the year is $" + str(50))

# 2. F-strings: Formatted String Lietrals
my_votes = int(input("How many votes did you get in the election?"))
total_votes = int(input("What is the total votes in the election?"))
percentage_votes = (my_votes / total_votes) *100
print("I received " + str(percentage_votes)+ "% of the total votes")
# edit the above code with f-strings.
my_votes = int(input("How many votes did you get in the election?"))
total_votes = int(input("What is the total votes in the election?"))
print(f"I received {my_votes / total_votes *100}% of the total votes.")

# 3. Using F-Strings with Dictionaries
counties_dict = {"Arapahoe": 369237,"Denver":413229,"Jefferson":390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")
# use f-strings
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

# 4. Multiline F-Strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes."
    f"The total number of votes in the election was {total_votes}."
    f"You received {candidate_votes / total_votes *100}% of the total votes.")
print(message_to_candidate)

# 5. Format Floating-Point Decimals
# f'{value:{width}.{precision}}'
# 'precision' indicates the number of decimal places to format the value.
# For example, to format the interest to two decimal places, we would use .2f
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
print(message_to_candidate)

#Skill Drill#1
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f'{county} county has {voters:,} registered voters.')

#Skill Drill#2
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, 
               {"county":"Denver", "registered_voters": 463353}, 
               {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict['county'] + str(county_dict['registered_voters']))
    
for voting_data:
    print(f"{county} county has {registered_voters:,} registered voters.")

