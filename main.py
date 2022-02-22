# os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
import os
import random
from kivy import clock
from kivymd.app import MDApp
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.utils import rgba
from kivy.factory import Factory
from kivymd.uix import menu
from kivymd.uix.card import MDCard
from kivy.core.window import Window
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.swiper import MDSwiperItem
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import  StringProperty
from kivymd.uix.boxlayout import MDBoxLayout 
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivymd.uix.bottomsheet import MDCustomBottomSheet, MDListBottomSheet
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.button import MDFillRoundFlatIconButton


#Getting the screens
from Interface.Screens.cat_screen import Cat_Screen
from Interface.Screens.home_screen import Home_Screen
from Interface.Screens.start_screen import Start_Screen
from Interface.Screens.school_screen import School_Screen
from Interface.Screens.criteria_screen import Criteria_Screen

#Getting the Modules
from Interface.Modules.DB_searcher import *
from Interface.Modules.searchpopupmenu import SearchPopupMenu


Window.size = (350, 550)


#classes interacting with kv

dirname = os.path.dirname(__file__)
logo_bg_dir = os.path.join(dirname, "Interface")


class Category(MDCard):
    image = StringProperty('')
    text = StringProperty('')

class Starter(MDFloatLayout):
    img = StringProperty('')
    # pass
    
class ElementCard(MDCard):
    image = StringProperty('')
    fees = StringProperty('')
    text = StringProperty('')
    
class StepsItem(MDBoxLayout):
    stepNum = StringProperty('')
    step = StringProperty('')

class ImageBlock(MDBoxLayout):
    image = StringProperty('')
    recipeName = StringProperty('')
    duration = StringProperty('')
    category = StringProperty('')
    
class IconListItem(OneLineIconListItem):
    icon = StringProperty('')
    
class ContentCustomSheet(MDBoxLayout):
    image = StringProperty('')
    fees = StringProperty('')
    info = StringProperty('')
    link = StringProperty('')

class All_Recipes(MDSwiperItem):
    image = StringProperty('')
    text1 = StringProperty('')
    text2 = StringProperty('')

class CatCardItem(RelativeLayout):
    image = StringProperty('')
    text = StringProperty('')

class RecipesCardItem(RelativeLayout):
    image = StringProperty('')
    text = StringProperty('')
    duration =  StringProperty('')




