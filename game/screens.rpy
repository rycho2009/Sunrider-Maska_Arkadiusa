# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

init -1 python hide:

    ## Used when exiting the game menu to the game.
    config.exit_transition = dissolve

    ## Used between screens of the game menu.
    config.intra_transition = dissolve

    ## Used when entering the game menu from the main menu.
    config.main_game_transition = dissolve

    ## Used when returning to the main menu from the game.
    config.game_main_transition = dissolve

    ## Used when entering the main menu from the splashscreen.
    config.end_splash_transition = dissolve

    ## Used when entering the main menu after the game has ended.
    config.end_game_transition = dissolve

    ## Used when a game is loaded.
    config.after_load_transition = dissolve

    ## Used when the window is shown.
    config.window_show_transition = dissolve

    ## Used when the window is hidden.
    config.window_hide_transition = dissolve

    config.thumbnail_width = 124
    config.thumbnail_height = 70
    config.game_menu_action = [ FileTakeScreenshot(), Show("save") ]

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:

    if 'mouseup_3' not in config.keymap['game_menu']:
        key 'mouseup_3' action Show('save')
    
    # Defaults for side_image and two_window
    default side_image = None
    default two_window = False
    zorder 100

    # Decide if we want to use the one-window or two-window varaint.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"
                ysize 380
                ypos 0.1

            if who:
                text who:
                    id "who"
                    size 35
                    outlines [ (2, "#0a0a0a", 0, 0) ]

        text what:
            id "what"
            xmaximum 1080       #change this to increase the max length of the text. (anything longer gets wrapped)
            ypos 0.8           #vertical position
            text_align 0.5      #centers the text inside the displayable
            xalign 0.5          #sets the text displayable itself in the center of the screen
            size 25
            outlines [ (2, "#0a0a0a", 0, 0) ]

        #textbutton "Dev Con" xpos 1800 ypos 0 action Show("devconsole", transition=None)

    # Use the quick menu.
    use quick_menu

screen devconsole:
    textbutton "Tweak stats" xpos 0.85 ypos 0.05 action None
    textbutton "quit" xpos 0.85 ypos 0.08 action Jump('quit')
    textbutton "Back" xpos 0.85 ypos 0.11 action Hide("devconsole", transition=None)


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

    vbox:
        ypos 0.65
        spacing 5

        # Create one textbutton per label, action pair.
        for label, action, chosen in items:
            imagebutton:
                action action
                xmargin 140
                xfill True
                idle "Menu/choice.png"
                hover "Menu/choice_hover.png"

    vbox:
        ypos 0.655
        xalign 0.5
        spacing 28
        for label, action, chosen in items:

            text label:
                size 25
                outlines [ (2, "#000", 0, 0) ]
                text_align 0.5
                xalign 0.5
                yalign 0.5

init -2 python:
    config.narrator_menu = True

    style.menu_window.set_parent(style.default)
    style.menu_choice.set_parent(style.button_text)
    style.menu_choice.clear()
    style.menu_choice_button.set_parent(style.button)
    style.menu_choice_button.xminimum = int(config.screen_width * 0.75)
    style.menu_choice_button.xmaximum = int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

    window:
        has vbox

        text prompt
        input id "input"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl:

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu:

    $store.BM = Battle()
    $store.MasterBM = store.BM
    $store.BM.phase = 'Player'

    imagemap:
        ground "Menu/menu_default.jpg"
        idle "Menu/menu_default.jpg"
        insensitive "Menu/menu_inactive.jpg"
        hover "Menu/menu_hover.jpg"

        hotspot (81, 412, 202, 43) action Show('campaigns', transition=dissolve)
        hotspot (86, 472, 197, 43) action FileLoad("1", page="auto", confirm=False)
        hotspot (100, 540, 183, 42) action ShowMenu('load')
        hotspot (130, 605, 155, 35) action ShowMenu('preferences')
        hotspot (175, 670, 108, 41) action ShowMenu('bonus')
        hotspot (175, 732, 108, 45) action Quit()

    text '[config.version]' xpos 0.01 ypos 0.98 size 12

    if CENSOR == False:

        text ' WYKRYTO DECENZOR' xpos 0.01 ypos 0.958 size 15

    if CENSOR == True:

        text ' EDYCJA VANILLA' xpos 0.01 ypos 0.958 size 15


screen campaigns:
    
    imagemap:
        ground "Menu/mainmenu_campaign.png"
        idle "Menu/mainmenu_campaign.png"
        insensitive "Menu/mainmenu_campaign.png"
        hover "Menu/mainmenu_campaign_hover.png"
        alpha False
        
        hotspot (320, 385, 250, 42) action Start()
        hotspot (320, 431, 260, 35) action Start("skiptomaskofarcadius")
        
