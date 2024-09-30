import json
from datetime import datetime, timedelta

# Load data from JSON file
with open('trainings.txt', 'r') as file:
    data = json.load(file)

# Task 1: List each completed training with a count of how many people completed it
def task_1_completed_trainings_count(data):
    training_counts = {}
    
    for person in data:
        for training in person["completions"]:
            training_name = training["name"]
            # Increment count for each completed training
            if training_name not in training_counts:
                training_counts[training_name] = 0
            training_counts[training_name] += 1
    
    return training_counts

# Task 2: List all people that completed specified trainings in fiscal year 2024
def task_2_completed_in_fiscal_year_by_training(data, trainings, fiscal_year_start, fiscal_year_end):
    results = {training: [] for training in trainings}  # Initialize results dictionary for each training

    for person in data:
        for completion in person["completions"]:
            training_name = completion["name"]
            completion_date = datetime.strptime(completion["timestamp"], "%m/%d/%Y")

            if training_name in trainings and fiscal_year_start <= completion_date <= fiscal_year_end:
                if person["name"] not in results[training_name]:
                    results[training_name].append(person["name"])

    return results

# Task 3: Find all people with expired or soon-to-expire trainings
def task_3_expired_or_expiring_soon(data, reference_date):
    expired_soon_list = {}
    
    for person in data:
        for training in person["completions"]:
            if training["expires"]:
                expiration_date = datetime.strptime(training["expires"], "%m/%d/%Y")
                expires_in = (expiration_date - reference_date).days
                
                # Check if training is expired or expiring soon
                if expires_in < 0:
                    status = "Expired"
                elif expires_in <= 30:
                    status = "Expiring Soon"
                else:
                    continue
                
                if person["name"] not in expired_soon_list:
                    expired_soon_list[person["name"]] = []
                
                expired_soon_list[person["name"]].append({
                    "training": training["name"],
                    "status": status,
                    "expires": training["expires"]
                })
    
    return expired_soon_list

# Running the tasks
fiscal_year_start = datetime(2023, 7, 1)
fiscal_year_end = datetime(2024, 6, 30)
reference_date = datetime(2023, 10, 1)

# Task 1
completed_trainings_count = task_1_completed_trainings_count(data)

# Task 2
specified_trainings = ["Electrical Safety for Labs", "X-Ray Safety", "Laboratory Safety Training"]
completed_in_fy2024 = task_2_completed_in_fiscal_year_by_training(data, specified_trainings, fiscal_year_start, fiscal_year_end)

# Task 3
expired_or_expiring_soon = task_3_expired_or_expiring_soon(data, reference_date)

# Writing outputs to JSON files
with open('task_1_output.json', 'w') as f:
    json.dump(completed_trainings_count, f, indent=4)

with open('task_2_output.json', 'w') as f:
    json.dump(completed_in_fy2024, f, indent=4)

with open('task_3_output.json', 'w') as f:
    json.dump(expired_or_expiring_soon, f, indent=4)