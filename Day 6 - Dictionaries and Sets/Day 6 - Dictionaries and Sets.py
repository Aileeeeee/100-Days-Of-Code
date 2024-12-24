'''
Store Health Metrics:

Create a dictionary to store the health metrics of a person, such as:
health_metrics = {
    "height": 170,  # in cm
    "weight": 70,   # in kg
    "blood_pressure": "120/80",
    "cholesterol": "normal"
}
Add a key-value pair for the "heart_rate" and update the "cholesterol" value to "high".
'''

# Global ID Counter
current_id = 100  # Starting ID

def get_response(prompt):
    """Prompt the user for input and return the response."""
    return input(prompt).strip()

def generate_patient_id():
    """Generate a unique patient ID using initials and a global counter."""
    # Add the global keyword to access the global counter
    global current_id  
    current_id += 1 
    return f'patient{current_id}'

def get_health_metric():
    " Prompt user for patient health metrics"
    # Collect patient's basic health metrices
    health_metrics = {
    'patient_id': generate_patient_id(),
    'height': float(get_response('Enter a height (in cm): ')),
    'weight': float(get_response('Enter a weight (in kg): ')),
    'blood_pressure' : f"{get_response('Enter the systolic blood pressure : ')}/ {get_response('Enter the diastolic blood pressure : ')}",
    'cholesterol' : get_response('Enter a cholesterol level (High,Low,Moderate): ')}
    
    return health_metrics


''' Add or update key-value pair for the health metric dictionary '''
# Add a key-value pair for 'heart_rate' to the health_metrices
def add_update_health_metric(health_metrics):
    # Collect the new key-value pair to be added or updated
    metric = get_response('Enter a metric you want to add/update: ')
    new_metric_value = get_response('Enter a new value for the metric: ')

    # Check if metric exists already
    if metric in health_metrics:
        print(f"'{metric}' already exists.Updating its value to '{new_metric_value}'.")
    else:
        print(f"'Adding a new metric '{metric}' with value {new_metric_value} .")
    health_metrics[metric] = new_metric_value


