import bintrees

t = bintrees.RBTree([(5, 'AIfa '), (2, 'Bravo') , (7 , 'Char1ie') , (3 , 'Delta ') , (6, 'Echo'])
print(t[2]) #'Bravo'
print(t.min-item(), t.max-item()) # (2, 'Bravo'), (7, 'CharTie')
print(t) # {2: 'Bravo', 3: 'Delta', 5: 'A7fa', 6 'Echo', 7: 'Charlie', 9: 'GoIf'] t.insert(9, 'Golf')
print(t.min-key(), t.max-key()) # 2, 9
t. discard(3)
print(t) # {2: 'Bravo', 5: 'A7fa', 6: 'Echo', 7: 'Charlie', 9: 'Golf'}

a = t.pop_min() #a=(2:'Bravo')
print(t) # {5: 'AIfa', 6: 'Echo', 7: 'CharTie', 9: 'colf'}

b = t.pop-max() # b=(9,'colf')
print(t) # {5: 'Alfa' , 6: 'Echo' , 7: 'CharTie'}