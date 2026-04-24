#import requests

def get_users():
    pass

def filter_users(users, city):
    pass

def main():
    users = get_users()
    filtered = filter_users(users, "South Christy")


    for user in filtered:
        print(user)

    print("Total:", len(filtered))

def hello():
    print("hi")

    print(" summer")

if __name__ == "__main__":
    main()