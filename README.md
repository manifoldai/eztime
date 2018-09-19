# eztime
A timer that easily integrates with functions and code chunks

Current version == 0.0.1

# Easily integrates into your code


## Decorate your functions
```
@time_func
def foo(barx, bary=3):
    return barx * bary
    
foo(3, bary=3)
```

## Call it as a wrapper around your functions
```
def foo(barx, bary=3):
    return barx * bary
    
time_func(foo)(3, bary=3)
```

## Write any code chunk using with:
```
with time_chunk('My timed hello world'):
    print('Hello World')
```