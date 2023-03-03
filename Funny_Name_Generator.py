def nameGenerator(name):
    firstname = name + "y";
    lastname = "Mc"+name+"erface";
    fullname = firstname + " " + lastname;
    print(fullname)

name = (input("What is your name? "))
nameGenerator(((name)))
