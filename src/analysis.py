def gc_content(sequence):
    """Calculate GC content percentage"""
    g = sequence.upper().count("G")
    c = sequence.upper().count("C")
    return ((g + c) / len(sequence)) * 100


def reverse_complement(sequence):
    """Return reverse complement of DNA"""
    complement = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }

    return "".join(complement[base] for base in reversed(sequence.upper()))


def transcribe_dna_to_rna(sequence):
    """Convert DNA to RNA"""
    return sequence.upper().replace("T", "U")



# Standard Genetic Code Table
codon_table = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'Stop', 'TAG':'Stop',
    'TGC':'C', 'TGT':'C', 'TGA':'Stop', 'TGG':'W'
}


def translate_dna(sequence):
    """Translate DNA sequence into protein sequence"""

    sequence = sequence.upper()
    protein = []

    # read codons (3 bases at a time)
    for i in range(0, len(sequence) - 2, 3):
        codon = sequence[i:i+3]

        if codon in codon_table:
            amino_acid = codon_table[codon]

            if amino_acid == "Stop":
                break

            protein.append(amino_acid)

    return "".join(protein)



#adding ORF function

def find_orfs(sequence):
    """
    Find Open Reading Frames (ORFs) in a DNA sequence
    """
    sequence = sequence.upper()
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]

    orfs = []

    for i in range(len(sequence)):
        codon = sequence[i:i+3]

        if codon == start_codon:
            # start scanning from here
            for j in range(i, len(sequence), 3):
                current_codon = sequence[j:j+3]

                if current_codon in stop_codons:
                    orf = sequence[i:j+3]
                    orfs.append(orf)
                    break

    return orfs


#adding k-mer function
from collections import defaultdict

def kmer_frequency(sequence, k=3):
    """
    Calculate frequency of k-mers in DNA sequence
    """
    sequence = sequence.upper()
    freq = defaultdict(int)

    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i+k]
        freq[kmer] += 1

    return dict(freq)


#creating rerport funciton
def generate_report(seq_data, gc, rev_comp, rna, protein, orfs, kmers):
    """
    Create a formatted bioinformatics report
    """

    report = []
    report.append("===== DNA SEQUENCE ANALYSIS REPORT =====\n")

    report.append(f"Sequence ID: {seq_data['id']}")
    report.append(f"Sequence: {seq_data['sequence']}\n")

    report.append(f"GC Content: {gc:.2f}%")
    report.append(f"Reverse Complement: {rev_comp}")
    report.append(f"RNA: {rna}")
    report.append(f"Protein: {protein}\n")

    report.append(f"ORFs Found: {len(orfs)}")
    for i, orf in enumerate(orfs):
        report.append(f" ORF {i+1}: {orf}")

    report.append("\nK-mer Frequencies:")
    for kmer, count in kmers.items():
        report.append(f" {kmer}: {count}")

    return "\n".join(report)