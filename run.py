from app import create_app

app = create_app()
# deebug start
app.config.from_object('config')

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=app.config['DEBUG'])
