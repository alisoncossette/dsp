[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)
><b>Problem: </b>Determine what perecentage of men are between 5'10" and 6'1".<br> 
><b>How: </b>Calculate the percentage of men that are 5'10 or shorter and the percentage of men that are 6.1" or shorter, then calculate the difference.<br>
><b>Solution </b><br>

    import scipy.stats

    #set CDF formula
    def EvalNormalCdf(x, mu, sigma):
        return scipy.stats.norm.cdf(x, loc=mu, scale=sigma)
    
    #determine CDF at short end   
    short_cdf=EvalNormalCdf(178,178,7.7)
    print "{:.3}%".format(short_cdf*100), "of men are up to 5'10."
    
    #determine CDF at tall end
    tall_cdf=EvalNormalCdf(185,178,7.7)
    print "{:.3}%".format(tall_cdf*100), " of men are are up to 6'1."
    
    #tall - short = %range
    bluemen=(tall_cdf - short_cdf)*100
    print "{:.3}%".format(bluemen), "of men are between 5'10 and 6'1 and therefore 'Blueman' eligible."
<b> OUTPUT</b></br>
>50.0% of men are up to 5'10.<br>
>81.8%  of men are are up to 6'1.<br>
>31.8% of men are between 5'10'' and 6'1'' and therefore 'Blueman' eligible.
