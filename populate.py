import pandas as pd
from database import SessionLocal
from models.user import User
from models.game import Game
from models.platform import Platform
from models.genre import Genre
from models.publisher import Publisher
from models.sale import Sale
from faker import Faker
import bcrypt
from datetime import date, timedelta
from random import sample, randint

session = SessionLocal()
df = pd.read_csv("vgsales.csv")

# -------------------
# Création des utilisateurs
# -------------------
def generate_users(n=5):
    print("⏳ Importation des utilisateurs...")
    fake = Faker()
    users_list = []

    for _ in range(n):
        pseudo = fake.user_name()
        mail = fake.email()
        password = fake.password()
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        consent = fake.boolean()
        limit_date = date.today() + timedelta(days=365*2)

        user = User(
            pseudo_user=pseudo,
            mail_user=mail,
            password_user=hashed_password,
            consent_user=consent,
            limitdate_user=limit_date
        )
        users_list.append(user)

    session.add_all(users_list)
    session.commit()

    print("✔ Utilisateurs créés :")
    for u in users_list:
        print(f"- {u.pseudo_user} ({u.mail_user})")

# -------------------
# Importation des jeux et relations
# -------------------
def import_games():
    print("\n⏳ Importation des jeux...")
    games_list = []

    # On récupère les listes existantes pour les liaisons
    all_users = session.query(User).all()
    all_platforms = {p.name_platform: p for p in session.query(Platform).all()}
    all_genres = {g.type_genre: g for g in session.query(Genre).all()}
    all_publishers = {p.name_publisher: p for p in session.query(Publisher).all()}

    for _, row in df.iterrows():
        # Vérifie que la plateforme, le genre et l'éditeur existent
        platform_obj = all_platforms.get(row["Platform"])
        genre_obj = all_genres.get(row["Genre"])
        publisher_obj = all_publishers.get(row["Publisher"])

        if not (platform_obj and genre_obj and publisher_obj):
            continue  # Ignore si les objets n'existent pas

        game = Game(
            name_game=row["Name"],
            rank_game=row["Rank"]
        )

        # Liaisons
        game.platforms.append(platform_obj)
        game.genres.append(genre_obj)
        game.publishers.append(publisher_obj)

        # Lier 1 à 3 utilisateurs
        game.users.extend(sample(all_users, k=randint(1, min(3, len(all_users)))))

        # Création de la vente associée
        sale = Sale(
            na_sales=row["NA_Sales"],
            eu_sales=row["EU_Sales"],
            jp_sales=row["JP_Sales"],
            other_sales=row["Other_Sales"],
            global_sales=row["Global_Sales"]
        )
        game.sales.append(sale)

        games_list.append(game)

    session.add_all(games_list)
    session.commit()

    print("✔ Jeux importés (exemples) :")
    for g in games_list[:5]:
        print(f"{g.name_game} ({g.rank_game}) - Joueurs: {[u.pseudo_user for u in g.users]}")

# -------------------
# Lancer tout
# -------------------
if __name__ == "__main__":
    generate_users(5)
    import_games()
    print("\n✅ Base de données remplie avec succès !")