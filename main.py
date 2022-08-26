# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

#function to convert USD to INR
def conv1(r):
    INR = 79.81 * r
    return INR

#function to convert INR to USD
def conv2(r):
    USD = r / 79.81
    return USD

#function to convert USD to GBP
def conv3(r):
    GBP = r / 1.18
    return GBP

#function to convert GBP to USD
def conv4(r):
    USD = 1.18 * r
    return USD

#function to convert INR to GBP
def conv5(r):
    GBP = r/ 94.10
    return GBP

#function to convert GBP to INR
def conv6(r):
    INR = r * 94.10
    return INR

#function to convert EURO to INR
def conv7(r):
    INR = r * 79.80
    return INR

#function to convert INR to EURO
def conv8(r):
    EURO = r/ 79.80
    return EURO

#function to convert USD to EURO
def conv9(r):
    EURO = r * 1
    return EURO

#function to convert EURO to USD
def conv10(r):
    USD = r/1
    return USD

#function to convert EURO to GBP
def conv11(r):
    GBP = r/1.18
    return GBP

#function to convert GBP to EURO
def conv12(r):
    EURO = r + 1.18
    return EURO

#function to convert INR to YEN
def conv13(r):
    YEN = r + 1.72
    return YEN

#function to convert YEN to INR
def conv14(r):
    INR = r/1.72
    return INR

#function to convert USD to YEN
def conv15(r):
    YEN = r * 137.35
    return YEN

#function to convert YEN to USD
def conv16(r):
    USD = r/137.35
    return USD

#function to convert GBP to YEN
def conv17(r):
    YEN = r * 161.66
    return YEN

#function to convert YEN to GBP
def conv18(r):
    GBP = r/161.66
    return GBP

#function to convert EURO to YEN
def conv19(r):
    YEN = r * 137.31
    return YEN

#function to convert YEN to EURO
def conv20(r):
    EURO = r/137.31
    return EURO


if __name__ == '__main__':
    print_hi('PyCharm')


ConvF = (input("Convert from: "))
ConvT = (input("Convert to: "))
Amount = int(input("Amount: "))



if ConvF == "USD" and ConvT == "INR":
    INR = conv1(Amount)
    print(INR)

elif ConvF == "INR" and ConvT == "USD":
     USD = conv2(Amount)
     print(USD)

elif ConvF == "USD" and ConvT == "GBP":
     GBP = conv3(Amount)
     print(GBP)

elif ConvF == "GBP" and ConvT == "USD":
     USD = conv4(Amount)
     print(USD)

elif ConvF == "INR" and ConvT == "GBP":
     GBP = conv5(Amount)
     print(GBP)

elif ConvF == "GBP" and ConvT == "INR":
     INR = conv6(Amount)
     print(INR)

elif ConvF == "EURO" and ConvT == "INR":
     INR = conv7(Amount)
     print(INR)

elif ConvF == "INR" and ConvT == "EURO":
     EURO = conv8(Amount)
     print(EURO)

elif ConvF == "USD" and ConvT == "EURO":
     EURO = conv9(Amount)
     print(EURO)

elif ConvF == "EURO" and ConvT == "USD":
    USD = conv10(Amount)
    print(USD)

elif ConvF == "EURO" and ConvT == "GBP":
    GBP = conv11(Amount)
    print(GBP)

elif ConvF == "GBP" and ConvT == "EURO":
    EURO = conv12(Amount)
    print(EURO)

elif ConvF == "INR" and ConvT == "YEN":
    YEN = conv13(Amount)
    print(YEN)

elif ConvF == "YEN" and ConvT == "INR":
    INR = conv14(Amount)
    print(INR)

elif ConvF == "USD" and ConvT == "YEN":
    YEN = conv15(Amount)
    print(YEN)

elif ConvF == "YEN" and ConvT == "USD":
    USD = conv16(Amount)
    print(USD)

elif ConvF == "GBP" and ConvT == "YEN":
    YEN = conv17(Amount)
    print(YEN)

elif ConvF == "YEN" and ConvT == "GBP":
    GBP = conv18(Amount)
    print(GBP)

elif ConvF == "EURO" and ConvT == "YEN":
    YEN = conv19(Amount)
    print(YEN)

elif ConvF == "YEN" and ConvT == "EURO":
    EURO = conv20(Amount)
    print(EURO)