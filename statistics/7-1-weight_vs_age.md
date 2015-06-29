[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)
    import nsfg
    import numpy as np
    import thinkplot
    import pandas
    import thinkstats2
    import math
    import matplotlib.pyplot as plt
    
    #set variables
    df=nsfg.ReadFemPreg()
    sample = thinkstats2.SampleRows(df,5000)
    weight, mat_age = sample.totalwgt_lb, sample.agepreg
    
    #age to weight scatter plot
    thinkplot.Scatter( mat_age, weight)
    plt.legend(loc='best')
    plt.ylabel=('Birth Weight')
    plt.xlabel=('Maternal Age')
    plt.title('Birth Weight to Maternal Age Scatter Plot')
    plt.show()
    
    
    #Percentiles of of birth weight versus maternal age
    plt.figure()
    df=df.dropna(subset=['agepreg', 'totalwgt_lb'])
    bins=np.arange(10,60,2)
    indices = np.digitize(df.agepreg, bins)
    groups=df.groupby(indices)

    thinkplot.PrePlot(3)
    for i, group in groups:
        print(i, len(group))
        
    ages =[group.agepreg.mean() for i, group in groups]
    cdfs =[thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups]
    
    for percent in [75,50,25]:
        weights = [cdf.Percentile(percent) for cdf in cdfs]
        label='%dth' % percent
        thinkplot.Plot(ages, weights, label=label)
        plt.legend(loc='best')
        plt.xlabel=('Maternal Age')
        plt.ylabel=('Birth Weight')
        plt.title('Percentiles of Weight for Maternal Age')
        plt.show()
        
    #Pearson's Correlation
    def Corr(xs, ys):
        xs=np.asarray(xs)
        ys=np.asarray(ys)
        
        meanx, varx =thinkstats2.MeanVar(xs)
        meany, vary =thinkstats2.MeanVar(ys)
        corr=thinkstats2.Cov(xs,ys, meanx,meany)/math.sqrt(varx*vary)
        return corr
        
    p=Corr(df.agepreg, df.totalwgt_lb)
    
    print 'p = ', p
    
    #Spearman's Correlation
    
    def SpearmanCorr(xs,ys):
        xranks=pandas.Series(xs).rank()
        yranks=pandas.Series(ys).rank()
        return Corr(xranks, yranks)
    
    print "Spearman's Rank Correlation = ", SpearmanCorr(df.agepreg, df.totalwgt_lb)
    
