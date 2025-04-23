def create_vcard():
    # Accept contact details from the user
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email Address: ")
    address = input("Enter Address: ")

    # Create a vCard formatted string
    vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
ADR:{address}
END:VCARD"""

    # Save the vCard to a file
    filename = f"{name.replace(' ', '_')}_contact.vcf"
    with open(filename, "w") as file:
        file.write(vcard)
    
    print(f"vCard created successfully! The file is saved as '{filename}'.")

# Call the function to create the vCard
create_vcard()
