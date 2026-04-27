import random
import string

# ─────────────────────────────────────────
#  Configuration
# ─────────────────────────────────────────
TOTAL_SEATS = 60

# seats: {seat_number: booking_id or None}
seats = {i: None for i in range(1, TOTAL_SEATS + 1)}

# bookings: {booking_id: {name, age, seat}}
bookings = {}


# ─────────────────────────────────────────
#  Helpers
# ─────────────────────────────────────────
def generate_booking_id():
    """Generate a random 6-character alphanumeric booking ID."""
    return "BK" + "".join(random.choices(string.ascii_uppercase + string.digits, k=6))


def available_seats():
    """Return list of free seat numbers."""
    return [seat for seat, bid in seats.items() if bid is None]


# ─────────────────────────────────────────
#  Feature 1 – Check Availability
# ─────────────────────────────────────────
def check_availability():
    free = available_seats()
    print("\n╔══════════════════════════════╗")
    print("║      SEAT AVAILABILITY       ║")
    print("╚══════════════════════════════╝")
    print(f"  Total seats  : {TOTAL_SEATS}")
    print(f"  Booked       : {TOTAL_SEATS - len(free)}")
    print(f"  Available    : {len(free)}")
    if free:
        print(f"\n  Available seat numbers:")
        # Print in rows of 10
        for i, s in enumerate(free, 1):
            print(f"  {s:3}", end="")
            if i % 10 == 0:
                print()
        print()
    else:
        print("\n  ⚠  No seats available. Train is full!")


# ─────────────────────────────────────────
#  Feature 2 – Book Ticket
# ─────────────────────────────────────────
def book_ticket():
    print("\n╔══════════════════════════════╗")
    print("║         BOOK TICKET          ║")
    print("╚══════════════════════════════╝")

    free = available_seats()
    if not free:
        print("  ⚠  Sorry, no seats available!")
        return

    name = input("  Passenger name : ").strip()
    if not name:
        print("  ✗ Name cannot be empty.")
        return

    try:
        age = int(input("  Passenger age  : ").strip())
        if age <= 0 or age > 120:
            raise ValueError
    except ValueError:
        print("  ✗ Please enter a valid age.")
        return

    seat = free[0]                        # assign first available seat
    booking_id = generate_booking_id()
    while booking_id in bookings:         # ensure uniqueness
        booking_id = generate_booking_id()

    seats[seat] = booking_id
    bookings[booking_id] = {"name": name, "age": age, "seat": seat}

    print("\n  ✔  Ticket booked successfully!")
    print(f"  ┌─────────────────────────┐")
    print(f"  │ Booking ID : {booking_id:<11} │")
    print(f"  │ Name       : {name:<11} │")
    print(f"  │ Age        : {age:<11} │")
    print(f"  │ Seat No.   : {seat:<11} │")
    print(f"  └─────────────────────────┘")
    print("  (Save your Booking ID to view or cancel later.)")


# ─────────────────────────────────────────
#  Feature 3 – View Ticket
# ─────────────────────────────────────────
def view_ticket():
    print("\n╔══════════════════════════════╗")
    print("║         VIEW TICKET          ║")
    print("╚══════════════════════════════╝")

    booking_id = input("  Enter Booking ID : ").strip().upper()
    if booking_id in bookings:
        b = bookings[booking_id]
        print(f"\n  ┌─────────────────────────┐")
        print(f"  │ Booking ID : {booking_id:<11} │")
        print(f"  │ Name       : {b['name']:<11} │")
        print(f"  │ Age        : {b['age']:<11} │")
        print(f"  │ Seat No.   : {b['seat']:<11} │")
        print(f"  └─────────────────────────┘")
    else:
        print("  ✗ Booking ID not found. Please check and try again.")


# ─────────────────────────────────────────
#  Feature 4 – Cancel Ticket
# ─────────────────────────────────────────
def cancel_ticket():
    print("\n╔══════════════════════════════╗")
    print("║        CANCEL TICKET         ║")
    print("╚══════════════════════════════╝")

    booking_id = input("  Enter Booking ID to cancel : ").strip().upper()
    if booking_id not in bookings:
        print("  ✗ Booking ID not found.")
        return

    b = bookings[booking_id]
    confirm = input(
        f"  Confirm cancel for {b['name']} (Seat {b['seat']})? [y/n] : "
    ).strip().lower()

    if confirm == "y":
        seats[b["seat"]] = None          # free up the seat
        del bookings[booking_id]
        print(f"  ✔  Booking {booking_id} cancelled. Seat {b['seat']} is now available.")
    else:
        print("  Cancellation aborted.")


# ─────────────────────────────────────────
#  Main Menu
# ─────────────────────────────────────────
def main():
    print("\n" + "=" * 40)
    print("   AUTOMATED RAILWAY RESERVATION SYSTEM")
    print("=" * 40)

    menu = {
        "1": ("Check Availability", check_availability),
        "2": ("Book Ticket",        book_ticket),
        "3": ("View Ticket",        view_ticket),
        "4": ("Cancel Ticket",      cancel_ticket),
        "5": ("Exit",               None),
    }

    while True:
        print("\n  ┌─── MAIN MENU ───────────────┐")
        for key, (label, _) in menu.items():
            print(f"  │  {key}. {label:<26}│")
        print("  └─────────────────────────────┘")

        choice = input("  Enter choice [1-5] : ").strip()
        if choice == "5":
            print("\n  Thank you for using the Railway Reservation System. Goodbye!\n")
            break
        elif choice in menu:
            menu[choice][1]()
        else:
            print("  ✗ Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
