from src.parser import read_fasta
from src.analysis import generate_report
from src.analysis import (
    gc_content,
    reverse_complement,
    transcribe_dna_to_rna,
    translate_dna,
    find_orfs,
    kmer_frequency
)


def analyze_sequence(seq_data):
    sequence = seq_data["sequence"]

    gc = gc_content(sequence)
    rev = reverse_complement(sequence)
    rna = transcribe_dna_to_rna(sequence)
    protein = translate_dna(sequence)
    orfs = find_orfs(sequence)
    kmers = kmer_frequency(sequence, 3)

    report = generate_report(seq_data, gc, rev, rna, protein, orfs, kmers)

    print(report)

    # SAVE REPORT TO FILE
    filename = f"{seq_data['id']}_report.txt"

    with open(filename, "w") as f:
        f.write(report)

    print(f"\n Report saved: {filename}\n")


def main():
    file_path = "data/sample.fasta"
    data = read_fasta(file_path)

    for seq in data:
        analyze_sequence(seq)


if __name__ == "__main__":
    main()