#Main App Class
class RecipiaApp(MDApp):
    global  name_in_db, ar_name_in_db, town_in_db
    
    search_menu = None
    notify = None
    
    def itemSetter(self,i_func, menu_list):
        menu_items = [
            {
                "viewclass": "IconListItem",
                "icon": "git",
                "text": item,
                "height": dp(56),
                "on_release": lambda x= item: i_func(x)
            }
            for item  in menu_list
            
        ]
        return menu_items

    def menuItems(self):
        menu_list1 = ['Accounting', 'Management', 'Software Engineering', 'Telecom', 'Netorking', 'Finance & Banking', 'Business', 'Nursing', 'Philosophy', 'Computer Science', 'Medicine', 'Law', 'ICA']
        menu_list2 = ["HND","Bachelors", "Masters", "PHD"]
        menu_list3 = ['Yaounde','Douala', 'Buea','Bamenda','Ebolowa', 'Bertoua', 'Maroua', 'Garoua', 'Adamawa', 'Ngaoundere']
        menu_list4 = ["English", "French"]
        menu_items1 = self.itemSetter(self.set_item1, menu_list1)
        menu_items2 = self.itemSetter(self.set_item2, menu_list2)
        menu_items3 = self.itemSetter(self.set_item3, menu_list3)
        menu_items4 = self.itemSetter(self.set_item4, menu_list4)
        
        self.scMenu1 = MDDropdownMenu(
            caller = sm.get_screen("Criteria").ids.drop_item1,
            items = menu_items1,
            # position = "center",
            width_mult = 4
        )
        self.scMenu2 = MDDropdownMenu(
            caller = sm.get_screen("Criteria").ids.drop_item2,
            items = menu_items2,
            # position = "center",
            width_mult = 4
        )
        self.tlMenu1 = MDDropdownMenu(
            caller = sm.get_screen("Criteria").ids.drop_item3,
            items = menu_items3,
            # position = "center",
            width_mult = 4
        )
        self.tlMenu2 = MDDropdownMenu(
            caller = sm.get_screen("Criteria").ids.drop_item4,
            items = menu_items4,
            # position = "center",
            width_mult = 4
        )
        self.scMenu1.bind()
        self.scMenu2.bind()
        self.tlMenu1.bind()
        self.tlMenu1.bind()
        
    def set_item1(self, text_item):
        sm.get_screen("Criteria").ids.drop_item1.set_item(text_item)
        sm.get_screen('Criteria').ids[f"drop_item1"].text = text_item
        self.scMenu1.dismiss()
    def set_item2(self, text_item):
        sm.get_screen("Criteria").ids.drop_item2.set_item(text_item)
        sm.get_screen('Criteria').ids[f"drop_item2"].text = text_item
        self.scMenu2.dismiss()
    def set_item3(self, text_item):
        sm.get_screen("Criteria").ids.drop_item3.set_item(text_item)
        sm.get_screen('Criteria').ids[f"drop_item3"].text = text_item
        self.tlMenu1.dismiss()
    def set_item4(self, text_item):
        sm.get_screen("Criteria").ids.drop_item4.set_item(text_item)
        sm.get_screen('Criteria').ids[f"drop_item4"].text = text_item
        self.tlMenu2.dismiss()

    #Methods to handle the changing and transitions of screen

    def homeScreen(self, name='Home'):
        # if self.root.current == 'Favourites' or self.root.current== 'Category':
        self.root.transition.direction = 'right'
        sm.current = name

    def recScreen(self, name='Recipes'):
        sm.current = name
        self.root.transition.direction = 'left'

    def catScreen(self, name='Category'):
        sm.current = name
        self.root.transition.direction = 'left'
        
    def criScreen(self, name="Criteria"):
        sm.current= name
        self.root.transition.direction = "left"
    
    def schoolScreen(self, name= "Schools"):
        sm.current = name
        self.root.transition.direction = "left"

    def dyrecScreen(self, name='DynamicRec'):
        sm.current = name
        self.root.transition.direction = 'left'


    def mode(self, instance):
        if self.theme_cls.theme_style == "Light":
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.bg_normal
            instance.icon = "weather-sunny"
        else:
            self.theme_cls.theme_style = "Light"
            instance.icon = "moon-waning-crescent"

    #Methods to handle the pop up
    def notipopup(self):
        if not self.notify:
            self.notify = MDDialog(
                title = "No Such School Found",
                type = "custom",
                content_cls = MDLabel(text="We are sorry we didn't find a School with that name."),
                buttons = [
                        MDFlatButton(
                        text="Ok", text_color= self.theme_cls.primary_color,on_press=lambda *args: self.notify.dismiss()
                    ),
                ],
            )

        self.notify.open()
    def searchpopup(self):
        if not self.search_menu:
            self.search_menu = MDDialog(
                title = "Search For Schools",
                type = "custom",
                content_cls = SearchPopupMenu(),
                buttons = [
                        MDFlatButton(
                        text="Search", text_color= self.theme_cls.primary_color,on_press=lambda *args: self.search_menu.dismiss(), on_release=self.search
                    ),
                ],
            )

        self.search_menu.open()

    #Method for executing the search funvtionalty
    def search(self, *args):
        search_var = f'{self.search_menu.content_cls.ids.user_search.text}'
        
        out = user_searches(search_var)
        if out:
            try:
                sm.get_screen("Schools")
                sm.get_screen("Schools").ids.school_card.clear_widgets()
            except:
                sm.add_widget(Builder.load_string(School_Screen))

            for i in range(len(school_name)):
                sm.get_screen("Schools").ids.school_card.add_widget(ElementCard(image = f"{school_image[i]}",text=f'{school_name[i]}', fees= f'{school_fees[i]}'))

            self.schoolScreen()
        else:
            self.search_menu.dismiss()
            self.notipopup()        

        self.search_menu.content_cls.ids.user_search.text = ""



    #Method to put all the recipes in the database on the screen
    def put_school_to_screen(self):
        search_school()
        try:
            sm.get_screen("Schools")
            sm.get_screen("Schools").ids.school_card.clear_widgets()
        except:
            sm.add_widget(Builder.load_string(School_Screen))

        for i in range(len(school_name)):
            sm.get_screen("Schools").ids.school_card.add_widget(ElementCard(image = f"{school_image[i]}",text=f'{school_name[i]}', fees= f'{school_fees[i]}'))

            self.schoolScreen()

    # Methods to put all the category in the database on the screen
    def put_category_to_screen(self):
        search_town()   
        try:
            sm.get_screen("Category")
            sm.get_screen("Category").ids.container.clear_widgets()
        except:
            sm.add_widget(Builder.load_string(Cat_Screen))

        for i in range(len(town_name)):
            sm.get_screen("Category").ids.container.add_widget(CatCardItem(image = f"{town_image[i]}",text=f'{town_name[i]}'))

            self.catScreen()

    #Methods to handle the dynamicness ofcards in the home screen
    def put_ar_card_to_screen(self):
        search_school()
        sm.get_screen("Home")
        for i in range(len(school_name)):
            sm.get_screen("Home").ids.ar_card.add_widget(All_Recipes(image = f"{school_image[i]}",text1=f'{school_name[i]}', text2=f'{school_fees[i]}'))
        self.homeScreen()

    def put_cat_card_to_screen(self):
        search_town()   
        sm.get_screen("Home")
        for i in range(6):
            sm.get_screen("Home").ids.cat_card.add_widget(Category(image = f"{town_image[i]}",text=f'{town_name[i]}'))
            
        self.homeScreen()


    #Methods to get the names of the cards of category or recipes inorder to search its data from the data base
    def labelTextAR(self, instance):
        self.ar_name_in_db = instance.parent.text
        search_labelTextAR(self.ar_name_in_db) 
        self.dynamic_holder()
        self.dyrecScreen()
        
