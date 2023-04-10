#Thomas Nguyen
#soundProcessing

"""
I, Thomas Nguyen, do hereby certify that we have derived no assistance for this project or
examination from any sources whatever, whether oral, written, or in print other than allowed
research which has been cited.

soundProcessing
Creates a main program that
asks the user how they would like to process the file,
e.g. 1. Fade In, 2. Reverse

"""

import numpy
import scipy.io.wavfile

"fade in fxn:" \
"This one takes the content of input and fades in the audio file"
def main(inputname):
    contents = scipy.io.wavfile.read(inputname) #reading the contents in file
    samplerate = contents[0] #getting the contents and putting it in samplerate
    data = contents[1].tolist()  # Now it's a Python list
    outputdata = fadeIn(data, samplerate, 4) #calling fadeIn fxn and using sample rate and how long to fade it in
    outputname = inputname.replace(".wav", ".fadeIn.wav")
    scipy.io.wavfile.write(outputname, samplerate,
                           numpy.asarray(outputdata, dtype="int16")) #this displays the output file into the folder
"reverse fxn:" \
"This one takes the content of inputted audio file and plays it in reverse"
def main1(inputname):


    contents = scipy.io.wavfile.read(inputname) #reading the contents in inputted file
    samplerate = contents[0] #getting the contents and putting it in samplerate
    data = contents[1].tolist()  # Now it's a Python list
    outputdata = reverse(data) #the output data is new data from the reverse fxn
    outputname = inputname.replace(".wav", ".reverse.wav")  # replace input name with this
    scipy.io.wavfile.write(outputname, samplerate,
                           numpy.asarray(outputdata, dtype="int16"))

def fadeIn(data, samplerate, seconds):
    count = seconds * samplerate #as the sampleRate get higher, count increases, so a fade occurs
    result = [] #empty array to put the new fadeIn contents here
    for i in range(len(data)): #loops through all the contents in input file

        '''this determines if the index is greater or less than count, 
        if it's less than count, it will append the division of data * count by count to get fade in values'''
        if i < count: #if index is less than count, we want to append the data here
            result.append(data[i] * i/count)
        else: #we keep data same if index is higher than count because we don't want to do all the seconds
            result.append((data[i]))
    return result

def reverse(data):
    result = [] #empty array to put the reversed data here
    for i in range(0, len(data)): #loops through data
        result = data[::-1] #this reverses the data and puts it in result

    return result #returns result back to main fxn

# Start the program.


ans = input("how would you like to process the file\n"
            "1: fade in\n"
            "2: reverse audio\n")

if ans == '1':
    inputname = input("Input file: ")
    main(inputname)
elif ans == '2':
    inputname = input("Input file: ")
    main1(inputname)
else:
    print("Error! please try again.")