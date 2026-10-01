print("Hello this is a password strength checker!")
# This is a code for strength of password based on length of a password only.
# The length of password is the most important aspect of in determining the password strength.
# The longer the password the more different possible combination more time taken to hack the password.
# In a typical password 92 character are allowed and in this we are going to assume we can choose any characters however many times we want and therfore there is 92^^length of password number of possible combinations.
# however a computer/a hacker can try large number per second and even passwords with large possible combination don't take that long to crack espcially if there a key board pattern or it is common password etc. 

password_ = input("enter a password to check: ")
Password_strength_score =
Num = ['0','1','2','3','4','5','6','7','8','9','10']
Specialcha_racter = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                     '-', '_', '=', '+', '[', ']', '{', '}', ';', ':',
                     "'", '"', ',', '.', '<', '>', '/', '?', '\\', '|', '`']

def length_ofpassword(password, Password_strength_score):
    length_ofpassword = len(password)
    if length_ofpassword < 6:
        Password_strength_score += 0
        print(f"Password length is too short therefore a score of 0 is given.Password has a length of {length_ofpassword}.") 
    elif length_ofpassword == 6 or length_ofpassword == 7:
        Password_strength_score += 5
        print(f"Your password has a {length_ofpassword} characters so there are {92**length_ofpassword} possible password.Length of your password is short and so small score of 5 is given.")
    elif length_ofpassword == 8 or length_ofpassword == 9:
        Password_strength_score += 20
        print(f"Your password has a {length_ofpassword} characters so there are {92**length_ofpassword} possible password.Length of your password is on the shorter side and so smaller score 20 is given.")
    elif length_ofpassword == 10 or length_ofpassword == 11:
        Password_strength_score += 50
        print(f"Your password has a {length_ofpassword} characters so there are {92**length_ofpassword} possible password.Length of your password is on the medium side and so medium score of 50 is given.")
    elif length_ofpassword == 12 or length_ofpassword == 13:
        Password_strength_score += 60
        print(f"Your password has a {length_ofpassword} characters so there are {92**length_ofpassword} possible password.Length of your password is on the longer side and so higher score of 60 is given.")
    elif length_ofpassword == 14 or length_ofpassword == 15:
        Password_strength_score += 65
        print(f"Your password has a {length_ofpassword} characters so there are {92**length_ofpassword} possible password.Length of your password is long and a high score of 65 is given.")
    else:
        Password_strength_score += 80
        print("Your password length exceeds 15 character.Good job!")

# Compute the length score
length_ofpassword(password_, Password_strength_score)

# Checking for special characters in the password
expectation = True
for x in Specialcha_racter:
    if expectation:
        for t in password_.lower():
            if t == x:
                Password_strength_score += 5
                expectation = False
                break 

otherexpecatation = True
for x in Num:
    if otherexpecatation:
        for t in password_.lower():
            if t == x:
                Password_strength_score += 5
                otherexpecatation = False
                break
                
if password_ != password_.lower():
    Password_strength_score += 5
    print("Contains a capital letters.")

# Code for checking character substitution patterns
def nrmalised_password(password):
    password = password_.lower()
    replacements = {
        "@": "a",
        "0": "o",
        "1": "i",
        "$": "s",
    }
    normalised_password = ""
    for k in password:
        if k in replacements:
            normalised_password += replacements[k]
            print(f"Character substitution is detected {k} is detected.")
        else:
            normalised_password += k
    return normalised_password        

cleanpassword = nrmalised_password(password_)

# Code for Dictionary words checks
dictionarys_words = []
try:
    with open("dictionary.txt", "r") as f:
        line = f.readline()
        while line != "":
            line = line.strip().lower()
            dictionarys_words.append(line)
            line = f.readline()
except FileNotFoundError:
    print("File is not found.")

# Penalty for using dictionary words
exact_match_found = False
for word in dictionarys_words:
    if cleanpassword == word.lower():
        Password_strength_score -= 80
        print("Given password is the same as one of the words in the dictionary so 80 points are deducted!")
        exact_match_found = True
        break

if not exact_match_found:
    for p in dictionarys_words:
        if len(p) >= 4 and p in cleanpassword:
            Password_strength_score -= 20
            print("A dictionary word is found on the password and so a score of 20 points will be deducted.")
            break

# Common password checker
common_password = ["123456", "password", "qwerty", "abc123", "letmein", "welcome", "football", "admintelecom", "trustno1", "michael", "superman", "asdfghjkll", "wers"]

# Scenario 1: Password exactly matches a common password
is_exactmatch = False
for x in common_password:
    if cleanpassword == x:
        Password_strength_score -= 80
        print("The password is the exact same as a common password. So a score of 80 points will be deducted.")
        is_exactmatch = True

# Scenario 2
if not exact_match_found:
    for x in common_password:
        if x in cleanpassword:
            Password_strength_score -= 20
            print("A common word is found within your password.So 20 points will be deducted.")
            break

# Score constraint checks
if Password_strength_score < 0:
    Password_strength_score = 0
    print("A score of 0 is given for your password. Consider changing it based on the feedback given!")   

if Password_strength_score > 100:
    Password_strength_score = 100

print(f"Final Password score: {Password_strength_score}/100.")    

if Password_strength_score >= 90:
    print("Password strength: Very Strong.")
    print("this password has many characters and will take a long time to crack.")
elif Password_strength_score >= 70:
    print("This password is strong.") 
    print("This has an good security overall.safe option to keep as a password.") 
elif Password_strength_score >= 50:
    print("Password strength: Moderate.")
    print("this has a reasonable security but could still be improved.")
elif Password_strength_score >= 40:
    print("Password strength:  Weak.")
    print("The password may be short and contain a predictable pattern also may also have a common word used in passwords.")
else:
    print("Password strength: Very weak")
    print("this password would be cracked very quickly.")
