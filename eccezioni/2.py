'''Password Validation:  Write a function validate_password(password) that checks whether a password meets the following criteria:
Minimum length of 20 characters, At least three uppercase letters, At least four special characters (non-alphanumeric).
If the password is valid, the function should return True.
If the password is invalid, the function should raise a built-in exception (e.g., ValueError) with a message indicating which criteria were not met.
'''
import string

def validate_password(password:str):

    if len(password)<20:
        raise ValueError("Password too short, must be at least 20 characters long")
    
    upper_count=0
    non_alpha_count=0

    for c in password:
        if c in list(string.ascii_uppercase):
            upper_count+=1
        if c in ["!","$","%","&","/","?",".","-","_"]:
            non_alpha_count+=1

    if upper_count<3:
            raise ValueError("Password must have at least 3 uppercase letters")
    if non_alpha_count<4:
            raise ValueError("Password must have at least 4 non aplhanumerical characters")
        
    return True
    

print(validate_password("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhHHH"))
        
        
    

