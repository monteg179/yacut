from yacut import app, db


@app.cli.command('clear_db')
def clear_db_command():
    """Очистка базы данных"""
    db.drop_all()
    db.create_all()