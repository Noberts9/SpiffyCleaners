from app import create_app
from datetime import datetime

app = create_app()  # ✅ First, create the app

@app.context_processor
def inject_year():
    return {'current_year': datetime.now().year}

if __name__ == '__main__':
    app.run(debug=True)
