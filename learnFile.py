# fo=open('package_runoob/foo.txt','w')
# fo.write('hello')
# fo.close()

fo=open('package_runoob/runoob1.py','r+')
str=fo.read(20)
print(str)
# 查找当前位置
position=fo.tell()
print(position)
# 把指针移到文件开头
position=fo.seek(0,0)
# seek()第一个参数指定偏移量，第二个参数是偏移的初始位置
# 被设为0，这意味着将文件的开头作为移动字节的参考位置。
# 如果设为1，则使用当前的位置作为参考位置。如果它被设为2，那么该文件的末尾将作为参考位置。
str=fo.read(10)
print(str)

# 读取所有行，包括换行符，返回列表
position=fo.seek(0,0)
str=fo.readlines()
print(str)

fo.close()