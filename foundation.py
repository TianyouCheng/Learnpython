# print('hello world 你好世界')
# #字典，通过键来存取，而不是通过偏移存取
# dict={}
# dict['one']="This is one"
# dict[2]="This is two"

# tinydict={'name':'runoob','code':3745,'dept':'sales'}

# print(dict['one'])
# print(tinydict)
# print(tinydict.keys())
# print(tinydict.values())

# 求质数
i=2
while(i<100):
    j=2
    while(j<=(i/j)):
        if not(i%j):break
        j+=1
    if(j>i/j):print(str(i)+"是质数")
    i+=1
print('goodbye')