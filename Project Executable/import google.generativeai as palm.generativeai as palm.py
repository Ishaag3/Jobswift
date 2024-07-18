import google.generativeai as palm
import creds

# Configure the API with your API key
palm.configure(api_key=creds.API_KEY)

# List available models and print them
models = palm.list_models()
for model in models:
    print(model)