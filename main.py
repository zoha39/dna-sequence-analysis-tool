import sys
from src.parser import read_fasta
from src.analysis import (
    gc_content,
    reverse_complement,
    transcribe_dna_to_rna,
    translate_dna,
    find_orfs,
    kmer_frequency,
    generate_report
)


def analyze(file_path):
    data = read_fasta(file_path)

    for seq in data:
        sequence = seq["sequence"]

        gc = gc_content(sequence)
        rev = reverse_complement(sequence)
        rna = transcribe_dna_to_rna(sequence)
        protein = translate_dna(sequence)
        orfs = find_orfs(sequence)
        kmers = kmer_frequency(sequence, 3)

        report = generate_report(seq, gc, rev, rna, protein, orfs, kmers)

        print(report)

        filename = f"{seq['id']}_report.txt"
        with open(filename, "w") as f:
            f.write(report)

        print(f"\nSaved: {filename}\n")


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python main.py <fasta_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    analyze(file_path)