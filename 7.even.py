# your given with a comma separeted natural number 1 to 10 print even numb
#list=list(map(int,input().split(",")))
#for i in range(1,len(list),2):
 #       print(list[i])
7.#how many even numbers are in the above question
list=list(map(int,input().split(",")))
count=0
for i in range(1,len(list),2):
    count+=1
print(count)