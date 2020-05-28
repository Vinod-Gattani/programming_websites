# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def iqr(*args):
    obs = args[0]
    weights = args[1]

    sum_weights = 0
    data = []

    for x, y in zip(obs, weights):
        data.append((x,y))
        sum_weights += y

    data = sorted(data, key = lambda x: x[0])
    
    q1_point = int(sum_weights//4)
    q3_point = int(sum_weights*3//4)
    q1 = None
    q3 = None

    cum_sum = 0
    for index, (x, y) in enumerate(data):
        cum_sum += y

        if cum_sum > q1_point and q1 is None:
            q1 = x
        elif cum_sum == q1_point and q1 is None:
            if sum_weights - cum_sum < 0.75*sum_weights:
                q1 = x
            else:
                q1 = (x + data[index+1][0])/2

        if cum_sum > q3_point and q3 is None:
            q3 = x
            break
        elif cum_sum == q3_point and q3 is None:
            if sum_weights-cum_sum > 0.25*sum_weights:
                q3 = data[index+1][0]
            else:
                q3 = (x + data[index+1][0])/2
            break
        
    result = q3 - q1

    return result

if __name__ == "__main__":
    
    lines = iter(sys.stdin)
    total_obs = int(next(lines))
    obs = map(int, next(lines).split())
    weights = map(int, next(lines).split())

    result = iqr(obs, weights)

    sys.stdout.write("{:.1f}".format(result))
        