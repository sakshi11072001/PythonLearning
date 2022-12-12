from collections import Counter
import math
'''Python has the module called statistics and we can use this module to do all the statistical calculations. 
However, to learn how to make function and reuse function let us try to develop a program, which calculates the
 measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). 
 In addition to those measures, find the min, max, of the sample. You can create a class 
 called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. Check the output 
 below.'''
​
class Statistics:
    
    def __init__(self,num):
       self.numbers = num
       
    def mean(self):
        return sum(self.numbers) / len(self.numbers)

    def median(self):
        index = len(self.numbers) // 2 
        if  len(self.numbers) % 2:
          return sorted(self.numbers)[index]
        else:
          return sum(sorted(self.numbers)[index - 1:index + 1]) / 2
      
    def mode(self):
        c = Counter(self.numbers)
        return [k for k, v in c.items() if v == c.most_common(10)[0][1]]

    def variance(self):
        mean = self.mean()   
        deviations = [(x - mean) ** 2 for x in self.numbers]
        return sum(deviations) / len(self.numbers)
        

    def stdev(self):
        mean = self.mean()   
        var = self.variance()   
        return math.sqrt(var)
       
    def range_no(self):
        sor = sorted(self.numbers)
        range_num  = sor[-1] + sor[1]
        return range_num

    def min_num(self):
        minimum_num = min(self.numbers)
        return minimum_num

    def max_num(self):
        maximum_num = max(self.numbers)
        return maximum_num
try:   
    s1 = Statistics([ 1, 2, 3, 4, 5])
    print(s1.mean())
    print(s1.median())
    print(s1.mode())
    print(s1.variance())
    print(s1.stdev())
    print(s1.range_no())
    print(s1.min_num())
    print(s1.max_num())
    
except Exception as e:
    print(e)
 