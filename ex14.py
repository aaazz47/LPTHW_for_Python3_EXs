from sys import argv

script, user_name, call = argv    # 加一个 call
prompt = '%s > ' % user_name    # 改成这样试试

print("Hi %s, I'm the %s script." % (user_name, script))
print("Hmmm， you want me call you %s" % call)    # call 在这里
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % user_name)
likes = input(call + " " + prompt)

print("Where do you live %s?" % user_name)
lives = input(call + " " + prompt)

print("What kind of computer do you have?")
computer = input(call + " " + prompt)

print("""
Alright, so you said %r about liking me.
you live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer))
