""""" This  project is first code of opencv  it include 3 methods  show simple image 
and second  for  black and white image and third one is for flip"""



import cv2

print("This is first project which i make in opencv.")
print("you can see  image which  you  givve")


print("Enter a type of  viewer you want use")
key = int(input("Options \n 1. simple \n 2. greyscale \n 3. flip \n 4. exit \n"))

if key == 1:
    path = input("Please enter full path of a image :- ")
    print("your enter path is", path)

    img = cv2.imread(path)

    print("this is matrix of image ",img)
    img = cv2.resize(img, (1280,700))
    cv2.imshow('this is window name', img)


    k = cv2.waitKey(5000)

    if k==ord("s"):
        cv2.destroyAllWindows()

    cv2.destroyAllWindows()

if key == 2:
    path = input("Please enter full path of a image :- ")
    print("your enter path is", path)

    img = cv2.imread(path)

    print("this is matrix of image ",img)
    img = cv2.resize(img, (1280,700))
    ime = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('this is window name', img)


    k = cv2.waitKey(5000)

    if k==ord("s"):
        cv2.destroyAllWindows()

    cv2.destroyAllWindows()

if key == 3:
    path = input("Please enter full path of a image :- ")
    print("your enter path is", path)

    img = cv2.imread(path)

    print("this is matrix of image ",img)
    img = cv2.resize(img, (1280,700))
    img = cv2.flip(img, -1)
    cv2.imshow('this is window name', img)


    k = cv2.waitKey(5000)

    if k==ord("s"):
        cv2.destroyAllWindows()

    cv2.destroyAllWindows()



cv2.destroyAllWindows()



