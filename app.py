from flask import Flask, render_template, jsonify
from openai import OpenAIAPI

# Assuming you have already initialized the OpenAI API key
client = OpenAIAPI(api_key='your_api_key')

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate/<content_type>')
def generate_content(content_type):
    prompt = get_prompt(content_type)
    generated_content = generate_with_openai(prompt)
    return jsonify({'content': generated_content})

def get_prompt(content_type):
    # Define different prompts based on content type
    prompts = {
        'article': 'Write an article on ',
        'music': 'Compose a music piece about ',
        'art': 'Create a visual artwork representing '
    }
    return prompts.get(content_type, 'Invalid content type.')

def generate_with_openai(prompt):
    response = client.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200
    )
    return response['choices'][0]['text']

if __name__ == '__main__':
    app.run(debug=True)
