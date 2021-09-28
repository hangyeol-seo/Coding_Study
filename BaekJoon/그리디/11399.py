n=int(input())
time_list=list(map(int,input().split()))
time_list.sort()
len_time_list=len(time_list)
partial_sum=[0 for _ in range(len_time_list+1)]

for i in range(len_time_list):
    partial_sum[i+1]=time_list[i]+partial_sum[i]

print(sum(partial_sum))
