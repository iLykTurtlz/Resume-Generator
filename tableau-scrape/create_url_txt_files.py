from lists import LISTS
import os

DIR_PATH = "url-lists"

if __name__ == "__main__":
    if not os.path.exists(DIR_PATH):
        os.mkdir(DIR_PATH)
        
    for list_name, urls in LISTS.items():
        with open(f"{DIR_PATH}/{list_name}.txt", "w") as f:
            f.write("\n".join(urls))