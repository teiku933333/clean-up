class KitchenEnvironment:
    def __init__(self):
        self.room = "kitchen"
        self.dirty_items = ["dirty plate", "dirty cup", "spoon"]

    def has_item(self, item):
        return item in self.dirty_items

    def remove_item(self, item):
        if item in self.dirty_items:
            self.dirty_items.remove(item)

    def show_state(self):
        print(f"Kitchen items: {self.dirty_items}")
