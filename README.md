# 🚂 Automated Railway Reservation System

A command-line Python application for managing train seat reservations.

---

## Features

| Feature | Description |
|---|---|
| ✅ Check Availability | View total, booked, and available seats |
| 🎫 Book Ticket | Enter passenger name & age to reserve a seat and get a Booking ID |
| 🔍 View Ticket | Look up booking details using a Booking ID |
| ❌ Cancel Ticket | Cancel a reservation and free up the seat |

---

## How to Run

**Requirements:** Python 3.x (no external libraries needed)

```bash
python main.py
```

Then follow the on-screen menu:
```
1. Check Availability
2. Book Ticket
3. View Ticket
4. Cancel Ticket
5. Exit
```

---

## Project Structure

```
railway-reservation-system/
│
├── main.py       # Main application file
└── README.md     # Project documentation
```

---

## Example Usage

```
Enter choice [1-5] : 2

  Passenger name : Alice
  Passenger age  : 25

  ✔  Ticket booked successfully!
  ┌─────────────────────────┐
  │ Booking ID : BKA3F9X2   │
  │ Name       : Alice      │
  │ Age        : 25         │
  │ Seat No.   : 1          │
  └─────────────────────────┘
```

---

## Commit History (minimum 3 commits)

1. `Initial setup` – Repository created with README
2. `Add booking feature` – Book, view, cancel ticket logic
3. `Final working system` – Menu, availability check, full testing