'''
Exercise:Count Frequencies: 
- Use a dictionary to count how many times each medication category appears.
- Display Frequencies: Print each category along with its frequency.
- Find Key Metrics:
   - The most frequent category.
   - The least frequent category.
- Display the frequencies in descending order.
'''
# A list of medication categories
medication_categories = [
    "Antibiotic", "Antibiotic", "Antibiotic", "Antibiotic", "Antibiotic", "Antibiotic",
    "Analgesic", "Analgesic", "Analgesic", "Analgesic", "Analgesic",
    "Antipyretic", "Antipyretic", "Antipyretic", "Antipyretic",
    "Antihistamine", "Antihistamine", "Antihistamine",
    "Antidepressant", "Antidepressant", "Antidepressant",
    "Antiviral", "Antiviral", "Antiviral",
    "Antifungal", "Antifungal", "Antifungal",
    "Antipsychotic", "Antipsychotic",
    "Antidiabetic", "Antidiabetic",
    "Antihypertensive", "Antihypertensive",
    "Anticoagulant",
    "Bronchodilator", "Bronchodilator", "Bronchodilator",
    "Diuretic", "Diuretic", "Diuretic", "Diuretic",
    "Laxative", "Laxative", "Laxative",
    "Sedative", "Sedative",
    "Vaccine", "Vaccine", "Vaccine", "Vaccine", "Vaccine",
    "Hormone Therapy", "Hormone Therapy", "Hormone Therapy",
    "Immunosuppressant", "Immunosuppressant",
    "Chemotherapy", "Chemotherapy",
    "Antacid", "Antacid", "Antacid",
    "Antiemetic", "Antiemetic",
    "Beta Blocker", "Beta Blocker",
    "Calcium Channel Blocker", "Calcium Channel Blocker",
    "NSAID", "NSAID", "NSAID",
    "Statin", "Statin",
    "Antiseptic", "Antiseptic",
    "Probiotic", "Probiotic",
    "Vitamin Supplement", "Vitamin Supplement",
    "Mineral Supplement", "Mineral Supplement",
    "Antimicrobial",
    "Antiparasitic", "Antiparasitic",
    "Anticonvulsant",
    "Antigout",
    "Muscle Relaxant", "Muscle Relaxant",
    "Antivertigo",
    "Expectorant", "Expectorant",
    "Antispasmodic", "Antispasmodic",
    "Anti-inflammatory",
    "Antithyroid", "Antithyroid",
    "Immunoglobulin",
    "Bronchial Dilator",
    "Electrolyte Solution",
    "Antineoplastic", "Antineoplastic",
    "Thrombolytic",
    "Antiarrhythmic", "Antiarrhythmic",
    "Anticholinergic",
    "Antianxiety", "Antianxiety",
    "Antimigraine",
    "Hypnotic", "Hypnotic",
    "Antihyperlipidemic",
    "Antirheumatic", "Antirheumatic",
    "Gastroprotective",
    "Antipruritic",
    "Enzyme Replacement",
    "Antioxidant",
    "Analgesic (Narcotic)", "Analgesic (Narcotic)",
    "Antidiarrheal",
    "Antiasthmatic",
    "Neuroprotective",
    "Antifibrotic",
    "Cardiac Glycoside",
    "Antiestrogen",
    "Antiprotozoal",
    "Corticosteroid",
    "Anesthetic",
    "Antiviral (HIV-specific)",
    "Antiepileptic",
    "Beta Agonist",
    "Antiglaucoma",
    "Antiviral (Influenza-specific)",
    "Uricosuric",
    "Immunotherapy",
    "Antiemetic (Chemo-specific)",
    "Proton Pump Inhibitor",
    "Antihypoglycemic",
    "Bisphosphonate",
    "Antidepressant (SSRI)",
    "Antidepressant (SNRI)",
    "Anticoagulant (Extended)",
    "Antioxidant (Natural)",
    "Antirheumatic (Biologic)",
    "Antithrombotic",
    "Antihyperuricemic",
    "Antianemic",
    "Immunomodulator",
    "Antifungal (Topical)",
    "Antiarrhythmic (Class I)",
    "Antiarrhythmic (Class II)",
    "Antiarrhythmic (Class III)",
    "Antiarrhythmic (Class IV)",
    "Antiemetic (Motion Sickness)",
    "Antipsychotic (Atypical)",
    "Antipsychotic (Typical)",
    "Antihistamine (Non-drowsy)",
    "Antihistamine (Sedative)",
    "Antidiabetic (Type 1)",
    "Antidiabetic (Type 2)",
    "Hypoglycemic Agent",
    "Antilipemic",
    "Antiosteoporotic",
    "Antiviral (Hepatitis-specific)",
    "Antiglaucoma (Beta Blocker)",
    "Antiglaucoma (Carbonic Anhydrase Inhibitor)",
    "Antitussive",
    "Antiviral (General)",
    "Steroid",
    "Mucolytic",
    "Antitubercular",
    "Antihypertensive (ACE Inhibitor)",
    "Antihypertensive (ARB)"
]


# Create an empty dictionary
medication_category_count = {}

# Count frequencies of the medication categories
for item in medication_categories:
    if item in medication_category_count:
        medication_category_count[item] += 1
    else:
        medication_category_count[item] = 1

# Display frequencies of medication categories
for key,value in medication_category_count.items():
    print(f'The frequency of {key}: {value}')

# Find the category with the most and least frequencies      
frequent_category = max(medication_category_count, key = medication_category_count.get)
least_category = min(medication_category_count, key = medication_category_count.get)

print(f'The most freqent category is {frequent_category} with {medication_category_count[frequent_category]}')
print(f'The category with the least frequency is {least_category} with {medication_category_count[least_category]}')


''' Display the frequencies in descending order.'''
# Retrieve items(key-value) pair from the dictionary
items = medication_category_count.items()

# Sort items by keys in descending order
medication_category_count_sorted = sorted(items,key = lambda item : item[1],reverse = True)

# Convert sorted values to a dictionary
medication_category_count_dict = dict(medication_category_count_sorted)


'''
Count Values in a Dictionary:

- Create a dictionary where the keys are items in a store, and the values are their quantities.
Example: items = {"apple": 10, "banana": 5, "orange": 8}
- Find the total quantity of items in the store.
'''
# List of health-related items
health_items = [
    'Hand Sanitizer',
    'Face Mask',
    'Disinfectant Wipes',
    'Thermometer',
    'First Aid Kit',
    'Vitamin C Supplements',
    'Pain Relievers',
    'Bandages',
    'Antiseptic Cream',
    'Cold and Flu Medicine'
]

# List of their corresponding quantities
quantities = [100, 200, 150, 50, 30, 120, 80, 200, 60, 100]

# Create a dictionary where the keys are items in a store, and the values are their quantities.
health_items_dict = {item : quantity for item,quantity in zip(health_items,quantities)}

