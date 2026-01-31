class StringReverse:
    def __init__(self, sentence):
        self.sentence = sentence

    def reverse_words(self):
        words = self.sentence.split()
        reversedwords= words[::-1]
        return " ".join(reversedwords)

text= input("Enter a sentence: ")

obj= StringReverse(text)
result= obj.reverse_words()

print("Reversed string (word by word):", result)