print("hellow world!")


def multiplication():

    x = input("give me a number to multiply: ")
    y = input("what do you want it multiplied by? ")

    z = int(x) * int(y)

    print("the result is: " + str (z))



def division():

    x = input("give me a number to divide: ")
    y = input("what do you want it divide by? ")

    z = float(x) / float(y)

    print("the result is: " + str (z))



def wide_boy_string():

    user_str = input("give me a string to w i d e n: \n")

    for char in user_str:
        print(char, end =" ")



def wide_boy_string2():

    user_str = input("give me a string to w i d e n: \n")

    i = 0 

    wide_str =" "

    for char in user_str:
        if i < len(user_str) - 1:
         wide_str = wide_str + char + " "
        else:
         wide_str = wide_str + char

        i += 1
        
    print(wide_str)





def for_loop_example():

    x = int(input ("how many times should I run? "))

    for i in range(x):
      print("Jake Peralta is the best detective/genius "+ str(i+1) +" time.")



def odd_even():
    x = int(input("which number do you want me to check? "))

    if x % 2 == 0:
        print("The number "+ str(x) +" is even!")
    else:
        print("The number "+ str(x) +" is odd!")



def ascii_values():
    user_str = input("give me a string for which you want the sum of the ASCII values of its chars: \n")

    str_size = len(user_str)

    i = 0 

    sum = 0

    while(i < str_size):

        sum = sum + ord(user_str[i])
        i = i + 1
        
    print("The sum of all these ASCII values is ", sum)



def string_flipper():
    user_str = input("Gime me a string you want reversed: \n")

    for char in reversed (user_str):
        print(char, end = "")



user_input = int(input("Which function do you want to run? "))

if user_input == 0:
    multiplication()
elif user_input == 1:
    division()

elif user_input == 2:
    wide_boy_string()

elif user_input == 3:
    wide_boy_string2()


elif user_input == 4:
    for_loop_example()

elif user_input == 5:
    odd_even()

elif user_input == 6:
    ascii_values()

