** CITYCAB FARE CALCULATOR **
## PROJECT DESCRIPTION
City Cab Fare Calculator is a Core Python console-based application developed to estimate ride fares based on distance, vehicle type, and travel time. 
It uses a loop-driven approach to allow users to calculate multiple rides and provides a formatted price receipt.
The system ensures proper validation using exception handling to avoid invalid inputs and incorrect data.

## FARE CALCULATION LOGIC
-Base fare is calculated as:
Distance × Rate per km
-Vehicle rates:
Economy → ₹10 per km
Premium → ₹18 per km
SUV → ₹25 per km
-Surge Pricing:
If ride time is between 5 PM (17:00) and 8 PM (20:00) → fare is multiplied by 1.5x

## KEY FEATURES
- Menu-driven console application
- Supports multiple ride calculations in a single run
- Dynamic fare calculation based on vehicle type
- Time-based surge pricing system
- Custom exception handling for vehicle validation
- Prevents invalid inputs (distance, time, vehicle type)
- Re-prompts user until valid input is entered
- Generates clean and formatted price receipt

## TECHNOLOGIES USED
- Core Python
- Functions 
- Exception Handling (Custom Exception)
- Loops and conditional statements

## HOW TO RUN
- python main.py

## SAMPLE OUTPUT
<img width="795" height="632" alt="Screenshot 2026-04-21 180748" src="https://github.com/user-attachments/assets/59ba06fd-5572-4261-9b69-7ad3c283dffa" />
<img width="795" height="706" alt="Screenshot 2026-04-21 180731" src="https://github.com/user-attachments/assets/570e55f4-6f4a-44bc-a930-0c644463b50c" />
<img width="778" height="424" alt="Screenshot 2026-04-21 180716" src="https://github.com/user-attachments/assets/7dafb273-124c-44eb-b716-b45a84ee4c87" />
<img width="848" height="468" alt="Screenshot 2026-04-21 180701" src="https://github.com/user-attachments/assets/3922d5a5-0fc8-4b07-aac9-1e5e4a6962a4" />

## AUTHOR
GORTHI SANTHOSHI



