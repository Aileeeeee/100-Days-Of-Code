This Python project calculates the daily calorie intake required for weight loss based on Basal Metabolic Rate (BMR) and Total Daily Energy Expenditure (TDEE). The tool personalizes recommendations by considering factors like gender, age, weight, height, and activity level.

# Features
- Calculates Basal Metabolic Rate (BMR) for men and women.
- Determines Total Daily Energy Expenditure (TDEE) using activity multipliers.
- Provides calorie recommendations for moderate or aggressive weight loss.

# Usage
- Provide inputs for gender, age, weight, height, and activity level when prompted.
- Select your weight loss goal (moderate or aggressive).
- The program will output your daily calorie requirements for weight loss.

# Formulas Used
- BMR for men: 10 × weight (kg) + 6.25 × height (cm) - 5 × age (years) + 5
- BMR for women: 10 × weight (kg) + 6.25 × height (cm) - 5 × age (years) - 161
- TDEE: BMR × Activity Level Multiplier

# Activity Levels and Multipliers
- Sedentary: 1.2
- Lightly active: 1.375
- Moderately active: 1.55
- Very active: 1.725
- Extra active: 1.9
