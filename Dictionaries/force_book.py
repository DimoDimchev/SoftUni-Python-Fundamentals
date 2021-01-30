command = input()
forces_dict = {}


def add_user(forces_dict, force_Side, force_User):
    if force_Side not in forces_dict:
        forces_dict[force_Side] = []


    for side, members in forces_dict.items():
        if force_User in members:
            return forces_dict

    if force_User not in forces_dict[force_Side]:
        forces_dict[force_Side].append(force_User)

    return forces_dict


def transfer_user(forces_dict, force_Side, force_User):
    is_new = True
    for side, user in forces_dict.items():
        if force_User in user:
            forces_dict[side].remove(force_User)
            is_new = False
            return add_user(forces_dict, force_Side, force_User)

    if is_new:
       return add_user(forces_dict, force_Side, force_User)


while command != "Lumpawaroo":
    data_list = command.split(" | ")
    if len(data_list) > 1:
        force_Side, force_User = command.split(" | ")
        forces_dict = add_user(forces_dict, force_Side, force_User)
    else:
        force_User, force_Side = command.split(" -> ")
        forces_dict = transfer_user(forces_dict, force_Side, force_User)
        print(f"{force_User} joins the {force_Side} side!")
    command = input()

final_dict = sorted(forces_dict.items(), key=lambda x: (-len(x[1]), x[0]))

for side, users in final_dict:
    if len(users) > 0:
        print(f"Side: {side}, Members: {len(users)}")
        for user in sorted(users):
            print(f"! {user}")