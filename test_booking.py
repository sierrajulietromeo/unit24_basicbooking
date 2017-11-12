import pandas as pd #For read/write to the file.
import os

#main program menu
def main():
    print("Welcome to the Ada Booking System")
    print("=================================")
    print("Please select from the following options")
    print("1: View room bookings for Tuesday")
    print("2: View room bookings for Wednesday")


    mainMenuSelection = int(input("Enter selection: "))

    if(mainMenuSelection == 1):

        os.system("cls")  #Only works on Windows machines
        viewTueRoomBookings()
    if(mainMenuSelection == 2):
        os.system("cls")  #Only works on Windows machines
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
        os.system("cls")  #Only works on Windows machines
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
    print("Please select from the following rooms:")
    print("1: SPUTNIK")
    print("2: ENDEAVOUR")
    print("3: VOYAGER")
    print("4: Back to main menu.")

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

    #print (df(index=False))
    print(df.head(7) ) #prints periods for the day (is df head the best to use?)
    print("Enter the period number you wish to book, or enter N to go back.")

    try:
        periodNumber = int(input("?"))
    except ValueError:
        os.system("cls")  #Only works on Windows machines
        main()

    if(periodNumber == 1 or 2 or 3 or 4 or 5 or 6 or 7):
        bookRoom(roomName, periodNumber)
    else:
        os.system("cls")  #Only works on Windows machines
        main()


def bookRoom(roomName, periodNumber):
    df = pd.read_csv(roomName)
    periodNumber -= 1 #to get the right place in the array because counting starts at 0

    if (df.at[periodNumber, "Name"] != "FREE"):
        os.system("cls")  #Only works on Windows machines
        print("Sorry, this room is already booked for that period by:", (df.at[periodNumber, "Name"])  )
        print("                                  ")
        displayRoomBookings(roomName)
    else:
        name = input("Enter name to book room under: ")
        df.at[periodNumber, "Name"] = name
        df.to_csv("sputnik_tues.csv", index=False)
        periodNumber += 1 #to get the right place in the array because counting starts at 0
        os.system("cls")  #Only works on Windows machines
        print("Room is now booked for you at period: ", periodNumber)
        print("                           ")



    #Loopthroughheretoseeifitsfree
    main()





def editRoomBooking():
    #df.at[1, "Name"] = "John"
    df.to_csv("sputnik_tues.csv", index=False)


#Sequential Code
main()
