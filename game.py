import pickle

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def take_item(self, item):
        self.inventory.append(item)
        print(f"You picked up the {item}.")

    def use_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"You used the {item}.")
        else:
            print(f"You do not have the {item} in your inventory.")

class Game:
    def __init__(self):
        self.player = None
        self.current_location = None

    def start(self):
        self.player = Player(input("Enter your name: "))
        self.current_location = "starting_room"
        print("Welcome to the game!")

    def save_game(self):
        with open("game_state.pkl", "wb") as file:
            pickle.dump((self.player, self.current_location), file)
        print("Game saved.")

    def load_game(self):
        try:
            with open("game_state.pkl", "rb") as file:
                self.player, self.current_location = pickle.load(file)
            print("Game loaded.")
        except FileNotFoundError:
            print("No saved game found.")

    def move(self, location):
        self.current_location = location
        print(f"You moved to the {location}.")

    def examine(self, item):
        if self.current_location == "room1":
            if item == "key":
                print("You see a shiny key on the table.")
            elif item == "book":
                print("The book is old and dusty.")
            else:
                print("There is nothing of interest.")
        else:
            print("There is nothing of interest.")

    def unlock_door(self):
        if self.current_location == "room2":
            if "key" in self.player.inventory:
                print("You unlocked the door and won the game!")
            else:
                print("The door is locked.")
        else:
            print("There is no door here.")

def display_menu():
    options = [
        "Save game",
        "Load game",
        "Move to a location",
        "Examine an item",
        "Take an item",
        "Use an item",
        "Quit the game",
    ]
    print("========== Menu ==========")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    print("==========================")

def display_locations():
    locations = [
        "Starting room",
        "Room 1",
        "Room 2",
    ]
    print("========== Locations ==========")
    for i, location in enumerate(locations, 1):
        print(f"{i}. {location}")
    print("===============================")

def display_location_description(location):
    if location == "Starting room":
        print("You are in the starting room. There is a door to the east.")
    elif location == "Room 1":
        print("You are in Room 1. There is a table in the center of the room with a book and a key on it.")
    elif location == "Room 2":
        print("You are in Room 2. There is a locked door to the east.")
    else:
        print("Invalid location.")

def main():
    # Create the game object
    game = Game()

    # Start the game
    game.start()

    # Game loop
    while True:
        display_menu()
        command = input("Select an option: ")

        if command == "1":
            game.save_game()
        elif command == "2":
            game.load_game()
        elif command == "3":
            display_locations()
            location_choice = input("Select a location: ")
            if location_choice == "1":
                location = "Starting room"
            elif location_choice == "2":
                location = "Room 1"
            elif location_choice == "3":
                location = "Room 2"
            else:
                print("Invalid choice.")
                continue
            game.move(location)
            display_location_description(location)
        elif command == "4":
            item = input("Enter the item to examine: ")
            game.examine(item)
        elif command == "5":
            item = input("Enter the item to take: ")
            game.player.take_item(item)
        elif command == "6":
            item = input("Enter the item to use: ")
            game.player.use_item(item)
        elif command == "7":
          print("The true exit to this escape room was just the quit command.")
          break
        else:
            print("Invalid option. Please try again.")

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
