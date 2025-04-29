

import openai

# Set your API key
api_key = "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"  # your real key

# Create OpenAI client
client = openai.OpenAI(api_key=api_key)

# Function to simplify a clinical note
def simplify_clinical_note(note):
    prompt = (
        "You are a healthcare assistant. Your job is to simplify complex doctor notes "
        "so that patients can easily understand them. Use simple, clear language without medical jargon.\n\n"
        f"Doctor's Note:\n{note}\n\nSimplified Patient-Friendly Note:"
    )

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You simplify doctor notes for patients."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        max_tokens=300,
    )

    simplified_note = response.choices[0].message.content.strip()
    return simplified_note

# Main program
if __name__ == "__main__":
    print("Clinical Note Simplifier using GPT-4")
    print("Type 'exit' to quit.\n")

    while True:
        user_note = input("Enter a clinical note to simplify:\n")
        if user_note.lower() == "exit":
            print("Goodbye!")
            break

        print("\n--- Simplified Patient-Friendly Version ---")
        try:
            simplified = simplify_clinical_note(user_note)
            print(simplified)
        except Exception as e:
            print(f"An error occurred: {e}")
        
        print("\n" + "-"*60 + "\n")
