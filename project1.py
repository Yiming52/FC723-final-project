import random
import string

class SeatBookingSystem:
    def __init__(self):
        # Initialize seating arrangement and booking records
        self.seats = [['F' for _ in range(6)] for _ in range(80)]
        self.bookings = {}  # Dictionary to store booking references and customer details
        for i in range(80):
            if i in [26, 27]:
                for j in range(6):
                    self.seats[i][j] = 'S'
            elif i % 4 == 3:
                for j in range(6):
                    self.seats[i][j] = 'X'

    def generate_booking_reference(self):
        """Generate a unique 8-character alphanumeric booking reference."""
        while True:
            ref = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            if ref not in self.bookings:
                return ref

    def show_seating(self):
        """Display the current state of the seating arrangement."""
        for row in self.seats:
            print(' '.join(row))

    def check_availability(self, row, seat):
        """Check if a specific seat is available."""
        if self.seats[row-1][seat] == 'F':
            print(f"Seat {row}{chr(65+seat)} is available.")
        else:
            print(f"Seat {row}{chr(65+seat)} is not available.")

    def book_seat(self, row, seat, passport, first_name, last_name):
        """Book a seat if it is free and store the booking reference and customer details."""
        if self.seats[row-1][seat] == 'F':
            ref = self.generate_booking_reference()
            self.seats[row-1][seat] = ref
            self.bookings[ref] = {
                'passport': passport,
                'first_name': first_name,
                'last_name': last_name,
                'row': row,
                'seat': chr(65+seat)
            }
            print(f"Seat {row}{chr(65+seat)} has been booked with reference {ref}.")
        else:
            print(f"Seat {row}{chr(65+seat)} cannot be booked.")

    def free_seat(self, row, seat):
        """Free a previously booked seat and remove the booking details."""
        ref = self.seats[row-1][seat]
        if ref != 'F' and ref != 'X' and ref != 'S':
            del self.bookings[ref]
            self.seats[row-1][seat] = 'F'
            print(f"Seat {row}{chr(65+seat)} has been freed.")
        else:
            print(f"Seat {row}{chr(65+seat)} is not currently booked.")

    def menu(self):
        """Display the menu and handle user input."""
        while True:
            print("\nMenu:")
            print("1. Check availability of seat")
            print("2. Book a seat")
            print("3. Free a seat")
            print("4. Show booking state")
            print("5. Exit program")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                row = int(input("Enter row number: "))
                seat = int(input("Enter seat number (0 for A, 1 for B, ...): "))
                self.check_availability(row, seat)
            elif choice == 2:
                row = int(input("Enter row number: "))
                seat = int(input("Enter seat number (0 for A, 1 for B, ...): "))
                passport = input("Enter passport number: ")
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                self.book_seat(row, seat, passport, first_name, last_name)
            elif choice == 3:
                row = int(input("Enter row number: "))
                seat = int(input("Enter seat number (0 for A, 1 for B, ...): "))
                self.free_seat(row, seat)
            elif choice == 4:
                self.show_seating()
            elif choice == 5:
                print("Exiting program.")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    system = SeatBookingSystem()
    system.menu()