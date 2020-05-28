# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
from collections import Counter

def central_tendency_measures(*args):
    obs = args[0]

    total_obs = len(obs)
    mean = sum(obs)/total_obs

    obs = sorted(obs)
    mid_point = int(total_obs // 2)

    if (total_obs % 2 == 0):
        median = (obs[mid_point] + obs[mid_point-1])/2
    else:
        median = obs[mid_point-1]

    
    count = Counter(obs)
    mode = max(count, key=count.get)
    
    return mean, median, mode

if __name__ == "__main__":
    
    lines = iter(sys.stdin)
    total_obs = int(next(lines))
    
    obs = map(int, next(lines).split())

    mean, median, mode = central_tendency_measures(list(obs))

    sys.stdout.write("{:.1f}\n{:.1f}\n{:.1f}".format(mean, median, mode))
