def solution():
    def integers():
        i = 1
        while True:
            yield i
            i += 1


    def halves():
        a= 5
        for i in integers():
            yield (i / 2)

    def take(n, seq):
        result = []
        for i in seq:
            result.append(i)
            n -= 1
            if n == 0:
                return result



    return (take, halves, integers)

take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
