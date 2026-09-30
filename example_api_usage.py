import os
from openai import OpenAI

def main():
    # Initialize the client pointing to Atria's base URL
    api_key = os.environ.get("ATRIA_API_KEY", "YOUR_ATRIA_API_KEY")

    client = OpenAI(
        api_key=api_key,
        base_url="https://api.atria-asi.ai/v1"
    )

    try:
        print("Sending request to Atria-Dawn-Preview...")
        response = client.chat.completions.create(
            model="Atria-Dawn-Preview",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello, how can you help me today?"}
            ]
        )
        print("Response:")
        print(response.choices[0].message.content)
    except Exception as e:
        print(f"Error (expected if dummy API key): {e}")

if __name__ == "__main__":
    main()
