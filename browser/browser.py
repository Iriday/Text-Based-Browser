import sys
import os
from _collections import deque

# temp  test pages
nytimes_com = "page1\ndata.."
bloomberg_com = "page2\ndata.."
google_com = "page3\ndata.."
test_pages = {"bloomberg.com": bloomberg_com, "nytimes.com": nytimes_com, "google.com": google_com}


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

    tab_history = deque()
    tab_history_index = -1
    # main loop
    while True:
        in_ = input()
        in_lower = in_.lower()

        if in_lower == "exit":
            return
        if in_.__contains__('.'):  # url
            if in_ in test_pages:
                print(test_pages[in_])

                filepath = args[1] + "\\" + in_[:in_.rindex(".")] + ".txt"
                save_tab_content_to_file(filepath, test_pages[in_])

                if tab_history_index == -1 or tab_history[tab_history_index] != filepath:
                    while len(tab_history) - 1 != tab_history_index:
                        tab_history.pop()
                    tab_history.append(filepath)
                    tab_history_index += 1
            else:
                print("Error, incorrect input, please try again\n")
            continue
        elif in_lower == "b" or in_lower == "back" or in_lower == "f" or in_lower == "forward":
            if in_lower == "b" or in_lower == "back":
                if tab_history_index == 0 or tab_history_index == -1:
                    continue
                tab_history_index -= 1
            else:
                if tab_history_index == tab_history.__len__() - 1:
                    continue
                tab_history_index += 1

            print(*load_tab_content_from_file(tab_history[tab_history_index]), sep="")
            continue

        try:  # tab
            filepath = args[1] + "\\" + in_ + ".txt"
            page_content = load_tab_content_from_file(filepath)

            if tab_history_index == -1 or tab_history[tab_history_index] != filepath:
                while len(tab_history) - 1 != tab_history_index:
                    tab_history.pop()
                tab_history.append(filepath)
                tab_history_index += 1
        except FileNotFoundError:
            print("Error, incorrect input, please try again\n")
        else:
            print(*page_content, sep="")


run()
