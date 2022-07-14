# put your python code here
line = str(input())
n = len(line)
def price(n):
    c = n*60
    r = c//100
    k = c%100
    return print(str(r) + ' ' + 'р.'+ ' ' + str(k) + ' ' +'коп.')
price(n)
