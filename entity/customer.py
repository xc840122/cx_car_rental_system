from entity.user import User


class Customer(User):
    def __init__(self, user_id, user_name, password, name, license_no, phone):
        super().__init__(user_id, user_name, password)
        self.name = name
        self.license_no = license_no
        self.phone = phone
