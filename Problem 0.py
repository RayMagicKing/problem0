name = input("Name: ")
age = input("Age: ")
pronouns = {
    "M": "he",
    "F": "she",
    "O": "they"
}
gender = input("What is your gender? (M)/(F) ").strip().upper()
pronoun = pronouns.get(gender, pronouns['O'])
like_age = input("Like your age? (Y)/(N) ")
print(f"There was once someone named {name},")
print(f"{pronoun} was {age} years old.")
print(f"{pronoun.title()} really liked the name {name},")
if like_age.upper() == "Y":
    print(f"and {pronoun} liked being {age}.")
elif like_age.upper() == "N":
    print(f"and {pronoun} didn't like being {age}.")
else:
    print(f"and {pronoun} wasn't sure {pronoun} liked being {age}.")
