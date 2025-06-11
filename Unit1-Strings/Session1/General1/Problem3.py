
#Character	Catchphrase
# "Pooh"	"Oh bother!"
# "Tigger"	"TTFN: Ta-ta for now!"
# "Eeyore"	"Thanks for noticing me."
# "Christopher Robin"	"Silly old bear."
def print_catchphrase(character):
    if(character == "Pooh"):
        print("Oh bother!")
    elif (character == "Tigger"):
        print("TTFN: Ta-ta for now!")
    elif(character == "Eeyore"):
        print("Thanks for noticing me.")
    elif(character == "Christopher Robin"):
        print("Silly old bear.")
    else :
        print("Sorry! I don't know <character>'s catchphrase!")
     
character = "Pooh"
print_catchphrase(character)

character = "Piglet"
print_catchphrase(character)

