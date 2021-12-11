import pathlib


def search_path_for_workfiles(path: str = ""):
    subdir = pathlib.Path.cwd() / path
    print(subdir)
    return [str(child.relative_to(subdir)) for child in subdir.rglob("*.pdf") if "praca" in child.name.lower()]


for index, element in enumerate(search_path_for_workfiles("pdfs1")):
    print(f"{index+1}. {element}")
for index, element in enumerate(search_path_for_workfiles()):
    print(f"{index+1}. {element}")
