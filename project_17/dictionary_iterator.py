class dictionary_iter:
    def __init__(self, dictionary:dict):
        self.dictionary = dictionary
        self.len = 0
        self.dictionary_1 = {}


    def __iter__(self):
        return self
    def __next__(self):
        if self.len == len(self.dictionary) + len(self.dictionary_1):
            self.dictionary = self.dictionary_1
            raise StopIteration
        else:
            key = None
            value = None
            self.len += 1
            for k, v in self.dictionary.items():
                key = k
                value = v
                self.dictionary_1[k] = v
                break
            del self.dictionary[key]
            return (key, value)

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
