print("Please enter the following information:")
print()
first_name=input("First name: ")
last_name = input("Last name: ")
email_address = input("Email address: ")
phone_number = input("Phone number: ")
job_title = input("Job Title: ")
id_number = input("ID Number: ")
hair = input("Hair: ")
eyes=input("Eyes: ")
month=input("Month: ")
training=input("Training: ")
print()
print("The ID Card is:")
print("------------------------------------------------")
output = f"{last_name.upper()}, {first_name.capitalize()}"
print(output)
output = f"{job_title.title()}"
print(output)
output = f"ID: {id_number}"
print(output)
print()
output=f"{email_address.lower()}"
print(output)
output=f"{phone_number}"
print(output)
print()
output=f"Hair: {hair.ljust(15)} Eyes: {eyes}"
print(output)
output=f"Month: {month.ljust(14)} Training: {training}"
print(output)
print("--------------------------------------------------")

#I obatined the same result with this form
#output=f"Hair: {hair} {'Eyes:' + eyes:>14}"
#print(output)
#output=f"Month: {month} {'Trainig:' + training:>15}"
#print(output)