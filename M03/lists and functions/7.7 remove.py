things = ["mozzarella", "cinderella ", "salmonella "]
for i in range(len(things)):
    if things[i] == 'mozzarella':
        things[i] = things[i].upper()
    if things[i] == 'cinderella': 
        things[i] = things[i].capitalize()    
    if things[i] == 'salmonella': 
        things.remove(things[i])
print(things)
