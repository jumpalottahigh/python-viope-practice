class ManageCustomer(Customer):
    def addbill(self):
        self.total += 50
    def payment(self):
        self.total -= 100