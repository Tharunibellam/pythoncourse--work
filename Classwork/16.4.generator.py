#Generators in Python
# A generator is a special type of iterator that allows you to iterate over a sequence of values without storing them all in memory at once.
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
#condition statement
for num in count_up_to(5):
    print(num)
#output:
'''
1
2
3
4
5
'''
def show_feed(l):
    for i in l:
        start,end=i.split('..')
        yield start,end
        yield i
