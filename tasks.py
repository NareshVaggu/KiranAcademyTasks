# Task 1: Hello World with Name
YOUR_NAME = "Naresh Govind Vaggu"
print("hello world ... by", YOUR_NAME)
print("-" * 40)


# Task 2: Calculate Profit or Loss
cost_price = 450
selling_price = 550

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit:", profit)
elif cost_price > selling_price:
    loss = cost_price - selling_price
    print("Loss:", loss)
else:
    print("No Profit, No Loss")
print("-" * 40)


# Task 3: Check Even or Odd Number
num = 7

if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")
print("-" * 40)


# Task 4: Check Voting Eligibility with valid age check
age = 20

if age >= 0 and age <= 120:
    if age >= 18:
        print("Age is valid and eligible for voting")
    else:
        print("Age is valid but NOT eligible for voting")
else:
    print("Invalid age!")
print("-" * 40)


# Task 5: Check if Two Words are Anagrams
word1 = "listen"
word2 = "silent"

clean_word1 = word1.replace(" ", "").lower()
clean_word2 = word2.replace(" ", "").lower()

if sorted(clean_word1) == sorted(clean_word2):
    print("Task 5:", word1, "and", word2, "are Anagrams")
else:
    print("Task 5:", word1, "and", word2, "are NOT Anagrams")