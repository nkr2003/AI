class MonkeyBananaProblem:
    def _init_(self):
        self.monkey_position = "floor"
        self.box_position = "floor"
        self.bananas_hanging = True

    def move_monkey(self, new_position):
        self.monkey_position = new_position

    def move_box(self, new_position):
        self.box_position = new_position

    def climb_on_box(self):
        if self.box_position == "floor" and self.monkey_position == "floor":
            self.monkey_position = "on_box"
            print("Monkey climbs onto the box.")
        else:
            print("Monkey can't climb on the box.")

    def grab_bananas(self):
        if self.monkey_position == "on_box" and self.bananas_hanging:
            self.bananas_hanging = False
            print("Monkey grabs the bananas!")
        elif not self.bananas_hanging:
            print("Bananas are already taken.")
        else:
            print("Monkey can't grab the bananas.")

    def solve(self):
        print("Welcome to the Monkey and Banana Problem!")
        print("Commands: move_box, move_monkey, climb_on_box, grab_bananas, exit")

        while self.bananas_hanging:
            command = input("Enter a command: ").strip().lower()

            if command == "move_box":
                new_position = input("Enter box position (floor/on_box): ").strip().lower()
                self.move_box(new_position)
            elif command == "move_monkey":
                new_position = input("Enter monkey position (floor/on_box): ").strip().lower()
                self.move_monkey(new_position)
            elif command == "climb_on_box":
                self.climb_on_box()
            elif command == "grab_bananas":
                self.grab_bananas()
            elif command == "exit":
                break
            else:
                print("Invalid command.")

if _name_ == "_main_":
    problem = MonkeyBananaProblem()
    problem.solve()
