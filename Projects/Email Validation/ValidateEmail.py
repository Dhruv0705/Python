
class StringFunction:
    '''
    Function that verifies if a given email address is valid or not. 
        It does this by checking several conditions and printing "Valid Email" 
        if the input meets all the conditions or "Invalid Email" if any of the conditions are not met.

    Conditions:
        The first condition checks if the email address has at least 6 characters.
        The second condition checks if the first character is a letter.
        The third condition checks if the email address contains exactly one "@" symbol.
        The fourth condition checks if the email address ends with either ".com" or ".net".
        The fifth condition checks if the email address contains any spaces, uppercase letters, or any characters that are 
            not letters, digits, "_", ".", or "@". If it does, the email is considered invalid.
        Finally, if all the conditions are met, the function prints "Valid Email". If any of the conditions are not met, 
            it prints "Invalid Email".
    '''

    # prompts the user to enter their email
    Email = input("Enter Your Email : ") 

    # Initialize three variables j, k, l to 0
    j, k, l = 0, 0, 0

    # Check if the length of the email is greater than or equal to 6
    if len(Email) >= 6:

        # Check if the first character of the email is a letter
        if Email[0].isalpha():

            # Check if the email contains the "@" symbol and that it only appears once
            if "@" in Email and Email.count("@") == 1:

                # Check if either the fourth to last or third to last characters are "."
                if (Email[-4]==".") ^ (Email[-3]=="."):
                    
                    # Loop through each character in the email
                    for i in Email:

                        # If the character is a space, set j to 1
                        if i==i.isspace():
                            j = 1

                        # If the character is a letter
                        elif i.isalpha():

                            # Check if the letter is uppercase, if it is set k to 1
                            if i==i.upper():
                                k = 1

                        # If the character is a digit, do nothing
                        elif i.isdigit():
                            continue

                        # If the character is "_", ".", or "@", do nothing
                        elif i =="_" or i =="." or i =="@":
                            continue

                        # If the character is none of the above, set l to 1
                        else:
                            l = 1

                    #print(f"Valid Email: {Email}")

                    # Check if any of the variables j, k, or l are equal to 1
                    if j == 1 or k == 1 or l == 1:

                        # If any are equal to 1, print "Invalid Email: {Email}"
                        print(f"Invalid Email: {Email}")
                    
                    # If none are equal to 1, print "Valid Email: {Email}"
                    else:
                        print(f"Valid Email: {Email}")
                
                # If the fourth to last or third to last characters are not ".", print "Invalid Email : {Email}"
                else:
                    print(f"Invalid Email : {Email}")
            
            # If the email does not contain "@" or it appears more than once, print "Invalid Email : {Email}"
            else:
                print(f"Invalid Email : {Email}")
        
        # If the email does not contain "@" or it appears more than once, print "Invalid Email : {Email}"
        else:
            print(f"Invalid Email: {Email}")
    
    # If the email length is less then six characters, print "Invalid Email: {Email}"
    else:
        print(f"Invalid Email: {Email}")

class RegularExpression:
    import re
    EmailCondition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w{2,3}$"
    UserEmail = input("Enter Your Email: ")
    
    if re.search(EmailCondition, UserEmail):
        print("Valid Email")
    else:
        print("Invalid Email")

        