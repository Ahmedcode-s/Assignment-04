import hashlib

def hash_pass(password):
    return hashlib.sha256(password.encode()).hexdigest()
    
stored_logins = {
    "userexample@gmail.com":hash_pass("password123"),
    "adminexample@gmail.com":hash_pass("admin123")
}

def login(email , password):
    if email in stored_logins:
        return stored_logins[email] == hash_pass(password)
    return False

if __name__ == "__main__":
    
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if login(email , password):
        print("Login successful!")
    else:
        print("Invalid email or password.")


