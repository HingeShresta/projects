import random
import string
import secrets

print("🔐 Smart Password Generator")

# Get valid password length
while True:
    try:
        length = int(input("Enter password length (8-128 recommended): "))
        if length <= 0:
            print("❌ Password length must be positive. Try again.")
        elif length < 8:
            print("⚠️  Warning: Short passwords are weak. Continue? (y/n): ")
            if input().lower() == 'y':
                break
        elif length > 128:
            print("⚠️  Warning: Very long passwords may be impractical. Continue? (y/n): ")
            if input().lower() == 'y':
                break
        else:
            break
    except ValueError:
        print("❌ Please enter a valid number.")

# Use cryptographically secure random generator
characters = string.ascii_letters + string.digits + string.punctuation
password = "".join(secrets.choice(characters) for _ in range(length))

print("\n✅ Generated Password:", password)
print(f"📏 Length: {len(password)} characters")

# Optional: Check password strength
def check_strength(pwd):
    if len(pwd) < 8:
        return "Weak 🔴"
    elif any(c.islower() for c in pwd) and any(c.isupper() for c in pwd) and any(c.isdigit() for c in pwd) and any(c in string.punctuation for c in pwd):
        return "Strong 🟢"
    else:
        return "Medium 🟡"

print(f"💪 Strength: {check_strength(password)}")

save = input("\n💾 Save password to file? (y/n): ")
if save.lower() == "y":
    with open("passwords.txt", "a") as file:
        file.write(password + "\n")
    print("✅ Password saved successfully to 'passwords.txt'!")