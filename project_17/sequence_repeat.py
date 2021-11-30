class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = str(sequence)
        self.number = number
        self.list_seq = []
        for n in self.sequence:
            self.list_seq.append(n)


    def __iter__(self):
        return self
    def __next__(self):

        if self.number == 0:
            raise StopIteration
        else:
            for char in self.list_seq:
                character = char
                self.list_seq.append(self.list_seq.pop(0))
                self.number -= 1
                return character



result = sequence_repeat('abc', 5)


for item in result:


    print(item, end='')
