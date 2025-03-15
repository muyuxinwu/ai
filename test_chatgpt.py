import openai

def test_chatgpt():
    # Initialize OpenAI API
    openai.api_key = "your-api-key"
    
    # Test ChatGPT completion
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": "Hello, how are you?"}
        ]
    )
    
    # Print response
    print(response['choices'][0]['message']['content'])

if __name__ == "__main__":
    test_chatgpt()
