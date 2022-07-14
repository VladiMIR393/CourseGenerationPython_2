# put your python code here
m = float(input())
h = float(input())
def IMT(m,h):
    imt = m/(h*h)
    if imt < 18.5:
        return "Недостаточная масса"
    elif imt > 25.0:
        return "Избыточная масса"
    else:
        return "Оптимальная масса"
print(IMT(m,h))

