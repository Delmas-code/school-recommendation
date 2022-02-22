Start_Screen = '''

<Starter>
    img: ""
    Image:
        # source:"C:/Users/DELMAS/Desktop/Invore/Demo Project/Recipia/Images/logo2.png"
        source: root.img
        pos_hint: {'center_x':0.45 ,'center_y':0.5}
        
    # MDLabel:
    #     text: "GRemend"
    #     pos_hint: {'center_x':0.5 ,'center_y':0.3}
    #     halign: "center"
    #     font_name: "Interface/fonts/Poppins-Regular"
    #     font_size: "25sp"
    # MDLabel:
    #     text: "From"
    #     pos_hint: {'center_x':0.5 ,'center_y':0.25}
    #     halign: "center"
    #     # font_name: "fonts\Poppins-Regular"
    #     font_size: "15sp"
    # MDLabel:
    #     text: "Group 3"
    #     pos_hint: {'center_x':0.5 ,'center_y':0.2}
    #     halign: "center"
    #     # font_name: "fonts\Poppins-SemiBold"
    #     font_size: "20sp"
    MDLabel:
        text: "679066479"
        pos_hint: {'center_x':0.5 ,'center_y':0.1}
        halign: "center"
        # font_name: "Interface/fonts/Poppins-SemiBold"
        font_size: "12sp"

MDScreen:
    name: 'StartScreen'
    md_bg_color: app.theme_cls.primary_color
    bg_img: ''
    Starter:
        img: root.bg_img
'''