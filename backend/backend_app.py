from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]


@app.route('/api/posts', methods=['GET', 'POST'])
def get_posts():
    if request.method == 'GET':
        return jsonify(POSTS)

    elif request.method == 'POST':
        data = request.json
        if not data.get('title') or not data.get('content'):
            return jsonify({"Error": "No title or content"}), 400

        new_id = max(post['id'] for post in POSTS) + 1
        new_post = {
            "id": new_id,
            "title": data['title'],
            "content": data['content']
        }
        POSTS.append(new_post)
        return jsonify(new_post), 201


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
