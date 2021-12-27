from datetime import datetime

def main():

    gender = input("Enter gender (M or F): ")
    birthdate = input("Enter birthday (YY-MM-DD): ")
    pounds = float(input("Enter your weight in US pounds: "))
    inches = float(input("Enter your height in US inches: "))

    years = compute_age(birth = birthdate)
    kg_weight = kg_from_lb(lb = pounds)
    cm_height = cm_from_in(inch = inches)
    
    print(f"Age (Years): {years}")
    print(f"Weight (Kg): {kg_weight}")
    print(f"Height (cm): {cm_height}")
    print(f"Body mass index: {body_mas_index(weight = kg_weight, height = cm_height)}")
    print(f"Basal metabolic rate (kcal /day): {basal_metabolic_rate(gender, weight=kg_weight, height=cm_height, age = years)}")



def compute_age(birth):

    # Compute and return a person's age in years.

    # Parameter birth: a person's birthdate stored as
    #     a string in this format: YYYY-MM-DD
    # Return: a person's age in years.

    birthday = datetime.strptime(birth, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the birthday in years.

    years = today.year - birthday.year

    # If necessary, subtract one from the difference.

    if birthday.month > today.month or \
        (birthday.month == today.month and birthday.day > today.day):
        years -= 1

    return years

def kg_from_lb(lb):

    kg = lb * 0.45359237

    return kg.__round__(1)

def cm_from_in(inch):

    cm = inch * 2.54

    return cm.__round__(1)

def body_mas_index(weight, height):

    bmi = (10000 * weight) / height ** 2 
    
    return bmi.__round__(1)

def basal_metabolic_rate(gender, weight, height, age):
    
    if gender.lower() == "m":

        bmr_men = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
        
        return bmr_men.__round__()
    
    else:

        bmr_women = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age

        return bmr_women.__round__()

main()

