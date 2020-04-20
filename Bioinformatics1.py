
# A Rapid Introduction to Molecular Biology
str = "TTGACTGCGTAAATCGAGAACACTCATGTGACTCCCGCTTGTCGCGAGTATGATCCGCGGCGGCAGAAGTAATACTGTTGCCCGTAACTCGTGTATTCATCATATGGCCAGAGATACATGCCGAACCGTAACTCGTCCAACGTCCTCGGCCCTTATAGATAGACTTCTAGTATGCTGAAGCCCTACTGGGCAATTTTTCGTGAAAAGTAATTCGTAGGCACCATGGATGGTACGTGTCGCCTTCGCAGTCGGAGGCCAACGACTTGAATGGAAACTACAGTAGGAGCCACGGTATCAGTTAGACTGGGCATAATGATGAGTAACCTTTATTTATCGACGCATGCGTCTTAGAGGTCCAACTGGGAGTCAACCCGTCGAAGGGTGCTCAAGTCGTCACAGTAGTGTACTGCTCCCATAGTTTTCTGAACACTGCAGCAATTGCAAAATGGTATTCGTCGCGTAACCAGCCGGCTGTGTTGGAATGATAGGTGAACCAAGGGCTGAGAGCACCTCGTGCTCAAAGGACATCTGCACCGGATTTTAGCCTGAGGCGGACGTATGTTGTTATCTACCGGTATAAAGCGGTGTTCGGCTAAGTCTGCAAGCTATTTTCCTTACGAGTACACCCTAAGCACTGGGGATAGGCATTGCGCATATGTGCGATTTTCGAACCCATGTCATAGACACAACCTTGCGGTCACCGTGGTTTCCTTCGGCAGGTGTGGCATCAGTGGGCCTTAGTGAGACGTTTGATACGAGGCCTGCGCAGTGTAATGTCACTTAGAGCACTCAACTTGCATTCACGATGGAACAGAGAACTGGCGGATTCCGGTCTTCTGCTAGACGGCCCACCCCGTGTTTGCATTTCGGGGTGAAGAGAGTATCTCACGTGCTTAGAAGTTGAGCGCGTGTAAGGAGACACTCCGTAT"
obj = {}
for char in str:
    if char in obj:
        obj[char] += 1
    else:
        obj[char] = 1
# print(obj['A'], ' ', obj['C'], ' ', obj['G'], ' ', obj['T'])


# Transcribing DNA into RNA
dna_1 = "TTTAAGTGCAGGCGTCAAATGGGATCGTTTATAACACGGATCCCGTTCCCGAACTCGGCCCAGTGCGTGGATGGTATAGCTAGTTCTTTCGTAACGTTACTACCCCTGCCGTTTGTAGCGATACAACCCTCCTTAAATCGGATTATTAGCAACCTAAAGGAGCCATTTGGGCTTTAAGCGCAATAGTCTCCGGTTGATACCGGGATAACGTTTCGGCCCGGTTAATAATTAGGCCCATACAAATGAGCGAATAGACAAGGATTATCCTCGGGGGGACTATGGCAAACACTAAGCCGTTGACCTGTTAACTTGTAATAAGGGCACACGCAGGATCTAGTCAAACGACTGAGTGCACTACGCGTCCTAGGCTGTGCGAAATTTCCCCCATTGCTCGTCATTGTTGCCCTCCCAACGACTTTTTAAAAATGTGCGAGGTAGTGTAGCAGAATGGATCTTCAACTGTTTAAGCGAGATTCCCCTAAGGGTGTCCCGATACCCCAGTTTTGATATAAGCCAGCCGCGTAGCAAACTGTGGAATCTATTTAAAGAACCATGCCCCTGGCGTTTGACTAGTCGACAGAGGATTTGAGGCCTGCGCATGAGTGCACTGTACGCTATCTATACGATAAATGTGCAGGATTCTACCTCAAGCACCGTTGGACCAAGCTAATTGAAGTCGCAGCTGACAGACAGATAACCGCCAAAGCCTAGCCTATACTAACCGCTATACGTTTTCACCATTAGTCTAACAATTAACTTGGAGAATCTTCGACACGATGAACGACCGCCGTAACAACGTGTAAATCACAGTCTGTCCAGTCACGCATTGTTCTGGATGATCGGCGGTCAATTCAATAGACAGCCAAGACTGTACGCTGCGTTCCGAATCATCTGTACCTCGTTACCCAAAGGATGACCTCCCAGCAATT"
rna_1 = ""
for char in dna_1: 
    if char == 'T':
        rna_1 = rna_1 + 'U'
    else: 
        rna_1 = rna_1 + char 
# print(rna_1)


# Complementing a Strand of DNA
dna_s = "CTTGACTCCTCTTGTCGGGACGACATTTCAGGCACATTTCTATTAACGGCAGTGGTCCGAAAACATCGAGCTACGCTATTTTTTCGCATAGAGTTCCCCCTTATCTCTTTAACGCCACGGAGTATCCTAGCGGAAGTCTGCATCGGCCATATGGTGACACGGTGACGGCCTACAACACTCGGGAAGTCCCGCCATACAAATCACTGTCTGTCATTCCGACCTGCCAATGCATGCCATTACAGGGCCTTATACACAGTGCCATCCGAGTACGACGTCTCATCTGAGAGCAACTTCAATTACGTGAAAAGATTGCCGGGTGCAGGACACAGCCAGGTTTAACTGCGTTTACCAGCCTGAAGAAGCTCGATTCTGGTTCTACCAGGCCCGCAAACCCCCTTCCGTCGGGAGTCATACCATAGAGACTGCCTCCATAAACCAGGGACTGGTGTCAGTGGGGGGTGGGTATTGCATTCCCGAAAAACTGCCTATGCAAGCACTGTCCATAGCTAATTAAGCCTTGGTACGAGTTCCCGGTTTAAAGGTCATCAACTAGCTTACTAGGGGGACCAGAGCTCTTCTCTGGGCTTGCTGTGAGGCCTTCTTCTCAGAAGGGTAGAAAGGCGGGGACGAGCTTCCTCAAATTCTCCATTCACCGTTGTTTGAGTTCCAATCGGTTTCCGGCTCGTGTCCTCAAGGATTGCTCTAACGAACTAGCTTACCGACTGGGATCGACCTTTCCTACAGACCTCCGTCGGTGGCGTAGCACTAAGGATGATCCGAGAGCGTTTTTATATAGCTGGAGTTCCGAAAGAAGTCTAGCCGGTCATTACAAAAACAGACGTCTAGAATATCCAGCGTACGCAGCAAGCCATGCGATCGTATTCCGTTTCGACGCTGGACCTCGTACCAGGCGCAGTAGATCATATACGAAGTCTAGTTTCCATGCGCCTTCGGGAAGCCACT"
dna_s_c = ""
dna_s_revers = dna_s[::-1]
obj_1 = {
    "A": "T", 
    "C": "G",
    "G": "C", 
    "T": "A"
}
for char in dna_s_revers:
    dna_s_c += obj_1[char]
print(dna_s_c)
