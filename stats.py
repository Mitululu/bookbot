from collections import Counter

def get_num_words(text: str):
    return len(text.split())

def count_chars(text: str):
    counts = Counter()
    for ch in text:
        counts[ch.lower()] += 1

    return counts

def char_sort_on(dict: dict):
    return dict["num"]

def char_report(char_counts: dict):
    chars = list(char_counts.keys())
    report = []

    for ch in chars:
        report.append({
            "char": ch, 
            "num": char_counts[ch]
        })

    report.sort(reverse=True, key=char_sort_on)
    return report