import bcrypt


def hash_password(password):
    """Hashes a password securely using bcrypt"""
    salt = bcrypt.gensalt()  # Generate a random salt
    hashed_password = bcrypt.hashpw(password.encode(), salt)  # Hash the password
    return hashed_password

def verify_password(password, hashed_password):
    """Verifies if a password matches its hashed version"""
    return bcrypt.checkpw(password.encode(), hashed_password)

# Example usage
if __name__ == "__main__":
    # Hash a password
    user_password = "MySecurePassword123"
    hashed_pw = hash_password(user_password)
    is_valid = verify_password(user_password, hashed_pw)
    print("Hashed Password:", hashed_pw)
# Verify the password
    print("Password verification result:", is_valid)
