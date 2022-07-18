class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = []
        if n <= 10000 and n >= 1:
            for i in range(1, n + 1):
                as_str = ""
                if i % 3 == 0 and i % 5 == 0:
                    as_str = as_str + "FizzBuzz"
                    answer.append(as_str)
                elif i % 3 == 0:
                    as_str = as_str + "Fizz"
                    answer.append(as_str)
                elif i % 5 == 0:
                    as_str = as_str + "Buzz"
                    answer.append(as_str)
                else:
                    answer.append(str(i))
        return answer