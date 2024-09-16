# word = input("Enter a word\n")
# valid = False

# if 'a'<=word[0]<='z':
#     if word[0]==word[-1]:
#         valid = True


# print(valid)

# def print_multiplication_table(number):
#     """
#     Prints the multiplication table for the given number up to 10.
    
#     Parameters:
#     number (int): The number for which the multiplication table is to be printed.
#     """
#     up_to = 10  # Default range for the multiplication table
#     print(f"Multiplication table for {number}:")
#     for i in range(1, up_to + 1):
#         print(f"{number * i}")

# # Example usage
# user_input = int(input("Enter a number to print its multiplication table: "))
# print_multiplication_table(user_input)

# def prime(lower_limit, upper_limit):
#     count = 0
#     numbers = list(range(lower_limit, upper_limit))
#     for i in range(lower_limit, upper_limit//2):
#         if numbers[:] % i == 0:
#             count +=1

#     print("ThePri")



# def is_prime(n):
#     if n <= 1:
#         return False
#     if n == 2 or n == 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# def print_primes_between(l, r):
#     primes = []
#     for num in range(l, r+1):
#         if is_prime(num):
#             primes.append(num)
#     return primes

# # Example usage:
# l = int(input("Enter  the lower limit: "))
# r = int(input("enter the upper limit"))
# print(print_primes_between(l, r))

# def sum_of_even_numbers(num):
#     sum_even = 0
#     for i in range(1, num + 1):
#         if i % 2 == 0:
#             sum_even += i
#     return sum_even

# # Example usage:
# num = int(input())
# result = sum_of_even_numbers(num)
# print(result)


# user_age = -3
# print("Strating before the if block")
# if user_age <0 or user_age>100:
#     print("Invalid age")
# elif user_age>5:   
#     print("Access denied.")
# elif user_age>10:
#     print("Hello")
# else:
#     print("inside the block")

# print("Outside the block")

# n = int(input())

# # use for loop to iterate from 1 to n+1 (exclusive) 
# for i in range(1,n+1):

#     # if number is even, skip printing of number
#     if i%2==0:
#         continue

#     # print number
#     print(i)

# heat = {'a':1, 'b':2}
# heat ['c']=3

# print(heat)

from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "Summarize content you are provided with for a second-grade student."
    },
    {
      "role": "user",
      "content": "Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter.[19] When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows,[20] and is on average the third-brightest natural object in the night sky after the Moon and Venus."
    }
  ],
  temperature=0.7,
  max_tokens=64,
  top_p=1
)















