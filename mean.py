""""
DNA to RNA converter
"""
def rna(seq):
    """will convert DNA to RNA sequence""""

    #first detrimen if the sequence is upper case
    seq_upper = seq.isupper()
    #convert to lowercase
    seq = seq.lower()
    #swao out t for u
    seq.replace('t','u')

    #return upper or lower
    if seq_upper:
        return seq.upper()
    else:
        return seq

def reverse_rna_complement(seq):
    """Convert a DNA seq to its revers RNA comp """

    seq_upper = seq.isupper()

    seq = seq[::-1]

    seq = seq.upper()

    #compute complement
    seq = seq.replace('A','u')
    seq = seq.replace('T','a')
    seq = seq.replace('G','c')
    seq = seq.replace('C','g')

     if seq_upper:
        return seq.upper()
    else:
        return seq
