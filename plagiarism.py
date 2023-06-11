import difflib

def check_plagiarism(text1, text2):
    # Split the texts into lines
    lines1 = text1.splitlines()
    lines2 = text2.splitlines()

    # Initialize the difflib differ
    differ = difflib.Differ()

    # Compare the lines
    diff = differ.compare(lines1, lines2)

    # Calculate the similarity ratio
    similarity_ratio = difflib.SequenceMatcher(None, lines1, lines2).ratio()

    return diff, similarity_ratio

# Example usage
document1 = """
This is the first document.
It contains some text that we will compare.
"""
document2 = """
This is the second document.
It contains some different text.
"""

# Check plagiarism
diff, similarity_ratio = check_plagiarism(document1, document2)

# Print the diff
print('\n'.join(diff))

# Print the similarity ratio
print(f"Similarity Ratio: {similarity_ratio}")
