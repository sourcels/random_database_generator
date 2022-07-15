from generator import generate_json, create_users_list, generate_password, generate_user, return_schema

generate_json(indent=4, user_amount=20, path="path/to/file.json")

test_list = create_users_list(user_amount=20)

test_string = generate_password(length=15)

test_dict = generate_user()

test_dict1 = return_schema()

