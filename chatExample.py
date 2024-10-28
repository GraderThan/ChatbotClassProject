from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

# Load the tokenizer and model
model_name = "facebook/blenderbot-400M-distill"
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)


print("Chat with the AI model (type 'quit' to stop)")

while True:
    # Get user input
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break

    # Encode user input and add EOS token
    inputs = tokenizer([user_input], return_tensors="pt")

    # Generate BlenderBot's response
    reply_ids = model.generate(**inputs)
    response = tokenizer.decode(reply_ids[0], skip_special_tokens=True)

    # Print the response
    print(f"Bot: {response.strip()}")
