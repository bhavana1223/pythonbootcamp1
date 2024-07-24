#given an space separator integer list avg of emlemnet in the even index
my_list=list(map(int,input().split(",")))
total=0
sum=0
for i in range(0,len(my_list)):
    total+=1
    sum=sum+my_list[i]        
avg=sum/total
print(avg)