from environment import KitchenEnvironment


class Robot:
    def __init__(self):
        self.location = "outside"
        self.holding = None

    # ----- Movement -----
    def move_to(self, place):
        print(f"Robot moves to {place}")
        self.location = place

    # ----- Actions with validation -----
    def pick_up(self, item, env):
        if self.location != env.room:
            print("❌ Robot is not in the kitchen")
            return

        if self.holding is not None:
            print("❌ Robot is already holding something")
            return

        if not env.has_item(item):
            print(f"❌ {item} not found in kitchen")
            return

        print(f"Robot picks up {item}")
        self.holding = item
        env.remove_item(item)

    def put_down(self, place):
        if self.holding is None:
            print("❌ Robot is holding nothing")
            return

        print(f"Robot puts {self.holding} into {place}")
        self.holding = None

    # ----- Task -----
    def clean_up_kitchen(self, env):
        self.move_to("kitchen")

        for item in list(env.dirty_items):
            self.pick_up(item, env)
            self.put_down("sink")

        print("Kitchen is clean now")


# ===== RUN =====
env = KitchenEnvironment()
robot = Robot()

env.show_state()
robot.clean_up_kitchen(env)
env.show_state()
