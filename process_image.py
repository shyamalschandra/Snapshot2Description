import sys
import ollama

def describe_image(image_path):
    # Use the ollama.chat function to interact with the model
    response = ollama.chat(
        model='llama3.2-vision',
        messages=[{
            'role': 'user',
            'content': 'What is in this image?',
            'images': [image_path]
        }]
    )

    # Output the description
    print("Image Description:", response['message']['content'])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 process_image.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    describe_image(image_path) 