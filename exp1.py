#program to find the number is palindrome or not 
number=int(input("number"))
rev_number=number[::-1]
if number==rev_number:
  print("palindrome number")
elif number!=rev_number:
  print("not a palindrome")
