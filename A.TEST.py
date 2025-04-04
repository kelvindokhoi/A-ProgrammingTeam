
def debug_wrapper(func):
    def wrapper(*args, **kwargs):
        print(f"Entering {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Exiting {func.__name__} with result: {result}")
        return result
    return wrapper

@debug_wrapper
def compute_pi(pattern):
    """
    Computes the failure function (π table) for the KMP algorithm.
    π[i] = length of the longest prefix that is also a suffix for pattern[0..i]
    """
    m = len(pattern)
    pi = [0] * m
    j = 0  # length of the previous longest prefix suffix

    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]  # fallback

        if pattern[i] == pattern[j]:
            j += 1
        pi[i] = j

    return pi

compute_pi('barbarbarbar')