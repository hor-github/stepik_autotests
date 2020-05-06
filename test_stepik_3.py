# -*- coding: utf-8 -*-
'''
Ожидания и с сообщения об ошибках
'''
import unittest

# составные сообщения об ошибках и поиск подстроки
# содержится ли сабстринг в фулстроке
def test_substring(full_string, substring):
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"

# рассмотрели вариант запуска тестов
#def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

#def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"

#if __name__ == "__main__":
#    test_abs1()
#    test_abs2()
#    print("Everything passed")

# Использование unittest
class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")

if __name__ == "__main__":
    unittest.main()


"""3.5 PyTest - маркировка"""
