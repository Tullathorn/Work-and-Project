import mysql.connector

#[1]
def add_pet(cursor, db):
    pet_id = input("Enter PetID: ")
    pet_name = input("Enter Pet Name: ")
    pet_type = input("Enter Pet Type: ")
    weight = input("Enter Pet Weight: ")
    sex = input("Enter Pet Sex: ")
    owner_phone = input("Enter Owner Phone Number: ")
    prescription_number = input("Enter Prescription Number: ")
    info_number = input("Enter Info Number: ")
    
    try:
        cursor.execute("INSERT INTO petInfo (PetID, OwnerPhoneNumber, Type, PetName, InfoNumber) VALUES (%s, %s, %s, %s, %s)", (pet_id, owner_phone, pet_type, pet_name, info_number))
        cursor.execute("INSERT INTO pet (PetID, PetName, Weight, Sex, PrescriptionNumber) VALUES (%s, %s, %s, %s, %s)", (pet_id, pet_name, weight, sex, prescription_number))
        db.commit()
        print("\nData added successfully!")
    except mysql.connector.Error as err:
        print(f"\nError: {err}")
        db.rollback()
    
#[2]
def add_treatment_record(cursor, db):
    pet_id = input("Enter PetID: ")
    vet_phone = input("Enter Veterinarian Phone Number: ")
    date_time = input("Enter Date and Time: ")
    treatment = input("Enter Treatment: ")
    treatment_costs = input("Enter Treatment Costs: ")
    
    try:
        cursor.execute("INSERT INTO treatmentRecord (PetID, VeterinarianPhoneNumber, DateAndTime, Treatment, TreatmentCosts) VALUES (%s, %s, %s, %s, %s)", (pet_id, vet_phone, date_time, treatment, treatment_costs))

        db.commit()
        print("\nData added successfully!")
    except mysql.connector.Error as err:
        print(f"\nError: {err}")
        db.rollback()    

#[3]
def add_owner(cursor, db):
    owner_phone = input("Enter Owner Phone Number: ")
    owner_name = input("Enter Owner Name: ")
    owner_address = input("Enter Owner Address: ")
    
    try:
        cursor.execute("INSERT INTO owner (OwnerPhoneNumber, OwnerName, Address) VALUES (%s, %s, %s)", (owner_phone, owner_name, owner_address))
        db.commit()
        print("\nData added successfully!")
    except mysql.connector.Error as err:
        print(f"\nError: {err}")
        db.rollback()

#[4]
def delete_pet_and_treatment(cursor, db):
    pet_id = input("Enter PetID to delete: ")
    
    cursor.execute("SELECT * FROM pet WHERE PetID = %s", (pet_id,))
    pet_exists = cursor.fetchone()
    
    if not pet_exists:
        print("\nPetID not found.")
        return
    
    try:
        cursor.execute("DELETE FROM treatmentRecord WHERE PetID = %s", (pet_id,))
        cursor.execute("DELETE FROM pet WHERE PetID = %s", (pet_id,))
        cursor.execute("DELETE FROM petInfo WHERE PetID = %s", (pet_id,))
        db.commit()
        print("\nPet and related treatment records deleted successfully!")
    except mysql.connector.Error as err:
        print(f"\nError: {err}")
        db.rollback()

#[5]
def delete_owner(cursor, db):
    owner_phone = input("Enter Owner Phone: ")

    cursor.execute("SELECT * FROM owner WHERE OwnerPhoneNumber = %s", (owner_phone,))
    phone_exists = cursor.fetchone()

    if not phone_exists:
        print("\nPhone Number not found.")
        return
    
    try:
        cursor.execute("DELETE FROM owner WHERE OwnerPhoneNumber = %s", (owner_phone,))
        db.commit()
        print("\nOwner records deleted successfully!")
    except mysql.connector.Error as err:
        print(f"\nError: {err}")
        db.rollback()

#[6]
def view_pet_name(cursor):
    pet_id = input("Enter PetID to view pet's name: ")
    query = "SELECT PetID, PetName FROM pet WHERE PetID = %s";

    cursor.execute(query, (pet_id,))
    results = cursor.fetchone()

    if results:
        col1_width = 25
        col2_width = 25
        print("\n" + "PetID".ljust(col1_width) + "PetName".ljust(col2_width))
        print("-" * (col1_width + col2_width))

        print(f"\n{results[0]:<25}{results[1]:<25}")
    else:
        print("\nNo records found for the given PetID.")
    

