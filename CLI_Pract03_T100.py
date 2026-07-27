import hmac
import hashlib

# ------------------ Functions ------------------ #

def generate_mac(message, secret_key):
    """
    Generate HMAC-SHA256 MAC
    """
    return hmac.new(
        secret_key.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()


def verify_mac(message, secret_key, received_mac):
    """
    Verify HMAC-SHA256 MAC
    """
    computed_mac = generate_mac(message, secret_key)
    return hmac.compare_digest(computed_mac, received_mac)


# ------------------ Main Program ------------------ #

def main():
    while True:
        print("\n" + "=" * 60)
        print("      MESSAGE AUTHENTICATION CODE (MAC) SYSTEM")
        print("=" * 60)
        print("1. Generate MAC")
        print("2. Verify MAC")
        print("3. Exit")
        print("=" * 60)

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            print("\n------ Generate MAC ------")

            message = input("Enter Message      : ")
            secret_key = input("Enter Secret Key   : ")

            mac = generate_mac(message, secret_key)

            print("\nGenerated MAC")
            print("-" * 60)
            print(mac)
            print("-" * 60)

        elif choice == "2":
            print("\n------ Verify MAC ------")

            message = input("Enter Message            : ")
            secret_key = input("Enter Secret Key         : ")
            received_mac = input("Enter MAC to Verify      : ")

            if verify_mac(message, secret_key, received_mac):
                print("\n✅ MAC Verification Successful")
                print("Message is Authentic.")
            else:
                print("\n❌ MAC Verification Failed")
                print("Message has been Tampered or Secret Key is Incorrect.")

        elif choice == "3":
            print("\nThank you for using the MAC Authentication System.")
            break

        else:
            print("\nInvalid Choice! Please enter 1, 2 or 3.")


# ------------------ Start Program ------------------ #

if __name__ == "__main__":
    main()