init -2 python:

    # Make all the main menu buttons be the same size.
    style.mm_button.size_group = "mm"


##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Wróć") action Return()
        textbutton _("Ustawienia") action ShowMenu("preferences")
        textbutton _("Zapisz Grę") action ShowMenu("save")
        textbutton _("Wczytaj Grę") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Pomoc") action Help()
        textbutton _("Wyjdź") action Quit()

init -2 python:
    style.gm_nav_button.size_group = "gm_nav"

    deletedScenes = BonusItem("Background/renpytomback.jpg", " Usunięte sceny", "deleted_scenes", 0.09)
    # chapterSelect = BonusItem("CG/cera.jpg", " Chapter Select", "chapter_select", 0.09)
    modScenes = BonusItem("CG/mochi1.jpg", " Wybór dodatkowych scen", "mod_scenes", 0.09)

    bonus_features = [deletedScenes, modScenes]  #, chapterSelect]

screen bonus:

    modal True
    zorder 200

    imagemap:
        ground "Menu/bonus_base.png"
        hover "Menu/bonus_hover.png"

        hotspot (726, 59, 137, 44) action [ Hide('bonus'), Show('save', transition=dissolve) ]
        hotspot (948, 926, 107, 23) action Hide('bonus', transition=dissolve)
        hotspot (864, 59, 137, 44) action [ Hide('bonus'), Show('load', transition=dissolve) ]
        hotspot (1002, 59, 137, 44) action [ Hide('bonus'), Show('preferences', transition=dissolve) ]
        hotspot (1140, 59, 137, 44) action Hide('bonus', transition=dissolve)

        $ columns = 1
        $ rows = 5

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            xpos 753
            ypos 216

            if hasattr(store,'BM'):
                $BM.phase = 'Player' # This is done to make sure that we can open the menu while in a bonus

            # Display five file slots, numbered 1 - 5.
            for i in range(1, columns * rows + 1):

                button:

                    xminimum 460
                    yminimum 130
                    background None #Solid(0,0,0,255)

                    has hbox

                    # Add the image and text.
                    if i - 1 < len(bonus_features):
                        $ bonusimage = 0
                        imagebutton:
                            idle (bonus_features[i - 1].image)
                            hover hoverglow(bonus_features[i - 1].image)
                            at zoom_button(bonus_features[i - 1].zoom)
                            action [ResetBonusPage(),Hide('bonus'),ShowMenu(bonus_features[i - 1].jumpLoc)]
                        text bonus_features[i - 1].text

                    else:
                        text str(i) + ". Niewykorzystany Bonus"

##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen load:

    modal True
    zorder 200

    key "mousedown_3" action Hide('load', transition=dissolve)
    key 'mousedown_4' action NullAction() #should fix a bug where you can rollback in battle when the menu is open.

    if not hasattr(store,'BM'):
        $ BM = Battle()
        $ MasterBM = BM
    if (BM.phase == 'PACT' or BM.phase == 'Pirate'):
        text 'UWAGA! \n Nie możesz wczytywać w trakcie tury\n przeciwnika.':
            xalign 0.5
            yalign 0.5
            size 35
            color 'fff'
            outlines [(2,'f00',0,0)]

        timer 2 action Hide('load')
    else:

        imagemap:
            ground "Menu/load_base.png"
            hover "Menu/load_hover.png"

            hotspot (752, 215, 137, 28) action FilePage(1)
            hotspot (913, 215, 137, 28) action FilePage("auto")
            hotspot (1075, 215, 137, 28) action FilePage("quick")
            hotspot (1221, 250, 30, 146) action FilePagePrevious()
            hotspot (1221, 724, 30, 146) action FilePageNext()
            hotspot (948, 926, 107, 23) action Hide('load', transition=dissolve)
            hotspot (726, 59, 137, 44) action [ Hide('load'), Show('save', transition=dissolve) ]
            hotspot (1002, 59, 137, 44) action [ Hide('load'), Show('preferences', transition=dissolve) ]
            hotspot (1140, 59, 137, 44) action MainMenu()

            style "file_picker_frame"

            $ columns = 1
            $ rows = 8

            # Display a grid of file slots.
            grid columns rows:
                transpose True
                xfill True
                style_group "file_picker"
                xpos 753
                ypos 251

                # Display eight file slots, numbered 1 - 8.
                for i in range(1, columns * rows + 1):

                    # Each file slot is an hbox containing two buttons.
                    hbox:

                        button:

                            xminimum 424
                            yminimum 77
                            action FileAction(i)

                            has hbox

                            # Add the screenshot.
                            add FileScreenshot(i)

                            # Format the description, and add it as text.
                            $ description = "% 2s. %s\n%s" % (
                                FileSlotName(i, columns * rows),
                                FileTime(i, empty=_("Pusty slot.")),
                                FileSaveName(i))

                            text description

                            key "save_delete" action FileDelete(i)

                        button:

                            yminimum 77
                            action FileDelete(i)
                            text "X" # Or this could be an image or something.

