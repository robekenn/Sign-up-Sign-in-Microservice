def sign_in(username, password, data):
    # Prevent empty input
    if not username or not password:
        return "NA"

    # Check database
    for user in data.get("users", []):
        if user.get("username") == username and user.get("password") == password:
            return user.get("id")
    
    # Not match
    return "NA"
