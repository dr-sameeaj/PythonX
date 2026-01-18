# Day 18: Regular Expressions - NLP Text Cleaning
# Using the 're' module to sanitize raw text data for AI models.

import re

# 1. Raw "Dirty" Data (Simulating a scraped tweet or comment)
raw_text = "Check out my AI project!!! Visit https://github.com/dr-sameeaj #Python #AI @2026"

# 2. CLEANING TASK: Remove URLs
# Logic: Look for http/https followed by non-whitespace characters
no_url = re.sub(r'https?://\S+', '[URL]', raw_text)

# 3. CLEANING TASK: Remove Special Characters & Numbers
# Logic: Keep only letters and spaces
clean_text = re.sub(r'[^a-zA-Z\s]', '', no_url)

# 4. EXTRACTION TASK: Find all Hashtags
hashtags = re.findall(r'#\w+', raw_text)

print(f"Original: {raw_text}")
print(f"Cleaned for NLP: {clean_text.strip()}")
print(f"Extracted Features (Hashtags): {hashtags}")