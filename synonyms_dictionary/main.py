class Dictionary:
    def __init__(self):
        self.__all_entries = []

    def get_all_entries(self):
        return self.__all_entries
    
    def find_entry(self, word):
        for entry in self.__all_entries:
            if word in entry:
                return entry
        return []
    
    def add_entry(self, entry: list):
        try:
            self.__all_entries.append(entry)
            return True
        except:
            return False

    def add_to_entry(self, word, new_words):
        for line in self.__all_entries:
            if word in line:
                line = line.extend(new_words)
                return True
        return False

    def remove_entry(self, word):
        index = -1
        for entry_index in range(len(self.__all_entries)):
            if word == self.__all_entries[entry_index][0]:
                index = entry_index
        if index >= 0:
            self.__all_entries.pop(index)
            return True
        return False


class FileHandler:
    def __init__(self, filename):
        if filename == "":
            self.__filename = "en.csv"
        else:
            self.__filename = filename + ".csv"
        

    def load_file(self):
        storage = []
        try:
            with open(self.__filename) as f:
                for line in f:
                    parts = line.strip().split(";")
                    storage.append(parts)
        except:
            open(self.__filename, "w").close()
        # print(storage)
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
add new <syn1,syn2,...,synN> -- add new dictionary entry
add to <word> <syn1,syn2,...,synN> -- add one or more synonyms to <word>
del entry <word> -- delete the whole line which starts with <word>
help -- see commands menu
exit -- close the program""")

    def stop_app(self):
        all_entries = self.__dictionary.get_all_entries()
        self.__filehandler.save_file(all_entries)
        exit()

    def find_synonyms(self, word):
        found = self.__dictionary.find_entry(word)
        final_str = ""
        if found == []:
            print("This word is not in dictionary. Type 'add <word1, word2, wordN>' to add new dictionary entry. Type 'help' to see more commands")
        if len(found) == 1:
            print(f"{found[0]} has no synonyms yet. To add a synonym type add syn <word>")
        else:
            print(", ".join(found))
    
    def add_synonyms(self, word, syns: list):
        syns = [i.strip() for i in syns]
        return self.__dictionary.add_to_entry(word, syns)

    def add_new_entry(self, syns: list):
        syns = [i.strip() for i in syns]
        return self.__dictionary.add_entry(syns)

    def delete_entry(self, word):
        return self.__dictionary.remove_entry(word.strip())
    
    def execute(self):
        self.help()
        while True:
            command = input(">>> ")
            if command == "exit":
                self.stop_app()

            elif command == "help":
                self.help()
            
            elif " " in command:
                words = command.split(" ")
                if "add to" in command and len(words) == 4:
                    word_to_find = words[2]
                    syns = words[3].split(",")
                    added = self.add_synonyms(word_to_find, syns)
                    if not added:
                        print(f"{word_to_find} is not found.")

                elif "add new" in command and len(words) == 3:
                    added = self.add_new_entry(words[2].split(","))
                    if added:
                        print(f"\nnew synonyms added\n")
                    else:
                        print("\nSomething went wrong, try again")

                elif "del entry" in command and len(words) == 3:
                    deleted = self.delete_entry(words[2])
                    if deleted:
                        print("\nEntry deleted.")
                    else:
                        print("\nSomething went wrong, try again.")

                else:
                    print("Command not found, type 'help' to see all commands")
            
            else:
                self.find_synonyms(command)

MainApp()