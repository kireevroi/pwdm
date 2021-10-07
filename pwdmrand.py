#This file handles random password generation

#for randomization
import random
#for ascii finding
import string

#constants that will be replaced when input is managed


#blank password as of now

#random integer generator
def rand_num():
    return str(random.randint(0,9))

#random special character generator
def rand_scar():
    return random.choice(string.punctuation)

#random lowercase letter generator
def rand_let_l():
    return random.choice(string.ascii_lowercase)

#random uppercase letter generator
def rand_let_u():
    return random.choice(string.ascii_uppercase)

#generating one of two: upper or lowercase letter
def rand_let_ul():
    return random.choice([rand_let_l(), rand_let_u()])

#shuffling the password because the numbers are always at the beginning
def shuffle_pwd(unpwd):
    unpwd = list(unpwd)
    random.shuffle(unpwd)
    return ''.join(unpwd)

#PASSWORD GENERATION
#input length, # of numbers and need for uppercase letters
def pwd_gen(pwdlen, nofnum, nofscar, uplcase):
    #creating a counter and empty string
    pwd = ""
    j = 0
    k = 0
    #starting a loop with password length
    for i in range(0, pwdlen):
        #adding the numbers first, while skipping the loop iterations
        if j < nofnum:
            pwd = pwd + rand_num()
            j += 1
            continue
        if k < nofscar:
            pwd = pwd + rand_scar()
            k += 1
            continue
        #checking if there should be uppercase
        if uplcase == True:
            pwd = pwd + rand_let_ul()
        #otherwise just adding lower
        else:
            pwd = pwd + rand_let_l()
    #shuffling everything
    pwd = shuffle_pwd(pwd)
    #returning result
    return pwd

#STRONG PASSWORD GENERATION
# input length and need of space
def pwd_str_gen(pwdlen, spcstr):
    #defining blank string
    pwd = ""

    #checking for the need of spaces and makeing a variable for the space
    if spcstr == True:
        spc = ' '
    else:
        spc = ''

    #extracting words from the dtb file and joining them either with or without
    #spaces
    for i in range(0, pwdlen):
        with open("data\worddtb.txt", "r") as file:
            text = file.read()
            words = list(map(str, text.split()))

        #first space case :)
        if i == 0:
            pwd = pwd + random.choice(words).lower()
        else:
            pwd = pwd + spc + random.choice(words).lower()

    #returning the result (technically already shuffled)
    return pwd

#getting result password for export
#pwdlen is the length of password, nofnum is the amount of numbers
#uplcase checks for uppercase, spcstr checks for spaces in power str
# pwdstr checks if you want strong keypass password
# nofscar checks for number of special characters
def pwd_exp(pwdlen = 8, nofnum = 1, nofscar = 1, uplcase = True, spcstr = True, pwdstr = False):

    #Checking if PWD should be STRONG
    if pwdstr == True:
        pwd = pwd_str_gen(pwdlen, spcstr)
    else:
        pwd = pwd_gen(pwdlen, nofnum, nofscar, uplcase)
    return pwd
