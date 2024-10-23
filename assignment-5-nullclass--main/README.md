# Task 5: Create a feature to translate the language with a combination of two languages at the same time . We should be able to convert the 2 different languages at the same time . translate English to French and Hindi at the same time . This model should work only for 10 letter English words . If we enter below 10 letters or above 10 letters it should not work.

## Overview
This task involves translating English sentences to both French and Hindi simultaneously, with the constraint that the English sentence must be exactly ten letters long.

## Model
- The model uses a multi-output architecture to generate translations in both languages.
- Constraints are applied to check sentence length before translation.

## Data
- Data consists of English-French-Hindi translation pairs.
- Sentences are preprocessed and tokenized.

## Files
- `task5.ipynb`: Contains the multi-output translation model.
- `gui.py`: GUI script to interact with the model.

## Setup
1. Clone the repository:
   ```bash
   git clone <repo_url>
   cd <repo_name>