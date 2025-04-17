         ###### MID LIBS GAME ###########
def mad_libs():
    print("\nLet's play Mad Libs! Fill in the blanks (like a noun, adjective, verb, etc.)")

    name = input("Give me a name: ")
    place = input("Give me a place: ")
    funny_adj = input("Give me a funny adjective: ")
    random_object = input("Give me a random object: ")
    animal = input("Give me an animal: ")
    action_verb = input("Give me an action verb: ")
    funny_exclamation = input("Give me a funny exclamation: ")

    story = f'''
One sunny day, {name} went to {place} to find the legendary {funny_adj} {random_object}.
While walking through the jungle, {name} suddenly saw a giant {animal} blocking the path.
Without thinking, {name} decided to {action_verb} as fast as possible.
"{funny_exclamation}!" they shouted, narrowly escaping with their life!

What an adventure!
'''

    print("\nHere is your Mad Libs story:")
    print(story)

if __name__ == '__main__':
    mad_libs()
