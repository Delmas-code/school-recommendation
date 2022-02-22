School_Screen = '''
<TabCard@MDCard>:
    icon: ""
    text: ""
    size_hint_y: None
    height: dp(55)
    radius: dp(15)
    MDIconButton:
        icon: root.icon
    MDLabel:
        text: root.text
        
<ContentCustomSheet>:
    orientation: 'vertical'
    size_hint_y: None
    height: "500dp"
    image: ""
    fees: ""
    info: ""
    link: ""
    padding: dp(8)
    spacing: dp(8)
    RelativeLayout:
        ElementCard:
            pos_hint: {"x":.05, "center_y":1.1}
            height: dp(150)
            image: root.image
            fees: root.fees
            Widget:
    Widget:
    MDLabel:
        text: root.info
        font_size: dp(13)
    Widget:
    MDBoxLayout:
        spacing: dp(5)
        MDRoundFlatIconButton:
            icon: 'cart'
            text: "Visit Website"
            size_hint_x: 1
            on_release:
                import webbrowser
                webbrowser.open(root.link)
        MDRoundFlatIconButton:
            icon: 'cards-heart'
            text: "Favourites"
            size_hint_x: 1
    MDRaisedButton:
        size_hint_x: 1
        text: "View Specialties"
        on_release: app.show_specialties()
        
            
        
        
<ElementCard>
    image: ''
    fees: ''
    text: ''
    orientation: 'vertical'
    on_release: app.show_school_info(root.image, root.fees, root.text)
    size_hint_x: .5
    size_hint_y: None
    md_bg_color: app.theme_cls.primary_color
    height: dp(200)
    padding: (10)
    radius: dp(25)
    MDBoxLayout:
        height: dp(80)
        size_hint_y: None
        Image:
            source: root.image
    Widget:
        height: dp(5)
            
    MDLabel:
        text: root.text
    Widget:
        height: dp(5)
    
    MDLabel:
        text: f"[font=Icons][color=#0000FF] {md_icons['clock-outline']}[/color][/font]" + root.fees
        markup:True
        halign: 'center'
    
    
MDScreen:
    name: 'Schools'
    MDBoxLayout:
        orientation: 'vertical'
        MDBoxLayout:
            orientation: 'vertical'
            adaptive_height: True
            MDBoxLayout:
                size_hint_y: None
                height: dp(65)
                AnchorLayout:
                    anchor_y: 'top'
                    anchor_x: 'left'
                    MDIconButton:
                        icon: 'arrow-left'
                        on_release: 
                            app.homeScreen()
                AnchorLayout:
                    anchor_y: 'top'
                    anchor_x: 'right'
                    MDIconButton:
                        icon: 'magnify'
                        on_release: app.searchpopup()
            MDBoxLayout:
                size_hint_y: None
                height: dp(55)
                spacing: dp(12)
                padding: dp(12)
                TabCard:
                    icon: 'shoe-sneaker'
                    text: "Fees"
                    md_bg_color: app.theme_cls.primary_color
                TabCard:
                    icon: 'tshirt-crew'
                    text: "Uniform"
                TabCard:
                    icon: 'redhat'
                    text: "school"
        MDBoxLayout:
            ScrollView:
                MDGridLayout:
                    id: school_card
                    adaptive_height: True
                    cols:2
                    padding: dp(20)
                    spacing: dp(20)
                    
        MDBoxLayout:
            size_hint_y:None
            height:dp(60)
            adaptive_width:True
            padding:dp(12)
            spacing:dp(10)
            pos_hint:{'center_x':.5}
            md_bg_color:.9,0.9,0.9,.5
            radius:[50,50,0,0]
            MDIconButton:
                icon:'food'
                size_hint_x:None
                width:root.width*.2
                on_press: app.criScreen()
            MDIconButton:
                icon:'magnify'
                size_hint_x:None
                width:root.width*.2
                on_press: app.searchpopup()
            MDFloatingActionButton:
                icon: "home"
                color: app.theme_cls.primary_color
                size_hint_x:None
                width:root.width*.2
                on_press: app.homeScreen()
            MDIconButton:
                icon: root.icon_item1
                size_hint_x:None
                width:root.width*.2
                on_press: app.mode(self)
                on_release: icon = root.icon_item2
            MDIconButton:
                icon:'group'
                size_hint_x:None
                width:root.width*.2
                on_press: app.schoolScreen()

                            
                
    

'''