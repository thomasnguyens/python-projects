#Thomas Nguyen
#P6.40 Fade in Program

"""
I, Thomas Nguyen, do hereby certify that we have derived no assistance for this project or
examination from any sources whatever, whether oral, written, or in print other than allowed
research which has been cited.

P6.40
Write a program that reads a sound file and “fades in” the sound.
Multiply the values of the first second with a factor that increases from 0 to 1.

"""

import numpy
import scipy.io.wavfile

def main(inputname):
    inputname = input("Input file: ") #prompting the user to input a file name
    contents = scipy.io.wavfile.read(inputname) #reading the contents in file
    samplerate = contents[0] #this is the amount of
    data = contents[1].tolist()  # Now it's a Python list
    outputdata = fadeIn(data, samplerate, 20)
    outputname = inputname.replace(".wav", ".fadeIn.wav")
    scipy.io.wavfile.write(outputname, samplerate,
                           numpy.asarray(outputdata, dtype="int16"))


def fadeIn(data, samplerate, seconds):
    count = seconds * samplerate #as the sampleRate get higher, count increases, so a fade occurs
    result = [] #empty array to put the new fadeIn contents here
    for i in range(len(data)): #loops through all the contents in input file
        if i < count: #if index is less than count, we want to append the data here
            result.append(data[i] * i/count)
        else: #we keep data same if index is higher than count because we don't want to do all the seconds
            result.append((data[i]))
    return result



# Start the program.
main()

