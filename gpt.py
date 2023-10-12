# gpt.py

def promptGPT(prompt):
    import openai
    import os
    
    # Setting the API key
    #openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = "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"
    # Create a chatbot using ChatCompletion.create() function
    completion = openai.ChatCompletion.create(
        # Use GPT 3.5 as the LLM
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
    import csv
    import openai
    import os
    
    # Specify file path for csv reading
    csv_file_path = 'property_insights_extended.csv'

    # Open the CSV file
    # With releases the variable file at the end. This is common in file operations
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        second_row = next(csv_reader)
        print(second_row)

    # Setting the API key
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Define the user prompt message
    string = ''
    for item in second_row:
        string = string + item + ', '
    prompt = "Make a sentence: " + string
    print("Prompt sent to GPT: \"" + prompt + "\"")

    # Create a chatbot using ChatCompletion.create() function
    completion = openai.ChatCompletion.create(
        # Use GPT 3.5 as the LLM
        model="gpt-3.5-turbo",
        # Pre-define conversation messages for the possible roles
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    # Print the returned output from the LLM model
    print(completion.choices[0].message)