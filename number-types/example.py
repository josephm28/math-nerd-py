from number_type import NumberType


def main():
    # for x in range(0, 100):
    #     test = NumberType(x)
    #     if(test.type == "Prime"):
    #         print(x)
    #     # else:
    #     #     test.show_rundown()
    find_by_type(0, 100, "Prime")
    find_by_type(0, 100, "Perfect")
    find_by_type(0, 100, "Abundant")
    find_by_type(0, 100, "Deficient")
    find_perfects(0, 10000)


def find_by_type(start, end, which):
    by_type = []
    for x in range(start, end):
        test = NumberType(x)
        if which == "Prime" and test.is_prime:
            by_type.append(x)
        if(test.type == which):
            by_type.append(x)
    print("Looking at", which, "from", start, "to", end, ":", by_type)


def find_perfects(start, end):
    for x in range(start, end):
        test = NumberType(x)
        if(test.type == "Perfect"):
            test.show_rundown()


if __name__ == "__main__":
    main()
