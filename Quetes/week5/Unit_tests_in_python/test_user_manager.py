import unittest
from user_manager import UserManager

class TestUserManager(unittest.TestCase):

    def setUp(self):
        self.manager = UserManager()

    def test_add_user(self):
        # Arrange
        name = "Lionel"
        age = 34

        # Act
        self.manager.add_user(name, age)

        # Assert
        self.assertTrue(self.manager.user_exists(name))
        self.assertEqual(self.manager.users[name], age)

    def test_delete_user(self):
        name = "Junior"
        age = 25
        
        self.manager.add_user(name, age)
        self.manager.delete_user(name)
        self.assertFalse(self.manager.user_exists(name))

    def test_delete_nonexistent_user(self):
        name = "Phil"

        with self.assertRaises(ValueError) as context:
            self.manager.delete_user(name)

        self.assertEqual(str(context.exception), "User not found")

    @unittest.skip("Skipping this test")
    def test_skipped(self):
        pass

if __name__ == '__main__':
    unittest.main()
