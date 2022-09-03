if __name__ == '__main__':
    names = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)
    min_score = min([i for i in scores if i > min(scores)])
    second_lowest = [j for j in range(len(scores)) if scores[j] == min_score]
    answer = sorted([names[k] for k in second_lowest])
    for k in answer:
        print(k)