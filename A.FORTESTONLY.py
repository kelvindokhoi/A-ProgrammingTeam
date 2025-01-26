import timeit

# Benchmark for a.append(2)
def test_append():
    a = []
    for i in range(10):
        a.append([2])
    print(a)

# Benchmark for a += [2]
def test_inplace_add():
    a = []
    a += [2]*10
    print(a)

# Measure time
append_time = timeit.timeit(test_append, number=1000)
inplace_add_time = timeit.timeit(test_inplace_add, number=1000)

print(f"a.append(2): {append_time:.6f} seconds")
print(f"a += [2]: {inplace_add_time:.6f} seconds")