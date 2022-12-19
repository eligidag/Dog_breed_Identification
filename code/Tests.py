def test_read_fasta():
    data = read_fasta("sample.fa")
    assert data.keys() == [">Sample seq 1", ">Sample seq 2",">Sample seq 3",">Sample seq 4"]
    assert data[">Sample seq 1"] == "ATGCTAGAGAAAAAAA"
test_read_fasta()


def test_find_most_similar():
    target_seq_dict = {'Mystery':"ATGCATGCATGCATGC"}