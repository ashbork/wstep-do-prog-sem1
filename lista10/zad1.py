import re


def remove_phrase(input: str, to_remove: str):
    '''Removes a phrase from the input string and shows the amount of occurences'''
    phrases = re.findall(f"({to_remove})", input)
    print(f"Found {len(phrases)} occurences of the phrase {to_remove}.")
    print(f"Final phrase is {re.sub(f'({to_remove})', '', input)}\n")


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
