try:
    from website import create_app
except:
    import os
    os.system('pip install -r requirements.txt')
    from website import create_app #a

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
