if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg_marks = sum(student_marks[query_name])/3.00 # calculate average marks
    print(f"{avg_marks:.2f}")   # “{:.2f}” is used to print average marks to 2 decimal places.