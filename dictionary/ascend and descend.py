d={1:30,2:20,3:10}
ascend=dict(sorted(d.items(),key=lambda x:x[1]))
print("ascending:",ascend)

descend=dict(sorted(d.items(),key=lambda x:x[1],reverse=True))
print("descending:",descend)
