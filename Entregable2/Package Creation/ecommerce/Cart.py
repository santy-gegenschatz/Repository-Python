class Cart():
    def __init__(self):
        self.items = []
        self.total = 0
        self.total_items = 0

    def add(self, item):
        self.items.append(item)
        self.total += item.price
        self.total_items += 1

    def remove(self, item):
        self.items.remove(item)
        self.total -= item.price
        self.total_items -= 1

    def __str__(self):
        return f'Items: {self.items} Total: {self.total} Total Items: {self.total_items}'