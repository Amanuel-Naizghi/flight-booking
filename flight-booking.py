import os
#This data is about flight numbers and the seats that are already booked
flightInfo={45435:45, 48486:40, 48487:35, 48488:10, 48489:25}
#This function moves all the data in the csv file into a list and returns the list
def get_flights(file):
  newPath="./data/"+file
  fileExists = os.path.exists(newPath)
  dataList = []
  if fileExists:
    with open(newPath, "r", encoding="utf-8-sig") as file:
      for line in file:
        row = line.strip().split(",")  #Clearing white spaces
        cleanRow = []
        for item in row:     
          if item != "":
            cleanRow.append(item)

        if cleanRow:                    # skip empty rows
          dataList.append(cleanRow)

    file.close()
    print("Data stored successfuly in a list")
    return dataList
  else:
    print("File does not exist")
    return None

def view_flights(flightList):
  print("{:>15s} {:>15s} {:>15s} {:>15s} {:>15s} {:>15s} {:>15s} {:>15s}".format(
      "Flight Number", "Flight Date", "First Name", "Occupation", "Number of Seats","Source","Destination", "Price in USD"))

  for row in flightList[1:]: # It is starting from index 1 b/c the name don't need to be printed again
    print("{:>15s} {:>15s} {:>15s} {:>15s} {:>15s} {:>15s} {:>15s} {:>15s}".format(
        row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
    
def book_flight_check(flightList):
  flightSelection=int(input("Enter flight number: "))
  flightFound=False
  totalSeats=0
  for row in flightList[1:]:
    if(int(row[0])==flightSelection):
      flightFound=True
      #We are finding the number of booked seated from our list based on flight number entered
      for key,value in flightInfo.items():
        if(int(row[0])==key):
          totalSeats=value
        
      break
  if(flightFound):
    numberOfSeats=int(input("Enter number of seats: "))
    #We assumed the maximum limit for number of seats per flight is 50
    if((totalSeats+numberOfSeats)>50):
      print("Seats are full!")
    else:
      newNumberOfSeats=numberOfSeats+totalSeats
      #Updating the flight info dictionary by adding the number of seats entered by the user
      flightInfo[flightSelection]=int(newNumberOfSeats)
      book_flight(flightSelection,numberOfSeats)
  else:
    print("Flight not found!")

def book_flight(flightSelection,numberOfSeats):
  attendantName=input("Enter Your name: ")
  dayOfFlight=input("Enter the date of flight in DD/MM/YYYY format: ")
  occupation=input("Enter your occupation, its opitonal: ")
  source=input("Enter the source: ")
  destination=input("Enter your destination: ")
  #price is based on the number of seats requested
  price=350*int(numberOfSeats)
  if(attendantName!="" and dayOfFlight!=""):
    # a stands for append mode, we are appending new flight data to our existing data
    with open("./data/flightData.csv", "a", encoding="utf-8-sig") as file: 
        file.write(f"{flightSelection},{dayOfFlight},{attendantName},{occupation},{numberOfSeats},{source},{destination},{price}\n")
  print("Flight booked successfuly")
def view_bookings(flightList):
  view_flights(flightList)
  flightSelection=int(input("Enter flight number: "))
  name=input("Enter your first name: ")
  flightFound=False
  for row in flightList[1:]:
    if(int(row[0])==flightSelection and name.lower()==row[2].lower()):
      flightFound=True
      print("Here is your flight details\n")

      print("{:>15s} {:>15s} {:>15s} {:>15s} {:>15s} {:>15s} {:>15s} {:>15s}".format(
      "Flight Number", "Flight Date", "First Name", "Occupation", "Number of Seats", "Source", "Destination", "Price in USD"))

      print("{:>15s} {:>15s} {:>15s} {:>15s} {:>15s} {:>15s} {:>15s} {:>15s}".format(
        row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
  if not flightFound:
     print("You have no bookings")

def cancel_booking(flightList):
  flightSelection=int(input("Enter flight number to cancel: "))
  name=input("Enter your first name: ")
  indexCounter=1
  flightFound=False
  for row in flightList[1:]:
    if(int(row[0])==flightSelection and name.lower()==row[2].lower()):
      flightFound=True
      numberOfSeat=int(input("Enter number of seats to cancel: "))
      #If the user selects number of seats to cancel >= the initial amount, it will wipe out all his booking
      if(numberOfSeat>=int(row[4])):
        delete_csv_row(numberOfSeat)
        print("Seat canceled successfuly")
      else:
        newNumberOfSeats=int(row[4])-numberOfSeat
        with open("./data/flightData.csv", "r", encoding="utf-8-sig") as file:
          lines = file.readlines()

        # Step 2: Split the row into columns
        row = lines[indexCounter].strip().split(",")

        # Step 3: Update the specific column
        row[4] = newNumberOfSeats

        # Step 4: Rebuild the row making sure that every item in a row is in string format
        lines[indexCounter] = ",".join(str(x) for x in row) + "\n"

        # Step 5: Write everything back
        with open("./data/flightData.csv", "w", encoding="utf-8-sig") as file:
          file.writelines(lines)
        print("Seat canceled successfuly")

    indexCounter+=1
  if not flightFound:
    print("Error, flight not found!")
def delete_csv_row(row_index):
    lines = []
    with open("./data/flightData.csv", "r") as f:
        lines = f.readlines()

    # remove the row
    lines.pop(row_index)

    # write back
    save_flights(lines)
    print("Item deleted!")
def save_flights(lines):
  with open("./data/flightData.csv", "w") as f:
        f.writelines(lines)

def exit_program():
  exit()

def main_menue():
  userSelection=input(
    "1. To see all flight data press 1\n"
    "2. To book a flight press 2\n"
    "3. To cancel a flight press 3\n"
    "4. View your booking data press 4\n"
    "5. Exit\n"
)

  return userSelection

def main():
  print("Welcome to our flight booking site!\n")
  # data path is recommended to be on flightData.csv
  fileName=input("Enter you data file name: ")
  list=get_flights(fileName)

  while list is None:
    fileName=input("Enter you data file name: ")
    list=get_flights(fileName)
  #This part of the program executes as long as the user puts correct file name
  if list is not None:
    userSelection=main_menue()
    while userSelection != 5:
      
      if(userSelection=="1"):
        view_flights(list)
      elif(userSelection=="2"):
        book_flight_check(list)
        list=get_flights(fileName)#refreshing the list so that updates will be shown as soon as user books a flight
      elif(userSelection=="3"):
        cancel_booking(list)
        list=get_flights(fileName)#refreshing the list so that updates will be shown as soon as user cancels a flight
      elif(userSelection=="4"):
        view_bookings(list)
      elif(userSelection=="5"):
        exit_program()

      userSelection=main_menue()

if __name__ == "__main__":
    main()
