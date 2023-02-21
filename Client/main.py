"""Модуль запуска приложения"""


from App import App
from Console_View import Console_View
from MVP.Presenter import Presenter

view = Console_View()
presenter = Presenter(view)
app = App(presenter, view)
app.start()