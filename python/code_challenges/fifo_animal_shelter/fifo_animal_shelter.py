class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)


class AnimalShelter:
    """holds only dogs and cats. The shelter operates using a first-in, first-out approach."""

    def __init__(self):
        self.all_animals = []

    def enqueue(self, animal:object):
        """adds animal to the shelter. animal can be either a dog or a cat object."""
        self.all_animals.append(animal)

    def dequeue(self, pref:str)-> object:
        """returns either a dog or a cat. If pref is not "dog" or "cat" then return null."""

        if pref.lower() != 'dog' and pref.lower() != 'cat':
            return None
        for animal in self.all_animals:
            if (pref.lower() == 'dog' and isinstance(animal,Dog)) or (pref.lower() == 'cat' and isinstance(animal,Cat)):
                self.all_animals.remove(animal)
                return animal
        return 'Sorry, no such animal'

    def __str__(self):
        output = ''
        for animal in self.all_animals:
            output += str(animal.name) + ', '
        output = output[:-2]
        return output


if __name__== '__main__':
    animal_shelter = AnimalShelter()
    print(animal_shelter)
    ketty = Cat('ketty', 1)
    rex = Dog('rex',2)
    jack = Dog('jack', 3)

    animal_shelter.enqueue(ketty)
    animal_shelter.enqueue(rex)
    animal_shelter.enqueue(jack)
    print(animal_shelter)

    animal_shelter.dequeue('dog')
    print(animal_shelter)

    animal_shelter.dequeue('cat')
    print(animal_shelter)


