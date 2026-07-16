print("Hello".rjust(10))
print("*********************************")
print("Hello World!".center(30,"="))
print(len("Hello World!"))
print(("Hello World!".center(30, "=")).count("="))
print(r"'    Hello World!    '".strip())
print(r"'    Hello World!    '".lstrip("'"))
print(r"'    Hello World!    '".rstrip())
spam = "SpamSpamBaconSpamEggsSpamSpam"
print(spam.strip("SnmBpaaco")) #order of letters is not imporant for stripping