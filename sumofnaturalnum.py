num=142
sum=0
while(num>0):
    count = num%10
    sum += count
    num //= 10
print(sum)