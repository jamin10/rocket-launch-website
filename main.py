from website import create_app

app = create_app()

# Only execute if we run this file 
if __name__ == '__main__':
    app.run(debug=True)