if __name__ == '__main__':
    nested_list = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        nested_list.append([name,-score])

    max_v = float("-inf")
    runner_v = float("-inf")
    runner_stu = []
    max_stu = []

    for name, score in nested_list:

        if score > runner_v:
            if score > max_v:
                max_v, runner_v = score, max_v
                
                runner_stu = max_stu[:]
                max_stu = [name]

            elif score < max_v:
                runner_v = score
                runner_stu = [name]
            
            else:
                max_stu.append(name)
        elif score == runner_v:
            runner_stu.append(name)
    
    for name in sorted(runner_stu):
        print(name, end="\n")