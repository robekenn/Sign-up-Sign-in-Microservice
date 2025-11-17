# Sign-up-Sign-in-Microservice

This microservice uses the Zero-MQ protocal.

For this microservice please connect via:
```
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5558")
```

Requesting:
Sign-In:

Sign-Up:

Delete-User:
The delete-user function will be called if the server recieves a JSON object that contains a list [3 (the protocal for delete-user), userID]
Example:
```
#request with serilization
request = [3, "user_001"]
serialized_list_json = json.dumps(siReq).encode('utf-8')

# send to the server
socket.send(serialized_list_json)
```


Receiveing:

Sign-In:

Sign-Up:


Delete-User:
The Server will return a "OK" or "ERROR".
```
#receive responce
message = socket.recv()
```


<img width="1191" height="473" alt="Screenshot 2025-11-17 at 1 51 36 PM" src="https://github.com/user-attachments/assets/ef8e2ada-193e-4c2f-851c-6ff1e871913f" />

