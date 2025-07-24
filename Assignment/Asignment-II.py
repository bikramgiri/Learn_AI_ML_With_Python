import time

class VacuumCleanerWorld:
    def __init__(self, location='A', status_A='Dirty', status_B='Dirty'):
        self.initial_location = location
        self.location = location
        self.status = {'A': status_A, 'B': status_B}
        self.actions = []

    def display_status(self):
        print(f"\n[Current Status]")
        print(f"Vacuum Location: Room {self.location}")
        print(f"Room A: {self.status['A']}, Room B: {self.status['B']}")
        time.sleep(1)

    def is_goal_reached(self):
        return self.status['A'] == 'Clean' and self.status['B'] == 'Clean'

    def move_to(self, destination):
        if self.location != destination:
            direction = "Right" if destination == 'B' else "Left"
            print(f"Action: Moving {direction} to Room {destination}...")
            time.sleep(1.5)
            self.location = destination
            self.actions.append(f"Move to Room {destination}")

    def simple_reflex_agent(self):
        print("\nStarting Vacuum Cleaner Simulation\n")
        time.sleep(1)

        # Step 1: Cleaning Phase
        while not self.is_goal_reached():
            self.display_status()

            if self.status[self.location] == 'Dirty':
                print(f"Action: Sucking dirt in Room {self.location}...")
                time.sleep(2)
                self.status[self.location] = 'Clean'
                self.actions.append(f"Suck in Room {self.location}")
            else:
                next_room = 'B' if self.location == 'A' else 'A'
                self.move_to(next_room)

        # Step 2: Confirm cleanliness of other room only if vacuum is not already there
        self.display_status()
        print("✅ Both rooms appear clean.")
        other_room = 'B' if self.initial_location == 'A' else 'A'

        if self.location != other_room:
            print(f"\n🔍 Visiting Room {other_room} to double-check...")
            self.move_to(other_room)
            self.display_status()
            if self.status[other_room] == 'Clean':
                print(f"✅ Room {other_room} confirmed clean.")
            else:
                print(f"❌ Warning: Room {other_room} is dirty! Cleaning again...")
                self.status[other_room] = 'Clean'
                self.actions.append(f"Suck in Room {other_room}")

        # Step 3: Return to initial location
        print(f"\n🔄 Returning to initial starting room: Room {self.initial_location} to double-check...")
        self.move_to(self.initial_location)
        self.display_status()
        if self.status[self.initial_location] == 'Clean':
            print(f"✅ Verified: Room {self.initial_location} is clean.")
        else:
            print(f"❌ Warning: Room {self.initial_location} is dirty! Cleaning again...")
            self.status[self.initial_location] = 'Clean'
            self.actions.append(f"Suck in Room {self.initial_location}")

        print("\n🏁 Simulation Complete: All rooms clean and verified.")
        print("🧭 Action Path:", " → ".join(self.actions))


# Test: Start at Room A with both rooms clean
vacuum = VacuumCleanerWorld(location='A', status_A='Clean', status_B='Dirty')
vacuum.simple_reflex_agent()
