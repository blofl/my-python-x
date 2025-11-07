from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class HelloApp(App):
    def build(self):
        # Create the main layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Create a label
        self.label = Label(
            text='Press the button below!',
            font_size='24sp',
            size_hint=(1, 0.7)
        )
        
        # Create a button
        button = Button(
            text='Click Me!',
            font_size='20sp',
            size_hint=(1, 0.3),
            background_color=(0.2, 0.6, 1, 1)  # Nice blue color
        )
        
        # Bind the button to the callback function
        button.bind(on_press=self.on_button_press)
        
        # Add widgets to the layout
        layout.add_widget(self.label)
        layout.add_widget(button)
        
        return layout
    
    def on_button_press(self, instance):
        # Change the label text when button is pressed
        self.label.text = 'Hello from Kivy!'
        self.label.color = (0, 1, 0, 1)  # Change to green


if __name__ == '__main__':
    HelloApp().run()