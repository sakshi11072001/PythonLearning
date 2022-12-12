from collections import Counter
import math
class MyStatsticalList(list):
    def __init__(self, x):
        super(MyStatsticalList,self).__init__( x )
        self.num = sum(self)
        self.length = len(self)
        self.numbers_sorted = sorted(self)
    
    def add_element(self, lis):
        print(type(lis))
        if(type(lis) == int or type(lis) == float):
            self.append(lis)
            self.length += 1
            self.num += lis
            self = self.numbers_sorted . append(lis)
            
    def mean(self):
        return self.num / self.length
    
    def median(self):
        index = self.length // 2 
        if self.length % 2:
          return self.numbers_sorted[index]
        else:
          return sum(self.numbers_sorted[index - 1:index + 1]) / 2
      
    def mode(self):
        c = Counter(self)
        return [k for k, v in c.items() if v == c.most_common(10)[0][1]]
    
    def variance(self):
        mean = self.mean()   
        deviations = [(x - mean) ** 2 for x in self]
        return sum(deviations) / self.length
    
    def stdev(self):
        mean = self.mean()   
        var = self.variance()   
        return math.sqrt(var)
    
    def range_no(self):
        sor = sorted(self)
        range_num  = sor[-1] - sor[0]
        return range_num

    
    def min_num(self):
        minimum_num = min(self)
        return minimum_num
    
    def max_num(self):
        maximum_num = max(self)
        return maximum_num
     
s1 = MyStatsticalList([1,2,3,4])
s1.add_element(0.2)
print(s1.mean())
print(s1.mode())
print(s1.median())
print(s1.variance())
print(s1.min_num())
print(s1.max_num())
print(s1.stdev())
print(s1.range_no())
