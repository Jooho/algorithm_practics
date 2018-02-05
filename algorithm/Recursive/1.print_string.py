'''
date: 2018.2.2
description:
  글자를 그대로 출력하거나 거꾸러 출력하는 예제
  for문을 이용하는 방법과 recursive를 이용하는 방법

'''


class DisplayString():


    def forward_iter_way(self, test_string):
        for char in self.test_string:
            print(char, end=" ")
        print("\n")


    def forward_recursive_way(self, test_string, backward=False):
        if (len(test_string) == 0):
            print("\n")
            return 0
        else:
            if (not backward):
                print(test_string[0], end=" ")

            # print(self.test_string[1:])
            self.forward_recursive_way(test_string[1:],backward)
            if (backward):
                print(test_string[0], end=" ")


displayStringInstance = DisplayString()
# For statement
# DisplayString.forward_iter_way("This is test string")

# Recursive
displayStringInstance.forward_recursive_way("This is test string", True)
