import sqlite3
from database.db import get_db_connection


class UserModel:
    @staticmethod
    def find_by_username(username):
        conn = get_db_connection()
        try:
            return conn.execute(
                'SELECT * FROM users WHERE username = ?',
                (username,)
            ).fetchone()
        finally:
            conn.close()

    @staticmethod
    def find_by_id(user_id):
        conn = get_db_connection()
        try:
            return conn.execute(
                'SELECT id, username FROM users WHERE id = ?',
                (user_id,)
            ).fetchone()
        finally:
            conn.close()

    @staticmethod
    def create_user(username, password):
        conn = get_db_connection()
        try:
            conn.execute(
                'INSERT INTO users (username, password) VALUES (?, ?)',
                (username, password)
            )
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()

    @staticmethod
    def update_user(user_id, username):
        conn = get_db_connection()
        try:
            conn.execute(
                'UPDATE users SET username = ? WHERE id = ?',
                (username, user_id)
            )
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()

    @staticmethod
    def delete_user(user_id):
        conn = get_db_connection()
        try:
            conn.execute('DELETE FROM users WHERE id = ?', (user_id,))
            conn.commit()
            return True
        except sqlite3.Error:
            return False
        finally:
            conn.close()
