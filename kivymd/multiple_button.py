from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp

from kivymd.uix.picker import MDTimePicker
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast



KV = '''
MDScreen:

    MDRaisedButton:
        text: "primary_light_mounav"
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        md_bg_color: app.theme_cls.primary_light

    MDRaisedButton:
        text: "primary_color_Sai"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}

    MDRaisedButton:
        text: "primary_dark_Rizwan"
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        md_bg_color: app.theme_cls.primary_dark
    
    MDSwitch:
        widget_style: "android"
        pos_hint: {"center_x": 0.5, "center_y": 0.9}
        opposite_colors: True
        # on_release: app.build()
    
    MDToolbar:
        title: "This is a Tool bar"
        left_action_items: [["dots-vertical"], ["clock"]]
        opposite_colors: False
    
    MDRaisedButton:
        text: "Time Picker"
        pos_hint: {'center_x':0.1, 'center_y':0.2}
        on_release: app.build()
          
    MDRectangleFlatIconButton:
        icon: "instagram"
        font_size: 20
        text: "Kevin Systrom"
        pos_hint: {"center_x": 0.2, "center_y": 0.95}
        theme_text_color: "Custom"
        text_color: 0, 0, 1, 1
        line_color: 1, 0, 1, 1
        theme_icon_color: "Custom"
        icon_color: 1, 0, 0, 1
    
    MDRoundFlatIconButton:
        icon: "snapchat"
        font_size: 25
        text: "M.J.N.V.Sai"
        pos_hint: {"center_x": 0.2, "center_y": 0.85}
        theme_text_color: "Custom"
        text_color: 0, 0, 1, 1
        line_color: 1, 0, 1, 1
        theme_icon_color: "Custom"
        icon_color: 1, 0, 0, 1
    
    MDLabel:
        text: "208W1A1291"
        pos_hint: {"center_x": 1.3, "center_y": 0.8}
        theme_text_color: "Custom"
        text_color: 0,0,1,1
        opposite_colors: False
    
    MDLabel:
        text: "208W1A12A0"
        pos_hint: {"center_x": 1.3, "center_y": 0.7}
        theme_text_color: "Custom"
        text_color: 1,0,0,1
        opposite_colors: False
    
    MDLabel:
        text: "208W1A12A1"
        pos_hint: {"center_x": 1.3, "center_y": 0.6}
        theme_text_color: "Custom"
        text_color: 0,0,1,1
        opposite_colors: False
        
    MDLabel:
        text: "208W1A1268"
        pos_hint: {"center_x": 1.3, "center_y": 0.5}
        theme_text_color: "Custom"
        text_color: 0,0,1,1
        opposite_colors: False
        
    MDLabel:
        text: "208W1A1284"
        pos_hint: {"center_x": 1.3, "center_y": 0.4}
        theme_text_color: "Custom"
        text_color: 0,0,1,1
        opposite_colors: False
        
    MDLabel:
        text: "208W1A12A4"
        pos_hint: {"center_x": 1.3, "center_y": 0.3}
        theme_text_color: "Custom"
        text_color: 0,0,1,1
        opposite_colors: False
    
    MDLabel:
        text: "208W1A1288"
        pos_hint: {"center_x": 1.3, "center_y": 0.5}
        theme_text_color: "Custom"
        text_color: 0,0,1,1
        opposite_colors: False
    
    MDIcon:
        icon: "language-python"
        pos_hint: {"center_x": 0.7, "center_y": 0.7}
        font_size: 70
        opposite_colors: False
    
    MDIcon:
        icon: "gmail"
        badge_icon: "numeric-10"
        pos_hint: {"center_x": 0.6, "center_y": 0.4}
        font_size: 50
        opposite_colors: False
    
    MDIcon:
        icon: "git"
        font_size: "50sp"
        opposite_colors: False
        
    MDIconButton:
        icon: "android"
        badge_icon: "numeric-20"
        pos_hint: {"center_x": 0.7,"center_y": 0.3}
        user_font_size: "72sp"
        md_bg_color: app.theme_cls.primary_dark
        
    MDIconButton:
        icon: "language-php"
        pos_hint: {"center_x": 0.7,"center_y": 0.5}
        user_font_size: "50sp"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
    
    MDIconButton:
        icon: "language-java"
        pos_hint: {"center_x": 0.7,"center_y": 0.7}
        user_font_size: "50sp"
        theme_text_color: "Error"
    
    MDIconButton:
        icon: "facebook"
        pos_hint: {"center_x": 0.7,"center_y": 0.9}
        user_font_size: "50sp"
        theme_text_color: "Custom"
        text_color: 0,0,1,1
    
    MDIconButton:
        icon: "instagram"
        pos_hint: {"center_x": 0.1,"center_y": 0.7}
        user_font_size: "100sp"
        theme_text_color: "Custom"
        text_color: 0,1,0,1
        
    MDFillRoundFlatIconButton:
        icon: "whatsapp"
        text: "M.J.N.V.SAI"
        pos_hint: {"center_x": 0.2,"center_y": 0.5}
        
    MDFloatingActionButtonSpeedDial:
        data: app.data
        root_button_anim: True
        
    MDSpinner:
        size_hint: None, None
        size: dp(35), dp(35)
        line_width: dp(3.25)
        color: [1,0,1,1]
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
    
    MDCheckbox:
        id: Check
        size_hint: None, None
        size: dp(40), dp(40)
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
    
    MDSlider:
        min: 0
        max: 100
        value: 50
        hint: True
        pos_hint: {'center_x': 0.5, 'center_y': 0.13}
        color: [0,0,1,1]
'''


class Mounav(MDApp):

    data = {
        'Guido-Van-rossum': 'language-python',
        'Radhe-syam Sir': 'language-c',
        'CS Pavan Sir': 'language-cpp',
        'K.Mounav' : 'twitter',
        'CR Mahith': 'facebook',
        'MD Rizwanullah' : 'gmail',
        'K.Prabhuram' : 'telegram',
        'M.J.N.V.Sai' : 'google',
        'A.Charan' : 'microsoft',
        'Ajay' : 'whatsapp',
        'Y.Sai Srinivas' : 'youtube',
        'Abhi venkat sai' : 'gacm.png',
        '208W1A12A0' : 'logo.png'
    }

    def build(self):
        self.icon = "logo.png"
        self.theme_cls.primary_palette = "Amber"
        self.theme_cls.theme_style = "Light"  # "Light" backgroud color

        time_dialog = MDTimePicker()
        time_dialog.open()

        return Builder.load_string(KV)


Mounav().run()