#Function to handle the town cards in the Town Screen

    def labelTextCAT(self, instance):
        self.town_in_db = instance.parent.text 
        search_labelTextCAT(self.town_in_db)
        if town_school_name:
            try:
                sm.get_screen("Schools")
                sm.get_screen("Schools").ids.school_card.clear_widgets()
            except:
                sm.add_widget(Builder.load_string(School_Screen))

            for i in range(len(town_school_name)):
                sm.get_screen("Schools").ids.school_card.add_widget(ElementCard(image = f"{town_school_image[i]}",text=f'{town_school_name[i]}', fees= f':{town_school_fees[i]}'))
            town_school_name.clear()
            town_school_image.clear()
            town_school_fees.clear()

            self.schoolScreen()

    def labelTextHomeAR(self, instance):
        self.ar_name_in_db = instance.parent.parent.text1
        search_labelTextAR(self.ar_name_in_db)
        self.dynamic_holder()
        self.dyrecScreen()

#Function to handle the town cards in the Homescreen
    def labelTextHomeCAT(self, instance):
        self.town_in_db  = instance.text
        search_labelTextCAT(self.town_in_db)
        if town_school_name:
            try:
                sm.get_screen("Schools")
                sm.get_screen("Schools").ids.school_card.clear_widgets()
            except:
                sm.add_widget(Builder.load_string(School_Screen))

            for i in range(len(town_school_name)):
                sm.get_screen("Schools").ids.school_card.add_widget(ElementCard(image = f"{town_school_image[i]}",text=f'{town_school_name[i]}', fees= f':{town_school_fees[i]}'))
            town_school_name.clear()
            town_school_image.clear()
            town_school_fees.clear()

            self.schoolScreen()

    #callback for bottomsheet
    def callback(*args):
        pass

    #Method that adds items to the bottomsheet
    def show_requirements(self, *kwargs):
        req_sheet = MDListBottomSheet()
        for i in range(len(req_list)):
            req_sheet.add_item(
                f'{req_list[i]}',
                lambda x, y=i: self.callback()
            )
        req_sheet.open()
    

        
    #MEthod handling the dynamic putting of specific recipe components on a dynamic screen
    def dynamic_holder(self):
        sm.get_screen("DynamicRec").ids.topblock.clear_widgets()
        sm.get_screen("DynamicRec").ids.container.clear_widgets()

        box = MDBoxLayout(size_hint_y= .10)
        btn = MDFillRoundFlatIconButton(text='Ingredients',
                icon= "food-fork-drink",
                pos_hint= {'center_y': .69, 'center_x':.8},
                # font_name= "fonts\Poppins-Regular",
                on_release= self.show_requirements
                
        )
        label = MDLabel(text=f'No of Steps: {len(steps_list)}')#, font_name= "fonts\Poppins-Light")
        box.add_widget(label)
        box.add_widget(btn)

        j =0
        sm.get_screen("DynamicRec").ids.topblock.add_widget(ImageBlock(recipeName = f"{ar_recipe[j]}",image=f'{ar_recipe[j+1]}', duration=f'{ar_recipe[j+2]}', category=f'{ar_recipe[j+3]}'))

        sm.get_screen("DynamicRec").ids.topblock.add_widget(box)

        for i in range(len(steps_list)):
            sm.get_screen("DynamicRec").ids.container.add_widget(StepsItem(stepNum = f"{i+1}",step=f'{steps_list[i]}'))


    
    #Main build func 
    def build(self):
        global sm
        
        #Call the func
        # self.arImagefunc()

        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.primary_hue = "A400"
        self.theme_cls.bg_darkest
        # if self.theme_cls.theme_style = "Dark":
        self.title = "GRemend"
        logo_path = f'{logo_bg_dir}\logo\logo2.png'
        self.icon = logo_path
        
        # print(logo_path)


       #Create an instance of the Screen Manager and add all the screen widgets to it
        sm = ScreenManager()
        
        sm.add_widget(Builder.load_string(Cat_Screen))
        sm.add_widget(Builder.load_string(Home_Screen))
        sm.add_widget(Builder.load_string(Start_Screen))
        sm.add_widget(Builder.load_string(School_Screen))
        sm.add_widget(Builder.load_string(Criteria_Screen))

        sm.get_screen("StartScreen").bg_img = logo_path
        
        

        return sm
    
    def current_slide(self, index):
        self.indexing = index
        for i in range(2):
            if index == i:
                self.root.get_screen("Criteria").ids[f"slide{index}"].text_color = rgba(111, 206, 203, 255)
                
            elif index != i:
                self.root.get_screen("Criteria").ids[f"slide{i}"].text_color = rgba(221, 221, 221, 255)
    
    #Funct to get the user criterias rom the dropdon menu   
    def get_user_criteria(self, req_5, **kargs):
        
        req_1 = sm.get_screen('Criteria').ids[f"drop_item1"].text
        req_2 = sm.get_screen('Criteria').ids[f"drop_item2"].text
        req_3 = sm.get_screen('Criteria').ids[f"drop_item3"].text
        req_4 = sm.get_screen('Criteria').ids[f"drop_item4"].text   
        try:
            query_user_criteria(req_1, req_2, req_3, req_4, req_5)
            
        except Error as e:
            # print(e)
            pass
        # print("After the for loop")
        for s_name in s_names:
            search_school_with_condition(s_name[0])
        try:
            sm.get_screen("Schools")
            sm.get_screen("Schools").ids.school_card.clear_widgets()
        except:
            sm.add_widget(Builder.load_string(School_Screen))
        for i in range(len(school_name1)):
            sm.get_screen("Schools").ids.school_card.add_widget(ElementCard(image = f"{school_image1[i]}",text=f'{school_name1[i]}', fees= f'{school_fees1[i]}'))

        self.schoolScreen()
            
            
    j = 1           
    def next(self):    
        if self.j == 1:
            self.root.get_screen("Criteria").ids.carousel.load_next(mode='next')   
            self.j += 1

        elif self.j == 2:
            userFees = sm.get_screen("Criteria").ids.current_fees.text
            # print(userFees)
            self.get_user_criteria(userFees)
            # self.schoolScreen()
            sm.get_screen("Criteria").ids.carousel.index = 0
            self.j = 1
            
    def previous(self):
        self.root.get_screen("Criteria").ids.carousel.load_previous()
        self.j -= 1
        # print(self.j)
      
    #a var to handle a list of specialties in a particular school       
    #Function to display all school data in a bottom sheet when a card is clicked
    def show_school_info(self, image, fees, text):
        search_school()
        bottom_sheet = Factory.ContentCustomSheet()
        bottom_sheet.image = image
        bottom_sheet.fees = fees
        row4, row5 = search_school_v2(text)
        bottom_sheet.info = row4   
        bottom_sheet.link = row5
        self.custom_sheet = MDCustomBottomSheet(screen = bottom_sheet)
        self.custom_sheet.open()
        
    def callback(*args):
        pass

    #Method that adds items to the bottomsheet
    def show_specialties(self, *kwargs):
        spec_sheet = MDListBottomSheet()
        for i in range(len(spec_list)):
            spec_sheet.add_item(
                f'{spec_list[i]}',
                lambda x, y=i: self.callback()
            )
        spec_sheet.open()
    
    def change_fees(self, value):
        userFees = sm.get_screen("Criteria").ids.current_fees
        userFees.text = str(int(value))
        
    def launcher(self, *args):
        self.put_ar_card_to_screen()
        self.put_cat_card_to_screen()

    def on_start(self):
        sm.current = "StartScreen"
        sm.get_screen("StartScreen")
        clock.Clock.schedule_once(self.launcher, 4)
        self.menuItems()


if __name__ == "__main__":
    RecipiaApp().run() 