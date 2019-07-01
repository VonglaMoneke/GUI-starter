



curr_lp = 0
opp_lp = 5000
time = 106
rem = curr_lp - opp_lp
if rem <= 0:
    rem = 100


score = round((rem * (time**2)) /(opp_lp + time**2.6))
print(score)