# Find the total quantity of items in the store.
total_quantity = 0
for item,quantity in health_items_dict.items():
    total_quantity += quantity
    
# Display the total quantity of items in the store
print(f'The total quantity of items in the store is {total_quantity}.')


'''
Calculate BMI from Health Data:

Given a dictionary with "height" and "weight", calculate the Body Mass Index (BMI) using the formula:
BMI = weight (kg)/height (m)2
'''

patient_health_metrics = {'Person_1': {'height': 179, 'weight': 60},
 'Person_2': {'height': 174, 'weight': 77},
 'Person_3': {'height': 165, 'weight': 91},
 'Person_4': {'height': 168, 'weight': 68},
 'Person_5': {'height': 200, 'weight': 82},
 'Person_6': {'height': 160, 'weight': 55},
 'Person_7': {'height': 172, 'weight': 88},
 'Person_8': {'height': 173, 'weight': 69},
 'Person_9': {'height': 185, 'weight': 57},
 'Person_10': {'height': 165, 'weight': 64},
 'Person_11': {'height': 150, 'weight': 67},
 'Person_12': {'height': 196, 'weight': 68},
 'Person_13': {'height': 194, 'weight': 85},
 'Person_14': {'height': 190, 'weight': 88},
 'Person_15': {'height': 183, 'weight': 61},
 'Person_16': {'height': 182, 'weight': 81},
 'Person_17': {'height': 195, 'weight': 72},
 'Person_18': {'height': 167, 'weight': 70},
 'Person_19': {'height': 200, 'weight': 85},
 'Person_20': {'height': 182, 'weight': 87},
 'Person_21': {'height': 199, 'weight': 61},
 'Person_22': {'height': 185, 'weight': 75},
 'Person_23': {'height': 150, 'weight': 64},
 'Person_24': {'height': 155, 'weight': 68},
 'Person_25': {'height': 183, 'weight': 90},
 'Person_26': {'height': 182, 'weight': 71},
 'Person_27': {'height': 188, 'weight': 92},
 'Person_28': {'height': 185, 'weight': 77},
 'Person_29': {'height': 155, 'weight': 60},
 'Person_30': {'height': 180, 'weight': 58},
 'Person_31': {'height': 185, 'weight': 54},
 'Person_32': {'height': 188, 'weight': 67},
 'Person_33': {'height': 169, 'weight': 72},
 'Person_34': {'height': 153, 'weight': 69},
 'Person_35': {'height': 164, 'weight': 65},
 'Person_36': {'height': 200, 'weight': 59},
 'Person_37': {'height': 157, 'weight': 67},
 'Person_38': {'height': 176, 'weight': 52},
 'Person_39': {'height': 163, 'weight': 71},
 'Person_40': {'height': 175, 'weight': 55},
 'Person_41': {'height': 177, 'weight': 83},
 'Person_42': {'height': 182, 'weight': 67},
 'Person_43': {'height': 161, 'weight': 58},
 'Person_44': {'height': 196, 'weight': 64},
 'Person_45': {'height': 182, 'weight': 73},
 'Person_46': {'height': 197, 'weight': 84},
 'Person_47': {'height': 189, 'weight': 69},
 'Person_48': {'height': 190, 'weight': 61},
 'Person_49': {'height': 191, 'weight': 57},
 'Person_50': {'height': 178, 'weight': 97}}

# A dictionary that stores people's bmi
people_bmi = {}
# Iterate over the patient_health_metrics data
for person,metric in patient_health_metrics.items():
    height_m = metric['height'] / 100
    weight = metric['weight'] 

    # Calculate and round off the bmi for each person
    bmi = round(weight / (height_m ** 2),2)

    # Store bmi in the `people_bmi` dictionary
    people_bmi[person] = bmi

# Display each person's bmi
for person,bmi in people_bmi.items():
    print(f'{person} bmi: {bmi}')


''' 
Exercises:

- Find Patients with Either Condition A or Condition B (Union):
- Find Patients with Only Condition A (Difference):
- Find Patients with Only Condition B (Difference):
- Find Patients with Either Condition A or Condition B, but Not Both (Symmetric Difference):
- Check if All Patients with Condition A are also in Condition B (Subset Check):
- Verify whether all patients in set_A are also in set_B.
- Check if There are Any Common Patients between Condition A and Condition B:
- Count the Number of Unique Patients across Both Conditions
- List Patients in Alphabetical Order who have Both Conditions:
- Determine if Condition A and Condition B have Exactly the Same Patients:
- Check if set_A and set_B contain the same patients.

'''
set_hypertension = {
    "James Smith", "Mary Johnson", "Robert Williams", "Patricia Brown", "John Jones",
    "Jennifer Garcia", "Michael Miller", "Linda Davis", "William Rodriguez", "Elizabeth Martinez",
    "David Hernandez", "Barbara Lopez", "Richard Gonzalez", "Susan Wilson", "Joseph Anderson",
    "Jessica Thomas", "Thomas Taylor", "Sarah Moore", "Charles Jackson", "Karen Martin"
}

