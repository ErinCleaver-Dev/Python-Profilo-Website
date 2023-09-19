import unittest
import server.fb as fb

class Test_Firebase(unittest.TestCase):
    def setup(self):
        print("Testing a function")
    
    def test_failed_to_setup_firebase(self):
        result = fb.setup_fb()
        print(result)
        self.assertFalse({} == result)
    
    def test_create_firebase(self):
        result = fb.setup_fb()
        print(result)
        self.assertTrue(result)

        
    def test_incorrect_password_test(self):
        user_name = "ecleaver@live.com"
        password = "Cdao4589!"
        result = fb.signed_in(user_name, password)
        print(result)
        self.assertFalse(result)
    def test_incorrect_email(self):
        user_name = "ecleaver@gmail.com"
        password = "Cdao4589!"
        result = fb.signed_in(user_name, password)
        print(result)
        self.assertFalse(result)

    def test_correct_password(self):
        user_name = "ecleaver@live.com"
        password = "None"
        result = fb.signed_in(user_name, password)
        print(result)
        self.assertTrue(result)

    def tearDown(self):
        print('cleaning up')


if __name__ == '__main__':
    unittest.main()