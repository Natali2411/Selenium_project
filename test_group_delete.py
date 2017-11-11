import random

def test_delete_group(app):
    app.login(username="admin", password="secret")
    app.delete_group_by_number(random.randrange(app.count_groups()))
    app.logout()