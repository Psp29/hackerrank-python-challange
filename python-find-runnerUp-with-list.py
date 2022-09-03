if __name__ == '__main__':
    n = int(input("Please enter total number of contestants: "))
    arr = map(int, input("Please enter scores of same: ").split())
    
    arr = list(set(arr))    # set is used to remove any redundant values.
    arr.sort()  # sorting
    try:
        print(f"Runner up score is: {arr[-2]}")  # Retrieve the second highest value.
    except:
        print("All are the Winners!")