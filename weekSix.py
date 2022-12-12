from excepter import fun, more_fun, last_fun, final_date_fun

# -> 1
try:
    first_try = ['spam', 'cheese', 'mr death']
    fun(first_try[0])
except TypeError as e:
    print(e)
    
# -> 2
try:
    not_joke = fun(first_try[2])
except SyntaxError as e:
    print(e)

# -> 3
try:
    langs = ['java', 'c', 'python']
    more_joke = more_fun(langs[3])
except IndexError as e:
    print(e)
# -> 4
try:
    last_fun(2)
except ValueError as e:
    print(e)

# -> 5
try:
    final_date_fun()
except TypeError as e:
    print(e)   
    
    