# Luhn Check Or Mod 10 Check
This algorithm is useful to determine whether a card number
is entered correctly by a scanner

It works in the following way:
Valid credit card numbers would have 13 to 16 digits and the numbers must start with
4 for visa cards, 5 for Master cards, 37 fro American Express cards and
6 for Discover cards

# "Sum of Double Even Places"
Once the card is validated by the above conditions, double every second digit from 
right to left. If doubling a digit results in a two-digit number, add up the two digits
to get a single digit number. Example: 8*2 = 16 (1+6 = 7)
Once all single digits are found, add them up

# "Sum Of Odd Places"
Add all digits in the odd places from right to left in the credit card number

# "Total Sum"
Then add the sum of double even places and sum of odd places

Then if the total sum is divisible by 10 then the number is valid, otherwise
its invalid
