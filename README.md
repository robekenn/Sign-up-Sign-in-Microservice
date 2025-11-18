# Sign-up-Sign-in-Microservice

This microservice uses the Zero-MQ protocal.

For this microservice please connect via:
```ruby
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5558")
```

## Requesting:
### Sign-In:

For sign-in, client will send a JSON list 

* '1' - (the protocal for sign-in)

* *[1, username, password]*

**Example:**
```ruby
#request with serilization
request = [1, "jane_doe", "coolerpassword"]
serialized_list_json = json.dumps(siReq).encode("utf-8")

# send to the server
socket.send(serialized_list_json)
```
### Sign-Up:

For sign-up, client will send a JSON list

* '2' - (the protocal for sign-up)

* *[2, username, password]*

**Example:**
```ruby
#request with serilization
request = [2, "Juan", "thebestpass"]
serialized_list_json = json.dumps(siReq).encode("utf-8")

# send to the server
socket.send(serialized_list_json)
```

### Delete-User:

The delete-user function will be called if the server recieves a JSON object that contains a list 

* '3' - (the protocal for delete-user)

* *[3, userID]*

**Example:**
```ruby
#request with serilization
request = [3, "user_001"]
serialized_list_json = json.dumps(siReq).encode('utf-8')

# send to the server
socket.send(serialized_list_json)
```


## Receiveing:

### Sign-In:
For sign-in, the Server will return
* userid (success)
* "NA" (fails)

**Example:**
```ruby
# receive responce
message = socket.recv()
```


### Sign-Up:
For sign-up, the Server will return
* userid (success)
* "NA" (fails)

**Example:**
```ruby
# receive responce
message = socket.recv()
```

### Delete-User:

The Server will return
* "OK" (success)
* "ERROR" (fails)

**Example:**
```ruby
#receive responce
message = socket.recv()
```

## UML Diagram
<img width="1191" height="473" alt="Screenshot 2025-11-17 at 1 51 36 PM" src="https://github.com/user-attachments/assets/ef8e2ada-193e-4c2f-851c-6ff1e871913f" />

## Team Contribution
### Kenneth Robertson
* Implemented the server.py core structure.
* Completed the delete_user function in the server.
* Wrote the testClient for demonstrating delete-user requests.
* Created the initial README framework, including layout and sections, and Delete-User part.

### Zhicheng Huang
* Implemented the sign-in and sign-up functions in the server.
* Wrote the sign-in and sign-up part in the README.
* Improved the README overall style, including formatting, clarity, and consistency across all microservices.
* Make the video.
