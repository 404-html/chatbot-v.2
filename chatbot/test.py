import re
import random
# input_string = "Free2 Quote!\n \n Protecting your family is the best investment you\'ll eve=\nr \n"
#
# output_string = ""
# array = input_string.split()
#
# print(array)
#
# for word in array:
#     output_string += re.sub(r'[\W]','', word) + " "
# print(output_string)
#
# print("."*30)
# x = re.sub(r'[\W]', ' ', input_string)
# print(x)
# sentence = "family"
# if sentence in x:
#     print("Found")
# else:
#     print("NO")
# print('.'*50)
#
#
# def simplistic_plural(word, text):
#     word_or_plural = re.escape(word) + 's?'
#     return re.match(word_or_plural, text)
#
# print(simplistic_plural("hellos", "owqeo hello siva how hello"))
GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up",)
GREETING_RESPONSES = ["'sup bro", "hey", "*nods*", "hey you get my snap?"]

sentence = "he2llo"
for word in sentence.split():
    if word.lower() in GREETING_KEYWORDS:
        print(random.choice(GREETING_RESPONSES))