#[7]
def view_treatment_by_pet(cursor):
    pet_id = input("Enter PetID to view treatment records: ")
    query = """
    SELECT pet.PetID, pet.PetName, treatmentRecord.Treatment
    FROM pet
    LEFT JOIN treatmentRecord ON pet.PetID = treatmentRecord.PetID
    WHERE pet.PetID = %s;
    """
    cursor.execute(query, (pet_id,))
    results = cursor.fetchall()
    
    if results:
        col1_width = 25
        col2_width = 25
        col3_width = 25
        print("\n" + "PetID".ljust(col1_width) + "PetName".ljust(col2_width) + "Treatment".ljust(col3_width))
        print("-" * (col1_width + col2_width + col3_width))

        for row in results:
            print(f"\n{str(row[0]):<25}{str(row[1]):<25}{str(row[2]):<25}")
    else:
        print("\nNo records found for the given PetID.")

#[8]
def view_all_treatment_records(cursor):
    query = """
    SELECT pet.PetID, pet.PetName, treatmentRecord.Treatment
    FROM pet
    LEFT JOIN treatmentRecord ON pet.PetID = treatmentRecord.PetID;
    """
    cursor.execute(query)
    results = cursor.fetchall()
    
    col1_width = 25
    col2_width = 25
    col3_width = 25
    print("\n" + "PetID".ljust(col1_width) + "PetName".ljust(col2_width) + "Treatment".ljust(col3_width))
    print("-" * (col1_width + col2_width + col3_width))

    for row in results:
        print(f"\n{str(row[0]):<25}{str(row[1]):<25}{str(row[2]):<25}")

#[9]
def view_owner_by_pet(cursor):
    pet_id = input("Enter PetID to view owner details: ")
    query = """
    SELECT owner.OwnerName, petInfo.PetName, owner.OwnerPhoneNumber, owner.Address
    FROM owner
    LEFT JOIN petInfo ON owner.OwnerPhoneNumber = petInfo.OwnerPhoneNumber
    WHERE petInfo.PetID = %s;
    """
    cursor.execute(query, (pet_id,))
    results = cursor.fetchall()
    
    if results:
        col1_width = 25
        col2_width = 25
        col3_width = 25
        col4_width = 50
        print("\n" + "Owner".ljust(col1_width) + "PetName".ljust(col2_width) + "Phone".ljust(col3_width) + "Address".ljust(col4_width))
        print("-" * (col1_width + col2_width + col3_width + col4_width))

        for row in results:
            address = str(row[3])[:col4_width] + "..." if len(str(row[3])) > col4_width else str(row[3])
            print(f"\n{str(row[0]):<25}{str(row[1]):<25}{str(row[2]):<25}{address:<50}")
    else:
        print("\nNo owner found for the given PetID.")

#[10]
def view_all_owners_and_pets(cursor):
    query = """
    SELECT owner.OwnerName, petInfo.PetName
    FROM owner
    LEFT JOIN petInfo ON owner.OwnerPhoneNumber = petInfo.OwnerPhoneNumber;
    """
    cursor.execute(query)
    results = cursor.fetchall()
    col1_width = 25
    col2_width = 25
    print("\n" + "Owner".ljust(col1_width) + "PetName".ljust(col2_width))
    print("-" * (col1_width + col2_width))

    for row in results:
        print(f"\n{str(row[0]):<25}{str(row[1]):<25}")

# Main menu
def main():
    try:
        db = mysql.connector.connect(
            host="134.209.101.105",
            user="group36",
            password="password36",
            database="db_group36"
        )
        cursor = db.cursor()
        
        while True:
            print("\n===== Veterinary Clinic Menu =====")
            print("1. Add Pet")
            print("2. Add Treatment Record")
            print("3. Add Owner")
            print("4. Delete Pet and Treatment Record")
            print("5. Delete Owner Record")
            print("6. View Pet's Name")
            print("7. View Treatment Records by PetID")
            print("8. View All Treatment Records")
            print("9. View Owner Details by PetID")
            print("10. View All Owners and Their Pets")
            print("11. Exit")

            choice = input("\nSelect an option (1-11): ")

            if choice == "1":
                add_pet(cursor, db)
            elif choice == "2":
                add_treatment_record(cursor, db)
            elif choice == "3":
                add_owner(cursor, db)
            elif choice == "4":
                delete_pet_and_treatment(cursor, db)
            elif choice == "5":
                delete_owner(cursor, db)
            elif choice == "6":
                view_pet_name(cursor)
            elif choice == "7":
                view_treatment_by_pet(cursor)
            elif choice == "8":
                view_all_treatment_records(cursor)
            elif choice == "9":
                view_owner_by_pet(cursor)
            elif choice == "10":
                view_all_owners_and_pets(cursor)
            elif choice == "11":
                print("\nExiting program...")
                break
            else:
                print("\nPlease select a valid option (1-11)!")
        
        cursor.close()
        db.close()
    except mysql.connector.Error as err:
        print(f"\nDatabase connection error: {err}")

# Run the main menu
if __name__ == "__main__":
    main()
