from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from datetime import datetime

start_date = datetime(2025, 1, 26)

class SemkaLoveMaho(App):
    def build(self):
        Window.clearcolor = (1, 0.9, 0.9, 1)

        layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        self.title_label = Label(
            text="♡ наши отношения ♡", 
            font_size=30, 
            bold=True, 
            color=(0.8, 0, 0.5, 1),
            halign='center'
        )
        layout.add_widget(self.title_label)

        self.days_label = Label(
            font_size=22, 
            color=(0.5, 0, 0.5, 1), 
            halign='center', 
            valign='middle'
        )
        layout.add_widget(self.days_label)
        self.update_days()

        update_button = Button(
            text="Обновить", 
            font_size=18, 
            on_press=self.update_days, 
            background_color=(1, 0.5, 0.7, 1),
            size_hint=(None, None),
            size=(200, 60),
            pos_hint={"center_x": 0.5},
            background_normal='',
            background_down='',
            color=(1, 1, 1, 1),
            bold=True
        )
        layout.add_widget(update_button)

        return layout

    def update_days(self, *args):
        today = datetime.today()
        days_together = (today - start_date).days
        self.days_label.text = f"♡ Мы вместе уже {days_together} дней! ♡"

SemkaLoveMaho().run()
