import sys
import os

# test pages
nytimes_com = "This New Liquid Is Magnetic, and Mesmerizing\n\nScientists have created...\nMost Wikipedia Profiles Are...\n...has added nearly 700 Wikipedia biographies for important.."
bloomberg_com = "The Space Race: From Apollo 11...\n\nIt's 50 years since...\nTwitter CEO...\nTwitter and Square Chief Executive Officer..."


def save_tab_content_to_file(path, page_content):
    with open(path, "w") as file:
        file.write(page_content)


def load_tab_content_from_file(path):
    with open(path, "r") as file:
        return file.readlines()


def create_directory(path):
    if os.path.exists(path):
        return
    else:
        os.makedirs(path)


def run():
    args = sys.argv
    if args.__len__() != 2:
        print("Error, incorrect number of arguments")
        return
    else:
        create_directory(args[1])  # directory for tabs

    # main loop
    while True:
        input_ = input()

        if input_.lower() == "exit":
            return
        if input_.__contains__('.'):  # url
            if input_ == "bloomberg.com":
                print(bloomberg_com)
                save_tab_content_to_file(args[1] + "\\" + input_[:input_.rindex(".")] + ".txt", bloomberg_com)
            elif input_ == "nytimes.com":
                print(nytimes_com)
                save_tab_content_to_file(args[1] + "\\" + input_[:input_.rindex(".")] + ".txt", nytimes_com)
            else:
                print("Error, incorrect input, please try again\n")
            continue

        try:  # tab
            page_content = load_tab_content_from_file(args[1] + "\\" + input_ + ".txt")
        except FileNotFoundError:
            print("Error, incorrect input, please try again\n")
        else:
            print(*page_content, sep="")


run()
