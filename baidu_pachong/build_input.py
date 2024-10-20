Name=[]
num=0
with open('list.txt','r') as fi:
    for line in fi:
        Name.append(line.strip())
num=0
with open('县局长.txt','r') as fil:
    for line in fil:
        Name[num]=Name[num]+line.strip()
print(Name)
count=1
count1=0
with open ('name.txt','a') as file:
    for line in file:
        if count>=387 :
         {
            file.write(Name[count1])
        }
        count=count+1
        count1=count1+1
  