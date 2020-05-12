from os import system

class TelephoneBill:
    def __init__(self):
        self.Name = ""
        self.Address = ""
        self.Pin = 0
        self.Telephone = 0
        self.calls = 0
        self.Rent = 200
        self.TotalCalls = 0

    def get(self):
        self.Name = input("Enter Customer Name: ")
        self.Address = input("Enter Billing Address: ")
        self.Pin = input("Enter Postal Code: ")
        self.Telephone = input("Enter Telephone Number: ")
        self.calls = int(input("Enter No. of calls of this month: "))

    def telephone_bill(self):
        call = 0
        call = self.calls
        if 0 < call <= 100:
            return 200
        elif 100 < call <= 150:
            call = call - 100
            return 200 + 0.60 * call
        elif 150 < call <= 200:
            call = call - 150
            return 230 + 0.50 * call
        else:
            call = call - 200
            return 255 + 0.40 * call

    def display(self):
        bill = f"""
        ------------------*************--------------------
        Name of the Customer: {self.Name}
        Billing Address: {self.Address}
        Postal Code: {self.Pin}
        Telephone Number: {self.Telephone}
        Monthly Rent for 180 pulse: {self.Rent} Rs.
        No. of Calls During this Month: {self.calls}
        ---------------------------------------------------
        Bill for this Month: Rs {self.telephone_bill()}
        ---------------------------------------------------"""
        print(bill)
        filename = 'bill_list.txt'
        file = None
        try:
            file = open(filename, 'a')
        except IOError:
            # If not exists, create the file
            file = open(filename, 'w')
        finally:
            file.write(bill)
            print('bill updated in bill_list in same directory')
            file.close()

while 1:
    system('cls')
    print("""
----------------------------------------------------    

    1. enter the details to generate bill
    
    2. exit
            """)
    selected = input('\t>>')
    if selected == '1':
        b1 = TelephoneBill()
        b1.get()
        b1.telephone_bill()
        b1.display()
    elif selected == '2':
        break
    else:
        continue
    input('press any key to go to main menu ... ')
