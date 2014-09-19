def trace(f):
    f.indent = 0
    def g(x):
        print '|  ' * f.indent + '|--', f.__name__, x
        f.indent += 1
        value = f(x)
        print '|  ' * f.indent + '|--', 'return', repr(value)
        f.indent -= 1
        return value
    return g
fib = trace(fib)
print fib(4)
def fib(n):
	if n is 0 or n is 1:
        	return 1
    	else:
        	return fib(n-1) + fib(n-2)
