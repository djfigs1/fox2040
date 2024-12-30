from core.application import Application
from core.navigator import Navigator
from widgets.gradient import Gradient

navigator = Navigator()
navigator.add_page(Gradient())

app = Application(navigator)

app.run()
