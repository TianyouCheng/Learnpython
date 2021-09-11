import glob
print(glob.glob('*.py'))

name='Runoob'
print(f'Hello {name}')
print(f'{1+2}')

# 关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符
a,b=0,1
while b<1000:
    print(b,end=',')
    a,b=b,a+b