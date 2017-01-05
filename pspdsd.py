#!/usr/bin/env python
#
# This is a python script for computing backbone dihedral angles from protein crystal structures.
#

import sys
import copy
from Protein import *


### Print program usage instructions and exit
def usage():
    print ""
    print "Usage: python pspdsd.py [OPTIONS]"
    print "       python pspdsd.py [-h | --help]"
    print "       python pspdsd.py [-i INPUT | --input INPUT]"
    print ""
    print "pspdsd.py is a script for computing backbone dihedral angles from protein"
    print "crystal structures."
    print ""
    print "OPTIONS:"
    print "  -h, --help    Print this help message and exit"
    print "  -i, --input   Name of protein input file in PDB format"
    print "  -o, --output  Name of output file"
    print ""
    exit()


### Print an error message, tell user how to get help information, and exit
def die(errorMessage):
    print errorMessage
    print "Use \'python " + progName + " --help\' for help info."
    exit()


### Given a file name, read a pdb file, save it as a Protein() object, and return that object.
### This is expecting that every atom starts with 'ATOM', every chain ends in 'TER', and the
### columns are formatted to standard PDB conventions.
def read_protein(inputFilename):
    myProtein = Protein()
    myChain = Chain()
    myResidue = Residue()
    myAtom = Atom()
    lastresid = ''
    
    inputFile = open(inputFilename, 'r')
    for line in inputFile:

        if line.startswith("TER"):
            myResidue.resid = lastresid
            myChain.chainid = line[21]
            myChain.residue.append(copy.deepcopy(myResidue))
            myProtein.chain.append(copy.deepcopy(myChain))

            myResidue.clean()
            myChain.clean()

        elif line.startswith("ATOM"):
            myAtom.atomname = line[12:16]
            myAtom.x = line[30:38]
            myAtom.y = line[38:46]
            myAtom.z = line[46:54]

            thisresname = line[17:20]
            thisresid = line[22:26]

            # if residue is the same as last time, add to residue
            if ( thisresid == lastresid ):
                myResidue.atom.append(copy.deepcopy(myAtom))

            else:
                if ( len(myResidue.atom) > 0 ):
                    myResidue.resid = lastresid
                    myChain.residue.append(copy.deepcopy(myResidue))
                myResidue.clean()
                myResidue.atom.append(copy.deepcopy(myAtom))
                lastresid = thisresid

            myAtom.clean()
        else:
            pass

    inputFile.close()
    myChain.clean()
    myResidue.clean()
    myAtom.clean()

    return myProtein


### Main function
def main():
    global progName
    progName = sys.argv[0]
    sys.argv.pop(0)

    inputFilename = ''
    outputFilename = ''

    if ( len(sys.argv) == 0 ): die ("Error: Missing command line options.")

    # Parse arguments
    while ( len(sys.argv) > 0 ):
        arg = sys.argv.pop(0)

        if ( arg == "-h" or arg == "--help" ):
            usage()

        elif ( arg == "-i" or arg == "--input" ):
            if ( len(sys.argv) >= 1 ):
                inputFilename=sys.argv[0]
                sys.argv.pop(0)
            else:
                die ("Input file not specified on the command line.")

        elif ( arg == "-o" or arg == "--output" ):
            if ( len(sys.argv) >= 1 ):
                outputFilename=sys.argv[0]
                sys.argv.pop(0)
            else:
                die ("Output file not specified on the command line.")

        else:
            die ("Command line option " + arg + " unrecognized.")

    thisProtein = read_protein(inputFilename)

    print "Printing chains: "
    thisProtein.print_chains()
    print ""

    print "Printing residues: "
    thisProtein.print_residues()
    print ""

    print "Printing atoms: "
    thisProtein.print_atoms()
    print ""

    exit()


if __name__ == "__main__":
    main()


