import pandas as pd #For read/write to the file.

#main program menu
def main():
    print("Welcome to the Ada Booking System")
    print("=================================")
    print("Please select from the following options")
    print("1: View room bookings for Tuesday")
    print("2: View room bookings for Wednesday")
    

    mainMenuSelection = int(input("Enter selection: "))

    if(mainMenuSelection == 1):
        viewTueRoomBookings()
    if(mainMenuSelection == 2):
        viewWedRoomBookings()
    else:
        main()

def viewTueRoomBookings():
    print("VIEW TUESDAY ROOM BOOKINGS")
    print("=================================")
    print("Please select from the following rooms")
    print("1: SPUTNIK")
    print("2: ENDEAVOUR")
    print("3: VOYAGER")

    viewTueSelection = int(input("Enter selection: "))

    if(viewTueSelection == 1):
        print("1")
        displayRoomBookings("sputnik_tues.csv")
    elif(viewTueSelection == 2):
        print("2")
    elif(viewTueSelection == 3):
        print("3")
    else:
        main()

def viewWedRoomBookings():
    print("VIEW WEDNESDAY ROOM BOOKINGS")
    print("=================================")
    print("Please select from the following rooms")
    print("1: SPUTNIK")
    print("2: ENDEAVOUR")
    print("3: VOYAGER")

    viewWedSelection = int(input("Enter selection: "))

    if(viewWedSelection == 1):
        print("1")
        displayRoomBookings("sputnik_tues.csv")
    elif(viewWedSelection == 2):
        print("2")
    elif(viewWedSelection == 3):
        print("3")
    else:
        main()
        
def displayRoomBookings(roomName):
    df = pd.read_csv(roomName)
    print(roomName +" BOOKINGS")
    print(df.head(7)) #prints periods for the day (is df head the best to use?)
    print("Press 1 to make a booking for this room on this day, or press any other key for main menu.")
    bookRoomYesNo = int(input("?"))

    if(bookRoomYesNo == 1):
        print("Y")
        bookRoom(roomName)
    else:
        main()


def bookRoom(roomName):
    bookPeriod = int(input("Which period?"))
    #Loopthroughheretoseeifitsfree
    main()



        
    
def editRoomBooking():
    #df.at[1, "Name"] = "John"
    df.to_csv("sputnik_tues.csv", index=False)


#Sequential Code
main()