screen save:

    modal True
    zorder 200

    key "mousedown_3" action Hide('save', transition=dissolve)
    key 'mousedown_4' action NullAction() #should fix a bug where you can rollback in battle when the menu is open.

    if not hasattr(store,"BM"):
        $ BM = Battle()
        #No need to update the MasterBM if there is no battle manager to begin with.  Besides, the MasterBM and the BM might not be the same
    if (BM.phase == 'PACT' or BM.phase == 'Pirate'):
        text 'UWAGA! \n Nie możesz zapisywać w trakcie tury\n przeciwnika.':
            xalign 0.5
            yalign 0.5
            size 35
            color 'fff'
            outlines [(2,'f00',0,0)]

        timer 2 action Hide('save')

    else:

        imagemap:
            ground "Menu/save_base.png"
            hover "Menu/save_hover.png"

            hotspot (752, 215, 137, 28) action FilePage(1)
            hotspot (913, 215, 137, 28) action FilePage("auto")
            hotspot (1075, 215, 137, 28) action FilePage("quick")
            hotspot (1221, 250, 30, 146) action FilePagePrevious()
            hotspot (1221, 724, 30, 146) action FilePageNext()
            hotspot (948, 926, 107, 23) action Hide('save', transition=dissolve)
            hotspot (864, 59, 137, 44) action [ Hide('save'), Show('load', transition=dissolve) ]
            hotspot (1002, 59, 137, 44) action [ Hide('save'), Show('preferences', transition=dissolve) ]
            hotspot (1140, 59, 137, 44) action MainMenu()

            style "file_picker_frame"

            $ columns = 1
            $ rows = 8

            # Display a grid of file slots.
            grid columns rows:
                transpose True
                xfill True
                style_group "file_picker"
                xpos 753
                ypos 251

                # Display eight file slots, numbered 1 - 8.
                for i in range(1, columns * rows + 1):

                    # Each file slot is an hbox containing two buttons.
                    hbox:

                        button:

                            xminimum 424
                            yminimum 77
                            action FileAction(i)

                            has hbox

                            # Add the screenshot.
                            add FileScreenshot(i)

                            # Format the description, and add it as text.
                            $ description = "% 2s. %s\n%s" % (
                                FileSlotName(i, columns * rows),
                                FileTime(i, empty=_("Pusty slot.")),
                                FileSaveName(i))

                            text description

                            key "save_delete" action FileDelete(i)

                        button:

                            yminimum 77
                            action FileDelete(i)
                            text "X" # Or this could be an image or something.

init -2 python:
    style.file_picker_frame = Style(style.menu_frame)

    style.file_picker_nav_button = Style(style.small_button)
    style.file_picker_nav_button_text = Style(style.small_button_text)

    style.file_picker_button = Style(style.large_button)
    style.file_picker_text = Style(style.large_button_text)
    style.large_button.idle_color = "#2E2E2E"
    style.large_button.hover_color = "#ccc"



##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences:
    zorder 200
    modal True

    key "mousedown_3" action Hide('preferences', transition=dissolve)
    key 'mousedown_4' action NullAction() #should fix a bug where you can rollback in battle when the menu is open.
    
    imagemap:

        ground "Menu/preferences_base.png"
        hover "Menu/preferences_hover.png"
        selected_idle "Menu/preferences_active.png"
        selected_hover "Menu/preferences_active.png"

        hotspot (864, 59, 137, 44) action [ Hide('preferences'), Show('load', transition=dissolve) ]
        hotspot (726, 59, 137, 44) action [ Hide('preferences'), Show('save', transition=dissolve) ]
        hotspot (1078, 130, 160, 45) action [ Hide('preferences'), Show('gameprefs', transition=dissolve) ]
        hotspot (1140, 59, 137, 44) action MainMenu()
        hotspot (840, 235, 60, 20) action Preference("display", "window")
        hotspot (1035, 235, 125, 20) action Preference("display", "fullscreen")
        hotspot (750, 340, 292, 20) action Preference("skip", "seen")
        hotspot (1060, 340, 110, 20) action Preference("skip", "all")
        hotspot (800, 410, 190, 20) action Preference("after choices", "skip")
        hotspot (1018, 410, 200, 20) action Preference("after choices", "stop")
        hotspot (822, 470, 146, 15) action Skip(fast=True)

        hotspot (948, 926, 107, 23) action Hide('preferences', transition=dissolve)

        bar:
            xpos 780
            ypos 570
            xmaximum 250
            value Preference("music volume")
        bar:
            xpos 780
            ypos 650
            xmaximum 250
            value Preference("sound volume")
        bar:
            xpos 780
            ypos 800
            xmaximum 250
            value Preference("text speed")

        bar:
            xpos 780
            ypos 725
            xmaximum 250
            value Preference("voice volume")
            
        textbutton "Test":
            xpos 1100
            ypos 650
            action Play("sound", "Sound/explosion1.ogg")
            style "soundtest_button"
        bar:
            xpos 780
            ypos 880
            xmaximum 250
            value Preference("auto-forward time")
            
