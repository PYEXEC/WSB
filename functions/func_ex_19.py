def master_function(a):
    def slave_function(b):
        nonlocal a
        a += 1

        return a + b

    return slave_function


function = master_function(5)
print(function(5))
