class Pizza:
    def __init__(self, size, cheese=False, pepperoni=False, mushrooms=False, onions=False, bacon=False):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.mushrooms = mushrooms
        self.onions = onions
        self.bacon = bacon

    def __str__(self):
        ingredients = []
        if self.cheese:
            ingredients.append("cheese")
        if self.pepperoni:
            ingredients.append("pepperoni")
        if self.mushrooms:
            ingredients.append("mushrooms")
        if self.onions:
            ingredients.append("onions")
        if self.bacon:
            ingredients.append("bacon")
        return f"Pizza(size={self.size}, ingredients={', '.join(ingredients)})"

class PizzaBuilder:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False
        self.bacon = False

    def set_size(self, size):
        self.size = size
        return self

    def add_cheese(self):
        self.cheese = True
        return self

    def add_pepperoni(self):
        self.pepperoni = True
        return self

    def add_mushrooms(self):
        self.mushrooms = True
        return self

    def add_onions(self):
        self.onions = True
        return self

    def add_bacon(self):
        self.bacon = True
        return self

    def build(self):
        return Pizza(self.size, self.cheese, self.pepperoni, self.mushrooms, self.onions, self.bacon)

class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    def make_pizza(self):
        self.builder.set_size("large")
        self.builder.add_cheese()
        self.builder.add_pepperoni()
        self.builder.add_mushrooms()
        return self.builder.build()

if __name__ == "__main__":
    builder = PizzaBuilder()
    director = PizzaDirector(builder)
    pizza = director.make_pizza()
    print(pizza)