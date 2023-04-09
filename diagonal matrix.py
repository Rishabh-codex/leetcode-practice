nums = [[1,2,3],[5,17,7],[9,11,10]]
diag=[]
count=0
prime=[]
for i in range(len(nums)):
    diag.append(nums[i][i])
    diag.append(nums[i][len(nums)-1-i])
for i in diag:
    count=0
    for x in range(1,i):
        if i%x==0:
            count+=1
    if count==1:
        prime.append(i)
 print(prime)
prime.sort()
print(prime[-1])
