# - **Day 4:** Build a simple age checker – if age < 13: kid, <18: teen, <60: adult, else: senior.

def age_checker(age: int) -> str:
    if age < 13:
        return "Kid"
    elif age >= 13 and age < 18:
        return "Teen"
    elif age >= 18 and age < 60:
        return "Adult"
    else:
       "Senior"


if __name__ == '__main__':
    print('Age Checker')
    age = input("Please input your age: ")

    try:
        age = int(age)
        print(f"You are a/an {age_checker(age)}!")
    except Exception as e:
        print("Error %s", e)
        print("Please input a valid age (integer)!")