import re
from rich.console import Console
from rich.rule import Rule

console = Console()

console.print(Rule(title="Regex", align="left"), "")


def remove_phrase(input: str, to_remove: str):
    '''Removes a phrase from the input string and shows the amount of occurences'''
    phrases = re.findall(f"({to_remove})", input)
    console.print(
        f"Found [red bold]{len(phrases)}[/] occurences of the phrase [red bold]{to_remove}.")
    console.print(
        f"Final phrase is [green italic]{re.sub(f'({to_remove})', '', input)}\n")


# the pattern is case-sensitive, as shown here:
remove_phrase("python2020@gusun_tomail.com", "Usun_to")
# it works on arbitrary input strings
remove_phrase("abcde", "a")
# finds non-overlapping occurences
# (if we were to search for overlapping ones too,
# it'd return an empty string):
remove_phrase("abbabbabba", "abba")
# works properly with the given string
remove_phrase("python2020@gusun_tomail.com", "usun_to")
