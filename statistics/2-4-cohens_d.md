[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)


    import nsfg
    import math as math
    
    #global variables
    
    df=nsfg.ReadFemPreg()   
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
        
        pooled_var=((n1*var1)-(n2*var2))/(n1+n2)
        d = diff / (math.sqrt(pooled_var))
        return d
        
    print "\nThe mean weight of first babies is ", firsts.totalwgt_lb.mean()
    print "The mean weight of other babies is ", others.totalwgt_lb.mean()
    
        
    print "Cohen's d for total birth weight in relation of other babies to first babies is ", CohensEffectSize(others.totalwgt_lb, firsts.totalwgt_lb)
    
    
    print "\nThe mean pregnancy length of first babies is ", firsts.prglngth.mean()
    print "The mean pregnancy length of other babies is ", others.prglngth.mean()
    
        
    print "Cohen's d for pregnancy length in relation of first babies to other babies is ", CohensEffectSize(firsts.prglngth, others.prglngth)
'''
REPLACE THIS TEXT WITH YOUR RESPONSE
