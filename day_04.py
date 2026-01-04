# Day 4: Strings - Building an NLP Text Pre-processor
raw_data = "  Building AI models with Python is AMAZING!  "

# 1. Cleaning data (Removing whitespace & lowercase)
clean_data = raw_data.strip().lower()

# 2. Slicing (Extracting specific keywords)
first_word = clean_data[0:8] # "building"

# 3. Formatting (Using f-strings - modern Python)
status_report = f"Keyword: {first_word} | Length: {len(clean_data)} characters"

# 4. Challenge: Reversing a string (A common interview question)
reversed_data = clean_data[::-1]

print(status_report)
print(f"Reversed for logic testing: {reversed_data}")

# Note: Strings are immutable; methods return a new string rather than modifying the original.
