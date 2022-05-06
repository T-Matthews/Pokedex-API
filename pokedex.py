
import requests as r
import random


#Pretty Print! Enable the next couple lines, and adjust the print output 
# to print the output more legibly. Unfortunately, it also arranges dictionaries 
# alphabetically by key, so the first key value pair is abilities instead of 
# pokemon name, which annoys the heck out of me. 
# Enable these and adjust print statement at end of code if you dont care about this.
#---------------------------------------------------------------------
# import pprint
# pp = pprint.PrettyPrinter(depth=4)
#---------------------------------------------------------------------

"""
This section of code takes a random 20 pokemon from the pokemon API using their
index number. This number corresponds to a temporary variable name, used to
assign "Name", "Abilities", "Types", and "Weight". Accounts for multiple types
and abilities.

"""
def pokedex(pokelist):
    user_pokedex = []
    
    for i in pokelist:
        i=r.get(f'https://pokeapi.co/api/v2/pokemon/{i}/')
        if i.status_code != 200:
            print(f'Something went wrong, you ar getting a {i.status_code} '
                    +'error.')
        else:
            i_dict = i.json()

            i = {}
            i['Name'] = i_dict['name']
            i['Abilities']=[]
            i['Types'] = []
            for v in i_dict['abilities']: i['Abilities'].append(v['ability']['name'])
            for v in i_dict['types']: i['Types'].append(v['type']['name'])
            i['Weight']= i_dict['weight']
            user_pokedex.append(i)

    return(user_pokedex)
  
#While there are 908 pokemon, the Pokemon API only has 898 included. That range
#is reflected here, choosing 20 pokemon at random from those 898.
full_pokedex = pokedex(random.randrange(1,898,1) for i in range(20))
print(full_pokedex)

print('\n\n\n---------------------------------------------------------\n\n\n')
"""
This section takes the list of pokemon generated above, and filters it into a 
separate dictionary. The types from each pokemon are added to one list, converted
to a set and back to eliminate duplicates. These are added to a dictionary, and 
then the dictionary keys and the pokemon list are looped through using a double 
for loop to move any pokemon with that type into the type-cooresponding dictionary
value.

"""


def sort_by_type(user_dex):
    type_list = []
    sorted_dict = {}
    my_type = [i['Types'] for i in user_dex]
    for i in my_type:
        type_list += i
    type_list = list(set(type_list))
    type_list.sort()
    for i in type_list:
        sorted_dict[i]=[]
        for j in user_dex:
            if i in j['Types']:
                sorted_dict[i]=(j)
        

    return sorted_dict




print(sort_by_type(full_pokedex))
# pp.pprint(sort_by_type(test))

# #Explained above, but the prettyprint looks nicer but alters the ordering of 
#the dictionary key value pairs, so i have it turned off. Enable if you care
#to do so.
