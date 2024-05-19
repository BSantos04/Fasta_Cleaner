import argparse

def fasta_cleaner(input_file, output_file):
    """
    Takes to inputs: the input file and the output file.
    While the first one is read, the output is generated and the cleaned sequences are written in the file.
    If the sequence contain any missing value (N,-), it is removed and printed in the new file.
    """
    with open(input_file, "r") as infasta:
        with open(output_file, "w") as outfasta:
            for seq in infasta:
                if seq.startswith(">"):
                    outfasta.write(seq)
                else:
                    outfasta.write(seq.strip().replace("N","") + "\n")
def parse_args():
    """
    We need to parse the command line arguments to prevent any future misuse from the user.
    
    For that, we use the method argparse.ArgumentParser() to contain the argument specifications. 
    
    After that, we need to specify the arguments we want to attach to the parser.
    
    In that case, we want to attach the input file and the output file.
    
    If there is a missing argument, the terminal will display a message with the required missing argument(s) and exit the program.
    
    If there is any extra argument, the terminal will display the unrecognized arguments and close the program.
    
    Returns the input file and the output file arguments from the command line using argparse.Namespace.
    """
    parser=argparse.ArgumentParser()  
    parser.add_argument("input_file", help="\nInput file missing (format: fasta).")
    parser.add_argument("output_file", help="\nOutput_file missing (format: fasta).") 
    return parser.parse_args().input_file, parser.parse_args().output_file
    

if __name__=="__main__":
    #We are just ensuring the code is only executed when the script is run as a standalone program.
    input_file, output_file = parse_args()
    fasta_cleaner(input_file, output_file)
                
        