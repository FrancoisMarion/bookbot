import os
import operator


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "books", "frankenstein.txt")

    with open(file_path) as f:
        #reads the file to 1 big ass string
        file_contents = f.read()
        
        #converts the big ass string to lowercase
        file_contents_lower = file_contents.lower()

        #converts the string to a list of individual words
        word_list = file_contents_lower.split()
        # word_list = {'abc', 'bcd', 'poulet'}

        #print((word_list))
        #prints the total number of words
        print(len(word_list))

        character_count = {}

        for word in word_list:
            for character in word:
                if character.isalpha():
                    if character in character_count:
                        character_count[character] += 1
                    else:
                        character_count[character] = 1
        print(character_count)

        sorted_x = sorted(character_count.items(), key=operator.itemgetter(1), reverse=True)

        print(sorted_x)

        print("Begin report on ", file_path)
        print(str(len(word_list)) + " words found in the book!")
        for char in sorted_x:
            print("The '" + char[0] +"' character was found " + str(char[1]) + " times in the book!")
        




    

if __name__ == "__main__":
    main()


