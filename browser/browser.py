import sys
import os
import requests
from _collections import deque


def save_tab_content_to_file(path, page_content):
    with open(path, "w", encoding="utf-8") as file:
        file.write(page_content)


def load_tab_content_from_file(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.readlines()


def create_directory(path):
    if os.path.exists(path):
        return
    else:
        os.makedirs(path)


def url_to_filename(url):
    name = url[:url.rindex(".")]
    name = name[name.rindex("/") + 1:]
    return name + ".txt"


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

        # tab
        filepath = args[1] + "\\" + in_ + ".txt"
        if os.path.exists(filepath):
            page_content = load_tab_content_from_file(filepath)

            if tab_history_index == -1 or tab_history[tab_history_index] != filepath:
                while len(tab_history) - 1 != tab_history_index:
                    tab_history.pop()
                tab_history.append(filepath)
                tab_history_index += 1

                print(*page_content, sep="")

        elif in_.__contains__('.'):  # url
            url = in_
            if not url.startswith("http"):
                url = "https://" + url
            try:
                response = requests.get(url)
            except IOError:
                print("Error, something went wrong\n")
                continue
            # response.encoding = "utf-8"

            if requests:
                print(response.text)

                filepath = args[1] + "\\" + url_to_filename(url)
                save_tab_content_to_file(filepath, response.text)

                if tab_history_index == -1 or tab_history[tab_history_index] != filepath:
                    while len(tab_history) - 1 != tab_history_index:
                        tab_history.pop()
                    tab_history.append(filepath)
                    tab_history_index += 1
            else:
                print("Error, something went wrong_\n")

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

        else:
            print("Error, incorrect input, please try again\n")


run()
