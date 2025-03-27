import os
import json
import markdown

# Define paths
POSTS_DIR = 'posts'
OUTPUT_DIR = '.'
TEMPLATE_DIR = 'templates'

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load templates
with open(os.path.join(TEMPLATE_DIR, 'post_template.html'), 'r') as f:
    post_template = f.read()

with open(os.path.join(TEMPLATE_DIR, 'index_template.html'), 'r') as f:
    index_template = f.read()

# Load posts information from posts.json
with open('posts.json', 'r') as f:
    posts_data = json.load(f)

# Function to generate HTML for a single post
def generate_post_html(md_content, description, image, filename):
    html_content = markdown.markdown(md_content)
    post_html = post_template.replace('{{ content }}', html_content)
    post_html = post_html.replace('{{ title }}', title)
    post_html = post_html.replace('{{ description }}', description)
    post_html = post_html.replace('{{ image }}', image if image else '')
    post_html = post_html.replace('{{ filename }}', filename)
    return post_html

# Function to generate the index page
def generate_index_html(posts):
    posts_html = ''
    for post in posts:
        post_html = f'''
        
            

                
{post["title"]}

                
{post["description"]}

            

        
        '''
        posts_html += post_html
    return index_template.replace('{{ posts }}', posts_html)

# List to store post metadata
posts = []

# Process each post defined in posts.json
for post in posts_data['posts']:
    filename = post['filename']
    title = post['title']
    description = post['description']
    image = post['image']

    print(f'Processing {filename}...')
    filepath = os.path.join(POSTS_DIR, filename)
    with open(filepath, 'r') as f:
        md_content = f.read()
    
    # Generate HTML for the post
    post_html = generate_post_html(md_content, description, image, filename)
    output_filepath = os.path.join(OUTPUT_DIR, f'{filename[:-3]}.html')
    with open(output_filepath, 'w') as f:
        f.write(post_html)
    
    # Add post metadata tAo the list
    posts.append({'filename': filename, 'title': title, 'description': description, 'image': image})

# Generate the index page
index_html = generate_index_html(posts)
with open(os.path.join(OUTPUT_DIR, 'index.html'), 'w') as f:
    f.write(index_html)

print('Blog generated successfully!')
