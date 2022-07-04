class Dictionary:
    def __init__(self):
        self.__all_entries = []

    def get_all_entries(self):
        return self.__all_entries
    
    def find_entry(self, word):
        for entry in self.__all_entries:
            if word in entry:
                print(self.__all_entries)
                print(entry)
                return entry
        return []
    
    def add_entry(self, line):
        line_split = line.strip().split(",")
        new_entry = []
        for word in line_split:
            new_entry.append(word.strip())
        self.__all_entries.append(line.split(','))

    def add_to_entry(self, word, synonyms: str):
        for line in self.__all_entries:
            if word in line:
                line = line.extend(synonyms.split(","))
                return True
        return False

class FileHandler:
    def __init__(self, filename):
        if filename == "":
            self.__filename = "en.txt"
        else:
            self.__filename = filename + ".txt"
        

    def load_file(self):
        storage = []
        try:
            with open(self.__filename) as f:
                for line in f:
                    parts = line.strip().split(";")
                    storage.append(parts)
        except:
            with open(self.__filename, "w") as f:
                pass
        print(storage)
        return storage
    
    def save_file(self, storage_list):
        with open(self.__filename, "w") as f:
            for item in storage_list:
                file_entry = ";".join(item)
                f.write(f"{file_entry}\n")


class MainApp:
    def __init__(self):
        print("\n\tWelcome to sysnonyms dictionary!")
        filename = input("Press enter to load the default dictionary\n\t\t or\n\
Input the name of your dictionary (new or existing) without extension: ")
        self.__filehandler = FileHandler(filename)
        self.__dictionary = Dictionary()
        self.load()
        self.execute()

             
    def load(self):
        all_entries_list = self.__filehandler.load_file()
        for line in all_entries_list:
            self.__dictionary.add_entry(line)
        print("\tThe dictionary has been loaded.")

    def help(self):
        print("""
<your word> -- see synonyms
add <syn1,syn2,...,synN> -- add new dictionary entry
add syn <word> <syn1,syn2,...,synN> -- add one or more synonyms to <word>
del <word> -- delete a word, the line will be reduced
del line <word> -- delete the whole line which starts with <word>
help -- see commands menu
exit -- close the program""")

    def stop_app(self):
        all_entries = self.__dictionary.get_all_entries()
        self.__filehandler.save_file(all_entries)
        exit()

    def find_synonyms(self, word):
        found = self.__dictionary.find_entry(word)
        if found == []:
            print("This word is not in dictionary. Type 'add <word1, word2, wordN>' to add new dictionary entry. Type 'help' to see more commands")
        if len(found) == 1:
            print(f"{found[0]} has no synonyms yet. To add a synonym type add syn <word>")
        else:
            for i in found:
                print(f"{i}, ", end="")
            print()
    
    def add_synonyms(self, word, syns: str):
        added = self.__dictionary.add_to_entry(word, syns)
        if not added:
            print(f"{word} is not found")
    
    def add_dict_entry(self, words_list):
        added = self.__dictionary.add_entry("".join(words_list))
        print(f"\nnew synonyms added\n")
        return added
    
    def execute(self):
        self.help()
        while True:
            command = input(">>> ")
            if command == "exit":
                self.stop_app()

            elif command == "help":
                self.help()

            elif "add syn" in command and len(command.split(" ")) == 4:
                word_to_find = command.split(" ")[2]
                syns_str = command.split(" ")[3]
                self.add_synonyms(word_to_find, syns_str)

            elif "add" in command and len(command.split(" ")) == 2:
                self.add_dict_entry(command.split(" ")[1])

            else:
                if " " in command:
                    print("Command not found, type 'help' to see all commands")
                else:
                    self.find_synonyms(command)

MainApp()