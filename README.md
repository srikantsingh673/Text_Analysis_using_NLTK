# Text Analysis using NLTK

This project performs text analysis on web content using various Python libraries including NLTK, TextBlob, and textstat. The analysis aims to understand and extract useful information from the text data, identify common trends, and address data quality issues.

## Project Overview

The script performs the following tasks:
- **Web Scraping**: Retrieves text content from a specified webpage.
- **Sentiment Analysis**: Calculates sentiment scores using VADER and TextBlob.
- **Text Statistics**: Computes various text statistics including average sentence length, percentage of complex words, and readability indices.
- **Text Features**: Analyzes the frequency of personal pronouns, nouns, adjectives, adverbs, and symbols.

## Key Features

1. **Sentiment Analysis**:
   - Uses VADER to calculate negative, neutral, and positive sentiment scores.
   - Uses TextBlob to determine polarity and subjectivity.

2. **Text Statistics**:
   - Calculates average sentence length.
   - Computes the percentage of complex words.
   - Measures readability using the Automated Readability Index (ARI).
   - Calculates the average number of syllables per word.

3. **Text Features Analysis**:
   - Counts occurrences of personal pronouns, nouns, adjectives, adverbs, and symbols.

## Requirements

Ensure you have the following Python libraries installed:

- `textstat`
- `nltk`
- `beautifulsoup4`
- `requests`
- `textblob`

You can install the required libraries using pip:

```bash
pip install textstat nltk beautifulsoup4 requests textblob
