def input_layer():
    """Processing the input data"""

    n, m = [int(el) for el in input().split(" ")]
    layer_1 = []
    bricks = []

    for _ in range(n):
        line = [int(el) for el in input().split(" ")]
        bricks.append(max(line))
        layer_1.append([str(el) for el in line])
    number_of_bricks = max(bricks)

    return [n, m, layer_1, number_of_bricks]


class Layer:
    """Blueprint for object Layer"""

    def __init__(self, n, m, layer_1, bricks):
        """Object initial attributes"""

        self.line = n
        self.column = m
        self.layer_initial = [el for el in layer_1]
        self.layer = [[False for _ in range(self.column)] \
                      for _ in range(self.line)]
        self.blocks = bricks
        self.count = 0
        self.database = [{str(el): {"coordinates": [], "times_occurrence": 0}} \
                         for el in range(1, self.blocks + 1)]
        self.key = ""
        self.flag_end = False
        self.flag_no_solut = False
        self.flag_end_line = False
        self.combinations = []
        self.max_chars = 0
        self.flag_valid = False

    def validation_check(self):
        """Validating the entries"""

        temp = set([len(el) for el in self.layer_initial])

        def spanning_el():
            """Checks for spanning bricks"""

            for_comparison = []
            for i in range(1, self.blocks + 1):
                for_comparison.append(sum([el.count(str(i)) for el in self.layer_initial if str(i) in el]))
            if len(set(for_comparison)) == 1 and set(for_comparison).pop() == 2:
                return True
            else:
                return False

        if self.line <= 100 \
                and self.column <= 100 \
                and self.line % 2 == 0 \
                and self.column % 2 == 0 \
                and len(temp) == 1 \
                and temp.pop() == self.column \
                and len(self.layer_initial) == self.line \
                and spanning_el():
            self.flag_valid = True
            return True
        else:
            return False

    def create(self):
        """Start building"""

        if not self.validation_check():
            return
        else:
            self.iterating()
            return

    def sorting_value_name(self, name, val):
        """Sorting the blocks at given condition"""

        first_with_val_zero = []
        for database_el in self.database:
            for el_value in database_el.values():
                if el_value[name] == val:
                    first_with_val_zero.append(database_el)
        if not first_with_val_zero:
            return [False]
        return first_with_val_zero

    def check_for_overlay(self, block_layer_1, block_layer_2, index, key):
        """Checks if the brick is satisfies the conditions of overlay"""

        if self.database[index][key]["times_occurrence"] == 2:
            coord_past = self.database[index][key]["coordinates"][0]
            coord_new = self.database[index][key]["coordinates"][1]
            block_layer_1_past = int(self.layer[coord_past[0]][coord_past[1]])
            block_layer_1_new = int(self.layer[coord_new[0]][coord_new[1]])
            block_layer_2_past = int(self.layer_initial[coord_past[0]][coord_past[1]])
            block_layer_2_new = int(self.layer_initial[coord_new[0]][coord_new[1]])
            pair_layer = (block_layer_1_past + block_layer_1_new) / 2
            pair_layer_initial = (block_layer_2_past + block_layer_2_new) / 2
            if pair_layer == int(key) \
                    and pair_layer_initial == int(self.layer_initial[block_layer_1][block_layer_2]):
                return True
            else:
                return False
        else:
            return False

    def iterating(self):
        """Iterating in the template and calling the main logic methods
        Adding the existing solution to a database"""

        for l_0, line in enumerate(self.layer):
            self.count = 0
            for c_0, column in enumerate(line):
                if l_0 % 2 == 0:
                    self.check_line_1(l_0, c_0)
                else:
                    self.check_line_2(l_0, c_0)
                if self.flag_end_line:
                    self.flag_end_line = False
                    if l_0 + 1 == len(self.layer):
                        self.combinations.append(self.layer)
                        return
                    break

    def check_line_1(self, l_0, c_0):
        """Main logic for line. Check for matches in the line. Modifying the main database"""

        while True:
            if not self.layer[l_0][c_0]:
                if not self.count == 2:
                    if not self.count == 1:
                        temp = self.sorting_value_name("times_occurrence", 0)[0]
                        if not temp:
                            self.flag_end = True
                            self.flag_no_solut = True
                            break
                        else:
                            for k in temp.keys():
                                self.key = k

                    index = self.get_index(self.key)
                    self.layer[l_0][c_0] = self.key
                    self.database[index][self.key]["times_occurrence"] += 1
                    self.database[index][self.key]["coordinates"].append([l_0, c_0])

                    if self.check_for_overlay(l_0, c_0, index, self.key):
                        self.layer[l_0][c_0] = False
                        self.database[index][self.key]["times_occurrence"] -= 1
                        self.database[index][self.key]["coordinates"].pop()
                        self.count = 0
                        continue

                    self.count += 1
                    break
                else:
                    self.count = 0
            else:
                break

    def check_row_2(self, l_0):
        """Checks for second time the logic of the even line,
        after the modification of the odd line"""

        data_keys_1_occ = self.sorting_value_name("times_occurrence", 1)[:]
        if not data_keys_1_occ[0]:
            for c_0_0 in range(self.column):
                self.check_line_1(l_0, c_0_0)
            for el in self.layer:
                if not el:
                    self.flag_end = True
                    self.flag_no_solut = True
                else:
                    self.flag_end_line = True
        else:
            return True

    def check_line_2(self, l_0, c_0):
        """Main logic for the even line. Checks for
        available matches with the odd line. Modifying the main database"""

        self.count = 0
        data_keys_1_occ = self.sorting_value_name("times_occurrence", 1)[:]
        if not self.check_row_2(l_0):
            pass
        else:
            for t, k in enumerate(data_keys_1_occ):
                for key in k.keys():
                    key_dat_k = key

                index = self.get_index(key_dat_k)

                if key_dat_k == self.layer[l_0 - 1][c_0]:
                    self.layer[l_0][c_0] = key_dat_k
                    self.database[index][key_dat_k]["times_occurrence"] += 1
                    self.database[index][key_dat_k]["coordinates"].append([l_0, c_0])

                    if self.check_for_overlay(l_0, c_0, index, key_dat_k):
                        self.layer[l_0][c_0] = False
                        self.layer[l_0 - 1][c_0] = False
                        self.layer[l_0 - 1][c_0 - 1] = False
                        index_of_line_1_previous_column = self.get_index(str(int(self.key) - 1))
                        self.database[index_of_line_1_previous_column][str(int(self.key) - 1)]["times_occurrence"] -= 1
                        self.database[index][key_dat_k]["times_occurrence"] = 0
                        self.database[index][key_dat_k]["coordinates"].pop()
                        for c_0_0 in range(self.column):
                            self.check_line_1(l_0 - 1, c_0_0)
                        for c_0_0 in range(self.column):
                            self.check_line_2(l_0, c_0_0)

                    elif c_0 == self.column - 1:
                        self.check_row_2(l_0)

    def get_index(self, key):
        """Checks the index of given param in the work database"""

        for i, el in enumerate(self.database):
            for k in el.keys():
                if k == key:
                    return i

    def __repr__(self):
        """Processing the graphical expression of
                the result"""

        if not self.flag_valid:
            return f"Not valid data"

        elif not self.flag_no_solut:
            chars_length = []
            for el in self.combinations[0]:
                for chars in el:
                    chars_length.append(len(chars))

            self.max_chars = max(chars_length) + 2
            middle_line = []
            rows = []
            columns = []
            evalu = 1

            for i, el in enumerate(self.combinations[0]):
                if i % 2 == 0:
                    middle_line.extend(el)
                    evalu -= 1
                else:
                    for n, chars in enumerate(el):
                        if n % 2 == 0:
                            middle_line.insert(n + evalu, chars)
                        else:
                            middle_line.insert(n + evalu, chars)
                        evalu += 1
                    evalu += self.column + 1
            for i in range(1, len(middle_line), 2):
                if not i % 2 == 0:
                    if not middle_line[i] == middle_line[i - 1]:
                        columns.append("-" * self.max_chars)
                    else:
                        columns.append(" " * self.max_chars)

            for el in self.combinations[0]:
                for i in range(len(el)):
                    if i == 0:
                        continue
                    elif not el[i] == el[i - 1]:
                        rows.append("*")
                    else:
                        rows.append(" ")

            row = "*"
            line = "*"
            count = 0
            result_rows = []
            result_lines = []
            for el in self.combinations[0]:
                for i, col in enumerate(el):
                    if i == len(el) - 1:
                        row += str(col).center(self.max_chars) + "*"
                    else:
                        row += str(col).center(self.max_chars) + rows[count]
                        count += 1
                result_rows.append(row)
                row = "*"
            for n in range(0, self.blocks, self.column):
                for i in range(n, n + self.column):
                    line += columns[i] + "*"
                result_lines.append(line)
                result_lines.append(f"*{''.join(['-' * self.max_chars + '*' for _ in range(self.column)])}")
                line = "*"
            result = ''
            for i in range(self.line):
                result += f"{result_rows[i]}\n" + f"{result_lines[i]}\n"
            return f"""*{''.join(['-' * self.max_chars + '*' for _ in range(self.column)])}\n{result}"""
        else:
            return f"{-1}"


layer_2 = Layer(*input_layer())
layer_2.create()
print(layer_2)