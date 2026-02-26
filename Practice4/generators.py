def m(args):
    for x in args:
        yield x*x
a = [1,2,3,4,5]
a = m(a)
print(type(a))
for x in a: 
    print(x,end=" ")
def large_sequence(n):
  for i in range(1,n+1):
    yield i

# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print()
print(next(gen)) # it will just simple stop BUT not exiting the function and wait for next action
print(next(gen))
print(next(gen))
def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"

gen = simple_gen()
print(next(gen)) # it activates function and pause it once yield is activated
print(next(gen))
print(next(gen))
# print(next(gen)) it will make StopIteration cause the function is executed fully and no next yield conditions
# so to make it work again we have to call our function again 
gen = simple_gen()
print(next(gen)) 
print(next(gen))
# we have one more step function is not executed fully
gen = simple_gen() # it will start function again from the beggining so the progress is restarted
print(next(gen))
def echo_generator():
  while True:
    received = yield
    print("Received:", received)

gen = echo_generator()
next(gen) # Prime the generator
gen.send("Hello") # The send() method allows you to send a value to the generator
gen.send("World")
gen.send(1293)