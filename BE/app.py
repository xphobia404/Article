from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/article'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    created_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_date = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    status = db.Column(db.String(50), nullable=False)

@app.route('/article', methods=['POST'])
def submit():
    try:
        payload = request.get_json()
        required_fields = ["title", "content", "category", "status"]
        
        if not all(field in payload for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400
        
        if len(payload["title"]) < 20:
            return jsonify({"error": "Title must be at least 20 characters"}), 400
        if len(payload["content"]) < 200:
            return jsonify({"error": "Content must be at least 200 characters"}), 400
        if len(payload["category"]) < 3:
            return jsonify({"error": "Category must be at least 3 characters"}), 400
        if payload["status"] not in ["publish", "draft", "trash"]:
            return jsonify({"error": "Status must be either 'publish', 'draft', or 'trash'"}), 400
        
        new_entry = Posts(
            title=payload["title"],
            content=payload["content"],
            category=payload["category"],
            status=payload["status"]
        )
        db.session.add(new_entry)
        db.session.commit()
        
        return jsonify({"message": "Data successfully received", "data": payload}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/article/', methods=['GET'])
def get_data():
    try:
        limit = request.args.get('limit', default=10, type=int)
        offset = request.args.get('offset', default=0, type=int)
        
        entries = Posts.query.limit(limit).offset(offset).all()
        result = [{
            "id": e.id, 
            "title": e.title, 
            "content": e.content, 
            "category": e.category, 
            "created_date": e.created_date,
            "updated_date": e.updated_date,
            "status": e.status
        } for e in entries]
        
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/article/<int:id>', methods=['GET'])
def get_article(id):
    article = Posts.query.get(id)
    if article:
        return jsonify({
            "id": article.id,
            "title": article.title,
            "content": article.content,
            "category": article.category,
            "created_date": article.created_date,
            "updated_date": article.updated_date,
            "status": article.status
        }), 200
    return jsonify({"error": "Article not found"}), 404

@app.route('/article/update', methods=['POST'])
def update_article():
    try:
        payload = request.get_json()
        article_id = payload.get("id")
        
        article = Posts.query.get(article_id)
        if not article:
            return jsonify({"error": "Article not found"}), 404
        
        if "title" in payload and len(payload["title"]) < 20:
            return jsonify({"error": "Title must be at least 20 characters"}), 400
        if "content" in payload and len(payload["content"]) < 200:
            return jsonify({"error": "Content must be at least 200 characters"}), 400
        if "category" in payload and len(payload["category"]) < 3:
            return jsonify({"error": "Category must be at least 3 characters"}), 400
        if "status" in payload and payload["status"] not in ["publish", "draft", "trash"]:
            return jsonify({"error": "Status must be either 'publish', 'draft', or 'trash'"}), 400
        
        article.title = payload.get("title", article.title)
        article.content = payload.get("content", article.content)
        article.category = payload.get("category", article.category)
        article.status = payload.get("status", article.status)
        
        db.session.commit()
        
        return jsonify({"message": "Article updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/article/delete', methods=['POST'])
def delete_article():
    try:
        payload = request.get_json()
        article_id = payload.get("id")
        
        article = Posts.query.get(article_id)
        if not article:
            return jsonify({"error": "Article not found"}), 404
        
        db.session.delete(article)
        db.session.commit()
        
        return jsonify({"message": "Article deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)