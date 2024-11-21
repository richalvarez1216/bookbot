def main():
    # Open the file and read its contents
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    # Count the number of words in the file
    num_words = count_words(file_contents)
    # Count the frequency of each character in the file
    frequency = count_character_frequency(file_contents)
    # Print the report with the word count and character frequencies
    print_report(num_words, frequency)


def count_words(text):
    # Split the text into words and return the number of words
    words = text.split()
    return len(words)


def count_character_frequency(text):
    # Convert text to lowercase to avoid duplicates
    text = text.lower()
    frequency = {}
    # Count the frequency of each character
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency


def print_report(num_words, frequency):
    # Print the header of the report
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
   
    # Sort the frequency dictionary by count in descending order
    sorted_frequency = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
    # Print the frequency of each alphabetic character
    for char, count in sorted_frequency:
        if char.isalpha():  # Only print alphabetic characters
            print(f"The '{char}' character was found {count} times")
    # Print the footer of the report
    print("--- End report ---\n")


main()