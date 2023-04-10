#Thomas Nguyen
#P6.45 Reverse Program
"""
I, Thomas Nguyen, do hereby certify that we have derived no assistance for this project or
examination from any sources whatever, whether oral, written, or in print other than allowed
research which has been cited.

P6.45 Write a program that reads a sound file,
reverses all values, and saves the result.
Try it out with the recording of speech or a song.


"""


import numpy
import scipy.io.wavfile

def main():
    inputname = input("Input file: ")

    contents = scipy.io.wavfile.read(inputname)
    samplerate = contents[0]
    data = contents[1].tolist()  # Now it's a Python list
    seconds = 5
    outputdata = reverse(data)
    outputname = inputname.replace(".wav", ".reverse.wav") #replace input name with this
    scipy.io.wavfile.write(outputname, samplerate,
                           numpy.asarray(outputdata, dtype="int16"))

"""In this function we reversed the data by calling the data to this function than
"""
def reverse(data):
    result = [] #empty array to put the reversed data here
    for i in range(0, len(data)): #loops through data
        result = data[::-1] #this reverses the data and puts it in result

    return result #returns result back to main fxn


# Start the program.
main()