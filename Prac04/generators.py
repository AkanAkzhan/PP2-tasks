#1
def large_sequence(n):
  for i in range(n):
    yield i

# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

#2
def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))

#3
def simple_gen():
    yield 1
    yield 2

gen = simple_gen()
print(next(gen))
print(next(gen))
#print(next(gen)) # This will raise StopIteration

#4
#List comprehension - creates a list
list_comp = [x * x for x in range(5)]
print(list_comp)

#Generator expression - creates a generator 
gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))

#5
# Calculate sum of squares without creating a list
total = sum(x * x for x in range(10))
print(total)

#6
def fib():
    a , b = 0 , 1
    while True:
        yield a
        a,b=b,a+b

gen = fib()
    for _ in range(100):
        print(next(gen))

#7
def echo_generator():
  while True:
    received = yield
    print("Received:", received)

gen = echo_generator()
next(gen) # Prime the generator
gen.send("Hello")
gen.send("World")

#8
def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("Generator closed")

gen = my_gen()
print(next(gen))
gen.close()