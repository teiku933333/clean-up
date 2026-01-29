from environment import KitchenEnvironment


class Robot:
    def __init__(self):
        self.location = "outside"
        self.holding = None

    # ----- Basic actions -----
    def move_to(self, place):
        print(f"Robot moves to {place}")
        self.location = place

    def pick_up(self, item):
        print(f"Robot picks up {item}")
        self.holding = item

    def put_down(self, place):
        print(f"Robot puts {self.holding} into {place}")
        self.holding = None

    # ----- Tasks -----
    def clean_up_kitchen(self, env):
        self.move_to("kitchen")

        for item in env.dirty_items:
            self.pick_up(item)
            self.put_down("sink")

        env.dirty_items.clear()
        print("Kitchen is clean now")

    def go_to_kitchen(self, env):
        self.move_to("kitchen")
        print("Robot is now in the kitchen")


# ===== TASK PLANNER =====
TASK_MAP = {
    "Clean-up the kitchen": Robot.clean_up_kitchen,
    "Go to the kitchen": Robot.go_to_kitchen
}


def execute_task(robot, task_name, env):
    print(f"\nReceived task: {task_name}")

    if task_name in TASK_MAP:
        TASK_MAP[task_name](robot, env)
    else:
        print("Task not supported")


# ===== RUN SIMULATION =====
env = KitchenEnvironment()
robot = Robot()

env.show_state()

execute_task(robot, "Go to the kitchen", env)
execute_task(robot, "Clean-up the kitchen", env)

env.show_state()
