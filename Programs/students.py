import csv


def main():

    ID_NUMBER = 0
    FIRST_NAME = 1
 
    student_name = read_dict("students.csv", ID_NUMBER)
    student_id = input("Please enter an I-Number (xxxxxxxxx): ")

    
    # if student_id in student_name.keys():
    #     print(name)
    # else:
    #     print("Not such Student")

    if student_id not in student_name:
        print("Not such student")
    else:
        name = student_name[student_id][FIRST_NAME]
        print(name)



def read_dict(filename, key_column_index):

    dictionary = {}

    with open(filename, "rt") as read_text:

        read_file = csv.reader(read_text)

        next(read_file)

        for row in read_file:

            # read_file.strip()

            key = row[key_column_index]

            dictionary[key] = row

    return dictionary

if __name__ == "__main__":
    main()




