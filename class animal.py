from abc import ABC, abstractmethod

class animal:
    def move(self):
        print("All of these are animals:")

class snake(animal):
    def move(self):
        print("1. I am a snake and I can crawl.")

class human(animal):
    def move(self):
        print("2. I am a hauman and I can walk on two feet.")

class horse(animal):
    def move(self):
        print("3. I am a horse and I can walk, trot, cantor and gallop on my four feet.")

class dog(animal):
    def move(self):
        print("4. I am a dog and I can walk, jump and run on my four feet.")

a= animal()
a.move()

s= snake()
s.move()

hu= human()
hu.move()

h= horse()
h.move()

d= dog()
d.move()