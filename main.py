from my_select import select_dict


def parsing_query(query_num: str) -> dict:    
    query_dict = {}
    args_dict = {}

    for key, value in select_dict.items():
        if query_num.strip() == key.removeprefix("select_"):
            query_dict["func"] = value["func"]

            for name in value["args"]:
                if name:
                    arg = input(f"Enter {name[0]} or {name[1]}: ")
                    if arg.isdigit():
                        args_dict.update({f"{name[1]}": arg})
                    else:
                        args_dict.update({f"{name[0]}": arg})
    
    query_dict.update({"args": args_dict})
    
    return query_dict


def main():
    
    while True:
        query_num = input("\nEnter the request number: ")

        if query_num == "":
            break
        
        try:
            query_dict = parsing_query(query_num)
            args = [item for item in query_dict["args"].values()]
            func = query_dict["func"]

            for i in func(*args):
                print(i)

        except FileNotFoundError:
            print("Invalid request number, such a number does not exist.")
        except Exception as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
