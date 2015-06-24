[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)
><b>Problem:</b> Compare the actual vs. perceived number of children in a household.
><b>How: </b>Determine probability mass function for observed number of children.  Then create a copy of the original then multiply occurrences by value to determine perceived or biased distribution.  Plot both on graph.
><b>Solution:</b>
  
      import matplotlib.pyplot as plt
      import thinkstats2
      import thinkplot
      import chap01soln
      
      resp = chap01soln.ReadFemResp()
      
      d=resp.numkdhh
      pmf=thinkstats2.Pmf(d, label='actual')
      
      def BiasPmf(pmf, label):
          new_pmf=pmf.Copy(label=label)
          
          for x, p in pmf.Items():
              new_pmf.Mult(x,x)
              
          new_pmf.Normalize()
          return new_pmf
      
      biased_pmf = BiasPmf(pmf, label='observed')
      
      plt.figure()
      thinkplot.PrePlot(2)
      thinkplot.Pmfs([pmf,biased_pmf])
      plt.legend(loc='best')
      plt.xlabel('No. of Children')
      plt.ylabel('PMF')
      plt.title('Plot Showing Actual vs. Observed No. of Children in Household')
      plt.show()
      
      print 'actual mean', pmf.Mean()
      print 'biased mean', biased_pmf.Mean()

<b>OUTPUT</b><br>
actual mean 1.02420515504<br>
biased mean 2.40367910066<br>

![Chapter3Exercise1](https://cloud.githubusercontent.com/assets/10352130/8342633/89372bfe-1a9b-11e5-9b4a-3a7043be5de7.png)
