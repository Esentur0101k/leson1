



########################## полиморфизм ######################


class Animal:
    def make_sound(self):
        raise NotImplemented("Subclass must implement methot")

class Dog (Animal):
    def make_sound(self):
        return  'Bark'

class Cat (Animal):
    def make_sond(self):
        return 'meow'

class Cow (Animal):
    def make_sound(self):
        return'moo'

#################### функция работы полиморфизмом ##################


def animal_sound(animal:Animal):
    print(animal.make_sound())


dog = Dog()
cat = Cat()
cow = Cow()


animal_sound(dog )
animal_sound(cow )
