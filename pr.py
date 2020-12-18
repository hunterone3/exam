import datetime

def calc(date):
    l = date.split(".")

    return datetime.date(int(l[0]), int(l[1]), int(l[2])).strftime("%V")

def main(date):

    n = int(calc(date))

    
    if n%2 == 1:
        result="Week is odd"
    else:
        result="Week is even"
    return result
