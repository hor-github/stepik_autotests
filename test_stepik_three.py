# -*- coding: utf-8 -*-
'''
Ожидания
'''


# составные сообщения об ошибках и поиск подстроки
# содержится ли сабстринг в фулстроке
def test_substring(full_string, substring):
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"

def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

if __name__ == "__main__":
    test_abs1()
    print("All tests passed!")