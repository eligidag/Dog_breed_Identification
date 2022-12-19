def test_read_fasta():
    data = read_fasta("test_data/simple.fasta")
    assert len(data) == 2, f"Expected 2 sequences, got {len(data)}"
    assert ">sequence1" in data, "Expected key '>sequence1' not found in data"
    assert data[">sequence1"] == "ATGCATGC", f"Unexpected sequence for key '>sequence1': {data['>sequence1']}"
    assert ">sequence2" in data, "Expected key '>sequence2' not found in data"
    assert data[">sequence2"] == "GCATGCAT", f"Unexpected sequence for key '>sequence2': {data['>sequence2']}"


    data = read_fasta("test_data/empty.fasta")
    assert len(data) == 0, f"Expected 0 sequences, got {len(data)}"