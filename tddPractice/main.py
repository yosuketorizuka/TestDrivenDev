from money import Dollar

def main():

    five = Dollar.Dollar(5)
    product = five.times(2)
    print(product.amount)

if __name__ == '__main__':

    main()

    