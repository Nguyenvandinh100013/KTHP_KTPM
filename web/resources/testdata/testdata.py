class TestAccount:
    def __init__(self, email, password):
        self.email = email
        self.password = password

class TestData:
    admin_account = TestAccount("shino1@gmail.com", "123456")
    user_shino_account = TestAccount("shino@gmail.com","123456")
