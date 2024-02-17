from fastapi import HTTPException
from password_strength import PasswordStats

def check_password_strength(password):
    result = PasswordStats(password)
    strength = result.strength()  
    
    if (strength < 0.5):
        password_strength = "Weak password"
    else:
        password_strength = "Strong password"
             
    return password_strength, strength
