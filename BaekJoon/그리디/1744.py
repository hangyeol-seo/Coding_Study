import sys
read=sys.stdin.readline

n=int(input())
nums=[0 for _ in range(n)]
for i in range(n):
    nums[i]=int(read())

nums.sort()
negative_cnt=0
positive_cnt=0
zero_cnt=0
one_cnt=0
result=0

for i in nums:
    if i==1:
        one_cnt+=1
    elif i>0:
        positive_cnt+=1
    elif i<0:
        negative_cnt+=1
    else:
        zero_cnt+=1
for i in range(1,negative_cnt,2):
    result+=nums[i]*nums[i-1]
if negative_cnt%2!=0:
    if zero_cnt==0:
        result+=nums[negative_cnt-1]
result+=one_cnt


if positive_cnt%2!=0:
    result+=nums[negative_cnt+zero_cnt+one_cnt]
    positive_start=negative_cnt+zero_cnt+one_cnt+1
    positive_cnt-=1
else:
    positive_start=negative_cnt+zero_cnt+one_cnt

nums=nums[positive_start:]
for i in range(0,positive_cnt,2):
    result+=nums[i]*nums[i+1]

print(result)
