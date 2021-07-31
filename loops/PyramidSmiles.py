smile = "\U0001f600"
for num in range (0,10):
    print(smile * num)
    
times = 1 
while times < 11:
    print(smile * times)
    times += 1
    
for x in range(3):
    for num in range (0,10):
        print(smile * num)
        
 #without string multiplication       
for num in range (0,10):
    count = 1
    smileys = ""
    while count <= num:
        smileys += smile
        count +=1
    print(smileys)
