import sys
import os
import requests
import re
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
    name = url[:50]
    name = name.lstrip("htps:").lstrip("/")
    name = re.sub("[/?]+", "_", name)
    return f"{name}__{url.__hash__()}.txt"


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
        in_ = input().strip()
        in_lower = in_.lower()

        if in_lower == "exit":
            return

        # url
        if in_.__contains__('.'):
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

                if tab_history_index == -1 or tab_history[tab_history_index] != url:
                    while len(tab_history) - 1 != tab_history_index:
                        tab_history.pop()
                    tab_history.append(url)
                    tab_history_index += 1
            else:
                print("Error, something went wrong_\n")

        # move to prev/next page
        elif in_lower == "b" or in_lower == "back" or in_lower == "f" or in_lower == "forward":
            if in_lower == "b" or in_lower == "back":
                if tab_history_index == 0 or tab_history_index == -1:
                    continue
                tab_history_index -= 1
            else:
                if tab_history_index == tab_history.__len__() - 1:
                    continue
                tab_history_index += 1

            print(*load_tab_content_from_file(args[1] + "\\" + url_to_filename(tab_history[tab_history_index])), sep="")

        else:
            print("Error, incorrect input, please try again\n")


run()
