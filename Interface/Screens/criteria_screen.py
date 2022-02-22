Criteria_Screen = '''
<IconListItem>:
    icon: ""
    IconLeftWidget:
        icon: root.icon

MDScreen:
    name: 'Criteria'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 1, 1, 1, 1
        MDBoxLayout:
            size_hint_y: .1
            MDIconButton:
                icon: "arrow-left"
                # md_bg_color: 0, 0, 0, 1
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color
                pos_hint: {'center_x': .1, 'y': .09}
                on_release: 
                    app.homeScreen()
            MDLabel:
                text: "Home"
                pos_hint: {'center_x': .3, 'y': .09}
        MDFloatLayout:   
            md_bg_color: 1, 1, 1, 1     
            Carousel:
                id: carousel
                scroll_timeout: 0
                on_current_slide: app.current_slide(self.index)
                MDFloatLayout:
                    Image:
                        source: "images.png"
                        pos_hint: {"center_x": .5, "center_y":.85}
                        size_hint: 1, .6
                        canvas.before:
                            Color:
                                rgb: rgba(247, 247, 247, 255)
                            Rectangle:
                                size: self.size
                                pos: self.pos
                                
                    MDLabel:
                        text: "Speciality And Certificate"
                        size_hint_x: .6
                        pos_hint: {"center_x": .34, "center_y": .52}
                    MDLabel:
                        text: "Choose the Specialty and Degree Certificate You are going in for"
                        size_hint_x: .8
                        pos_hint: {"center_x": .49, "center_y": .42}
                        font_size: "12sp"
                        color: rgba(135, 145, 158, 255)
                        
                    MDDropDownItem:
                        id:drop_item1
                        pos_hint: {'center_x': .5, "center_y":.3}
                        text: "Software Engineering"
                        on_release: app.scMenu1.open()
                    MDDropDownItem:
                        id:drop_item2
                        pos_hint: {'center_x': .5, "center_y":.2}
                        text: "HND"
                        on_release: app.scMenu2.open()
                                
                MDFloatLayout:
                    Image:
                        source:"online-registration-sign-up-concept-with-man-character_268404-98.jpg"
                        pos_hint: {"center_x": .5, "center_y":.85}
                        size_hint: 1, .6
                        canvas.before:
                            Color:
                                rgb: rgba(247, 247, 247, 255)
                            Rectangle:
                                size: self.size
                                pos: self.pos
                    MDLabel:
                        text: "Town And Language"
                        size_hint_x: .6
                        pos_hint: {"center_x": .34, "center_y": .53}
                    MDLabel:
                        text: "Choose the Town and Language You want to study in"
                        size_hint_x: .8
                        pos_hint: {"center_x": .49, "center_y": .46}
                        font_size: "12sp"
                        color: rgba(135, 145, 158, 255)
                        
                    MDDropDownItem:
                        id:drop_item3
                        pos_hint: {'center_x': .5, "center_y":.39}
                        text: "Douala"
                        on_release: app.tlMenu1.open()
                    MDDropDownItem:
                        id:drop_item4
                        pos_hint: {'center_x': .5, "center_y":.3}
                        text: "English"
                        on_release: app.tlMenu2.open()
                    MDBoxLayout:
                        pos_hint: {'center_x': .5, "center_y":.19}
                        size_hint_y: .1
                        orientation: 'vertical'
                        Slider:
                            id: progressBar
                            # color: [.1, .1, .4, .3]
                            min: 0
                            max: 2000000
                            value: 0 
                            # background_width: '20dp'
                            # cursor_image: ''
                            cursor_color: app.theme_cls.primary_color
                            cursor_size: ('20dp', '20dp')
                            value_track_color: app.theme_cls.primary_color
                            value_track: True
                            # active: True
                            on_value: app.change_fees(self.value)
                        MDBoxLayout:  
                            #current time  
                            MDLabel:
                                id: current_fees
                                text: '0'
                                font_size: dp(12)
                            #Music time    
                            MDLabel:
                                id: music_time
                                text: '2,000,000'
                                halign: 'right'
                                font_size: dp(12)
                        
                    MDIconButton:
                        icon: "arrow-left"
                        md_bg_color: app.theme_cls.primary_color
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        pos_hint: {'center_x': .15, 'center_y': .08}
                        on_release: 
                            app.previous()
                        
            MDIconButton:
                icon: "arrow-right"
                md_bg_color: app.theme_cls.primary_color
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                pos_hint: {'center_x': .85, 'center_y': .08}
                on_release: 
                    app.next()
                    
            MDIconButton:
                id: slide0
                icon: "circle"
                theme_text_color: "Custom"
                text_color: rgba(111, 206, 203, 255)
                pos_hint: {'center_x': .5, 'center_y': .075}
                user_font_size: "8sp"
            MDIconButton:
                id: slide1
                icon: "circle"
                theme_text_color: "Custom"
                text_color: rgba(221, 221, 221, 255)
                pos_hint: {'center_x': .54, 'center_y': .075}
                user_font_size: "8sp"
                
            Widget:
            
            

'''