# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

def median(*args):

    obs = args[0]
    n_obs = len(obs)

    mid_point = int(n_obs//2)

    if n_obs % 2 == 0:

        result = (obs[mid_point] + obs[mid_point-1]) / 2
    
    else:
        result = obs[mid_point]
    
    return result

def quartiles(*args):

    obs = args[0]
    n_obs = len(obs)
    obs = sorted(obs)
    mid_point = int(n_obs//2)

    if n_obs % 2 == 0:
        l_obs = obs[:mid_point]
        u_obs = obs[mid_point:]
    else:
        l_obs = obs[:mid_point]
        u_obs = obs[mid_point+1:]
    
    return median(l_obs), median(obs), median(u_obs)

if __name__ == "__main__":
    
    lines = iter(sys.stdin)
    total_obs = int(next(lines))
    
    obs = map(int, next(lines).split())

    q1, q2, q3 = quartiles(list(obs))

    sys.stdout.write("{:.0f}\n{:.0f}\n{:.0f}".format(q1, q2, q3))