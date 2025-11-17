import re

def _is_valid_username(username: str) -> bool:
    pattern = r'^[A-Za-z0-9_]+$'
    return re.match(pattern, username) is not None


def sign_up(username, password, data):
    if not username or not password:
        return "NA"

    if not _is_valid_username(username):
        return "NA"

    users = data.get("users", [])

    for user in users:
        if user.get("username") == username:
            return "NA"

    new_id = _generate_userid(users)

    new_user = {
        "id": new_id,
        "username": username,
        "password": password
    }

    users.append(new_user)
    data["users"] = users

    return new_id


def _generate_userid(users):
    if not users:
        return "user_001"

    used_numbers = set()

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