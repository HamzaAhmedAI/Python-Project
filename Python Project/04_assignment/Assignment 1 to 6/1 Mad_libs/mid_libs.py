# #  String concatenation (aka how to put strings together)
# # Suppose we want to create a string that says "Subscribe to ______"
# Youtuber = "Ozzy Gaming" # some string variable

# # a few way to do this
# print("Subscribe to " + Youtuber)
# print("Subcribe to {}".format(Youtuber))
# print(f"Subscribe to {Youtuber}")

adj = input("Addjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

maflib = f"Computer programmming is so {adj}! it makes me so excited all the times because\
    I love to {verb1}. stay hydrated and {verb2} liks you are {famous_person}"

print(maflib)