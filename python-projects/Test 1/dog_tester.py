from dog import Dog

with open("dogs.txt") as file:
    dogs_list = []

    for line in file:
        stripped_line=line.strip()
        tokens = stripped_line.split()
        name = tokens[0]
        trick = tokens[1]
        breed = tokens[2]
        hungry = tokens[3]

        dog = Dog(name, trick, breed, hungry)
        print(dog)
        dogs_list.append(dog)

#dog 1
    print(' ')
    print(f"Dog 1 : {dogs_list[0]}")    

    speak = dogs_list[0].speak()
    print(f"Dog says: {speak}")

    feed = dogs_list[0].feed()
    print(f"Feed: {feed}")

    trick = dogs_list[0].get_trick()
    print(f"New trick: {trick}")

    isHungry = dogs_list[0].isHungry()
    print(f"Dog is hungry: {isHungry}")

    