def find_duplicates(items):
    duplicates=[]
    dups=[]
    for item in items:
        if items.count(item)>1:
            dups.append(item)
    for i in dups:
        if i not in duplicates:
            duplicates.append(i)
    return duplicates        
items =  [1, 2, 3, 2, 4, 1, 5, 2]
print(find_duplicates(items))