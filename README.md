#  DNA Sequence Analysis Tool

A modular Python-based bioinformatics tool for DNA sequence analysis.  
This project demonstrates core bioinformatics workflows including sequence parsing, GC content analysis, ORF detection, k-mer analysis, and protein translation.

---

##  Features

- FASTA file parsing
- GC content calculation
- Reverse complement generation
- DNA → RNA transcription
- DNA → Protein translation
- ORF (Open Reading Frame) detection
- K-mer frequency analysis
- Automated report generation
- Command-line interface (CLI)

---

##  Project Structure

dna-sequence-analysis-tool/
│
├── main.py
├── run.py (legacy)
├── data/
│ └── sample.fasta
├── src/
│ ├── parser.py
│ └── analysis.py
├── reports/
├── requirements.txt
└── README.md


---

##  Installation

```bash
git clone https://github.com/your-username/dna-sequence-analysis-tool.git
cd dna-sequence-analysis-tool
pip install -r requirements.txt


##  Usage

Run analysis on a FASTA file:

```bash
python main.py data/sample.fasta

-- Example Output
GC Content %
Reverse Complement
RNA Sequence
Protein Sequence
ORFs Found
K-mer Frequencies
Auto-generated report files

--- Bioinformatics Concepts Used
Molecular biology (DNA → RNA → Protein)
Sequence analysis
Genome feature detection
Pattern frequency analysis
>>>>>>> 35088e7 (Added .gitignore and removed cache files)
