class TestAccount:
    def __init__(self, email, password):
        self.email = email
        self.password = password

class TestData:
    user_shino_account = TestAccount("phuctv123@gmail.com", "Password678")
    admin_account = TestAccount("admin@gmail.com","123123")
