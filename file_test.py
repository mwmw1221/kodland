import discord
with open("test.txt") as f:
    ff = open("test2.txt","w")
    ff.write(f.read())
    ff.close()

with open("test2.txt") as f:
    print(f.read())

with open("test.txt") as f:
    print(f.read())