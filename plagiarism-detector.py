#!/usr/bin/env python3

import string
import os

# TEXT PROCESSING FUNCTION
def clean_text(file_path):
    """Read text, lowercase, remove punctuation, and filter stop words."""
    stop_words = {'a','an','the','are','on','of','in','and','at','for','by','to'}
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read().lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        return [w for w in text.split() if w not in stop_words]
    except FileNotFoundError:
        print(f"File unavailable: {file_path}")
        return []

def load_essays(files):
    """Load and clean both essays."""
    words = []
    for file in files:
        words.append(clean_text(file))
    return words

# WORD SEARCHER FUNCTION
def word_search(word, words1, words2):
    count1 = words1.count(word)
    count2 = words2.count(word)
    print(f"\n'{word}' appears {count1} times in essay1 and {count2} times in essay2.\n")

# SIMILAR WORDS REPORT
def common_words(words1, words2):
    common = set(words1) & set(words2)
    print(f"Common words ({len(common)}):")
    print(", ".join(sorted(common)) if common else "None found.")
    return common

# SIMILARITY CALCULATOR
def jaccard_similarity(words1, words2):
    set1, set2 = set(words1), set(words2)
    inter = set1 & set2
    union = set1 | set2
    return (len(inter) / len(union)) * 100 if union else 0

def save_report(plagiarism_percent, common):
    os.makedirs("reports", exist_ok=True)
    report_path = "reports/similarity_report.txt"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(f"Similarity: {plagiarism_percent:.2f}%\n")
        f.write("Common words:\n")
        f.write(", ".join(sorted(common)))
    print(f"Report saved to {report_path}")

# MAIN PROGRAM FLOW
def main():
    essay_files = ["essays/essay1.txt", "essays/essay2.txt"]
    words1, words2 = load_essays(essay_files)

    if not words1 or not words2:
        print("There is no  essay files that was submitted.")
        return

    print("\n Essays processed successfully.\n")

    # Step 1: Ask user for a word to search
    word = input("Enter a word to search for: ").lower()
    word_search(word, words1, words2)

    # Step 2: Find and print common words
    common = common_words(words1, words2)

    # Step 3: Calculate similarity
    plagiarism_percent = jaccard_similarity(words1, words2)
    print(f"\nPlagiarism similarity: {plagiarism_percent:.2f}%")

    if plagiarism_percent >= 50:
        print("High similarity rate  detected (possible plagiarism).")
    else:
        print("Acceptable similarity level detected.")

    # Step 4: Ask if user wants to save the report
    choice = input("\nSave similarity report? (y/n): ").lower()
    if choice == 'y':
        save_report(plagiarism_percent, common)

if __name__ == "__main__":
    main()

