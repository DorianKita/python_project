f_name = input("What is your first name:")
l_name = input("What is your last name:")

def format_name(f_name, l_name):
    title_f_name = f_name.title()
    title_l_name = l_name.title()

    return f"{title_f_name} {title_l_name}"

formatted_string = format_name(f_name, l_name)
print(formatted_string)