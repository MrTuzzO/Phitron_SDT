class Star_Cinema:
    hall_list = []

    def __init__(self, name) -> None:
        self.name = name

    def entry_hall(self, seats: dict, show_list: list, rows: int, cols: int, hall_no: int):
        newHall = Hall(seats, show_list, rows, cols, hall_no)
        self.hall_list.append(newHall)


class Hall:
    def __init__(self, seats: dict, show_list: list, rows: int, cols: int, hall_no: int):
        self.seats = seats
        self.show_list = show_list
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

    def entry_show(self, id, movie_name, time):
        showInfo = (id, movie_name, time)
        self.show_list.append(showInfo)
        seatMatrix = [[0 for i in range(self.cols)] for i in range(self.rows)]
        self.seats[id] = seatMatrix

    def view_show_list(self):
        for show in self.show_list:
            print(f"Show ID: {show[0]} Movie Name: {show[1]}, Time: {show[2]}")

    def book_seats(self, id, seat_position: tuple):
        if id not in self.seats:
            print("Invalid Show ID")
            return
        
        row, col = seat_position
        seatMatrix = self.seats.get(id)
        
        if seatMatrix[row][col] == 0:
            seatMatrix[row][col] = 'B'
            print(f"Seat ({row+1}, {col+1}) successfully booked.")
        else:
            print(f"Seat ({row+1}, {col+1}) is already booked.")

    def view_available_seats(self, id):
        seatMatrix = self.seats.get(id)
        if seatMatrix:
            print(f"Available seats for Show ID: {id}:")
            for i, row in enumerate(seatMatrix):
                available_seats = ['F' if seat == 0 else 'B' for seat in row]
                print(f"Row {i+1}: {' '.join(available_seats)}")
        else:
            print("Invalid Show ID")


cinema = Star_Cinema("Star S")
cinema.entry_hall({}, [], 5, 5, 1)

hall1 = cinema.hall_list[0]
hall1.entry_show(1, "Jawan Maji", "11:00 PM")
hall1.entry_show(2, "Sujan Maji", "03:00 PM")

while True:
    print("\n--- Star Cinema Management System ---")
    print("1. View Show list")
    print("2. View available seats")
    print("3. Book a seat")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        hall1.view_show_list()

    elif choice == '2':
        show_id = int(input("Enter show ID: "))
        hall1.view_available_seats(show_id)

    elif choice == '3':
        show_id = int(input("Enter show ID: "))
        row = int(input("Enter seat row (1-5): ")) - 1
        col = int(input("Enter seat column (1-5): ")) - 1
        seat_position = (row, col)
        hall1.book_seats(show_id, seat_position)

    elif choice == '4':
        print("Exiting system...")
        break
    else:
        print("Invalid choice!")