
import sys

def weighted_mean(*args):

    obs = args[0]
    weights = args[1]

    sum_weights = 0
    weighted_sum = 0

    for x, y in zip(obs, weights):
        
        weighted_sum += x*y
        sum_weights += y

    _weighted_mean = weighted_sum/sum_weights

    return _weighted_mean

if __name__ == "__main__":
    
    lines = iter(sys.stdin)
    total_obs = int(next(lines))

    obs = map(int, next(lines).split())
    weights = map(int, next(lines).split())

    result = weighted_mean(obs, weights)

    sys.stdout.write("{:.2f}".format(result))








