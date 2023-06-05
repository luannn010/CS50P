def main():

    time = input('What time is this? ' )
    time = convert(time)
    meal(time)
def convert(n):

    hours,mins = n.split(':')
    hours = int(hours)
    mins = int(mins)
    mins = mins/60
    n = hours+mins
    return n
def meal(time):
    if time >= 7 and time <= 8:
        print('breakfast time')
    elif time >= 12 and time <= 13:
        print('lunch time')
    elif time >= 18 and time <= 19:
        print('dinner time')
    else:
        print(' ')

if __name__ == "__main__":
    main()