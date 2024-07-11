class SeatBookingSystem:
    def __init__(self):
        self.seats = [['F' for _ in range(6)] for _ in range(80)]
        for i in range(80):
            if i in [26, 27]:
                for j in range(6):
                    self.seats[i][j] = 'S'
            elif i % 4 == 3:
                for j in range(6):
                    self.seats[i][j] = 'X'

    def show_seating(self):
        for row in self.seats:
            print(' '.join(row))

    def check_availability(self, row, seat):
        if self.seats[row-1][seat] == 'F':
            print(f"Seat {row}{chr(65+seat)} is available.")
        else:
            print(f"Seat {row}{chr(65+seat)} is not available.")

    def book_seat(self, row, seat):
        if self.seats[row-1][seat] == 'F':
            self.seats[row-1][seat] = 'R'
            print(f"Seat {row}{chr(65+seat)} has been booked.")
        else:
            print(f"Seat {row}{chr(65+seat)} cannot be booked.")

    def free_seat(self, row, seat):
        if self.seats[row-1][seat] == 'R':
            self.seats[row-1][seat] = 'F'
            print(f"Seat {row}{chr(65+seat)} has been freed.")
        else:
            print(f"Seat {row}{chr(65+seat)} is not currently booked.")

    def menu(self):
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