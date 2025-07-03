from input import collect_data, get_input, valid_email, empty_input
import unittest 
from unittest.mock import patch, MagicMock

class Testing(unittest.TestCase):

    # testing valid_email w regex check 
    def test_valid_email(self):
        with patch("builtins.input", retun_value = "test@example.com"):
            result = valid_email("test@example.com")
            self.assertEqual(result, "test@example.com")
        
    def test_valid_input(self):
        with patch("builtins.input", retun_value="Some Name"):
            result = get_input("Insert name: ")
            self.assertEqual(result, "Some Name")

    def test_collect_data(self):
        inputs = [
            "Annie",
            "annie@gmail",
            "Data Scientist",
            "",
            "I love meeting people and challenging myself!",
            "Experience in Hack4Impact organization, creating websites for non-profits, working in a professional setting"
        ]

        with patch("builtins.input", side_effect=inputs):
            result = collect_data()

            keys = ["name", "email", "position", "company", "about", "exp"]
            self.assertTrue(all(key in result for key in keys))
            self.assertTrue(result["name"], "Annie")
            self.assertTrue(result["email"], "annie@gmail")
            self.assertTrue(result["position"], "Data Scientist")
            self.assertTrue(result["company"], "")
            self.assertTrue(result["about"], "I love meeting people and challenging myself!")
            self.assertTrue(result["exp"], "Experience in Hack4Impact organization, creating websites for non-profits, working in a professional setting")

    if __name__ == "__main__":
        unittest.main()