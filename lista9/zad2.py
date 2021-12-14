import pathlib


def search_path_for_workfiles(path: str = ""):
    # First, get the current working directory and append the path parameter.
    subdir = pathlib.Path.cwd() / path
    print(subdir)
    # Using a list comprehension, return a list of stringified paths relative
    # to the subdirectory (subdir) which are both
    # .pdf files and contain "praca" in their name.
    return [str(child.relative_to(subdir)) for child in subdir.rglob("*.pdf")
            if "praca" in child.name.lower()]


for index, element in enumerate(search_path_for_workfiles("pdfs1")):
    print(f"{index+1}. {element}")
for index, element in enumerate(search_path_for_workfiles()):
    print(f"{index+1}. {element}")
