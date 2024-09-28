import openai
from config import apikey  # Ensure you have your API key in a config file

# Initialize OpenAI API with your API key
openai.api_key = apikey

def generate_response(prompt):
    try:
        # Make an API call to OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=150,
        )

        # Extract and return the response text
        return response['choices'][0]['message']['content'].strip()

    except openai.error.RateLimitError:
        print("You have exceeded your API quota. Please check your OpenAI account.")
        return "Error: Quota exceeded."
    except openai.error.OpenAIError as e:
        print(f"OpenAI API Error: {e}")
        return "Error: OpenAI API request failed."

if __name__ == "__main__":
    user_input = input("Enter your question: ")
    response = generate_response(user_input)
    print("AI Response:", response)
