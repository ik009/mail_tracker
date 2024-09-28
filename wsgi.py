from app import app


if __name__ == "__main__":
    try:
        # port = int(os.environ.get('PORT', 5000))
        # app.run(host='localhost', port=port)
        app.run()
    except:
        # logging.exception('error')
        "error"