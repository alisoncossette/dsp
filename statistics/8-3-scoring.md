# 4) Think Stats Exercise 8.3

Problem: [Think Stats Chapter 8 Exercise 3](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77)

---
import estimation
import thinkstats2
import random
import thinkplot
import matplotlib.pyplot as plt
lam =2
m=1000000

def Game(lam):
    points=0
    t=0
    while True:
        time_between_goals = random.expovariate(lam)
        t += time_between_goals
    if t > 1:      
        return points
    points += 1
    return L
    
estimates = []
for i in range(m):
    L = Game(lam)
    estimates.append(L)

print('Sports - Time to Goal')
print('rmse L', estimation.RMSE(estimates, lam))
print('mean error L', estimation.MeanError(estimates, lam))
    
pmf = thinkstats2.Pmf(estimates)
thinkplot.Hist(pmf)
plt.show()
        
---
