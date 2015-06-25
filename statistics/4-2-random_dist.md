[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

    import random
    import thinkplot
    import thinkstats2
    import matplotlib.pyplot as plt
    
    random_nums=[random.random() for _ in range(1000)]
    
    cdf=thinkstats2.Cdf(random_nums, label='random nums')
    pmf=thinkstats2.Pmf(random_nums)
    
    plt.figure()
    thinkplot.Cdf(cdf)
    thinkplot.Config(xlabel='random nums', ylabel='CDF')
    plt.show()
    
    plt.figure()
    thinkplot.Hist(pmf, linewidth=0.1)
    thinkplot.Config(ylabel='PMF')
    plt.show()

<b>OUTPUT</b><br>
