import itertools                                   
                                                 
d = {}                                            
l = []
contd = 0;


while (contd == 0):                                 
    i = raw_input("\n----- REVERSE TRANSLATOR -----\n a) Enter 1 to display all possible RNA sequences for a protein sequence in the Window \n 2) Enter 2 to store all possible RNA sequences for a protein sequence in a text file \n\n ")                               #main menu 

    
    if i == "1":
        seq = raw_input("\nEnter the protein sequence to be processed: ")

        for AA in seq:                                
            with open("ct.txt") as fin:               
                for line in fin:                      
                    items = line.split()              
                    p = items[2:]                      
                    if str(AA) == str(items[0]):      
                        l.append(p)                 
                
        posbl = list(itertools.product(*l))         
    
        print ("****** All Possible Sequences ******\n")
        for sequence in posbl:                      
            for codon in sequence:
                print str(codon) + " ",
            print ("\n ")
    d = {}                                             
    l = []
        
    if i == "2":
        with open("Output.txt", "w") as text_file:     
            seq = raw_input("\nEnter the protein sequence to be processed: ")

            for c in seq:
                with open("ct.txt") as fin:
                    for line in fin:
                        items = line.split()
                        p = items[2:]
                        if str(c) == str(items[0]):
                            l.append(p)
                    
            posbl = list(itertools.product(*l))

            text_file.write("****** All Possible Sequences ******\n")
            for sequence in posbl:
                text_file.write("5'- ")
                for codon in sequence:
                    text_file.write( str(codon) + " ",)
                text_file.write("-3' \n" )
            print("\n done. check Output.txt \n")
    d = {}
    l = []            
            
    contd= int(input("Press 0 to continue, Any other key to exit.\n"))      