# Training Completion Analyzer

This project analyzes training completion data from a JSON file and produces three different outputs.

## How to Run

1. Ensure Python 3.x is installed.
2. Run the Python script `Main.py` with the provided `trainings.txt` data file.
3. The results will be outputted into three JSON files for each task:
   - `task_1_output.json`
   - `task_2_output.json`
   - `task_3_output.json`

## Output

- **Task 1:** Count of how many people completed each training.
- **Task 2:** List of people who completed specified trainings within fiscal year 2024.
- **Task 3:** List of people whose trainings are expired or expiring soon based on a specified date.
