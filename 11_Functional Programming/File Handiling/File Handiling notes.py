try:
    stream = open('animals.txt')

    stream.close
except Exception as e:
    print('An error occurred: ', e)