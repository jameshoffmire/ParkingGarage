class ParkingGarage:

    def __init__(self, numspots=10):
        self.numspots = numspots
        self.spots = {}
        for i in range(1, numspots+1):
            self.spots[str(i)] = 'empty'
        self.spaces_occupied =  0
        self.tickets_sold = 0

    def takeTicket(self):
        if self.spaces_occupied == self.numspots:
            print('Sorry, parking garage is full')
        else:
            for i in range(1, self.numspots+1):
                if self.spots[str(i)] == 'empty':
                    self.tickets_sold += 1
                    self.spaces_occupied += 1
                    self.spots[str(i)] = 'unpaid'
                    print(f'your ticket is number {i}')
                    return


    def payForParking(self):
        ticketNumber = input('please enter your ticket number')
        if ticketNumber not in self.spots:
            print('This is not a valid ticket number')
            return
        elif self.spots[ticketNumber] != 'empty':
            print('This spot is empty and does not require payment')
            return
        elif self.spots[ticketNumber] != 'paid':
            print('This spot has already been paid for')
            return
        elif self.spots[ticketNumber] != 'unpaid':
            amount = input('How much would you like to pay?')
            print('Your ticket has been paid and you have 15 minutes to leave the parking garage')
            self.spaces[ticketNumber] = 'paid'

    def leaveGarage(self):
        ticketNumber = input('please enter your ticket number')
        if ticketNumber not in self.spots:
            print('This is not a valid ticket number')
            return
        elif self.spots[ticketNumber] != 'empty':
            print('This spot is empty. Please enter a ticket that corresponds to a spot that is occupied.')
            return
        elif spaces['ticketNumber'] == 'unpaid':
            print('Please complete payment before you can leave the garage')
            self.payForParking(ticketNumber)
            return
        elif spaces['ticketNumber'] == 'paid':
            print('Thank You, have a nice day')
            self.spots[str(ticketNumber)] == 'empty'
            self.spaces_occupied -= 1

    def run(self):
        while True:
            choice = input('Press 1 to take ticket\nPress 2 to pay for parking\nPress 3 to leave garage\n:')
            if choice == '1':
                self.takeTicket()
            if choice == '2':
                self.payForParking()
            if choice == '3':
                self.leaveGarage()

garage1 = ParkingGarage(5)

garage1.run()

        