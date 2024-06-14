class Example:
    def sub_sets(self, sset):
        return self.subsets_recur([], sorted(sset))

    def subsets_recur(self, current, sset):
        if sset:
            return self.subsets_recur(current, sset[1:]) + self.subsets_recur(current + [sset[0]], sset[1:])
        return [current]


print(Example().sub_sets([4, 5, 6]))
