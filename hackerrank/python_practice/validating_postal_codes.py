regex_integer_in_range = r"[1-9]{1}[0-9]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair =  r'(?=(([0][0-9][0])|([1][0-9][1])|([2][0-9][2])|([3][0-9][3])|([4][0-9][4])|([5][0-9][5])|([6][0-9][6])|([7][0-9][7])|([8][0-9][8])|([9][0-9][9])))'	# Do not delete 'r'.
#regex_alternating_repetitive_digit_pair = r"(.)(?=.\1)" #r'(\d)(?=\d\1)'


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)