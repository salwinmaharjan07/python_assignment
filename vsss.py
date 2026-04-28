# 1
# name = 'rahUl Dahal'
# formatted_name = name.title()
# print(formatted_name)

# 2
password = "Pass@123"
print(password.lower())

# 3
movie = "spider-man no way home"
print(movie.title())

# 4
# ⁠Display heading in ALL CAPS
heading = "annual sports day"
print(heading.upper())

# 5
# Swap case of every letter
text = "hELLO wORLD"
print(text.swapcase())
# String Search & Check Methods

# 6
# Find first position of 'error'
log = "System error detected, error code 404"
print(log.find("error"))   # returns first occurrence index

# 7
# Check if email ends with @gmail.com
email = "user@gmail.com"

if email.endswith("@gmail.com"):
    print("Valid Gmail address")
else:
    print("Invalid email domain")

# 8
# Count occurrences of 'free'
message = "Get free stuff, free gifts and free coupons now!"
print(message.count("free"))

# 9
# Check if URL starts with https
url = "https://example.com"

if url.startswith("https"):
    print("Secure website")
else:
    print("Not secure")

# 10
# Resume scanner using in operator
resume = "I have experience in Java, C++, and Python development"

if "Python" in resume:
    print("Keyword found")
else:
    print("Keyword not found")

# 11
# Check if 'Python' is present in resume (using in operator)
resume = "I have experience in Java and Python development"

if "Python" in resume:
    print("Keyword found")
else:
    print("Keyword not found")

# 12
# Find position of 'FAILED' using index()
log = "Transaction FAILED due to low balance"
print(log.index("FAILED"))

# 13
# Check if file is a PDF using endswith()
file_name = "budget_report.pdf"
print(file_name.endswith(".pdf"))
 
# 14
# Check if URL belongs to government website
url = "https://www.moha.gov.np/"

if ".gov.np" in url:
    print("Government website")
else:
    print("Not a government website")

# 15
# Remove extra spaces using strip()
feedback = " Great service! "
print(feedback.strip())

# 16
# Replace banned word using replace()
message = "I hate this, hate it completely"
print(message.replace("hate", "**"))

# 17
# Remove leading slashes using lstrip()
filename = "///student_records.pdf "
print(filename.lstrip("/ "))

# 18
# Clean price string using rstrip() and replace symbols
price = "Price: $120.33   "

clean_price = price.rstrip().replace("Price: $", "")
print(clean_price)


# 19
# Remove dashes using replace()
phone = "+977 984-345-4667"
print(phone.replace("-", ""))

# 20
# Split CSV data and print each field
data = "Aarav,22,Kathmandu,Computer Science"

fields = data.split(",")

for item in fields:
    print(item)

# 21
# Add # prefix using join()
hashtags = "Python, Coding, Nepal, Tech"

words = hashtags.split(", ")

result = " ".join("#" + word for word in words)
print(result)

# 22
# Count passengers using split()
passengers = "Ram, Shyam, Hari, Sita"

names = passengers.split(", ")
print(len(names))

# 23
# Build sentence using join()
words = ['The', 'flight', 'departs', 'at', '6AM']

sentence = " ".join(words)
print(sentence)
# String Validation Methods

#24
#24
# Check if age contains only digits (isdigit())
age = "25abc"

if age.isdigit():
    print("Valid age")
else:
    print("Invalid age")

#25
# Username contains only letters and numbers (isalnum())
username = "User123"

if username.isalnum():
    print("Valid username")
else:
    print("Invalid username")


#26
# Name contains only alphabets (isalpha())
name = "Aarav"

if name.isalpha():
    print("Valid name")
else:
    print("Invalid name")



#27
# Check if PIN is uppercase (isupper())
pin = "ASDF"

if pin.isupper():
    print("Valid PIN")
else:
    print("Invalid PIN")

# 28
# Check if input is only spaces (isspace())
field = "   "

if field.isspace():
    print("Field is empty")
else:
    print("Field has data")