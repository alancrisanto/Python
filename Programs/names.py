def make_full_name(given_name, family_name):
    """Return a string in this form "family_name; given_name".
    For example, if this function were called like this:
    make_full_name("Sally", "Brown"), it would return "Brown; Sally".
    """
    full_name = f"{family_name}; {given_name}"
    return full_name


def extract_family_name(full_name):
    """Extract and return the family name from a
    string in this form "family_name; given_name".
    For example, if this function were called like this:
    extract_family_name("Brown; Sally"), it would return "Brown".
    """
    # Find the index where "; " appears within the full name string.
    semicolon_index = full_name.index("; ")

    # Extract a substring from the full name and return it.
    family_name = full_name[0 : semicolon_index]
    # family_name = full_name[semicolon_index : -1]
    return family_name


def extract_given_name(full_name):
    """Extract and return the given name from a
    string in this form "family_name; given_name".
    For example, if this function were called like this:
    extract_given_name("Brown; Sally"), it would return "Sally".
    """
    # Find the index where "; " appears within the full name string.
    semicolon_index = full_name.index("; ")

    # Extract a substring from the full name and return it.
    given_name = full_name[semicolon_index + 2 : ]
    return given_name


# import csv


# def main():
    
#     ID_NUMBER = 0
#     FIRST_NAME = 1
#     LAST_NAME = 2

#     students = read_dict("students.csv", ID_NUMBER)

#     student_id = input("Please enter an I-Number (xx-xxx-xxx): ")

    

#     print(students)


# def read_dict(filename, key_column_index):

#     dictionary = {}

#     with open(filename, "rt") as csv_file:

#         file_id = csv.reader(csv_file)

#         next(file_id)

#         for row in file_id:

#             key = row[key_column_index]

#             dictionary[key] = row
    
#     return dictionary

# if __name__ == "_main_":
#     main()