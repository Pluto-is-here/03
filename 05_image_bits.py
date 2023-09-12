
# checks input is a number more than a given value
def num_check(question, low):

    valid = False
    while not valid:

        error = "Please enter a number that is more than (or equal to) {}".format(low)

        try:
            # asks user to enter a number
            response =int(input(question))

            # checks number is more than zero
            if response >= low:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)

# finds # bits for 24 bit colour


def image_bits():

    img_width = num_check("What is your image width? ", 1)
    img_height = num_check("What is your image height? ", 1)

    # calculate # of bits (length of string x 8
    num_pixels = img_width * img_height

    num_bits = num_pixels * 24

    # output answer with working

    print()
    print("# of pixels = {} x {} = {}".format(img_height, img_width, num_bits))
    print("# of bits = {} x 24 = {}".format(num_pixels, num_bits))
    print()

    return ""

# Main routine


image_bits()

