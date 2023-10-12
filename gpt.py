import openai
import os
import csv

def set_openai_api_key():
    # You can set the API key here or via environment variable OPENAI_API_KEY
    openai.api_key = os.getenv("OPENAI_API_KEY", "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")

def promptGPT(prompt):
    set_openai_api_key()
    
    # Create a chatbot using ChatCompletion.create() function
    completion = openai.ChatCompletion.create(
        # Use GPT-3.5 as the LLM
        model="gpt-3.5-turbo",
        # Pre-define conversation messages for the possible roles
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    
    # Print the returned output from the LLM model
    print(completion.choices[0].message)

def GPT():
    set_openai_api_key()
    
    # Specify file path for csv reading
    csv_file_path = 'property_insights_extended.csv'

    # Open the CSV file
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        second_row = next(csv_reader)
        print(second_row)

    # Define the user prompt message
    string = ', '.join(second_row)
    prompt = "Make a sentence: " + string
    print("Prompt sent to GPT: \"" + prompt + "\"")

    # Create a chatbot using ChatCompletion.create() function
    completion = openai.ChatCompletion.create(
        # Use GPT-3.5 as the LLM
        model="gpt-3.5-turbo",
        # Pre-define conversation messages for the possible roles
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    insights = [choice.message for choice in completion.choices]

    return insights
