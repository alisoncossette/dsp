[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

The problem was to determine if first babies are lighter or heavier on average than other babies.  Then to calculate Cohen's d to compare the two groups.   Then we were to calculate the differnce in pregnancy lengths.
>1.  First babies are heavier by .13 lbs., with a Cohen's D of .089%
>2.  First babies are born about .1 weeks later (about 1/2 day), with a Cohen's d of -.029%
>
> To solve the problem, I had to establish first live births.  Then first babies are defined as live births with a pregnancy order of 1, and all other live births become others.  I then used these firsts & others distinctions to calculate and print the mean.  These same distinctions were used to feed the Cohen's d function with the totalwgt__lbs variable.  For the subsequent question, I just changed the arguments being fed to the function to represent pregnancy length instead.<br>
><i>* NOTE:  I had to adjust the order of the arguments so that the pooled_var was a positive number (you see that the formula takes the sqrt of pooled_var and if it is negative it throws a math error</i>
    
    import nsfg
    import math as math
    
    #global variables
    
    preg = nsfg.ReadFemPreg()
    
    live = preg[preg.outcome == 1]
    firsts = live[live.birthord == 1]
    others = live[live.birthord != 1]
    
    def CohensEffectSize(group1, group2):
        #calculates the pooled standard deviation
        diff=group1.mean() - group2.mean()
        var1=group1.var()
        var2=group2.var()
        n1, n2=len(group1), len(group2)
        
        pooled_var=((n1 * var1) + ( n2 * var2))/(n1+n2)
        d = diff / (math.sqrt(pooled_var))
        return d
        
    print "\nThe mean weight of first babies is ", firsts.totalwgt_lb.mean()
    print "The mean weight of other babies is ", others.totalwgt_lb.mean()
    
        
    print "Cohen's d for total birth weight in relation of other babies to first babies is ", CohensEffectSize(others.totalwgt_lb, firsts.totalwgt_lb)
    
    
    print "\nThe mean pregnancy length of first babies is ", firsts.prglngth.mean()
    print "The mean pregnancy length of other babies is ", others.prglngth.mean()
    
        
    print "Cohen's d for pregnancy length in relation of first babies to other babies is ", CohensEffectSize(firsts.prglngth, others.prglngth)
'''
<table><tr><td><b>OUTPUT</b></td></tr>

<tr><td>The mean weight of first babies is  7.20109443044<br>
The mean weight of other babies is  7.32585561497<br>
Cohen's d for total birth weight in relation of other babies to first babies is  0.691</tr></td>
<tr><td>The mean pregnancy length of first babies is  38.6009517335<br>
The mean pregnancy length of other babies is  38.5229144667<br>
Cohen's d for pregnancy length in relation of first babies to other babies is  -.0289</tr></td></table>

