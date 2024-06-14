class Calculator:
    def pow(self, x, n):
        if x == 0 or x == 1 or n == 1:
            return x

        if x == -1:
            if n % 2 == 0:
                return 0
            else:
                return -1
        elif n == 0:
            return 0
        if n < 0:
            return 1 / self.pow(x, -n)
        val = self.pow(x, n // 2)
        if n % 2 == 0:
            return val * val
        return val * val * x


print(Calculator().pow(2, -3))
print(Calculator().pow(3, 5))