screen gameprefs:
    
    zorder 200
    modal True
    
    key "mousedown_3" action Hide('gameprefs', transition=dissolve)
    key 'mousedown_4' action NullAction() #should fix a bug where you can rollback in battle when the menu is open.
    
    imagemap:

        ground "Menu/preferences_gameplay_base.png"
        hover "Menu/preferences_gameplay_hover.png"
        selected_idle "Menu/preferences_gameplay_active.png"
        selected_hover "Menu/preferences_gameplay_active.png"
    
        hotspot (864, 59, 137, 44) action [ Hide('gameprefs'), Show('load', transition=dissolve) ]
        hotspot (726, 59, 137, 44) action [ Hide('gameprefs'), Show('save', transition=dissolve) ]
        hotspot (750, 130, 180, 45) action [ Hide('gameprefs'), Show('preferences', transition=dissolve) ]
        hotspot (750, 260, 350, 26) action SetVariable("Difficulty", 0)
        hotspot (750, 339, 350, 26) action SetVariable("Difficulty", 1)
        hotspot (750, 400, 350, 26) action SetVariable("Difficulty", 2)
        hotspot (750, 460, 350, 26) action SetVariable("Difficulty", 3)        
        hotspot (750, 538, 350, 26) action SetVariable("Difficulty", 4)        
        hotspot (750, 598, 350, 26) action SetVariable("Difficulty", 5)
        
        hotspot (796, 707, 36, 20) action SetField(BM, 'show_tooltips', True)  
        hotspot (1014, 707, 34, 20) action SetField(BM, 'show_tooltips', False)

        hotspot (796, 780, 36, 20) action SetField(BM, 'edgescroll', (100,800))
        hotspot (1014, 780, 34, 20) action SetField(BM, 'edgescroll', (0,0)) 

        hotspot (796, 850, 36, 20) action SetField(BM, 'show_battle_log', True)
        hotspot (1014, 850, 34, 20) action SetField(BM, 'show_battle_log', False)
        
        hotspot (948, 926, 107, 23) action Hide('gameprefs', transition=dissolve)

init -2 python:
    style.bar.hover_color = "#ccc"
    style.pref_frame.xfill = True
    style.pref_frame.xmargin = 5
    style.pref_frame.top_margin = 5

    style.pref_vbox.xfill = True

    style.pref_button.size_group = "pref"
    style.pref_button.xalign = 1.0

    style.pref_slider.xmaximum = 192
    style.pref_slider.xalign = 1.0

    style.soundtest_button.xalign = 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt:
    zorder 200
    modal True

    imagemap:
        ground "Menu/yesno_menu.png"

        textbutton _("Tak"):
            xalign 0.48
            yalign 0.57
            action yes_action
        textbutton _("Nie"):
            xalign 0.58
            yalign 0.57
            action no_action

        label _(message):
            xalign 0.53
            yalign 0.48

init -2 python:
    style.yesno_button.size_group = "yesno"
    style.yesno_label_text.text_align = 0.5


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu:

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 0.99
        yalign 0.99

        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Zapisz") action [ FileTakeScreenshot(), Show('save',transition=dissolve) ]
        textbutton _("Wczytaj") action [ FileTakeScreenshot(), Show('load',transition=dissolve) ]
        textbutton _("Pomiń") action Skip()
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Ust.") action [ FileTakeScreenshot(), Show('preferences',transition=dissolve) ]
        textbutton _("Menu") action MainMenu()

init -2 python:
    style.quick_button.set_parent('default')
    style.quick_button.background = None
    style.quick_button.xpadding = 5

    style.quick_button_text.set_parent('default')
    style.quick_button_text.size = 20
    style.quick_button_text.idle_color = "#8888"
    style.quick_button_text.hover_color = "#ccc"
    style.quick_button_text.selected_idle_color = "#cc08"
    style.quick_button_text.selected_hover_color = "#cc0"
    style.quick_button_text.insensitive_color = "#4448"

    # Set a default value for the auto-forward time, and note that AFM is
    # turned off by default.
    config.default_afm_time = 1
    config.default_afm_enable = False
