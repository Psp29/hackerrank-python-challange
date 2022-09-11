def minion_game(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    n = len(string)
    kevin = sum([n-i for i in range(n) if string[i] in vowels])
    total = n*(n+1)/2
    stuart = total - kevin
    
    if kevin == stuart:
        print("Draw")
    elif kevin > stuart:
        print(f"Kevin {int(kevin)}")
    else:
        print(f"Stuart {int(stuart)}")

if __name__ == '__main__':
    s = input()
    minion_game(s)