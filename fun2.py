import statistics
"""Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode,
calculate_range, calculate_variance, calculate_std (standard deviation)."""
def calculate_mean(a):
    n = len(a)
    sum = n * (n + 1) / 2
    mean = sum / n
    return mean
print(calculate_mean([1, 3, 5, 6]))

def calculate_median(b):
    n = len(b)
    median = n / 2
    return median
print(calculate_median([1, 3, 5, 6]))

def calculate_mode(c):
    mode = statistics.mode(c)
    return mode
print(calculate_mode([1, 2, 3, 4]))

def calculate_range(d): 
    max_list = max(d)
    min_list = min(d)
    range = max_list - min_list
    return range
print(calculate_range([1, 3, 5, 6]))

def calculate_variance(e):
    variance_list = statistics.variance(e)
    return variance_list
print(calculate_variance([1, 3, 5, 6]))

def calculate_std(f):
    std_list = statistics.stdev(f)
    return std_list
print(calculate_std([1, 3, 5, 6]))


#                  Exercises: Level 3
#Write a function called is_prime, which checks if a number is prime.

def is_prime(numb):
    if(numb <= 1):
     return False
    for i in range(2, numb):
        if (numb % i == 0):
            return True
        else:
            return False
print(is_prime(34))

#Write a function which checks if all the items of the list are of the same data type.
def is_datatype(ls):
        a = all(type(val) == type(ls[0]) for val in ls)
        return a
print(is_datatype([1, 2.2, 3]))
