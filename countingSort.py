#numbering sort

max=-1
sample=[12,23,453,12,1,23,53,123,32,53]

#find max value in sample array
for x in range (0, len(sample), 1):
    if max<sample[x]:
        max=sample[x]

#create new holder array
max+=1
holder=[0]*max

#count the frequency in the sample array & put into holder array
for x in range (0, len(sample), 1):
    holder[sample[x]]+=1

#perform arithmetic in the holder array
for x in range (1, len(holder),1):
    holder[x]=holder[x]+holder[x-1]

#create final array and sort the number given
finalArray= [0] * (len(sample)+1)
for x in range (0, len(sample),1):
    finalArray[holder[sample[x]]]+=sample[x]
    holder[sample[x]]-=1

#print result
print("Before sort: ")
print(list(sample))
print("After sort: ")
print(list(finalArray))