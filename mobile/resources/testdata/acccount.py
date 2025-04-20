class TestAccount:
    def __init__(self, email, password):
        self.email = email
        self.password = password

class TestData:
    user_account = TestAccount("admin@gmail.com", "123123")
    user_account_test = TestAccount("thaivanphuc@example.com","password456")
    