set_diabetes = {
    "James Smith", "Mary Johnson", "Robert Williams", "Patricia Brown", "John Jones",
    "Christopher Lee", "Nancy Perez", "Daniel White", "Lisa Harris", "Matthew Clark",
    "Betty Lewis", "Anthony Robinson", "Margaret Walker", "Donald Young", "Sandra Hall",
    "Mark Allen", "Ashley King", "Paul Wright", "Kimberly Scott", "Steven Green"
}


# Find Patients with Either Condition A or Condition B (Union)
patient_hypertension_or_diabetes = set_hypertension.union(set_diabetes)

# Display patients with either condition A or Condition B
print(f'The patients with either hypertension or diabetes are:')
for index,patient in enumerate(patient_hypertension_or_diabetes,1):
    print(f'{index}.{patient}')


# Find Patients with Only Condition A (Difference)
patient_hypertension_only = set_hypertension.difference(set_diabetes)

# Display patients with either condition A or Condition B
print(f'The patients with only hypertension are:')
for index,patient in enumerate(patient_hypertension_only,1):
    print(f'{index}.{patient}')


# Find Patients with Only Condition A (Difference)
patient_diabetes_only = set_diabetes.difference(set_hypertension)

# Display patients with either condition A or Condition B
print(f'The patients with only diabetes are:')
for index,patient in enumerate(patient_diabetes_only,1):
    print(f'{index}.{patient}')


# Find Patients with Either hypertension or diabetes, but Not Both (Symmetric Difference)
patient_diabetes_only = set_diabetes.symmetric_difference(set_hypertension)

# Display patients with either condition A or Condition B
print(f'The patients with either only hypertension or diabetes but not both are:')
for index,patient in enumerate(patient_diabetes_only,1):
    print(f'{index}.{patient}')


# Check if All Patients with Condition A are also in Condition B (Subset Check)
is_hypertension_subset_diabetes = set_hypertension.issubset(set_diabetes)

# Output message if Patients with Condition A are also in Condition B (Subset Check)
if is_hypertension_subset_diabetes:
    print('All patients with hypertension are also listed as having diabetes.')
else:
    print('Not all patients with hypertension are also listed as having diabetes.')


#  Check if There are Any Common Patients between Condition A and Condition B
patient_with_diabetes_and_hypertension = set_diabetes.intersection(set_hypertension)

# Display patients with both hypertension or diabetes
print(f'The patients with both hypertension or diabetes are:')
for index,patient in enumerate(patient_with_diabetes_and_hypertension,1):
    print(f'{index}.{patient}')


# The unique patients across both conditions are those patients with who have either hypertension or diabetes(i.e union)

# Count the Number of Unique Patients across Both Conditions 
unique_patients_count = len(patient_hypertension_or_diabetes)

# Display output
print(f'The total number of patients across each conditions are {unique_patients_count}.')


# A list of patients who have both conditions(i.e hypertension and diabetes) is the intersection of both sets.

# List Patients in Alphabetical Order who have Both Conditions
sorted_common_patients = sorted(patient_with_diabetes_and_hypertension)

# Display output
print(f'Patients who have both conditions arranged in alphabetical order')
for index,patient in enumerate(sorted_common_patients ,1):
    print(f'{index}. {patient}')


# A list of patients who have both conditions(i.e hypertension and diabetes) is the intersection of both sets.

# List Patients in Alphabetical Order who have Both Conditions
sorted_common_patients = sorted(patient_with_diabetes_and_hypertension)

# Display output
print(f'Patients who have both conditions arranged in alphabetical order')
for index,patient in enumerate(sorted_common_patients ,1):
    print(f'{index}. {patient}')


# Check if set_hypertension and set_diabetes contain the same patients
is_equal = set_hypertension == set_diabetes

# Display output
if is_equal:
    print('All patients with hypertension are also listed as having diabetes.')
else:
    print('Not all patients with hypertension are also listed as having diabetes.')
