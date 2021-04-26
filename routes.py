from resources.user import UserRegister, User
from resources.item import Item, ItemList
from resources.store import Store, StoreList

ROUTES = [
    {'resource': Item, 'endpoint': '/item/<string:name>'},
    {'resource': Store, 'endpoint': '/store/<string:name>'},
    {'resource': ItemList, 'endpoint': '/items'},
    {'resource': StoreList, 'endpoint': '/stores'},
    {'resource': UserRegister, 'endpoint': '/register'},
    {'resource': User, 'endpoint': '/user<int:user_id'},
]
