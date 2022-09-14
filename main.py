from website import create_app
import os

app = create_app()

# Only execute if we run this file 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
