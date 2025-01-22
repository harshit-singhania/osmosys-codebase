def count_letters(text):
    count = sum(1 for char in text if char.isalpha())
    return count

def count_words(text):
    # Split the text by whitespace and filter out empty strings
    words = text.split()
    return len(words)

def count_sentences(text):
    count = sum(1 for char in text if char in '.!?')
    return count

def calculate_index(letters, words, sentences):
    L = (letters / words) * 100
    S = (sentences / words) * 100
    return round(0.0588 * L - 0.296 * S - 15.8)

def main():
    # Get input text from the user
    text = input("Text: ")

    # Count letters, words, and sentences
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    # Calculate the Coleman-Liau index
    index = calculate_index(letters, words, sentences)

    # Print the grade level
    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")

if __name__ == "__main__":
    main()