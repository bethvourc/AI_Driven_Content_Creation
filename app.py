from flask import Flask, render_template, jsonify
import random

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate/<content_type>')
def generate_content(content_type):
    prompt = get_prompt(content_type)
    generated_content = generate_mock_content(content_type)
    return jsonify({'content': generated_content})

def get_prompt(content_type):
    # Define different prompts based on content type
    prompts = {
        'article': 'Write an article on ',
        'music': 'Compose a music piece about ',
        'art': 'Create a visual artwork representing '
    }
    return prompts.get(content_type, 'Invalid content type.')

def generate_mock_content(content_type):
    # Placeholder content generation
    if content_type == 'article':
        return "This is a sample article content."
    elif content_type == 'music':
        return "This is a sample music piece."
    elif content_type == 'art':
        return "This is a sample visual artwork."
    else:
        return "Invalid content type."

if __name__ == '__main__':
    app.run(debug=True)
