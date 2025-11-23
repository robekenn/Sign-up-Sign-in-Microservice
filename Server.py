import deleteU
import zmq
import json
import sign_in
import sign_up

#This function dumps all the data stored in the program into the JSON file.
def JSONDump(data):
    with open("data.json", 'w') as f:
        json.dump(data, f, indent=4)

#This function establishes the server for clients to connect to
def init_Connection():
      #initilises the socket
      context = zmq.Context()
      socket = context.socket(zmq.REP)
      socket.bind("tcp://*:5558")
      return socket

#read JSON Database's data
def get_data():
      with open('data.json', 'r') as file:
            return json.load(file)

#This takes in the socket(for sending a return message), the message (for getting the users input(username, password)),
#     and data for the validation of the database and to get the UserID this function is to sign in the user
def sign_in_protocal(socket, message, data):
      print("signin") #for debug purposes
      retMessage = sign_in.sign_in(message[1], message[2], data) #Sends the username and password
      socket.send_string(retMessage)
      JSONDump(data)

#This takes in the socket(for sending a return message), the message (for getting the users input(username, password)),
#     and data for the validation of the database and to get the UserID this function is to sign-up the user
def sign_up_protocal(socket, message, data):
      print("Signup") #for debug purposes
      retMessage = sign_up.sign_up(message[1], message[2], data)#Sends the username and password
      socket.send_string(retMessage)
      JSONDump(data)

#This takes in the socket(for sending a return message), the message (for getting the users input(UserID)),
#     and data for the validation of the database and to delete the user.
def delete_user_protocal(socket, message, data):
      print("Delete User") #for debug purposes
      retMessage = deleteU.delete_user(message[1], data)
      socket.send_string(retMessage)
      JSONDump(data)

def main():
      data = get_data()

      while True:
            #  Wait for next request from client
            socket = init_Connection()
            message = socket.recv()

            #changes the recieved JSON to normal data
            message = json.loads(message)

            if message[0] == 1:
                  sign_in_protocal(socket, message, data)
            elif message[0] == 2:
                  sign_up_protocal(socket, message, data)
            elif message[0] == 3:
                  delete_user_protocal(socket, message, data)

if __name__ == "__main__":
    main()