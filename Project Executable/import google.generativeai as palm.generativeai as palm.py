import google.generativeai as palm

# Configure the API with your API key
palm.configure(api_key='AIzaSyBMEbC7L6Y-NVyJeWQfTX_K665jgi1Tj90')

# List available models and print them
models = palm.list_models()
for model in models:
    print(model)