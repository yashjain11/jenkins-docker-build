import unittest

from gamestore.app import *


class GamestoreTest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'gamestore.db')

        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_crud_game(self):
        b1 = Game(title="Game #1")
        b2 = Game(title="Game #2")
        b3 = Game(title="Game #3")

        db.session.add(b1)
        db.session.add(b2)
        db.session.add(b3)
        db.session.commit()

        all_games = Game.query.all()
        self.assertEqual(len(set(all_games).intersection({b1, b2, b3})) == 3, True)

        b1.title = "Updated Game #1"
        db.session.commit()

        self.assertEqual(b1.title, "Updated Game #1")

        db.session.delete(b1)
        db.session.delete(b2)
        db.session.delete(b3)
        db.session.commit()

        all_books = Game.query.all()
        self.assertEqual(len(set(all_books).intersection({b1, b2, b3})) == 0, True)


if __name__ == '__main__':
    unittest.main()
