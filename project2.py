import string

class SeatBookingSystem:
    def __init__(self):
        """
        Initialize seating arrangement and booking records.
        'F' indicates a free seat, 'R' indicates a reserved seat,
        'X' indicates an aisle, and 'S' indicates a storage area.
        """
        self.seats = [['F' for _ in range(7)] for _ in range(80)]
        self.bookings = {}  # Dictionary to store seat identifiers and customer details

        # Set 'X' for aisle seats in the 4th column
        for i in range(80):
            self.seats[i][3] = 'X'

        # Set 'S' for storage seats in the 77th and 78th rows
        for j in range(7):
            self.seats[76][j] = 'S'
            self.seats[77][j] = 'S'

    def show_seating(self):
        """Display the current state of the seating arrangement."""
        for row in self.seats:
            print(' '.join(row))

    def check_availability(self, row, seat):
        """
        Check if a specific seat is available.

        Args:
            row (int): The row number of the seat.
            seat (int): The seat number in the row (0 for A, 1 for B, ...).
        """
        if self.seats[row - 1][seat] == 'F':
            print(f"Seat {row}{chr(65 + seat)} is available.")
        else:
            print(f"Seat {row}{chr(65 + seat)} is not available.")

    def book_seat(self, row, seat):
        """
        Book a seat if it is free and store the customer details.

        Args:
            row (int): The row number of the seat.
            seat (int): The seat number in the row (0 for A, 1 for B, ...).
        """
        if self.seats[row - 1][seat] == 'F':
            passport = input("Enter passport number: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            self.seats[row - 1][seat] = 'R'
            seat_id = f"{row}{chr(65 + seat)}"
            self.bookings[seat_id] = {
                'passport': passport,
                'first_name': first_name,
                'last_name': last_name,
            }
            print(f"Seat {seat_id} has been booked.")
        else:
            print(f"Seat {row}{chr(65 + seat)} cannot be booked.")

    def free_seat(self, row, seat):
        """
        Free a previously booked seat and remove the booking details.

        Args:
            row (int): The row number of the seat.
            seat (int): The seat number in the row (0 for A, 1 for B, ...).
        """
        seat_id = f"{row}{chr(65 + seat)}"
        if seat_id in self.bookings:
            del self.bookings[seat_id]
            self.seats[row - 1][seat] = 'F'
            print(f"Seat {seat_id} has been freed.")
        else:
            print(f"Seat {row}{chr(65 + seat)} is not currently booked.")

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
                self.book_seat(row, seat)
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
