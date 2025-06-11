# Problem 2: Mad Libs
# Write a function madlib() that accepts one parameter, a string verb. The function should print the sentence: "I have one power. I never <verb>. - Batman".

def madlib(verb):
	print(f"I have one power. I never {verb}. - Batman")
# Example Usage

verb = "give up"
madlib(verb)

verb = "nap"
madlib(verb)
# Example Output:

# "I have one power. I never give up. - Batman"
# "I have one power. I never nap. - Batman"