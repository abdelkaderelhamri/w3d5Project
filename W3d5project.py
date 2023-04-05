import random

class Parkinggarage:
    def __init__(self, num_tickets=10, num_parking_space=10):
        self.tickets = list(range(1, num_tickets + 1))
        self.parking_spaces = list(range(1, num_parking_space + 1))
        self.current_ticket = {}

    def take_ticket(self):
        if self.tickets:
            ticket = self.tickets.pop()
            parking_space = self.parking_spaces.pop(random.randint(0, len(self.parking_spaces) - 1))
            self.current_ticket[ticket] = {'paid': False, 'parking space': parking_space}
            print(f'you have taken ticket number {ticket} and parking space {parking_space}.')
        else:
            print('Sorry, no more spcae in the parking garage.')

    def pay_for_parking(self):
        ticket_num = int(input('please enter ticket number you want to pay for parking:'))
        if ticket_num in self.current_ticket: 
            if not self.current_ticket[ticket_num]['paid']:
                payment = input('please enter payment amount:')
                self.current_ticket[ticket_num]['paid'] = True
                print(f'you have paid {payment} for ticket {ticket_num}.')
            else:
                print('Sorry, ticket already paid.')
        else:
            print('sorry, ticket not found.')

    def leave_garage(self):
        ticket_num = int(input('please enter ticket number you want to leave:'))
        if ticket_num in self.current_ticket: 
            if self.current_ticket[ticket_num]['paid']:
                print('Thank you for your payment. have a nice day.')
                parking_space = self.current_ticket[ticket_num]['parking space']
                self.parking_spaces.append(parking_space)
                del self.current_ticket[ticket_num]
            else:
                print('sorry, ticket not found.')
        else:
            print('sorry, ticket not found.')
    
    def get_parking_status(self):
       print('Current Parking Status:')
       print(f'Total Parking Spaces: {len(self.parking_spaces)}')
       print(f'Total Tickets: {len(self.tickets)}')
       print(f'Total Occupied Space: {len(self.current_ticket)}')
       print('Occupied Spaces: ')
       for ticket, info in self.current_ticket.items():
           print(f'Ticket: {ticket}, Parking Space: {info["parking_space"]}')

def main():
    Parking_garage = Parkinggarage(num_tickets=random.randint(1, 10), num_parking_space=random.randint(1, 10))
    while True:
       print('Welcome to the parking garage! What would you like to do?')
       print('1, Take a ticket.')
       print('2, pay for parking.')
       print('3, leave the garage.')
       print('4, check parking status.')
       print('5, exit.')
       choice = input('Enter your choice: ')
       if choice == '1':
            Parking_garage.take_ticket()
       elif choice == '2':
            Parking_garage.pay_for_parking()
       elif choice == '3':
            Parking_garage.leave_garage()
       elif choice == '4':
            Parking_garage.get_parking_status() 
       elif choice == '5':
            print('Thank you for visiting our parking garage.')
            break
       else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()

