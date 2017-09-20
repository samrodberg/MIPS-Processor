#By Sam Rodberg
import sys

from hf import *

opcodeDict = {'add':'00000', 'addi': '10000', 'and': '00001', 'or': '00010', 'sub': '00011', 'lw': '10100', 'sw': '11000', 'neg': '00011', 'mov': '00001'}

def ConvertAssemblyToMachineCode(inline):
    '''given a string corresponding to a line of assembly,
    strip out all the comments, parse it, and convert it into
    a string of binary values'''

    outstring = ''

    if inline.find('#') != -1:
        inline = inline[0:inline.find('#')] #get rid of anything after a comment
    if inline != '':
        words = inline.split() #assuming syntax words are separated by space, not comma
        operation = words[0]
        operands = words[1:]
        outstring += opcodeDict[operation]
        count = 0
        print words
        while count < len(operands):
            if operation == 'lw':
                outstring += int2bs(operands[0][1:],3)
                if operands[1][0] == '-':
                    outstring += int2bs(operands[1][4],3)
                    outstring += int2bs(operands[1][1],3)
                else: 
                    outstring += int2bs(operands[1][3],3)
                    outstring += int2bs(operands[1][0],3)
                count = len(operands)
            elif operation == 'sw':
                if operands[1][0] == '-':
                    outstring += int2bs(operands[1][4],3)
                    outstring += int2bs(operands[0][1:],3)
                    outstring += int2bs(operands[1][1],3)
                else:
                    outstring += int2bs(operands[1][3],3)
                    outstring += int2bs(operands[0][1:],3)
                    outstring += int2bs(operands[1][0],3)
                count = len(operands)
	    elif operation == 'neg':
		outstring += int2bs(operands[0][1],3)
		outstring += '000'
		outstring += int2bs(operands[1][1],3)
		count = len(operands)
	    elif operation == 'mov':
		outstring += int2bs(operands[0][1],3)
		outstring += int2bs(operands[1][1],3)
		outstring += '000'
		count = len(operands)
            else:
                if operands[count][0] == '$':
                    outstring += int2bs(operands[count][1:],3)
                else:
                    outstring += int2bs(negative(operands[count]),3)
            count += 1
    return outstring


def AssemblyToHex(infilename,outfilename):
    '''given an ascii assembly file , read it in line by line and convert each line of assembly to machine code
    then save that machinecode to an outputfile'''
    outlines = []
    with open(infilename) as f:
        lines = [line.rstrip() for line in f.readlines()]  #get rid of \n whitespace at end of line
        for curline in lines:
            outstring = ConvertAssemblyToMachineCode(curline)
            if outstring != '':
                outstring_hex = bs2hex(outstring)
                outlines.append(outstring_hex)

    f.close()

    with open(outfilename,'w') as of:
        of.write("v2.0 raw\n")
        for outline in outlines:
            of.write(outline)
            of.write("\n")
    of.close()

def negative(num_string):
    if num_string[0] == '-':
        output = num_string[0] + num_string[1]
    else:
        output = num_string[0]
    return output

if __name__ == "__main__":
    print 'Number of arguments:', len(sys.argv), 'arguments.'
    print 'Argument List:', str(sys.argv)

    if (len(sys.argv) != 3):
        print('usage: python rodberg-assembler_final.py inputfile.asm outputfile.hex')
        exit(0)
    inputfile = sys.argv[1]
    outputfile = sys.argv[2]
    AssemblyToHex(inputfile,outputfile)
