# Author: Hussein Parpia (hparpia8)

# Luhn Check or Mod 10 check
# This algorithm is useful to determine whether a card number
# is entered correctly by a scanner
# 
# It works in the following way:
# Valid credit card numbers would have 13 to 16 digits and the numbers must start with
# 4 for visa cards, 5 for Master cards, 37 fro American Express cards and
# 6 for Discover cards
#
#   "Sum of Double Even Places"
# Once the card is validated by the above conditions, double every second digit from 
# right to left. If doubling a digit results in a two-digit number, add up the two digits
# to get a single digit number. Example: 8*2 = 16 (1+6 = 7)
# Once all single digits are found, add them up
#   
#   "Sum Of Odd Places"
# Add all digits in the odd places from right to left in the credit card number
#
#   "Total Sum"
#  Then add the sum of double even places and sum of odd places
#
#  Then if the total sum is divisible by 10 then the number is valid, otherwise
# it's invalid
#---------------------------------------------------------------------------------------------------------------------

# Returns True if the card number is valid
def isValid(number):
    if (getSize(number) >= 13 and getSize(number) <= 16 and number>0):
        if (prefixMatched(number,4) or prefixMatched(number,5) or prefixMatched(number,37) or prefixMatched(number,6)):
            return True
        else:
            return False
        
    return False

# Returns the sum of double of even places from right to left
def sumOfDoubleEvenPlace(number):
    digits = [int(x) for x in str(number)] #Converts the number to an array of integers
    digits.reverse()
    sum = 0
    for i in range(1,len(digits), 2):
        sum += getDigit(2*digits[i]) 
    return sum

# Return sum of odd place digits in number from right to left
def sumOfOddPlace(number):
    digits = [int(x) for x in str(number)] #Converts the number to an array of integers
    digits.reverse()
    sum = 0
    for i in range(0,len(digits), 2):
        sum += getDigit(digits[i])
    return sum

# Return True if the digit d is a prefix for number
def prefixMatched(number,d):
    if d == getPrefix(number,getSize(d)):
        return True
    else:
        return False


# Return this number if it is a single digit, otherwise, return
# the sum of the two digits
def getDigit(number):
    if getSize(number)==1:
        return number
    else:
        digit1 = number // 10
        digit2 = number - digit1*10
        return digit1 + digit2

# Return the number of digits in d
def getSize(d):
    n = 0
    while(d > 0):
            n = n+1
            d = d//10
    return n


# Return the first k digits from number.  If the number
# of digits in number is less than k, return number
def getPrefix(number,k):
    if getSize(number) <= k:
        return number
    else:
        digits = [int(x) for x in str(number)]
        new_number = 0
        for i in range(0,k):
            new_number = digits[i]*10**(k-(i+1)) + new_number
            
        return new_number


def main():
    number = int(input("Enter the credit card number: "))
    if(isValid(number)):
        even = sumOfDoubleEvenPlace(number)
        odd = sumOfOddPlace(number)
        sum = even + odd

        if(sum % 10 == 0):
            print("The credit card number in valid")

        else:
            print("The credit card number is invalid")
    else:
        print("The number is invalid")


main()














