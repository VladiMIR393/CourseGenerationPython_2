# put your python code here
num = input()
if len(num) == 6:
    print(int(num[0]+num[:-6:-1]))
else:
    print(int(num[::-1]))