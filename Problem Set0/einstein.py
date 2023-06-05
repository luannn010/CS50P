def main():
    calculation()

def calculation():
    #call mass and convert to integer
    m = int(input("m: "))
    #call square of C
    sqr_c = pow(300000000,2)
    #calculation
    e = m*sqr_c
    #print out result
    print("E: "+ str(e))
    return
main()



