import requests
    #req for webex api
import os
    #os for exit

    #f' is string format for python
WEBEX_BASE_URL = 'https://webexapis.com/v1'
def test_connection(accT):
    try:
        url = f'{WEBEX_BASE_URL}/people/me'
        headers = {'Authorization' : f'Bearer {accT}'}
        response = requests.get(url, headers = headers)
        response.raise_for_status() 
        print("Connetion test to Webex successful!")
    #except block to handle exceptions
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")
        print("Please check your access token and try again.")
        exit()

def get_userInfo(accT):
    try:
        url = f'{WEBEX_BASE_URL}/people/me'
        headers = {'Authorization' : f'Bearer {accT}'}
        response = requests.get(url, headers = headers)
        response.raise_for_status()
            
        
        datawebex = response.json()
        print("\nDisplay Name : " + datawebex["displayName"])
        print("\nNickname : " + datawebex["nickName"])
        print("\nEmail : " + datawebex["emails"][0]) 
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")

def list_rooms(accT):
    try:
        url = f'{WEBEX_BASE_URL}/rooms'
        headers = {'Authorization' : f'Bearer {accT}'}
        response = requests.get(url, headers = headers)
        response.raise_for_status()
            
        rooms = response.json()['items'][:5] #get the first 5 rooms
        for room in rooms: 
                print("\nRoom ID : " + room["id"])
                print("\nRoom Title : " + room["title"])
                print("\nDate Created : " + room["created"])
                print("\nLast Activity : " + room["lastActivity"])
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")

def create_room(accT):
    try:
        url = f'{WEBEX_BASE_URL}/rooms'
        headers = {'Authorization': f'Bearer {accT}', 'Content-Type': 'application/json'}
        room_title = input("Enter room title: ")
        data = {'title': room_title}
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        print("Room created successfully!")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def send_message(accT):
    try:
        url = f'{WEBEX_BASE_URL}/rooms'
        headers = {'Authorization': f'Bearer {accT}'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        rooms = response.json()['items'][:5] #get the first 5 rooms
        for i, room in enumerate(rooms, start=1):
            print(f"{i}. {room['title']}")

        room_number = int(input("Choose room: \n>>: ").strip())
        message = input("Enter the message: ")

        selected_room_id = rooms[room_number - 1]['id']
        url = f'{WEBEX_BASE_URL}/messages'
        headers = {'Authorization': f'Bearer {accT}', 'Content-Type': 'application/json'}
        data = {'roomId': selected_room_id, 'text': message}
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        print("Message sent successfully!")
        cont_send_message(accT)  #send another message
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def cont_send_message(accT):
    try:
        while True:
            choice = input("Do you want to send another message? Insert (y/n):\n\n>>: ").strip()
            if choice == 'y' or choice == 'Y':
                send_message(accT)  # Send another message
            elif choice == 'n' or choice == 'N':
                break  # Exit loop
            else:
                print("ERROR: INVALID CHOICE\nPlease Try Again\nExiting...")
                exit()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def print_menu():
        menu_title = "Wazo-byte WEBEX Troubleshoot Tool"
        menu_opts = [
                        "1. Display user information",
                        "2. List of rooms",
                        "3. Create a room",
                        "4. Send message to a room",
                        "5. Exit"
                    ]
        # Determine width of the box len to get length of the string
        box_width = max(len(menu_title), max(len(option) for option in menu_opts)) + 6
        # Print top border
        print("+" + "-" * (box_width - 2) + "+")
        # Print menu title
        print("|" + menu_title.center(box_width - 2) + "|")
        # Print middle border
        print("+" + "-" * (box_width - 2) + "+")
        # Print menu options
        for option in menu_opts:
            print("|" + option.ljust(box_width - 2) + "|")
        # Print bottom border
        print("+" + "-" * (box_width - 2) + "+")

    #main function
def main():
    print("+" + "-" * 45 + "+")
    print("|" + "Welcome To Wazo-byte WEBEX Troubleshoot Tool ".center(30) + "|")
    print("+" + "-" * 45 + "+")
    print("|" + "Enter your Webex Access Token:".center(45) + "|")
    print("+" + "-" * 45 + "+")
    accT = input(">>: ").strip()#strip removes white space
    test_connection(accT)
    

    while True:
        print_menu()  # Print menu 
            
        # Get user option
        opt = int(input(">>: ")) 
            # get_userInfo
        if opt == 1:
            get_userInfo(accT)
            # option 2
        elif opt == 2:
            list_rooms(accT)
            # option 3
        elif opt == 3:
            create_room(accT)
        # option 4
        elif opt == 4:
            send_message(accT)
            # option 5
        elif opt == 5:
            print("Thank you for choosing us\nExiting...")
            exit()
        else:
            print("Invalid option. Please try again.")
        continue  # will loop until user chooses a valid option

    # check if script is runned by python idle
if __name__ == "__main__":
    main()
