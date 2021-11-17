from project_10.customer import Customer
from project_10.dvd import DVD


class MovieWorld:
    def __init__(self, name:str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)
        return

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)
        return


    def rent_dvd(self, customer_id:int, dvd_id:int):
        dvd = [d for d in self.dvds if d.id == dvd_id]
        customer = [c for c in self.customers if c.id == customer_id]
        try:

            if dvd[0].is_rented:
                if not [d for d in customer[0].rented_dvds if d.id == dvd_id]:
                    return f"DVD is already rented"
                else:
                    return f"{customer[0].name} has already rented {dvd[0].name}"
            elif customer[0].age < dvd[0].age_restriction:
                return f"{customer[0].name} should be at least {dvd[0].age_restriction} to rent this movie"
            else:
                dvd_index = [k for k, d in enumerate(self.dvds) if d.id == dvd_id]
                customer_index = [k for k, c in enumerate(self.customers) if c.id == customer_id]
                customer = self.customers.pop(customer_index[0])
                dvd = self.dvds.pop(dvd_index[0])
                dvd.is_rented = True
                customer.rented_dvds.append(dvd)
                self.customers.append(customer)
                self.dvds.append(dvd)

                return f"{customer.name} has successfully rented {dvd.name}"
        except IndexError:
            return


    def return_dvd(self, customer_id, dvd_id):

        dvd = [d for d in self.dvds if d.id == dvd_id]
        customer = [c for c in self.customers if c.id == customer_id]
        try:
            if [i for i in customer[0].rented_dvds if i.id == dvd_id]:
                dvd_index = [k for k, d in enumerate(self.dvds) if d.id == dvd_id]
                customer_index = [k for k, c in enumerate(self.customers) if c.id == customer_id]
                customer = self.customers.pop(customer_index[0])
                dvd = self.dvds.pop(dvd_index[0])
                dvd.is_rented = False
                customer_dvd_index = [i for i, n in enumerate(customer.rented_dvds) if n.id == dvd_id]
                customer.rented_dvds.pop(customer_dvd_index[0])
                self.customers.append(customer)
                self.dvds.append(dvd)
                return f"{customer.name} has successfully returned {dvd.name}"

            else:
                return f"{customer[0].name} does not have that DVD"
        except IndexError:
            return
    pass

    def __repr__(self):
        customers_dict = {i.id: i for i in self.customers}
        self.customers = [v for k, v in sorted(customers_dict.items(), key=lambda x: x[0], reverse=False)]
        dvds_dict = {i.id: i for i in self.dvds}
        self.dvds = [v for k, v in sorted(dvds_dict.items(), key=lambda x: x[0], reverse=False)]
        result = ['\n'.join([c.__repr__() for c in self.customers]), '\n'.join([v.__repr__() for v in self.dvds])]

        return '\n'.join(result)
        pass


