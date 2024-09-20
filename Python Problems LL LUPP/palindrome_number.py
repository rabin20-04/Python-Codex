import re  # noqa        -----   regular expression module


def check_palindrome(get_string):
    forward = "".join(re.findall(r"[a-z]+", get_string.lower()))
    # a,z match either a  or z  and a-z  match a to z
    reverse = forward[::-1]

    return forward == reverse


print(check_palindrome("Nice car"))
print(check_palindrome("Race car"))
get_string = str(input("Enter a string: "))
print(check_palindrome(get_string))
