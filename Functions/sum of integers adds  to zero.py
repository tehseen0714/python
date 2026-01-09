def sum_triplets(arr,n):
    count=0
    print("Triplets whose sum is zero:")
    for i in range (n):
        for j in range (i+1,n):
            for k in range (j+1,n):
                if arr[i]+arr[j]+arr[k]==0:
                    print(arr[i],arr[j],arr[k])
                    count+=1
    return count
n=int(input("enter number of elements:"))
arr=[]
print("enter the elements:")
for i in range(n):
    arr.append(int(input()))
result=sum_triplets(arr,n)
print("number of triplets:",result)