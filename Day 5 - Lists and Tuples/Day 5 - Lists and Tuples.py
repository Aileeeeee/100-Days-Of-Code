'''
Exercise: Patient Information Management
Create a list to store patient data in the format [first_name, last_name, weight] for multiple patients.

- Add a new patient to the end of the list.

- Insert a new patient at the second position of the list.

- Remove the first patient's details from the list.

- Print the final list of patient data.

'''
# I'm making this story-wise; print message to my user interface
print('Welcome to my database for storing patient information.')
print('\nInformation is stored in a list and is arranged in this way;`first_name, last_name,weight.`')
print("E.g Every 3 step is the value for the patient's weight")

# Create list and store in a variable `patient_data`
patients = ['Anabelle','Clarke',67.5,'Ariana', 'Brown',65.0, 'Joseph','Duke',80.0]

# Add information for a new patient at the end of the `patients` list
patient1 = ['Joe','Babylon',75.6] 
patients.extend(patient1)

# Imagine its a waiting list , add a patient at the second position based on the level of urgency
urgent_patient = ['Ken','Eric',75.6]
# Iterate over `new_patient` list and each data to the ` patient data` list
for i,data in enumerate(urgent_patient,3):
    patients.insert(i,data)

# Remove information of first patient from the list
del patients[:3]

patients




'''
Patient Record System
Create a system for managing patient records. You will use lists and tuples to store and manipulate information like patient details, treatment history, and prescriptions.

Tasks:
- Store patient records as tuples in a list. Each tuple contains: (patient_id, name, diagnosis, treatment_plan, medications).
- Add a new patient record to the list.
- Update an existing patient’s treatment plan.
- Delete a patient record by patient_id.
- Search for a patient by their diagnosis and display their treatment plan and medications.
'''
# Patient Record System

# List to store patient records
patient_records = []

# Global ID Counter
current_id = 100  # Starting ID

def get_response(prompt):
    """Prompt the user for input and return the response."""
    return input(prompt).strip()


def generate_patient_id(first_name, last_name):
    """Generate a unique patient ID using initials and a global counter."""
    # Add the global keyword to access the global counter
    global current_id  
    current_id += 1 
    return f'{first_name[:1]}{last_name[:1]}{current_id}'


def get_patient_record():
    """Collect and return a new patient record."""
    medications = []
    
    # Collect patient's basic details
    first_name = get_response('/nEnter First name: ').capitalize()
    last_name = get_response('Enter Last name: ').capitalize()
    name = f"{first_name} {last_name}"

    
    # Collect diagnosis and treatment plan
    diagnosis = get_response(f"\nWhat's your diagnosis for {name}? ").capitalize()
    treatment_plan = get_response(f"\nEnter a treatment plan: ").capitalize()

    # Collect medications and enter `quit` to stop
    while True:
        medication = get_response("Enter the name of the medication to be prescribed ('quit' to stop entering): ").lower()
        if medication == 'quit':
            break
        medications.append(medication)
    
    # Generate a unique patient ID
    patient_id = generate_patient_id(first_name, last_name)

    return (patient_id, name, diagnosis, treatment_plan, medications)


def update_treatment_plan(patient_id):
    """Update an existing patient’s treatment plan."""
    for record in patient_records:
        if record[0] == patient_id:
            new_treatment = get_response("\nEnter the new treatment plan: ").capitalize()
            patient_records[patient_records.index(record)] = (
                record[0], record[1], record[2], new_treatment, record[4]
            )
            print("Treatment plan updated successfully.")
            break
    else:
        print("Patient ID not found.")

def delete_patient_record(patient_id):
    """Delete a patient record by patient_id."""
    global patient_records
    
    for record in patient_records:
        if record[0] == patient_id:
            patient_records.remove(record)
            print("Patient record deleted successfully.")
            break
    else:
        print("Patient ID not found. No record was deleted.")


def search_by_diagnosis(diagnosis):
    """Search for a patient by diagnosis and display their details."""
    for record in patient_records:
        if record[2] == diagnosis:
            print(f"\nPatient Name: {record[1]}")
            print(f"Treatment Plan: {record[3]}")
            print(f"Medications: {', '.join(record[4]) if record[4] else 'None'}")
            break
    else:
        print("No patients found with that diagnosis.")


# Main Program Loop
while True:
    print("\nPatient Record System Menu:")
    print("1. Add a new patient record")
    print("2. Update treatment plan")
    print("3. Delete a patient record")
    print("4. Search by diagnosis")
    print("5. Display all records")
    print("6. Exit")
    
    choice = get_response("Enter your choice (1-6): ")

    if choice == '1':
        patient_records.append(get_patient_record())
    elif choice == '2':
        patient_id = get_response("Enter Patient ID to update: ")
        update_treatment_plan(patient_id)
    elif choice == '3':
        patient_id = get_response("Enter Patient ID to delete: ")
        delete_patient_record(patient_id)
    elif choice == '4':
        diagnosis = get_response("Enter the diagnosis to search for: ").capitalize()
        search_by_diagnosis(diagnosis)
    elif choice == '5':
        print("\nAll Patient Records:")
        for record in patient_records:
            print(record)
    elif choice == '6':
        print("Exiting the Patient Record System. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")