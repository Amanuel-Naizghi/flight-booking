# Flight Booking System

## Overview
This is a simple command-line flight booking system written in Python. The program allows users to view available flights, book seats, cancel bookings, and check their existing reservations. All booking data is stored in a CSV file.

## How the Program Works

1. **Loading Data**
   - The program reads flight data from a CSV file located in the `data` folder.
   - The data is stored in a list for processing.

2. **Main Menu**
   - The user is presented with a menu that includes:
     - View all flights
     - Book a flight
     - Cancel a booking
     - View personal booking
     - Exit program

3. **Viewing Flights**
   - Displays all available flight records in a formatted table.

4. **Booking a Flight**
   - The user enters a flight number and number of seats.
   - The program checks seat availability (maximum 50 seats per flight).
   - If available, booking details are collected and saved to the CSV file.

5. **Viewing Bookings**
   - The user can search for their booking using flight number and name.
   - Matching booking details are displayed.

6. **Canceling a Booking**
   - The user can cancel all or part of their booked seats.
   - The CSV file is updated accordingly.

7. **Data Storage**
   - All bookings are stored in `flightData.csv`.
   - Updates (booking or cancellation) are written directly to the file.

## Requirements
- Python 3
- A `data` folder containing `flightData.csv`

## Notes
- The program assumes a maximum of 50 seats per flight.
- File name must be entered correctly when prompted.
- All operations are performed through the terminal.