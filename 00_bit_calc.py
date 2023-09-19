# Function goes here

# Puts a series of symbols at the start and end of text (for emphasis)

def statement_generator(text, decoration):

    # Make string with five characters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# displays instructions / information
def instructions():

    statement_generator("Instructions / Information", "=")
    print()
    print("Please choose a data type (Image / Text / Integer")
    print()
    print("This program assumes that images are being represented in 24 bit colour ")
    print( "(ie: 24 bits per pixel). For text, "
           "we assume that ascii encoding is being used ")
    print("(8 bits per character).")
    print()
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to "
          "quit.")
    print()
    return ""


# check user choice is integer, text, or image
def user_choice():

    valid = False

    while not valid:

        response = input("File type (integer / text / image): ").lower()
        text_ok = ["text", "t", "txt"]
        img_ok = ["image", "pix", "img", "picture", "pic", "p"]
        int_ok = ["integer", "#", "int", "number"]
        if response in text_ok:
            return "text"

        elif response in img_ok:
            return "image"

        elif response in int_ok:
            return "integer"

        elif response == "i":
            want_integer = input("Press <enter> for an integer or any key for image")
            if want_integer == "":
                return "integer"
            else:
                return "image"

        else:
            # if response is not valid, out put error
            print("Please choose a valid file type!")
            print()


# checks input is a number more than a given value
def num_check(question, low):

    valid = False
    while not valid:

        error = "Please enter a number that is more than (or equal to) {}".format(low)

        try:
            # asks user to enter a number
            response = int(input(question))

            # checks number is more than zero
            if response >= low:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)


# calculates the # of bits for text ( # of characters x 8)
def int_bits():
    var_integer = num_check("Please enter an integer: ", 0)
    var_binary = "{0:b}".format(var_integer)

    num_bits = len(var_binary)

    print()
    print("{} in binary is {}".format(var_integer, var_binary))
    print("# of bits is {}".format(num_bits))
    print()

    return ""


# finds # bits for 24 bit colour
def image_bits():

    img_width = num_check("What is your image width? ", 1)
    img_height = num_check("What is your image height? ", 1)

    # calculate # of bits (length of string x 8
    num_pixels = img_width * img_height

    num_bits = num_pixels * 24

    # output answer with working

    print()
    print("# of pixels = {} x {} = {}".format(img_height, img_width, num_pixels))
    print("# of bits = {} x 24 = {}".format(num_pixels, num_bits))
    print()

    return ""


# calculates the # of bits for text (# of characters x 8)
def text_bits():

    print()
    # ask user for a string ...
    var_text = input("Enter some text: ")

    # calculate # of buts (length of string x 8
    var_length = len(var_text)
    num_bits = 8 * var_length

    # output answer with working
    print()
    print("\'{}\' has {} characters ... ".format(var_text, var_length))
    print(" # of bits is {} x 8...".format(var_length))
    print("We need {} bit to represent {}".format(num_bits, var_text))
    print()

    return ""

# main routine goes here


# Heading
statement_generator("Bit Calculator for Integers, Text and Images", "-")

# Display instructions if user has not used the program before
first_time = input("Press <enter> to see the instructions or any key to continue")

if first_time == "":
    instructions()


keep_going = ""
while keep_going == "":

    print()
    data_type = user_choice()
    print("You chose", data_type)

# for integers, ask for integer

    if data_type == "integer":
        int_bits()

        # For images, ask for width and height
        # ( must be integers more than / equal to 1 )
    elif data_type == "image":
        image_bits()

        # for text, ask for a string
    else:
        text_bits()

    print()
    keep_going = input("Please <enter> to continue or  any key to quit")
    print()


