from database import Base, engine, SessionLocal

from models.user_game import UserGame
from models.game_publisher import GamePublisher
from models.game_platform import GamePlatform
from models.game_genre import GameGenre

from models.user import User
from models.game import Game
from models.sale import Sale
from models.publisher import Publisher
from models.platform import Platform
from models.genre import Genre




Base.metadata.create_all(engine)

session = SessionLocal()