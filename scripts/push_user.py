import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from src import db, app
from src.models.entities import User

if len(sys.argv) == 8:
    username = sys.argv[1]
    password = sys.argv[2]
    firstName = sys.argv[3]
    lastName = sys.argv[4]
    number = sys.argv[5]
    email = sys.argv[6]
    flag = sys.argv[7]

    user = User(
        username=username,
        password=password,
        firstName=firstName,
        lastName=lastName,
        number=number,
        email=email,
        flag=flag,
    )

    with app.app_context():
        db.session.add(user)
        db.session.commit()
        db.session.close()
else:
    print(sys.argv)
