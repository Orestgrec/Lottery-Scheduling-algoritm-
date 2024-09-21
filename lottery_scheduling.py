
import random

# Create Process class to handle creating processes
class Process:
    def __init__(self, id) -> None:
        self.uuid = id
        self.tickets = []

# Create a Scheduler class that can add process, allocate tickets, etc. 
class Scheduler:
    def __init__(self) -> None:
        self.processes = []
        self.winning_processes = []

    # Add all processes to a list
    def add(self, process):
        self.processes.append(process)

    # Show the current state of the scheduler
    def state(self, process):
        print(f"Process ID: {process.uuid}, Tickets: {process.tickets}")

    # Allocate a certain number of ticket to each process
    def allocate_tickets(self):
        init_tickets = 1
        for process in self.processes:
            rand_assign = random.randint(1, 10)
            process.tickets = list(range(init_tickets, init_tickets + rand_assign))
            self.state(process)
            init_tickets += rand_assign
        print('\n')

    # Start the scheduling process and pick a random process as winner
    def start(self):
        tot_tickets = []
        for process in self.processes:
            for tickets in process.tickets:
                tot_tickets.append(tickets)
        lottery_winner = random.choice(tot_tickets)
        for process in self.processes:
            if lottery_winner in process.tickets:      
                #print(f"Process {process.uuid} wins the lottery!")
                self.winning_processes.append(process.uuid)
                break
        
    def calculate_percentage(self):
        total_wins = len(self.winning_processes)
        print("Percentuale di vittorie per ciascun processo:")
        for process in self.processes:
            wins = self.winning_processes.count(process.uuid)
            percentage = (wins / total_wins) * 100
            print(f"Process {process.uuid}: {percentage:.2f}% vittorie")
    
    def calculate_ticket_percentage(self):
        total_tickets = sum(len(process.tickets) for process in self.processes)

        print("Percentuale prevista di CPU asseganata per ciascun processo:")
        for process in self.processes:
            ticket_percentage = (len(process.tickets) / total_tickets) * 100
            print(f"Process {process.uuid}: {ticket_percentage:.2f}% dei ticket")

# Define main function of the program
def main():
    process = int(input("Enter the total number of process to allocate: ")) #random.randint(2, 6)
    scheduler = Scheduler()

    print("Adding processes to scheduler...")
    for i in range(1, process + 1):
        scheduler.add(Process(i))

    print("Assigning tickets...")
    scheduler.allocate_tickets()

    scheduler.calculate_ticket_percentage()

    iteration = int(input("Enter the number of iteration: "))

    print("Starting scheduling...")
    for i in range(0,iteration):
        scheduler.start()
    
    scheduler.calculate_percentage()

    

if __name__ == '__main__':
    main()
