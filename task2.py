def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, *args


def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid arguments. Expected add <username> <phone>"

    name, phone = args

    if name in contacts:
        return "Contact aready exists. Use update command"

    contacts[name] = phone

    return "Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid arguments. Expected: add <username> <phone>"

    name, phone = args

    if not name in contacts:
        return "Contact does not exist. Use add command first"

    contacts[name] = phone

    return "Contact updated."


def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid arguments. Expected: phone <username>"

    name, = args

    if not name in contacts:
        return "Contact does not exist"

    return contacts[name]


def show_all(contacts):
    if not len(contacts.keys()):
        return "No contacts added, use add command to add some"

    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        command_input = input("Enter a command: ").strip().lower()
        command, *args = parse_input(command_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        output = "Invalid command."

        if command == "add":
            output = add_contact(args, contacts)
        elif command == "change":
            output = change_contact(args, contacts)
        elif command == "phone":
            output = show_phone(args, contacts)
        elif command == "all":
            output = show_all(contacts)
        elif command == "hello":
            output = "How can I help you?"

        print(output)


if __name__ == "__main__":
    main()
