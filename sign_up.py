import re


def sign_up(username, password, data):
    # Prevent empty input
    if not username or not password:
        return "NA"

    # Check whether it contains any invalid characters
    if not _is_valid_username(username):
        return "NA"

    users = data.get("users", [])

    # Check whether the username already exists
    for user in users:
        if user.get("username") == username:
            return "NA"

    # Generate a new user ID
    new_id = _generate_userid(users)

    # Create a new user
    new_user = {
        "id": new_id,
        "username": username,
        "password": password
    }

    # Add new user to the list and send to data
    users.append(new_user)
    data["users"] = users

    return new_id

def _is_valid_username(username: str) -> bool:
    # The password rule is: it can only contain letters, digits, and underscores
    pattern = r'^[A-Za-z0-9_]+$'
    return re.match(pattern, username) is not None

def _generate_userid(users):
    # No users, return user_001
    if not users:
        return "user_001"

    used_numbers = set()

    # Generate the smallest unused user_xxx based on the existing list of user IDs.
    for user in users:
        user_id = user.get("id", "")
        parts = user_id.split("_")
        if len(parts) == 2 and parts[1].isdigit():
            num = int(parts[1])
            used_numbers.add(num)

    new_num = 1
    while new_num in used_numbers:
        new_num += 1

    return f"user_{new_num:03d}"
