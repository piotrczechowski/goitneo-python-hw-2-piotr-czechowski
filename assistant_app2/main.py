def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except TypeError:
            return "Invalid command. Please provide name and phone number()."
        except IndexError:
            return "Wrong index number."
    return inner

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command. Please provide name and phone number."    
    name, phone = args
    contacts[name] = phone
    return ("Contact added.")

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command. Please provide name and new phone number."
    name, phone = args
    if name not in contacts:
        return "Contact not found."
    contacts[name] = phone
    return "Contact updated."


@input_error   
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid command. Please provide name."
    name = args[0]
    if name not in contacts:
        return "Contact not found."
    return contacts[name]


def main():
    contacts = {}
    
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        try:
            command, args = parse_input(user_input)
        except ValueError:
            print("Invalid input format. Please try again.")
            continue

        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")
        
if __name__ == "__main__":
    main()
