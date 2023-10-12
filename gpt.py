import openai
import os
import csv

def GPT():
    # Set your OpenAI API key here
    openai.api_key = os.getenv("OPENAI_API_KEY", "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")

    # Specify file path for csv reading
    csv_file_path = 'property_insights_extended.csv'

    # Open the CSV file
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        second_row = next(csv_reader)

    # Define the user prompt message
    string = ', '.join(second_row)
    prompt = "Make a sentence: " + string

    # Create a chatbot using ChatCompletion.create() function
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    insights = [choice.message for choice in completion.choices]

    return insights
