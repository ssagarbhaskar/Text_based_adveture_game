# Adventure_game------------------

# first step is to define the locations we have for all the specific numbers

locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are on top of a hill",
             3: "You are in a building",
             4: "You are in a valley beside a stream",
             5: "You are in a forest"}


# second step is to make a list in of possible exits at a specific location

exits = {0: {"Q": 0},
         1: {"N": 5, "S": 4, "E": 3, "W": 2, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 2, "Q": 0},
         4: {"N": 5, "W": 2, "Q": 0},
         5: {"S": 4, "W": 2, "Q": 0}}


# THIRD is to give the user option either to enter letter or a word
voc = {"QUIT": "Q",
       "NORTH": "N",
       "SOUTH": "S",
       "EAST": "E",
       "WEST": "W"}


# When the player starts the game they will be at location 1

loc = 1

while True:
    available_exits = ", ".join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exits are {} \n".format(available_exits)).upper()

    if len(direction) > 1:
        words = direction.split()
        for word in words:
            if word in voc:
                direction = voc[word]
                break

    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")
