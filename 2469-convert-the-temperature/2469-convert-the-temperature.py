class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        ans=[]
        kelvin = celsius + 273.15
        ans.append(kelvin)
        Fahrenhit = celsius * 1.80 + 32.00
        ans.append( Fahrenhit)

        return ans
