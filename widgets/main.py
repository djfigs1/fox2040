from core.application import Application
from core.navigator import Navigator
from widgets.gradient import Gradient
from widgets.social_battery import SocialBattery

navigator = Navigator()
navigator.add_page(SocialBattery())
navigator.add_page(Gradient())

app = Application(navigator)

app.run()
