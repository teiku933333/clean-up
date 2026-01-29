class KitchenEnvironment:
    def __init__(self):
        # Objects in the kitchen
        self.dirty_items = [
            "dirty plate",
            "dirty cup",
            "spoon"
        ]

    def show_state(self):
        print("Kitchen environment state:")
        print(f"Dirty items: {self.dirty_items}")
