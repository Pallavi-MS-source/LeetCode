class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        answer=[]
        i=0
        for i in range (1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                ans = "FizzBuzz"
            elif i % 3 == 0:
                ans = "Fizz"
            elif i % 5 == 0:
                ans = "Buzz"
            else:
                ans = str(i)
            answer.append(ans)
        return answer
                


     
      
        