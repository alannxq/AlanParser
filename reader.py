## writing will change the contents of a file
## using a method changes the initial list that has been parsed, which is a problem
## once the list has been updated and over-written

## TODO: write a method that re-parses the file (like __init__) and run it at the beginning
## of every method, to make sure that the parsed file (list) is current.

class file:
    def __init__(self, file):
        self.file = file
        self.primary_line_split = []
        with open(self.file, "r+") as file:
            for line in file:
                single_line_stripped_space = line.rstrip("\n")
                self.primary_line_split.append(single_line_stripped_space.split(","))

        self.final_work_list = []
        for line in self.primary_line_split:
            temp_split_one_line = []

            for statement in line:
                single_statement_split = statement.split(" = ")
                single_statement_removed_space_temp = []

                for i in single_statement_split:
                    despace_temp_word = i
                    try:
                        if despace_temp_word[-1] == " ":
                            despace_temp_word = despace_temp_word[:-1]
                        if despace_temp_word[0] == " ":
                            despace_temp_word = despace_temp_word[1:]
                    except:
                        pass
                    #print(f"i in single split statement: {i}")
                    single_statement_removed_space_temp.append(despace_temp_word)

                #print("single statement:",single_statement_removed_space_temp)
                temp_split_one_line.append(single_statement_removed_space_temp)
            self.final_work_list.append(temp_split_one_line)



    def parseFile(self):
        self.primary_line_split = []
        with open(self.file, "r+") as file:
            for line in file:
                single_line_stripped_space = line.rstrip("\n")
                self.primary_line_split.append(single_line_stripped_space.split(","))

        self.final_work_list = []
        for line in self.primary_line_split:
            temp_split_one_line = []

            for statement in line:
                single_statement_split = statement.split(" = ")
                single_statement_removed_space_temp = []

                for i in single_statement_split:
                    despace_temp_word = i
                    try:
                        if despace_temp_word[-1] == " ":
                            despace_temp_word = despace_temp_word[:-1]
                        if despace_temp_word[0] == " ":
                            despace_temp_word = despace_temp_word[1:]
                    except:
                        pass
                    #print(f"i in single split statement: {i}")
                    single_statement_removed_space_temp.append(despace_temp_word)

                #print("single statement:",single_statement_removed_space_temp)
                temp_split_one_line.append(single_statement_removed_space_temp)
            self.final_work_list.append(temp_split_one_line)

    def showRaw(self):
        self.parseFile()
        return self.final_work_list

    def lineFromValue(self, value): ## if value exists in a line, return the entire line 
        self.parseFile()
        temp_return = []
        for line in self.final_work_list:
            for single_statement in line:
                if single_statement[1] == value:
                    temp_return.append(line)

        final_return = []
        for first_bracket in temp_return:
            for second_bracket in first_bracket:
                final_return.append(second_bracket[0])
        return "null" if len(temp_return) == 0 else final_return

    def lineFromKey(self, key): ## if value exists in a line, return the entire lineForKey
        self.parseFile()
        temp_return = []
        for line in self.final_work_list:
            for single_statement in line:
                if single_statement[0] == key:
                    temp_return.append(line)

        final_return = []
        for line in temp_return:
            temp_return = []
            for statement in line:
                line = f"{statement[0]} = {statement[1]}"
                temp_return.append(line)
            final_return.append(temp_return)

        return "null" if len(temp_return) == 0 else final_return

    def keyFromValue(self, value):
        self.parseFile()
        temp_return = []
        for line in self.final_work_list:
            for single_statement in line:
                if single_statement[1] == value:
                    temp_return.append(single_statement)

        final_return = []
        for first_bracket in temp_return:
            final_return.append(first_bracket[0])
        return "null" if len(temp_return) == 0 else final_return

    def valueFromKey(self, key):
        self.parseFile()
        temp_return = []
        for line in self.final_work_list:
            for single_statement in line:
                if single_statement[0] == key:
                    temp_return.append(single_statement)

        final_return = []
        for first_bracket in temp_return:
            final_return.append(first_bracket[1]) ## for the statements matches, append the value
        return "null" if len(temp_return) == 0 else final_return

    def addEntry(self, key=None, value=None): ## i think i will have to overwrite the whole file with the final_list var 
        added_line = f"{key} = {value}"        
        
        with open(self.file, "w+") as f:
            pretty_print_in_list_return = []
            for line in self.final_work_list:
                pretty_print_line = []
                for index, statement in enumerate(line):
                    try:
                        if index != 0:
                            pretty_print_line.append(" , ")
                        pretty_print_line.append(statement[0] + " = " +statement[1])
                    except:
                        pass

                pretty_print_in_list_return.append(pretty_print_line)

            pretty_print_return = []
            for line in pretty_print_in_list_return:
                pretty_print_return.append(''.join(line))
        
            pretty_print_return.append(added_line) ## WE ADD USER KEY/VAL HERE

            f.write('\n'.join(pretty_print_return))

    def prettyPrint(self): ## returns a list that can be easily printed with '\n'.join()
        self.parseFile()
        pretty_print_in_list_return = []
        for line in self.final_work_list:
            pretty_print_line = []
            for index, statement in enumerate(line):
                try:
                    if index != 0:
                        pretty_print_line.append(" , ")
                    pretty_print_line.append(statement[0] + " = " +statement[1])
                except:
                    pass

            pretty_print_in_list_return.append(pretty_print_line)

        pretty_print_return = []
        for line in pretty_print_in_list_return:
            pretty_print_return.append(''.join(line))
        
        return pretty_print_return
