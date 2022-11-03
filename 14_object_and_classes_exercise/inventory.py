class Inventory:

    def __init__(self, __capacity, items=[]):
        self.capacity = __capacity
        self.items = items
        self.left_capacity = __capacity

    def add_item(self, item):
        if self.left_capacity > 0:
            self.items.append(item)
            self.left_capacity -= 1
        return "not enough room in the inventory"

    def get_capacity(self):
        return self.capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.left_capacity}"

inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)



