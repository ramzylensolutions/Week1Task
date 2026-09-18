class a():
  def animal(self):
    print("This is a animal")

class b(a):
  def animal(self):
    super().animal()
    print("I'm cat")
class c(b):
  def animal(self):
    super().animal()
    print("Im kitten")


obj = c()
obj.animal()
