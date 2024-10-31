class MyCat:
  def __init__(Object, name, age, breed):
    Object.name = name
    Object.age = age
    Object.breed = breed
  def eating(cat):
    print("My cat " + cat.name + " is eating")
  def sleeping(cat):
    print("My cat " + cat.name + " is sleeping")
  def walking(cat):
    print("My cat " + cat.name + " is walking")
  def kaput(cat):
    print("My cat " + cat.name + " is kaput...")
  def married(cat):
    print("My cat " + cat.name + " is married")
p1 = MyCat("Barsik", 5, "british")
p1.walking()
p1.eating()
p1.sleeping()
p1.married()
for i in range(0, 3):
    p1.eating()
    p1.sleeping()
p1.kaput()