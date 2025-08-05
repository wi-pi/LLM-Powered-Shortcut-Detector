import base64
from parse_xml.actions.action_start_stopwatch import action_start_stopwatch
from parse_xml.actions.add_tag_notes import action_add_tag_notes
from parse_xml.actions.add_to_pinnote import action_add_to_pinnote
from parse_xml.actions.add_workflow_to_screen import action_add_workflow_to_screen
from parse_xml.actions.addframetogif import action_addframetogif
from parse_xml.actions.addmusictoupnext import action_addmusictoupnext
from parse_xml.actions.addnewcalendar import action_addnewcalendar
from parse_xml.actions.addnewcontact import action_add_new_contact
from parse_xml.actions.addnewevent import action_addnewevent
from parse_xml.actions.addnewreminder import action_addnewreminder
from parse_xml.actions.address import action_address
from parse_xml.actions.addtoplaylist import action_addtoplaylist
from parse_xml.actions.adjustdate import action_adjustdate
from parse_xml.actions.airdropdocument import action_airdropdocument
from parse_xml.actions.airplanemode_set import action_airplanemode_set
from parse_xml.actions.alert import action_alert
from parse_xml.actions.appearance import action_appearance
from parse_xml.actions.appendnote import action_appendnote
from parse_xml.actions.appendvariable import action_appendvariable
from parse_xml.actions.ask import action_ask
from parse_xml.actions.avairyeditphoto import action_avairyeditphoto
from parse_xml.actions.base64encode import action_base64encode
from parse_xml.actions.bluetooth_set import action_bluetooth_set
from parse_xml.actions.bookmark_safari import action_bookmark_safari
from parse_xml.actions.calculateexpression import action_calculateexpression
from parse_xml.actions.call import action_call
from parse_xml.actions.cancel_timer import action_cancel_timer
from parse_xml.actions.cellulardata_set import action_cellulardata_set
from parse_xml.actions.change_focus_mail import action_change_focus_mail
from parse_xml.actions.change_setting_recording import action_change_setting_recording
from parse_xml.actions.choosefromlist import action_choosefromlist
from parse_xml.actions.choosefrommenu import action_choosefrommenu
from parse_xml.actions.clearupnext import action_clearupnext
from parse_xml.actions.comment import action_comment
from parse_xml.actions.compresspdf import action_compresspdf
from parse_xml.actions.conditional import action_conditional
from parse_xml.actions.contacts import action_contacts
from parse_xml.actions.converttimezone import action_converttimezone
from parse_xml.actions.correctspelling import action_correctspelling
from parse_xml.actions.count import action_count
from parse_xml.actions.create_alarm import action_create_alarm
from parse_xml.actions.create_icloudlink import action_create_icloudlink
from parse_xml.actions.create_newtab import action_create_newtab
from parse_xml.actions.create_newtabgtoup import action_create_new_tab_group
from parse_xml.actions.create_note_folder import action_create_note_folder
from parse_xml.actions.create_private_tab import action_create_private_tab
from parse_xml.actions.create_recording import action_create_recording
from parse_xml.actions.create_remainderlist import action_create_remainderlist
from parse_xml.actions.create_shortcut import action_create_shortcut
from parse_xml.actions.create_tag_notes import action_create_tag_notes
from parse_xml.actions.createplaylist import action_createplaylist
from parse_xml.actions.date import action_date
from parse_xml.actions.decayed_action import action_decayed_action
from parse_xml.actions.delay import action_delay
from parse_xml.actions.delete_alarm import action_delete_alarm
from parse_xml.actions.delete_note_folder import action_delete_note_folder
from parse_xml.actions.delete_recording import action_delete_recording
from parse_xml.actions.delete_tag_notes import action_delete_tag_notes
from parse_xml.actions.deletenote import action_deletenote
from parse_xml.actions.deletephoto import action_deletephoto
from parse_xml.actions.deleteworkflow import action_deleteworkflow
from parse_xml.actions.detect_address import action_detect_address
from parse_xml.actions.detect_contacts import action_detect_contacts
from parse_xml.actions.detect_date import action_detect_date
from parse_xml.actions.detect_dictionary import action_detect_dictionary
from parse_xml.actions.detect_emailaddress import action_detect_emailaddress
from parse_xml.actions.detect_images import action_detect_images
from parse_xml.actions.detect_link import action_detect_link
from parse_xml.actions.detect_number import action_detect_number
from parse_xml.actions.detect_phonenumber import action_detect_phonenumber
from parse_xml.actions.detect_text import action_detect_text
from parse_xml.actions.detectlanguage import action_detectlanguage
from parse_xml.actions.dictatetext import action_dictatetext
from parse_xml.actions.dictionary import action_dictionary
from parse_xml.actions.dismisssiri import action_dismisssiri
from parse_xml.actions.dnd_getfocus import action_dnd_getfocus
from parse_xml.actions.dnd_set import action_dnd_set
from parse_xml.actions.documentpicker_open import action_documentpicker_open
from parse_xml.actions.documentpicker_save import action_documentpicker_save
from parse_xml.actions.downloadurl import action_downloadurl
from parse_xml.actions.edit_alarm import action_edit_alarm
from parse_xml.actions.email import action_email
from parse_xml.actions.encodemedia import action_encodemedia
from parse_xml.actions.exit import action_exit
from parse_xml.actions.exportsong import action_exportsong
from parse_xml.actions.external_app import action_external_app
from parse_xml.actions.extracttextfromimage import action_extracttextfromimage
from parse_xml.actions.facetime import action_facetime
from parse_xml.actions.file import action_file
from parse_xml.actions.file_append import action_file_append
from parse_xml.actions.file_createfolder import action_file_createfolder
from parse_xml.actions.file_delete import action_file_delete
from parse_xml.actions.file_getfoldercontents import action_file_getfoldercontents
from parse_xml.actions.file_getlink import action_file_getlink
from parse_xml.actions.file_move import action_file_move
from parse_xml.actions.file_rename import action_file_rename
from parse_xml.actions.file_select import action_file_select
from parse_xml.actions.filter_alarms import action_filter_alarms
from parse_xml.actions.filter_articles import action_filter_articles
from parse_xml.actions.filter_calendarevents import action_filter_calendarevents
from parse_xml.actions.filter_cellular import action_filter_cellular
from parse_xml.actions.filter_contact import action_filter_contacts
from parse_xml.actions.filter_eventattendees import action_filter_eventattendees
from parse_xml.actions.filter_files import action_filter_files
from parse_xml.actions.filter_health_quantity import action_filter_health_quality
from parse_xml.actions.filter_images import action_filter_images
from parse_xml.actions.filter_locations import action_filter_locations
from parse_xml.actions.filter_music import action_filter_music
from parse_xml.actions.filter_notes import action_filter_notes
from parse_xml.actions.filter_photos import action_filter_photos
from parse_xml.actions.filter_readinglist_item import action_filter_readinglist_item
from parse_xml.actions.filter_reminders import action_filter_reminders
from parse_xml.actions.filter_tab import action_filter_tab
from parse_xml.actions.filter_tabgroup import action_filter_tabgroup
from parse_xml.actions.flashlight import action_flashlight
from parse_xml.actions.format_date import action_format_date
from parse_xml.actions.format_filesize import action_format_filesize
from parse_xml.actions.format_number import action_format_number
from parse_xml.actions.generatebarcode import action_generatebarcode
from parse_xml.actions.get_detail_timer import action_get_detail_timer
from parse_xml.actions.get_object_ofclass import action_get_object_ofclass
from parse_xml.actions.get_playlist import action_get_playlist
from parse_xml.actions.getarticle import action_getarticle
from parse_xml.actions.getbatterylevel import action_getbatterylevel
from parse_xml.actions.getclipboard import action_getclipboard
from parse_xml.actions.getcurrentlocation import action_getcurrentlocation
from parse_xml.actions.getcurrentsong import action_getcurrentsong
from parse_xml.actions.getdevicedetails import action_getdevicedetails
from parse_xml.actions.getdirections import action_getdirections
from parse_xml.actions.getdistance import action_getdistance
from parse_xml.actions.getepisodesforpodcast import action_getepisodesforpodcast
from parse_xml.actions.getframesfromimage import action_getframesfromimage
from parse_xml.actions.gethalfwaypoint import action_gethalfwaypoint
from parse_xml.actions.gethomeaccessorystate import action_gethomeaccessory
from parse_xml.actions.gethtmlfromrichtext import action_gethtmlfromrichtext
from parse_xml.actions.getipaddress import action_getipaddress
from parse_xml.actions.getitemfromlist import action_getitemfromlist
from parse_xml.actions.getitemname import action_getitemname
from parse_xml.actions.getitemtype import action_getitemtype
from parse_xml.actions.getlastphoto import action_getlastphoto
from parse_xml.actions.getlastscreenshot import action_getlastscreenshot
from parse_xml.actions.getlastvideo import action_getlastvideo
from parse_xml.actions.getlatestburst import action_getlatestburst
from parse_xml.actions.getlatestlivephotos import action_getlatestlivephotos
from parse_xml.actions.getlatestphotoimport import action_getlatestphotoimport
from parse_xml.actions.getmapslink import action_getmapslink
from parse_xml.actions.getmarkdownfromrichtext import action_getmarkdownfromrichtext
from parse_xml.actions.getmyworkflows import action_getmyworkflows
from parse_xml.actions.getnameofemoji import action_getnameofemoji
from parse_xml.actions.getonscreencontent import action_getonscreencontent
from parse_xml.actions.getorientation import action_getorientation
from parse_xml.actions.getparkedcarlocation import action_getparkedcarlocation
from parse_xml.actions.getphysicalactivity import action_getphysicalactivity
from parse_xml.actions.getpodcastsfromlibrary import action_getpodcastsfromlibrary
from parse_xml.actions.getrichtextfromhtml import action_getrichtextfromhtml
from parse_xml.actions.getrichtextfrommarkdown import action_getrichtextfrommarkdown
from parse_xml.actions.gettext import action_gettext
from parse_xml.actions.gettextfrompdf import action_gettextfrompdf
from parse_xml.actions.gettimebetweendates import action_gettimebetweendates
from parse_xml.actions.gettraveltime import action_gettraveltime
from parse_xml.actions.gettypeaction import action_gettypeaction
from parse_xml.actions.getupcomingevents import action_getupcomingevents
from parse_xml.actions.getupcomingreminders import action_getupcomingreminders
from parse_xml.actions.geturlcomponent import action_geturlcomponent
from parse_xml.actions.getvalueforkey import action_getvalueforkey
from parse_xml.actions.getvariable import action_getvariable
from parse_xml.actions.getwebpagecontents import action_getwebpagecontents
from parse_xml.actions.getwifi import action_getwifi
from parse_xml.actions.giphy import action_giphy
from parse_xml.actions.handoffplayback import action_handoffplayback
from parse_xml.actions.hash import action_hash
from parse_xml.actions.health_quantity_log import action_health_quantity_log
from parse_xml.actions.health_workout_log import action_health_workout_log
from parse_xml.actions.homeaccessory import action_homeaccessory
from parse_xml.actions.image_combine import action_image_combine
from parse_xml.actions.image_convert import action_image_convert
from parse_xml.actions.image_crop import action_image_crop
from parse_xml.actions.image_flip import action_image_flip
from parse_xml.actions.image_mask import action_image_mask
from parse_xml.actions.image_removebackground import action_image_removebackground
from parse_xml.actions.image_rotate import action_image_rotate
from parse_xml.actions.intercom import action_intercom
from parse_xml.actions.lap_stopwatch import action_lap_stopwatch
from parse_xml.actions.list import action_list
from parse_xml.actions.listeningmode_set import action_listeningmode_set
from parse_xml.actions.location import action_location
from parse_xml.actions.makegif import action_makegif
from parse_xml.actions.makeimagefrompdfpage import action_makeimagefrompdfpage
from parse_xml.actions.makeimagefromrichtext import action_makeimagefromrichtext
from parse_xml.actions.makepdf import action_makepdf
from parse_xml.actions.makevideofromgif import action_makevideofromgif
from parse_xml.actions.makezip import action_makezip
from parse_xml.actions.math import action_math
from parse_xml.actions.move_notes import action_move_notes
from parse_xml.actions.note_changesetting import action_note_changesetting
from parse_xml.actions.note_openaccount import action_note_openaccount
from parse_xml.actions.open_bookmark import action_open_bookmark
from parse_xml.actions.open_card import action_open_card
from parse_xml.actions.open_mailbox import action_open_mailbox
from parse_xml.actions.open_safariview import action_open_safariview
from parse_xml.actions.open_smartlist import action_open_smartlist
from parse_xml.actions.open_tabgroup import action_open_tabgroup
from parse_xml.actions.open_tag_notes import action_open_tag_notes
from parse_xml.actions.open_view_note import action_open_view_note
from parse_xml.actions.opencamera import action_open_camera
from parse_xml.actions.openin import action_openin
from parse_xml.actions.openpasswords import action_openpasswords
from parse_xml.actions.opentab import action_opentab
from parse_xml.actions.opentab_safari import action_opentab_safari
from parse_xml.actions.openurl import action_openurl
from parse_xml.actions.openworkflow import action_openworkflow
from parse_xml.actions.overlayimageonimage import action_overlayimageonimage
from parse_xml.actions.overlaytext import action_overlaytext
from parse_xml.actions.pause_timer import action_pause_timer
from parse_xml.actions.pausemusic import action_pausemusic
from parse_xml.actions.phonenumber import action_phonenumber
from parse_xml.actions.photo_createalbum import action_photo_createalbum
from parse_xml.actions.pingmyphone import action_pingmyphone
from parse_xml.actions.play_recording import action_play_recording
from parse_xml.actions.playpodcast import action_playpodcast
from parse_xml.actions.podcasts_subscribe import action_podcasts_subscribe
from parse_xml.actions.print import action_print
from parse_xml.actions.lockscreen import action_lockscreen
from parse_xml.actions.lowpowermode_set import action_lowpowermode_set
from parse_xml.actions.makespokenaudiofromtext import action_makespokenaudiofromtext
from parse_xml.actions.measurement_convert import action_measurement_convert
from parse_xml.actions.measurement_create import action_measurement_create
from parse_xml.actions.mobileslideshow_streamshareservice import action_mobileslideshow_streamshareservice
from parse_xml.actions.nightshift_set import action_nightshift_set
from parse_xml.actions.nothing import action_nothing
from parse_xml.actions.notification import action_notification
from parse_xml.actions.number import action_number
from parse_xml.actions.number_random import action_number_random
from parse_xml.actions.openxcallbackurl import action_openxcallbackurl
from parse_xml.actions.orientationlock_set import action_orientationlock_set
from parse_xml.actions.output import action_output
from parse_xml.actions.personalhotspot_password_get import action_personalhotspot_password_get
from parse_xml.actions.personalhotspot_set import action_personalhotspot_set
from parse_xml.actions.playmusic import action_playmusic
from parse_xml.actions.playsound import action_playsound
from parse_xml.actions.posters_get import action_posters_get
from parse_xml.actions.posters_switch import action_posters_switch
from parse_xml.actions.previewdocument import action_previewdocument
from parse_xml.actions.properties_appstore import action_properties_appstore
from parse_xml.actions.properties_articles import action_properties_articles
from parse_xml.actions.properties_calendarevents import action_properties_calendarevents
from parse_xml.actions.properties_contacts import action_properties_contacts
from parse_xml.actions.properties_eventattendees import action_properties_eventattendees
from parse_xml.actions.properties_files import action_properties_files
from parse_xml.actions.properties_health_quantity import action_properties_health_quantity
from parse_xml.actions.properties_images import action_properties_images
from parse_xml.actions.properties_itunes import action_properties_itunes
from parse_xml.actions.properties_locations import action_properties_location
from parse_xml.actions.properties_music import action_properties_music
from parse_xml.actions.properties_parkedcar import action_properties_parkedcar
from parse_xml.actions.properties_podcast import action_properties_podcast
from parse_xml.actions.properties_podcastshow import action_properties_podcasthow
from parse_xml.actions.properties_reminders import action_properties_reminders
from parse_xml.actions.properties_safariwebpage import action_properties_safariwebpage
from parse_xml.actions.readinglist import action_readinglist
from parse_xml.actions.reboot import action_reboot
from parse_xml.actions.recognize_music import action_recognize_music
from parse_xml.actions.recognized_sound import action_setting_recognized_sound
from parse_xml.actions.recordaudio import action_recordaudio
from parse_xml.actions.reminders_showlist import action_reminders_showlist
from parse_xml.actions.remove_tag_notes import action_remove_tag_notes
from parse_xml.actions.removeevents import action_removeevents
from parse_xml.actions.removefromalbum import action_removefromalbum
from parse_xml.actions.removereminders import action_removereminders
from parse_xml.actions.repeat_count import action_repeat_count
from parse_xml.actions.repeat_each import action_repeat_each
from parse_xml.actions.requestride import action_requestride
from parse_xml.actions.reset_cellulardata_statistics import action_reset_cellulardata_statistics
from parse_xml.actions.reset_stopwatch import action_reset_stopwatch
from parse_xml.actions.resize import action_resize
from parse_xml.actions.resume_timer import action_resume_timer
from parse_xml.actions.returntohomescreen import action_returntohomescreen
from parse_xml.actions.round import action_round
from parse_xml.actions.rss import action_rss
from parse_xml.actions.rss_extract import action_rss_extract
from parse_xml.actions.runextension import action_runextension
from parse_xml.actions.runjavascriptonwebpage import action_runjavascriptonwebpage
from parse_xml.actions.runsshscript import action_runsshscript
from parse_xml.actions.runworkflow import action_runworkflow
from parse_xml.actions.safari_closetab import action_safari_closetab
from parse_xml.actions.savetocameraroll import action_savetocameraroll
from parse_xml.actions.scan_doc import action_scan_doc
from parse_xml.actions.scanbarcode import action_scanbarcode
from parse_xml.actions.search_inreminder import action_search_inreminder
from parse_xml.actions.search_message_mail import action_search_message_mail
from parse_xml.actions.search_shortcut import action_search_shortcut
from parse_xml.actions.searchappstore import action_searchappstore
from parse_xml.actions.searchfile import action_searchfile
from parse_xml.actions.searchitunes import action_searchitunes
from parse_xml.actions.searchlocalbusinesses import action_searchlocalbusinesses
from parse_xml.actions.searchmaps import action_searchmap
from parse_xml.actions.searchpodcasts import action_searchpodcasts
from parse_xml.actions.searchweb import action_searchweb
from parse_xml.actions.seek import action_seek
from parse_xml.actions.select_recording import action_select_recording
from parse_xml.actions.selectcontacts import action_selectcontacts
from parse_xml.actions.selectemail import action_selectemail
from parse_xml.actions.selectphone import action_selectphone
from parse_xml.actions.selectphoto import action_selectphoto
from parse_xml.actions.sendemail import action_sendemail
from parse_xml.actions.sendmessage import action_sendmessage
from parse_xml.actions.set_calendar_focus import action_set_calendar_focus
from parse_xml.actions.set_contact import action_set_contact
from parse_xml.actions.set_default_cellular import action_set_default_cellular
from parse_xml.actions.set_schooltime import action_set_schooltime
from parse_xml.actions.set_theatermode import action_theatermode
from parse_xml.actions.set_waterlock import action_set_waterlock
from parse_xml.actions.setairdroppreceiving import action_setairdroppreceiving
from parse_xml.actions.setbrightness import action_setbrightness
from parse_xml.actions.setclipboard import action_setclipboard
from parse_xml.actions.setdataroaming import action_setdataroaming
from parse_xml.actions.setflashlight import action_setflashlight
from parse_xml.actions.setitemname import action_setitemname
from parse_xml.actions.setparkedcar import action_setparkedcar
from parse_xml.actions.setplaybackdestination import action_setplaybackdestination
from parse_xml.actions.setters_calendarevents import action_setters_calendarevents
from parse_xml.actions.setters_reminders import action_setters_reminders
from parse_xml.actions.setting_announcenotification import action_setting_announcenotification
from parse_xml.actions.setting_assistivetouch import action_setting_assistivetouch
from parse_xml.actions.setting_audiodescription import action_setting_audiodescription
from parse_xml.actions.setting_autoanswer import action_setting_autoanswer
from parse_xml.actions.setting_backgroundsound import action_setting_backgroundsound
from parse_xml.actions.setting_backgroundsounds import action_setting_backgroundsounds
from parse_xml.actions.setting_captionssdh import action_setting_captionssdh
from parse_xml.actions.setting_classicinvert import action_setting_classicinvert
from parse_xml.actions.setting_colorfilter import action_setting_colorfilter
from parse_xml.actions.setting_develpersetting import action_setting_develpersetting
from parse_xml.actions.setting_flashlight import action_setting_flashlight
from parse_xml.actions.setting_increasecontrast import action_setting_increasecontrast
from parse_xml.actions.setting_leftrightbalance import action_setting_leftrightbalance
from parse_xml.actions.setting_livecaption import action_setting_livecaption
from parse_xml.actions.setting_magnifier import action_setting_magnifier
from parse_xml.actions.setting_monoaudio import action_setting_monoaudio
from parse_xml.actions.setting_opens import action_setting_opens
from parse_xml.actions.setting_setbackgroundsound import action_setting_setbackgroundsound
from parse_xml.actions.setting_smartinvert import action_setting_smartinvert
from parse_xml.actions.setting_soundrecognition import action_setting_soundrecognition
from parse_xml.actions.setting_textsize import action_setting_textsize
from parse_xml.actions.setting_voiceover import action_setting_voiceover
from parse_xml.actions.setting_zoom import action_setting_zoom
from parse_xml.actions.setvalueforkey import action_setvalueforkey
from parse_xml.actions.setvariable import action_setvariable
from parse_xml.actions.openapp import action_openapp
from parse_xml.actions.setvoicedatamode import action_set_voice_data_mode
from parse_xml.actions.setvolumne import action_setvolume
from parse_xml.actions.share import action_share
from parse_xml.actions.show_notefolder import action_show_notefolder
from parse_xml.actions.show_quicknote import action_show_quicknote
from parse_xml.actions.showdefinition import action_showdefinition
from parse_xml.actions.showincalendar import action_showincalendar
from parse_xml.actions.showinstore import action_showinstore
from parse_xml.actions.shownote import action_shownote
from parse_xml.actions.showresult import action_showresult
from parse_xml.actions.showwebpage import action_showwebpage
from parse_xml.actions.skipback import action_skipback
from parse_xml.actions.skipforward import action_skipforward
from parse_xml.actions.slientcaller import action_slientcaller
from parse_xml.actions.speaktext import action_speaktext
from parse_xml.actions.splitpdf import action_splitpdf
from parse_xml.actions.start_guidedaccess import action_start_guidedaccess
from parse_xml.actions.statistics import action_statistics
from parse_xml.actions.stock_quote import action_stock_quote
from parse_xml.actions.stop_recording import action_stop_recording
from parse_xml.actions.stop_stopwatch import action_stop_stopwatch
from parse_xml.actions.takephoto import action_takephoto
from parse_xml.actions.takescreenshot import action_takescreenshot
from parse_xml.actions.takevideo import action_takevideo
from parse_xml.actions.text_combine import action_text_combine
from parse_xml.actions.text_match import action_text_match
from parse_xml.actions.text_match_getgruop import action_text_match_getgroup
from parse_xml.actions.text_replace import action_text_replace
from parse_xml.actions.text_split import action_text_split
from parse_xml.actions.text_changecase import action_text_changecase
from parse_xml.actions.text_translate import action_text_translate
from parse_xml.actions.timer_start import action_timer_start
from parse_xml.actions.toggle_cellularplan import action_toggle_cellular_plan
from parse_xml.actions.toggle_turn_alarm import action_toggle_turn_alarm
from parse_xml.actions.toggle_turnsilentmode import action_toggle_turnsilentmode
from parse_xml.actions.transcribe_audio_action import action_transcribe_audio
from parse_xml.actions.trim_whitespace import action_trim
from parse_xml.actions.trimvideo import action_trimvideo
from parse_xml.actions.truetone_set import action_truetone_set
from parse_xml.actions.turn_voicecontrol import action_turn_voicecontrol
from parse_xml.actions.unzip import action_unzip
from parse_xml.actions.url import action_url
from parse_xml.actions.url_expand import action_url_expand
from parse_xml.actions.url_getheaders import action_url_getheaders
from parse_xml.actions.urlencode import action_urlencode
from parse_xml.actions.user_activity_open import action_user_activity_open
from parse_xml.actions.venmo_pay import action_venmo_pay
from parse_xml.actions.venmo_request import action_venmo_request
from parse_xml.actions.vibrate import action_vibrate
from parse_xml.actions.viewresult import action_viewresult
from parse_xml.actions.vpn_set import action_vpn_set
from parse_xml.actions.waittoreturn import action_waittoreturn
from parse_xml.actions.wallpaper_set import action_wallpaper_set
from parse_xml.actions.weather_condition import action_weather_condition
from parse_xml.actions.weather_currentconditions import action_weather_currentconditions
from parse_xml.actions.weather_forecast import action_weather_forecast
from parse_xml.actions.weather_notification import action_weather_notification
from parse_xml.actions.weather_weatherintent import action_weather_weatherintent
from parse_xml.actions.whatsapp_openin import action_whatsapp_openin
from parse_xml.actions.whatsapp_send import action_whatsapp_send
from parse_xml.actions.wifi_set import action_wifi_set
from parse_xml.actions.createnote import action_createnote
from parse_xml.shortcut_uuid import uuid_tracker
# from shortcut_uuid import uuid_tracker, client_number
from parse_xml_output.parse_output_to_natural_language import parse_get_attachment


def check_validation(elem):
    if elem.tag != 'dict' or len(list(elem)) == 0:
        return False
    return True

def fine_key_from_dict(elem, key_name):
    for item in elem.findall('key'):
        if item.text == key_name:
            return True
    return False

def get_metadata(elem, keyname):
    elements = list(elem)
    for i in range(len(elements) - 1):
        if elements[i].tag == 'key' and elements[i].text == keyname:
            return extract_value(elements[i + 1])
    return None

def interpret_turn_toggle(elem):
    # Get the action
    action = extract_value_from_string_or_dict(elem, 'operation')
    if action is None:
        action = 'Turn'

    res = {'Action': action}

    # Get the state if action is 'Turn'
    state = 'On'
    if action == 'Turn':
        state_elem = get_elements_after_key(elem, 'OnValue', 'integer')
        if state_elem is not None:
            state_elem = state_elem[0].text
            if state_elem == '0':
                state = 'Off'
        res['State'] = state

    return res


def get_final_value(element):
    """
    Recursively traverses 'Value' keys in the element until it reaches the final element.

    Parameters:
    - element (ET.Element): The current XML element.

    Returns:
    - ET.Element: The final element after traversing all 'Value' keys, which could be a <dict> or <array>.
    """
    while True:
        # Look for a dict after 'Value' key
        value_elements = get_elements_after_key(element, 'Value', 'dict')
        if value_elements:
            element = value_elements[0]
        else:
            # If no dict is found, look for an array after the 'Value' key
            value_elements = get_elements_after_key(element, 'Value', 'array')
            if value_elements:
                return value_elements[0]  # Return the array directly
            else:
                break  # If neither dict nor array is found, stop recursion
    return element


def track_uuid(elem):
    uuid = detect_uuid(elem)
    return uuid


def extract_value_from_string_or_dict(elem, key_name):
    """
    Extracts the value from a string or a dictionary element after specific key.
    :return: a string or the value in a dictionary
    """
    if key_name is None:
        raise ValueError('Key name is None')
    if elem is None:
        raise ValueError('Element is None')
    result_elem = get_elements_after_key(elem, key_name, 'string')
    if result_elem is not None:
        result = extract_value(result_elem[0])
        return result
    else:
        result_elem = get_elements_after_key(elem, key_name, 'real')
        if result_elem is not None:
            result = extract_value(result_elem[0])
            return result
        result_elem = get_elements_after_key(elem, key_name, 'dict')
        if result_elem is not None:
            result = get_final_value(result_elem[0])
            result = get_attachments_by_range(result)
            return result
    return None


def append_data_interface(data_a, data_b, to_append, function, condition=None):
    if function == 'action_setvariable':
        if to_append is None:
            return {'data': {'variable name': data_a, 'input': data_b}, 'uuid': None}
        else:
            return {'data': {'variable name': data_a, 'input': data_b}, 'uuid': to_append}
    if function == 'action_conditional':
        if to_append is None:
            return {'data': {'input a': data_a, 'condition': condition, 'input b': data_b}, 'uuid': None}
        else:
            return {'data': {'input a': data_a, 'condition': condition, 'input b': data_b}, 'uuid': to_append}


def append_data(original, to_append):
    """
    Appends a string to a string by creating a dictionary,
    or merges a dictionary into another dictionary. Use to append UUID to output

    Parameters:
    - original (str or dict): The original data (string or dictionary).
    - to_append (str or dict): The data to append (string or dictionary).

    Returns:
    - dict: A dictionary that contains the combined strings or merged dictionaries.
    """
    if to_append is None:
        return {'data': original, 'uuid': None}
    else:
        # If both are strings, combine them into a dictionary
        return {'data': original, 'uuid': to_append}


def detect_uuid(elem):
    """
    Detects and tracks the UUID in an XML element.

    Parameters:
    - elem (ET.Element): The XML element to search for a UUID.
    - uuid_tracker (dict): A dictionary to track all detected UUIDs.

    Returns:
    - str: The UUID if found, otherwise None.
    """
    uuid_elem = get_elements_after_key(elem, 'UUID', 'string')
    if uuid_elem:
        uuid = uuid_elem[0].text
        if uuid not in uuid_tracker:
            uuid_tracker[uuid] = {}  # Initialize tracking for the new UUID
        return uuid
    return None


def detect_outuuid(elem):
    out_uuid_elem = get_elements_after_key(elem, 'OutputUUID', 'string')
    if out_uuid_elem:
        out_uuid = out_uuid_elem[0].text
        return out_uuid
    return None


def extract_value(elem):
    # This function extracts the value based on the type
    if isinstance(elem, list):  # Corrected list type check
        ans = []
        print("Processing a list element")
        for i in elem:
            ans.append(extract_value(i))
        return ans
    if elem.tag == 'string':
        if elem.text is not None:
            return elem.text
        else:
            return ''
    elif elem.tag == 'array':
        return [extract_value(child) for child in elem]
    elif elem.tag == 'integer':
        return int(elem.text)
    elif elem.tag == 'real':
        return float(elem.text)
    elif elem.tag == 'true':
        return True
    elif elem.tag == 'false':
        return False
    elif elem.tag == 'dict':
        child = list(elem)
        dic_res = {}
        if len(child) == 0:
            return {}
        else:
            out = get_elements_after_key(elem, 'OutputUUID', 'string')
            # Check for simple key-value pair with a 'string' key
            if len(child) == 2 and child[0].tag == 'key' and (child[1].tag == 'string' or child[1].tag == 'dict'):
                dic_res[child[0].text] = extract_value(child[1])
                if out is not None:
                    dic_res[child[0].text] = append_data(dic_res[child[0].text], out)
                return dic_res[child[0].text]
            else:
                i = 0
                while i < len(child):
                    if child[i].tag == 'key':
                        key = child[i].text
                        value = extract_value(child[i + 1])
                        dic_res[key] = value
                        i += 2
                    else:
                        i += 1
                if out is not None:
                    dic_res = append_data(dic_res, out)
                return dic_res
    elif elem.tag == 'date':
        return elem.text
    else:
        return None


def get_elements_after_key(element, key_name, element_type):
    """
    Finds elements of a specified type that come after a specific <key>.

    Parameters:
    - element (ET.Element): The current XML element (should be a <dict>).
    - key_name (str): The name of the key to search for.
    - element_type (str): The tag of the elements to look for after the key (default is 'dict').

    Returns:
    - List[ET.Element]: A list of elements of the specified type after the key, or None if not found.
    """
    elements = list(element)
    res_list = []
    # if tmp: print(00)
    for i in range(len(elements) - 1):
        # if tmp: print(11)
        if elements[i].tag == 'key' and elements[i].text == key_name:
            # if tmp: print(22)
            next_elem = elements[i + 1]
            if next_elem.tag == element_type:
                res_list.append(next_elem)
    if res_list:
        return res_list
    else:
        return None


def check_if_key_exist(element, key_name):
    elements = list(element)
    for i in range(len(elements) - 1):
        if elements[i].tag == 'key' and elements[i].text == key_name:
            return True
    return False


def parse_dict(elem):
    """
    Parses an XML dict element into a Python dictionary.

    Parameters:
    - elem (ET.Element): The XML dict element.

    Returns:
    - dict: A dictionary mapping keys to values (strings or elements).
    """
    elements = list(elem)
    result = {}
    i = 0
    while i < len(elements) - 1:
        key_elem = elements[i]
        value_elem = elements[i + 1]
        if key_elem.tag == 'key':
            key = key_elem.text
            if value_elem.tag == 'string':
                value = value_elem.text
            elif value_elem.tag in ('array', 'dict'):
                value = value_elem
            elif value_elem.tag in ('true', 'false'):
                if value_elem.tag == 'true':
                    value = True
                else:
                    value = False
            else:
                value = value_elem.text
            result[key] = value
            i += 2
        else:
            i += 1
    return result


def get_attachments_by_range(elem):
    # if elem.tag != 'dict':
    #     return None

    elements = list(elem)
    res = []
    current_index = 0
    # Ensure there are enough elements to check
    if len(elements) >= 2:
        # Check if the first key is 'attachmentsByRange'
        if elements[0].tag == 'key' and elements[0].text == 'attachmentsByRange':
            # The next element should be a <dict> containing the attachment data
            attachments_dict = elements[1]
            current_index = 2  # Index after attachmentsByRange and its value

            # Look for the 'string' key to get the text containing placeholders
            string_elem = None
            for i in range(current_index, len(elements), 2):
                if elements[i].tag == 'key' and elements[i].text == 'string':
                    string_elem = elements[i + 1]
                    current_index = i + 2
                    break

            if string_elem is not None and string_elem.tag == 'string' and string_elem.text is not None:
                string_text = string_elem.text
                # Process the 'attachmentsByRange' dict
                attachment_positions = []
                attachment_elements = list(attachments_dict)
                for j in range(0, len(attachment_elements), 2):
                    range_key_elem = attachment_elements[j]
                    attachment_value_elem = attachment_elements[j + 1]
                    if range_key_elem.tag == 'key' and attachment_value_elem.tag == 'dict':
                        range_str = range_key_elem.text  # e.g., '{0, 1}'
                        start_end = range_str.strip('{}').split(',')
                        if len(start_end) == 2:
                            start = int(start_end[0])
                            length = int(start_end[1])
                            end = start + length
                            # Process attachment_value_elem to get attachment info
                            attachment_info = process_attachment(attachment_value_elem)
                            # Store attachment position and info
                            attachment_positions.append((start, end, attachment_info))

                # Now reconstruct the text with attachments in correct positions
                output_list = []
                last_index = 0
                attachment_positions.sort()
                for start, end, attachment_info in attachment_positions:
                    # Add text before attachment
                    if start > last_index:
                        text_segment = string_text[last_index:start].replace('￼', '')
                        if text_segment:
                            output_list.append(text_segment)
                    # Add attachment
                    output_list.append(attachment_info)
                    last_index = end
                # Add any remaining text after last attachment
                if last_index < len(string_text):
                    text_segment = string_text[last_index:].replace('￼', '')
                    if text_segment:
                        output_list.append(text_segment)
                res.extend(output_list)
                return res
            else:
                # If 'string' not found or empty, process attachments without string
                # Process the 'attachmentsByRange' dict
                current = get_all_dicts_at_depth_n(attachments_dict, 1)
                if len(current) == 0:
                    pass  # No attachments to process
                else:
                    for item in current:
                        attachment_info = process_attachment(item)
                        res.append(attachment_info)
                # Since there's no string, we don't need to process text segments
                return res
        else:
            # Existing code to handle 'Aggrandizements' and other keys
            # Parse the dict into a Python dict
            elem_dict = parse_dict(elem)

            # Initialize variables
            property_name = None
            output_name = None
            outuuid = None

            # Check for 'Aggrandizements'
            if 'Aggrandizements' in elem_dict:
                aggrandizements = elem_dict['Aggrandizements']
                # 'Aggrandizements' is an array element
                # Get the list of dicts in the array
                aggrandizements_list = list(aggrandizements)
                for aggrandizement in aggrandizements_list:
                    if aggrandizement.tag == 'dict':
                        # Parse the dict to get 'PropertyName' or 'DictionaryKey'
                        aggrandizement_dict = parse_dict(aggrandizement)
                        if 'PropertyName' in aggrandizement_dict:
                            property_name = aggrandizement_dict['PropertyName']
                            break  # Assume only one is needed
                        elif 'DictionaryKey' in aggrandizement_dict:
                            property_name = aggrandizement_dict['DictionaryKey']
                            break
                # If no property_name found in Aggrandizements, check for 'Type' == 'ExtensionInput'
                if not property_name:
                    if 'Type' in elem_dict and elem_dict['Type'] == 'ExtensionInput':
                        property_name = "Shortcut Input"
            else:
                # If 'Aggrandizements' is not in elem_dict, check if 'Type' == 'ExtensionInput'
                if 'Type' in elem_dict and elem_dict['Type'] == 'ExtensionInput':
                    property_name = "Shortcut Input"
                elif 'Value' in elem_dict:
                    return elem_dict['Value']


            # Check for 'OutputName'
            if 'OutputName' in elem_dict:
                output_name = elem_dict['OutputName']

            # Check for 'OutputUUID'
            if 'OutputUUID' in elem_dict:
                outuuid = elem_dict['OutputUUID']
            else:
                outuuid = detect_outuuid(elem)  # In case OutputUUID is nested

            # Construct data
            if property_name and output_name:
                data = f"{property_name} or {output_name}"
            elif property_name:
                data = property_name
            elif output_name:
                data = output_name
            else:
                # Attempt to extract specific fields from elem_dict
                data = None
                if 'VariableName' in elem_dict:
                    data = elem_dict['VariableName']
                elif 'DictionaryKey' in elem_dict:
                    data = elem_dict['DictionaryKey']
                elif 'Type' in elem_dict:
                    data = elem_dict['Type']
                # If none of the above, data remains None

            if data:
                res.append(append_data(f"{data} (attachment)", outuuid))
                return res
    value = extract_value(elem)
    return value

def process_attachment(attachment_elem):
    # attachment_elem is a <dict> element
    attachment_dict = parse_dict(attachment_elem)
    out = detect_outuuid(attachment_elem)
    type_elem = get_elements_after_key(attachment_elem, 'Type', 'string')
    if type_elem:
        type_text = type_elem[0].text
        if type_text == 'Variable':
            # If the Type is 'Variable', get the 'VariableName'
            variable_name_elem = get_elements_after_key(attachment_elem, 'VariableName', 'string')
            if variable_name_elem:
                variable_name = variable_name_elem[0].text
                if out is not None:
                    return append_data(f"{variable_name} (attachment)", out)
                else:
                    return f"{variable_name} (attachment)"
            else:
                if out is not None:
                    return append_data("Unnamed Variable (attachment)", out)
                else:
                    return "Unnamed Variable (attachment)"
        elif type_text == 'ActionOutput':
            # If the Type is 'ActionOutput', get the 'OutputName'
            output_name_elem = get_elements_after_key(attachment_elem, 'OutputName', 'string')
            if output_name_elem:
                output_name = output_name_elem[0].text
                if out is not None:
                    return append_data(f"{output_name} (attachment)", out)
                else:
                    return f"{output_name} (attachment)"
            else:
                if out is not None:
                    return append_data(f"{type_text} (attachment)", out)
                else:
                    return f"{type_text} (attachment)"
        else:
            # For other types, return the type text
            if out is not None:
                return append_data(f"{type_text} (attachment)", out)
            else:
                return f"{type_text} (attachment)"
    else:
        # If 'Type' is not found, attempt to get 'OutputName'
        output_name_elem = get_elements_after_key(attachment_elem, 'OutputName', 'string')
        if output_name_elem:
            output_name = output_name_elem[0].text
            if out is not None:
                return append_data(f"{output_name} (attachment)", out)
            else:
                return f"{output_name} (attachment)"
        else:
            return "Unknown Attachment"


def get_all_dicts_at_depth_n(element, n):
    """
    Retrieves all <dict> elements at depth n within a given element using depth-first traversal.

    Parameters:
    - element (ET.Element): The current XML element.
    - n (int): The depth level (0-based index) at which to retrieve <dict> elements.

    Returns:
    - List[ET.Element]: A list of all <dict> elements at depth n.
    """
    result = []

    def dfs(current_element, current_depth):
        if current_depth == n and current_element.tag == 'dict':
            result.append(current_element)
        for child in current_element:
            dfs(child, current_depth + 1)

    dfs(element, 0)
    return result

def unpack_file_dict(elem):
    """
    Unpacks a dictionary element into a file name.

    Parameters:
    - elem (ET.Element): The XML file dictionary element.

    Returns:
    - string: name of the file
    """
    if elem.tag != 'dict':
        raise ValueError('Element is not a dictionary')
    elements = list(elem)
    result = ''
    for i in range(len(elements) - 1):
        key_elem = elements[i]
        value_elem = elements[i + 1]
        if key_elem.tag == 'key':
            key = key_elem.text
            if key == 'filename':
                if value_elem.tag == 'string':
                    result = value_elem.text
                else:
                    raise ValueError('WFSerializationType is not a string')
    return result

def parse_location_wfinput(elem):
    if elem is None:
        return None
    if elem[0].text == 'Value':
        elem = get_final_value(elem)
        return get_attachments_by_range(elem)
    if elem[0].text == 'isCurrentLocation':
        if elem[1].tag == 'true':
            return 'Current Location'
    if elem is None or (elem[0].text != 'placemark'):
        return None
    elem = get_all_dicts_at_depth_n(elem, 2)
    items = get_elements_after_key(elem[0], 'FormattedAddressLines', 'array')
    if items is None:
        return 'N/A'
        # raise ValueError('Invalid location input')
    res  = ' '.join(item.text for item in items[0])
    return res

def parse_app_input(elem):
    # get the app name, string after key Name
    app_name = get_elements_after_key(elem, 'Name', 'string')
    if app_name is None:
        return None
    return app_name[0].text

def helper_parse_file_input(elem):
    if elem[1].tag == 'string':
        display_name = extract_value(elem[1])
    else:
        raise ValueError('Invalid file input1')
    # get file location
    location = get_elements_after_key(elem, 'fileLocation', 'dict')
    if location is None:
        raise ValueError('Invalid file input2')
    location = get_elements_after_key(location[0], 'relativeSubpath', 'string')
    if location is None:
        raise ValueError('Invalid file input3')
    location_str = extract_value(location[0])
    return f'{display_name} ({location_str})'

def parse_file_input(elem, input_or_file):
    if input_or_file == 'WFFile' or input_or_file == 'WFFolder':
        if elem.tag == 'array':
            file_list = []
            list_dict = list(elem)
            for item in list_dict:
                file_list.append(helper_parse_file_input(item))
            return file_list
    if elem[0].text == 'Value':
        elem = get_final_value(elem)
        return get_attachments_by_range(elem)
    elif elem[0].text == 'displayName':
        return helper_parse_file_input(elem)
    else:
        return None




def parse_contact_info(elem, client_number):
    if elem is None: return None
    content_list = []
    recipients_dic = get_final_value(elem)
    data_dict = get_elements_after_key(recipients_dic, 'WFContactFieldValues', 'array')
    if data_dict is None:
        return 1
    for item in data_dict[0]:
        if client_number == 411 or client_number == 784 or len(item) == 0:
            content_list.append(extract_value(item))
            continue
        if item[0].tag == 'key' and item[0].text == 'EntryType':
            res_dict = get_elements_after_key(item, 'SerializedEntry', 'dict')
            if res_dict is None:
                content_list.append('')
                continue
            final_dict = get_elements_after_key(res_dict[0], 'link.contentkit.phonenumber', 'string')
            if final_dict is None:
                final_dict = get_elements_after_key(res_dict[0], 'link.contentkit.emailaddress', 'string')
            if final_dict is None:
                raise ValueError('No phone number found while parsing the send message action')
            content_list.append(final_dict[0].text)
        elif item[0].tag == 'key' and item[0].text == 'WFContactData':
            # If it's a contact, the first key is 'WFContactData'
            coded_data = get_elements_after_key(item, 'WFContactData', 'data')
            if coded_data is None:
                raise ValueError('No contact data found while parsing the send message action')
            # Assuming coded_data[0].text contains the Base64 encoded string
            encoded_data = coded_data[0].text  # This is already a string
            contact_data_bytes = base64.b64decode(encoded_data)  # Decodes to bytes

            # If the original data was text, convert bytes to string
            contact_data_str = contact_data_bytes.decode('utf-8')
            content_list.append(contact_data_str)
        elif item[0].tag == 'key' and item[0].text == 'WFIsINPerson':
            # Extract 'personHandle' -> 'value'
            person_handle_dict = get_elements_after_key(item, 'personHandle', 'dict')
            if person_handle_dict is None:
                raise ValueError('No personHandle found while parsing the send message action')
            value_elem = get_elements_after_key(person_handle_dict[0], 'value', 'string')
            if value_elem is None:
                raise ValueError('No value found in personHandle while parsing the send message action')
            contact_value = value_elem[0].text

            # Extract 'displayName'
            display_name_elem = get_elements_after_key(item, 'displayName', 'string')
            if display_name_elem is not None:
                display_name = display_name_elem[0].text
            else:
                display_name = None  # or set a default value

            # Extract 'contactIdentifier'
            contact_identifier_elem = get_elements_after_key(item, 'contactIdentifier', 'string')
            if contact_identifier_elem is not None:
                contact_identifier = contact_identifier_elem[0].text
            else:
                contact_identifier = None  # or set a default value

            # Extract 'nameComponents' if available
            name_components_dict = get_elements_after_key(item, 'nameComponents', 'dict')
            name_components = {}
            if name_components_dict is not None:
                # List of possible name components
                components = ['familyName', 'givenName', 'middleName', 'namePrefix', 'nameSuffix', 'nickname']
                for component in components:
                    component_elem = get_elements_after_key(name_components_dict[0], component, 'string')
                    if component_elem is not None:
                        name_components[component] = component_elem[0].text
                # Handle 'phoneticRepresentation' if it exists
                phonetic_dict = get_elements_after_key(name_components_dict[0], 'phoneticRepresentation',
                                                              'dict')
                if phonetic_dict is not None:
                    phonetic_components = {}
                    for component in components:
                        phonetic_elem = get_elements_after_key(phonetic_dict[0], component, 'string')
                        if phonetic_elem is not None:
                            phonetic_components[component] = phonetic_elem[0].text
                    name_components['phoneticRepresentation'] = phonetic_components
            else:
                name_components = None  # or keep it as an empty dictionary

            # Create metadata dictionary
            metadata = {
                'contactValue': contact_value,
                'displayName': display_name,
                'contactIdentifier': contact_identifier,
                'nameComponents': name_components
            }

            # Append metadata to content_list
            content_list.append(metadata)
        else:
            raise ValueError('Invalid contact data while parsing the send message action')
    return content_list

def list_to_str(elem):
    if type(elem) is list:
        return parse_get_attachment(elem)
    return elem

def parse_note_helper(elem):
    # Get the identifier
    identifier = get_elements_after_key(elem, 'identifier', 'string')
    if identifier is None:
        raise ValueError('Invalid note input')
    # Get the title
    title = get_elements_after_key(elem, 'title', 'dict')
    title = get_elements_after_key(title[0], 'key', 'string')
    return {'identifier': identifier[0].text, 'title': title[0].text}

def parse_note(elem, type='dict'):
    if elem is None: return None
    if elem[0].tag == 'key' and elem[0].text == 'Value':
        elem = get_final_value(elem)
        return get_attachments_by_range(elem)
    if type == 'dict':
        return parse_note_helper(elem)
    elif type == 'array':
        res_list = []
        for item in elem:
            res_list.append(parse_note_helper(item))
        return res_list



def track_custom_name(elem):
    custom_output_name = get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        return custom_output_name[0].text
    return None


function_map = {
    'is.workflow.actions.dictionary': action_dictionary,
    'is.workflow.actions.comment': action_comment,
    'is.workflow.actions.gettext': action_gettext,
    'is.workflow.actions.choosefromlist': action_choosefromlist,
    'is.workflow.actions.conditional': action_conditional,
    'is.workflow.actions.setvariable': action_setvariable,
    'is.workflow.actions.openapp': action_openapp,
    'is.workflow.actions.sendmessage': action_sendmessage,
    'is.workflow.actions.playmusic': action_playmusic,
    'is.workflow.actions.showresult': action_showresult,
    'is.workflow.actions.alert': action_alert,
    'is.workflow.actions.getlastphoto': action_getlastphoto,
    'is.workflow.actions.image.resize': action_resize,
    'is.workflow.actions.image.convert': action_image_convert,
    'is.workflow.actions.base64encode': action_base64encode,
    'is.workflow.actions.detect.text': action_detect_text,
    'is.workflow.actions.text.split': action_text_split,
    'is.workflow.actions.repeat.each': action_repeat_each,
    'com.apple.mobiletimer-framework.MobileTimerIntents.MTCreateAlarmIntent': action_create_alarm,
    'com.apple.mobiletimer.DeleteAlarmIntent': action_delete_alarm,
    'is.workflow.actions.ask': action_ask,
    'is.workflow.actions.count': action_count,
    'is.workflow.actions.choosefrommenu': action_choosefrommenu,
    'is.workflow.actions.repeat.count': action_repeat_count,
    'is.workflow.actions.delay': action_delay,
    'is.workflow.actions.getvariable': action_getvariable,
    'is.workflow.actions.appendvariable': action_appendvariable,
    'is.workflow.actions.list': action_list,
    'is.workflow.actions.getitemfromlist':action_getitemfromlist,
    'is.workflow.actions.getvalueforkey': action_getvalueforkey,
    'is.workflow.actions.setvalueforkey': action_setvalueforkey,
    'is.workflow.actions.detect.dictionary': action_detect_dictionary,
    'is.workflow.actions.number': action_number,
    'is.workflow.actions.number.random': action_number_random,
    'is.workflow.actions.round': action_round,
    'is.workflow.actions.statistics': action_statistics,
    'is.workflow.actions.measurement.create': action_measurement_create,
    'is.workflow.actions.measurement.convert': action_measurement_convert,
    'is.workflow.actions.date': action_date,
    'is.workflow.actions.format.date': action_format_date,
    'is.workflow.actions.adjustdate': action_adjustdate,
    'is.workflow.actions.gettimebetweendates': action_gettimebetweendates,
    'is.workflow.actions.detect.date': action_detect_date,
    'is.workflow.actions.converttimezone': action_converttimezone,
    'is.workflow.actions.getnameofemoji': action_getnameofemoji,
    'is.workflow.actions.showdefinition': action_showdefinition,
    'is.workflow.actions.text.changecase': action_text_changecase,
    'is.workflow.actions.text.combine': action_text_combine,
    'is.workflow.actions.text.replace': action_text_replace,
    'is.workflow.actions.text.match': action_text_match,
    'is.workflow.actions.correctspelling': action_correctspelling,
    'is.workflow.actions.text.match.getgroup': action_text_match_getgroup,
    'is.workflow.actions.dictatetext': action_dictatetext,
    'com.apple.ShortcutsActions.TranscribeAudioAction': action_transcribe_audio,
    'is.workflow.actions.speaktext': action_speaktext,
    'is.workflow.actions.makespokenaudiofromtext': action_makespokenaudiofromtext,
    'is.workflow.actions.detectlanguage': action_detectlanguage,
    'is.workflow.actions.text.translate': action_text_translate,
    'is.workflow.actions.getitemname': action_getitemname,
    'is.workflow.actions.setitemname': action_setitemname,
    'is.workflow.actions.getitemtype': action_getitemtype,
    'is.workflow.actions.getmyworkflows': action_getmyworkflows,
    'is.workflow.actions.viewresult': action_viewresult,
    'is.workflow.actions.previewdocument': action_previewdocument,
    'is.workflow.actions.runworkflow': action_runworkflow,
    'is.workflow.actions.getonscreencontent': action_getonscreencontent,
    'is.workflow.actions.hash': action_hash,
    'is.workflow.actions.urlencode': action_urlencode,
    'is.workflow.actions.exit': action_exit,
    'is.workflow.actions.openxcallbackurl': action_openxcallbackurl,
    'is.workflow.actions.runsshscript': action_runsshscript,
    'is.workflow.actions.waittoreturn': action_waittoreturn,
    'is.workflow.actions.output': action_output,
    'is.workflow.actions.format.filesize': action_format_filesize,
    'is.workflow.actions.flashlight': action_flashlight,
    'is.workflow.actions.dnd.set': action_dnd_set,
    'is.workflow.actions.dnd.getfocus': action_dnd_getfocus,
    'is.workflow.actions.nothing': action_nothing,
    'is.workflow.actions.bluetooth.set': action_bluetooth_set,
    'is.workflow.actions.wifi.set': action_wifi_set,
    'is.workflow.actions.airplanemode.set': action_airplanemode_set,
    'is.workflow.actions.reboot': action_reboot,
    'is.workflow.actions.lowpowermode.set': action_lowpowermode_set,
    'is.workflow.actions.appearance': action_appearance,
    'is.workflow.actions.setairdropreceiving': action_setairdroppreceiving,
    'is.workflow.actions.vpn.set': action_vpn_set,
    'is.workflow.actions.personalhotspot.set': action_personalhotspot_set,
    'is.workflow.actions.cellulardata.set': action_cellulardata_set,
    'is.workflow.actions.lockscreen': action_lockscreen,
    'is.workflow.actions.nightshift.set': action_nightshift_set,
    'is.workflow.actions.truetone.set': action_truetone_set,
    'is.workflow.actions.setbrightness': action_setbrightness,
    'is.workflow.actions.orientationlock.set': action_orientationlock_set,
    'is.workflow.actions.returntohomescreen': action_returntohomescreen,
    'is.workflow.actions.takephoto': action_takephoto,
    'is.workflow.actions.takevideo': action_takevideo,
    'is.workflow.actions.recordaudio': action_recordaudio,
    'is.workflow.actions.takescreenshot': action_takescreenshot,
    'is.workflow.actions.getdevicedetails': action_getdevicedetails,
    'is.workflow.actions.getbatterylevel': action_getbatterylevel,
    'com.apple.ShortcutsActions.GetOrientationAction': action_getorientation,
    'com.apple.ShortcutsActions.GetPhysicalActivity': action_getphysicalactivity,
    'is.workflow.actions.setclipboard': action_setclipboard,
    'is.workflow.actions.playsound': action_playsound,
    'is.workflow.actions.notification': action_notification,
    'is.workflow.actions.getclipboard': action_getclipboard,
    'is.workflow.actions.vibrate': action_vibrate,
    'is.workflow.actions.getipaddress': action_getipaddress,
    'is.workflow.actions.getwifi': action_getwifi,
    'is.workflow.actions.personalhotspot.password.get': action_personalhotspot_password_get,
    'com.apple.ShortcutsActions.ResetCellularDataStatisticsAction': action_reset_cellulardata_statistics,
    'is.workflow.actions.wallpaper.set': action_wallpaper_set,
    'is.workflow.actions.posters.get': action_posters_get,
    'is.workflow.actions.getcurrentlocation': action_getcurrentlocation,
    'is.workflow.actions.searchlocalbusinesses': action_searchlocalbusinesses,
    'is.workflow.actions.posters.switch': action_posters_switch,
    'is.workflow.actions.getdirections': action_getdirections,
    'is.workflow.actions.searchmaps': action_searchmap,
    'is.workflow.actions.filter.locations': action_filter_locations,
    'is.workflow.actions.ride.requestride': action_requestride,
    'is.workflow.actions.properties.locations': action_properties_location,
    'is.workflow.actions.location': action_location,
    'is.workflow.actions.getmapslink': action_getmapslink,
    'is.workflow.actions.address': action_address,
    'is.workflow.actions.detect.address': action_detect_address,
    'is.workflow.actions.getdistance': action_getdistance,
    'is.workflow.actions.gethalfwaypoint': action_gethalfwaypoint,
    'is.workflow.actions.gettraveltime': action_gettraveltime,
    'is.workflow.actions.getparkedcarlocation': action_getparkedcarlocation,
    'is.workflow.actions.properties.parkedcar': action_properties_parkedcar,
    'is.workflow.actions.setparkedcar': action_setparkedcar,
    'is.workflow.actions.share': action_share,
    'is.workflow.actions.runextension': action_runextension,
    'is.workflow.actions.sendemail': action_sendemail,
    'is.workflow.actions.airdropdocument': action_airdropdocument,
    'com.apple.mobileslideshow.StreamShareService': action_mobileslideshow_streamshareservice,
    'is.workflow.actions.generatebarcode': action_generatebarcode,
    'is.workflow.actions.scanbarcode': action_scanbarcode,
    'is.workflow.actions.print': action_print,
    'is.workflow.actions.avairyeditphoto': action_avairyeditphoto,
    'is.workflow.actions.makepdf': action_makepdf,
    'is.workflow.actions.compresspdf': action_compresspdf,
    'is.workflow.actions.splitpdf': action_splitpdf,
    'is.workflow.actions.gettextfrompdf': action_gettextfrompdf,
    'is.workflow.actions.file': action_file,
    'is.workflow.actions.file.select': action_file_select,
    'is.workflow.actions.file.move': action_file_move,
    'is.workflow.actions.file.rename': action_file_rename,
    'is.workflow.actions.documentpicker.save': action_documentpicker_save,
    'is.workflow.actions.file.delete': action_file_delete,
    'is.workflow.actions.file.getlink': action_file_getlink,
    'is.workflow.actions.file.createfolder': action_file_createfolder,
    'is.workflow.actions.file.getfoldercontents': action_file_getfoldercontents,
    'is.workflow.actions.openin': action_openin,
    'is.workflow.actions.file.append': action_file_append,
    'is.workflow.actions.makezip': action_makezip,
    'is.workflow.actions.unzip': action_unzip,
    'is.workflow.actions.documentpicker.open': action_documentpicker_open,
    'is.workflow.actions.properties.files': action_properties_files,
    'is.workflow.actions.filter.files': action_filter_files,
    'is.workflow.actions.gethtmlfromrichtext': action_gethtmlfromrichtext,
    'is.workflow.actions.getmarkdownfromrichtext': action_getmarkdownfromrichtext,
    'is.workflow.actions.getrichtextfrommarkdown': action_getrichtextfrommarkdown,
    'is.workflow.actions.getrichtextfromhtml': action_getrichtextfromhtml,
    'is.workflow.actions.searchweb': action_searchweb,
    'is.workflow.actions.openurl': action_openurl,
    'is.workflow.actions.giphy': action_giphy,
    'is.workflow.actions.showwebpage': action_showwebpage,
    'is.workflow.actions.readinglist': action_readinglist,
    'is.workflow.actions.rss': action_rss,
    'is.workflow.actions.rss.extract': action_rss_extract,
    'is.workflow.actions.filter.articles': action_filter_articles,
    'is.workflow.actions.properties.articles': action_properties_articles,
    'is.workflow.actions.url': action_url,
    'is.workflow.actions.detect.link': action_detect_link,
    'is.workflow.actions.geturlcomponent': action_geturlcomponent,
    'is.workflow.actions.url.expand': action_url_expand,
    'is.workflow.actions.downloadurl': action_downloadurl,
    'is.workflow.actions.url.getheaders': action_url_getheaders,
    'is.workflow.actions.getwebpagecontents': action_getwebpagecontents,
    'is.workflow.actions.properties.safariwebpage': action_properties_safariwebpage,
    'is.workflow.actions.runjavascriptonwebpage': action_runjavascriptonwebpage,
    'is.workflow.actions.filter.images': action_filter_images,
    'is.workflow.actions.properties.images': action_properties_images,
    'is.workflow.actions.detect.images': action_detect_images,
    'is.workflow.actions.makeimagefromrichtext': action_makeimagefromrichtext,
    'is.workflow.actions.makeimagefrompdfpage': action_makeimagefrompdfpage,
    'is.workflow.actions.extracttextfromimage': action_extracttextfromimage,
    'is.workflow.actions.image.combine': action_image_combine,
    'is.workflow.actions.image.crop': action_image_crop,
    'is.workflow.actions.image.flip': action_image_flip,
    'is.workflow.actions.image.mask': action_image_mask,
    'is.workflow.actions.overlayimageonimage': action_overlayimageonimage,
    'is.workflow.actions.overlaytext': action_overlaytext,
    'is.workflow.actions.image.rotate': action_image_rotate,
    'is.workflow.actions.image.removebackground': action_image_removebackground,
    'is.workflow.actions.makegif': action_makegif,
    'is.workflow.actions.makevideofromgif': action_makevideofromgif,
    'is.workflow.actions.addframetogif': action_addframetogif,
    'is.workflow.actions.getframesfromimage': action_getframesfromimage,
    'is.workflow.actions.selectphoto': action_selectphoto,
    'is.workflow.actions.filter.photos': action_filter_photos,
    'is.workflow.actions.getlastvideo': action_getlastvideo,
    'is.workflow.actions.getlastscreenshot': action_getlastscreenshot,
    'is.workflow.actions.getlatestbursts': action_getlatestburst,
    'is.workflow.actions.getlatestlivephotos': action_getlatestlivephotos,
    'is.workflow.actions.getlatestphotoimport': action_getlatestphotoimport,
    'is.workflow.actions.removefromalbum': action_removefromalbum,
    'is.workflow.actions.deletephotos': action_deletephoto,
    'is.workflow.actions.savetocameraroll': action_savetocameraroll,
    'is.workflow.actions.encodemedia': action_encodemedia,
    'is.workflow.actions.trimvideo': action_trimvideo,
    'is.workflow.actions.setvolume': action_setvolume,
    'is.workflow.actions.pausemusic': action_pausemusic,
    'is.workflow.actions.seek': action_seek,
    'is.workflow.actions.skipback': action_skipback,
    'is.workflow.actions.skipforward': action_skipforward,
    'is.workflow.actions.listeningmode.set': action_listeningmode_set,
    'is.workflow.actions.handoffplayback': action_handoffplayback,
    'is.workflow.actions.setplaybackdestination': action_setplaybackdestination,
    'is.workflow.actions.exportsong': action_exportsong,
    'is.workflow.actions.filter.music': action_filter_music,
    'is.workflow.actions.addmusictoupnext': action_addmusictoupnext,
    'is.workflow.actions.clearupnext': action_clearupnext,
    'is.workflow.actions.getcurrentsong': action_getcurrentsong,
    'is.workflow.actions.properties.music': action_properties_music,
    'is.workflow.actions.addtoplaylist': action_addtoplaylist,
    'is.workflow.actions.createplaylist': action_createplaylist,
    'is.workflow.actions.get.playlist': action_get_playlist,
    'is.workflow.actions.searchpodcasts': action_searchpodcasts,
    'is.workflow.actions.podcasts.subscribe': action_podcasts_subscribe,
    'is.workflow.actions.playpodcast': action_playpodcast,
    'is.workflow.actions.getepisodesforpodcast': action_getepisodesforpodcast,
    'is.workflow.actions.getpodcastsfromlibrary': action_getpodcastsfromlibrary,
    'is.workflow.actions.properties.podcastshow': action_properties_podcasthow,
    'is.workflow.actions.properties.podcast': action_properties_podcast,
    'is.workflow.actions.searchappstore': action_searchappstore,
    'is.workflow.actions.properties.appstore': action_properties_appstore,
    'is.workflow.actions.filter.health.quantity': action_filter_health_quality,
    'is.workflow.actions.health.quantity.log': action_health_quantity_log,
    'is.workflow.actions.health.workout.log': action_health_workout_log,
    'is.workflow.actions.properties.health.quantity': action_properties_health_quantity,
    'is.workflow.actions.addnewcalendar': action_addnewcalendar,
    'is.workflow.actions.addnewevent': action_addnewevent,
    'is.workflow.actions.setters.calendarevents': action_setters_calendarevents,
    'is.workflow.actions.filter.eventattendees': action_filter_eventattendees,
    'is.workflow.actions.properties.calendarevents': action_properties_calendarevents,
    'is.workflow.actions.properties.eventattendees': action_properties_eventattendees,
    'is.workflow.actions.getupcomingevents': action_getupcomingevents,
    'is.workflow.actions.showincalendar': action_showincalendar,
    'is.workflow.actions.removeevents': action_removeevents,
    'com.apple.mobilecal.SetCalendarFocusConfiguration': action_set_calendar_focus,
    'is.workflow.actions.filter.calendarevents': action_filter_calendarevents,
    'com.apple.mobiletimer-framework.MobileTimerIntents.MTGetAlarmsIntent': action_filter_alarms,
    'com.apple.mobiletimer.EditSleepAlarmIntent': action_edit_alarm,
    'com.apple.mobiletimer-framework.MobileTimerIntents.MTToggleAlarmIntent': action_toggle_turn_alarm,
    'com.apple.mobiletimer.LapStopwatchIntent': action_lap_stopwatch,
    'com.apple.mobiletimer.ResetStopwatchIntent': action_reset_stopwatch,
    'com.apple.mobiletimer.StartStopwatchIntent': action_start_stopwatch,
    'com.apple.mobiletimer.StopStopwatchIntent': action_stop_stopwatch,
    'com.apple.mobiletimer.OpenTab': action_opentab,
    'com.apple.mobiletimer.CancelTimerIntent': action_cancel_timer,
    'com.apple.mobiletimer.GetCurrentTimerDetailsIntent': action_get_detail_timer,
    'com.apple.mobiletimer.PauseTimerIntent': action_pause_timer,
    'com.apple.mobiletimer.ResumeTimerIntent': action_resume_timer,
    'is.workflow.actions.timer.start': action_timer_start,
    'com.apple.facetime.facetime': action_facetime,
    'is.workflow.actions.homeaccessory': action_homeaccessory,
    'is.workflow.actions.gethomeaccessorystate': action_gethomeaccessory,
    'is.workflow.actions.intercom': action_intercom,
    'is.workflow.actions.email': action_email,
    'is.workflow.actions.detect.emailaddress': action_detect_emailaddress,
    'com.apple.mobilemail.OpenMailboxEntityAction': action_open_mailbox,
    'com.apple.mobilemail.SearchMessagesAction': action_search_message_mail,
    'is.workflow.actions.selectemail': action_selectemail,
    'com.apple.mobilemail.MailFocusConfigurationAction': action_change_focus_mail,
    'is.workflow.actions.useractivity.open': action_user_activity_open,
    'is.workflow.actions.appendnote': action_appendnote,
    'com.apple.mobilenotes.SharingExtension': action_createnote,
    'com.apple.mobilenotes.DeleteNotesLinkAction': action_deletenote,
    'is.workflow.actions.filter.notes': action_filter_notes,
    'is.workflow.actions.shownote': action_shownote,
    'com.apple.mobilenotes.PinNotesLinkAction': action_add_to_pinnote,
    'com.apple.mobilenotes.ICNotesFolderIntent': action_show_notefolder,
    'com.apple.mobilenotes.ShowQuickNoteIntent': action_show_quicknote,
    'com.apple.mobilenotes.OpenAccountLinkAction': action_note_openaccount,
    'com.apple.mobilenotes.ChangeSettingLinkAction': action_note_changesetting,
    'com.apple.mobilenotes.OpenAppLocationLinkAction': action_open_view_note,
    'com.apple.mobilenotes.CreateFolderLinkAction': action_create_note_folder,
    'com.apple.mobilenotes.DeleteFoldersLinkAction': action_delete_note_folder,
    'com.apple.mobilenotes.MoveNotesToFolderLinkAction': action_move_notes,
    'com.apple.mobilenotes.AddTagsToNotesLinkAction': action_add_tag_notes,
    'com.apple.mobilenotes.DeleteTagsLinkAction': action_delete_tag_notes,
    'com.apple.mobilenotes.CreateTagLinkAction': action_create_tag_notes,
    'com.apple.mobilenotes.OpenTagLinkAction': action_open_tag_notes,
    'com.apple.mobilenotes.RemoveTagsFromNotesLinkAction': action_remove_tag_notes,
    'is.workflow.actions.weather.currentconditions': action_weather_currentconditions,
    'is.workflow.actions.weather.forecast': action_weather_forecast,
    'is.workflow.actions.properties.weather.conditions': action_weather_condition,
    'com.apple.weather.OpenNotificationsConfigurationIntent': action_weather_notification,
    'com.apple.weather.WeatherIntent': action_weather_weatherintent,
    'com.apple.Passbook.OpenPassIntent': action_open_card,
    'is.workflow.actions.openpasswords': action_openpasswords,
    'is.workflow.actions.venmo.request': action_venmo_request,
    'is.workflow.actions.venmo.pay': action_venmo_pay,
    'com.apple.ShortcutsActions.SetDataRoamingAction': action_setdataroaming,
    'com.apple.AccessibilityUtilities.AXSettingsShortcuts.AXToggleLEDFlashIntent': action_setting_flashlight,
    'com.apple.AccessibilityUtilities.AXSettingsShortcuts.AXToggleClassicInvertIntent': action_setting_classicinvert,
    'com.apple.AccessibilityUtilities.AXSettingsShortcuts.AXToggleColorFiltersIntent': action_setting_colorfilter,
    'com.apple.AccessibilityUtilities.AXSettingsShortcuts.AXToggleContrastIntent': action_setting_increasecontrast,
    'com.apple.AccessibilityUtilities.AXSettingsShortcuts.AXToggleSmartInvertIntent': action_setting_smartinvert,
    'com.apple.AccessibilityUtilities.AXSettingsShortcuts.AXSetLargeTextIntent': action_setting_textsize,
    'com.apple.AccessibilityUtilities.AXSettingsShortcuts.AXToggleAutoAnswerCallsIntent': action_setting_autoanswer,
    'com.apple.AccessibilityUtilities.AXSettingsShortcuts.AXSetBackgroundSoundIntent': action_setting_backgroundsound,
    'com.apple.Preferences.DeveloperSettingsDeepLink': action_setting_develpersetting,
    'com.apple.AccessibilityUtilities.AXSettingsShortcuts.AXStartMagnifierIntent': action_setting_magnifier,
    'com.apple.Preferences.OpenSoundsAndHapticsDeepLinks': action_setting_opens,
    'com.apple.AccessibilityUtilities.AXSettingsShortcuts.AXToggleAssistiveTouchIntent': action_setting_assistivetouch,
    'com.apple.AccessibilityUtilities.AXSettingsShortcuts.AXToggleAudioDescriptionsIntent': action_setting_audiodescription,
    'com.apple.AccessibilityUtilities.AXSettingsShortcuts.AXSetBackgroundSoundVolumeIntent': action_setting_backgroundsounds,
    'com.apple.AccessibilityUtilities.AXSettingsShortcuts.AXSetLeftRightBalanceIntent': action_setting_leftrightbalance,
    'com.apple.AccessibilityUtilities.AXSettingsShortcuts.AXToggleCaptionsIntent': action_setting_captionssdh,
    'is.workflow.actions.format.number': action_format_number,
    'is.workflow.actions.detect.number': action_detect_number,
    'is.workflow.actions.math': action_math,
    'is.workflow.actions.calculateexpression': action_calculateexpression,
    'com.apple.mobilephone.call': action_call,
    'net.whatsapp.WhatsApp.send': action_whatsapp_send,
    'net.whatsapp.WhatsApp.openin': action_whatsapp_openin,
    'is.workflow.actions.addnewreminder': action_addnewreminder,
    'com.apple.reminders.TTRCreateListAppIntent': action_create_remainderlist,
    'is.workflow.actions.setters.reminders': action_setters_reminders,
    'is.workflow.actions.filter.reminders': action_filter_reminders,
    'is.workflow.actions.properties.reminders': action_properties_reminders,
    'is.workflow.actions.getupcomingreminders': action_getupcomingreminders,
    'is.workflow.actions.reminders.showlist': action_reminders_showlist,
    'com.apple.reminders.TTROpenSmartListAppIntent': action_open_smartlist,
    'is.workflow.actions.removereminders': action_removereminders,
    'com.apple.reminders.TTRSearchRemindersAppIntent': action_search_inreminder,
    'com.alexhay.ToolboxProForShortcuts.AverageColourIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.CreateMatteIntent': action_external_app,
    'com.apple.VoiceMemos.RecordVoiceMemoIntent': action_create_recording,
    'is.workflow.actions.sirikit.donation.handle': action_create_recording,
    'com.apple.VoiceMemos.PlaybackVoiceMemoIntent': action_play_recording,
    'com.apple.VoiceMemos.ChangeRecordingPlaybackSetting': action_change_setting_recording,
    'com.apple.VoiceMemos.SelectRecording': action_select_recording,
    'com.apple.VoiceMemos.StopRecording': action_stop_recording,
    'com.apple.VoiceMemos.DeleteRecording': action_delete_recording,
    'is.workflow.actions.selectcontacts': action_selectcontacts,
    'is.workflow.actions.selectphone': action_selectphone,
    'is.workflow.actions.contacts': action_contacts,
    'is.workflow.actions.filter.contacts': action_filter_contacts,
    'is.workflow.actions.detect.phonenumber': action_detect_phonenumber,
    'com.burbn.instagram.openin': action_external_app,
    'is.workflow.actions.tweet': action_external_app,
    'com.google.chrome.ios.OpenInChromeIntent': action_external_app,
    'is.workflow.actions.shazamMedia': action_external_app,
    'com.apple.TVRemoteUIService.LaunchApplicationIntent': action_external_app,
    'com.apple.TVRemoteUIService.LaunchRemoteIntent': action_external_app,
    'is.workflow.actions.alarm.create': action_create_alarm,
    'is.workflow.actions.alarm.toggle': action_toggle_turn_alarm,
    'com.openai.chat.AskIntent': action_external_app,
    'is.workflow.actions.detect.contacts': action_detect_contacts,
    'is.workflow.actions.getarticle': action_getarticle,
    'com.rivian.ios.consumer.OpenFrunkIntent': action_external_app,
    'com.apple.mobilesafari.CloseTab': action_safari_closetab,
    'com.apple.TVRemoteUIService.WakeAppleTVIntent': action_external_app,
    'com.apple.TVRemoteUIService.SleepAppleTVIntent': action_external_app,
    'com.rivian.ios.consumer.CloseFrunkIntent': action_external_app,
    'is.workflow.actions.openworkflow': action_openworkflow,
    'is.workflow.actions.photos.createalbum': action_photo_createalbum,
    'is.workflow.actions.gettypeaction': action_gettypeaction,
    'com.sindresorhus.Actions.IsReachableIntent': action_external_app,
    'com.google.chrome.ios.openurl': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.CropIntent': action_external_app,
    'dk.simonbs.Scriptable.RunScriptInlineIntent': action_external_app,
    'is.workflow.actions.properties.contacts': action_properties_contacts,
    'is.workflow.actions.pocket.add': action_external_app,
    'is.workflow.actions.folder': action_file,
    'is.workflow.actions.phonenumber': action_phonenumber,
    'is.workflow.actions.postonfacebook': action_external_app,
    'is.workflow.actions.imgur.upload': action_external_app,
    'com.microsoft.msedge.OpenInChromeIntent': action_external_app,
    'com.apple.Pages.TSADocumentOpenIntent': action_external_app,
    'com.apple.TVRemoteUIService.PauseContentIntent': action_external_app,
    'com.apple.TVRemoteUIService.SkipContentIntent': action_external_app,
    'com.apple.TVRemoteUIService.LaunchScreenSaverIntent': action_external_app,
    'com.apple.TVRemoteUIService.SwitchUserAccountIntent': action_external_app,
    'com.apple.TVRemoteUIService.ToggleSystemAppearanceIntent': action_external_app,
    'com.apple.TVRemoteUIService.ToggleCaptionsIntent': action_external_app,
    'com.apple.TVRemoteUIService.ReduceLoudSoundsIntent': action_external_app,
    'is.workflow.actions.searchitunes': action_searchitunes,
    'is.workflow.actions.properties.itunesstore': action_properties_itunes,
    'is.workflow.actions.showinstore': action_showinstore,
    'com.apple.shortcuts.SearchShortcutsAction': action_search_shortcut,
    'com.alexhay.ToolboxProForShortcuts.TrimTextIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.InternetConnectionIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.IsVPNConnectedIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.DeviceStorageIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.CheckIfInstalledIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.SortListIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.ViewMapIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.DeviceDetailsIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.PerformCalculationIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.DeviceLanguageIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.BatteryStatusIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.QuickLookExtendedIntent': action_external_app,
    'com.apple.shortcuts.DeleteWorkflowAction': action_deleteworkflow,
    'com.apple.shortcuts.CreateWorkflowAction': action_create_shortcut,
    'is.workflow.actions.evernote.get': action_external_app,
    'is.workflow.actions.evernote.delete': action_external_app,
    'is.workflow.actions.evernote.append': action_external_app,
    'com.winterowls.Night-Shift.RandomWallpaperIntent': action_external_app,
    'com.apple.ShortcutsActions.SetSilentModeAction': action_toggle_turnsilentmode,
    'com.apple.musicrecognition.RecognizeMusicIntent': action_recognize_music,
    'com.brave.ios.browser.OpenWebsiteIntent': action_external_app,
    'com.google.GoogleMobile.GoogleForQueryIntent': action_external_app,
    'is.workflow.actions.dismisssiri': action_dismisssiri,
    'net.shinyfrog.bear-IOS.create': action_external_app,
    'is.workflow.actions.runapplescript': action_external_app,
    'com.apple.DocumentsApp.SearchFile': action_searchfile,
    'com.apple.mobilesafari.TabEntity': action_filter_tab,
    'com.sindresorhus.Actions.IsOnlineIntent': action_external_app,
    'com.sindresorhus.Actions.Authenticate': action_external_app,
    'com.sindresorhus.Actions.RemoveNonPrintableCharactersIntent': action_external_app,
    'com.sindresorhus.Actions.RemoveEmojiIntent': action_external_app,
    'com.sindresorhus.Actions.TransformTextIntent': action_external_app,
    'is.workflow.actions.workout.start': action_health_workout_log,
    'is.workflow.actions.stocks.quote': action_stock_quote,
    'com.tijo.opener.Opener.show-options': action_external_app,
    'com.apple.iBooks.BookAppEntity': action_external_app,
    'com.apple.AccessibilityUtilities.AXSettingsShortcuts.AXToggleZoomIntent': action_setting_zoom,
    'com.tapbots.Tweetbot.tweet': action_external_app,
    'com.culturedcode.ThingsTouch.addtask': action_external_app,
    'com.sindresorhus.Actions.IsShakingDevice': action_external_app,
    'dk.simonbs.DataJar.GetValueIntent': action_external_app,
    'dk.simonbs.DataJar.SetValueIntent': action_external_app,
    'com.sindresorhus.Actions.IsCellularDataOn': action_external_app,
    'com.sindresorhus.Actions.IsBluetoothOnIntent': action_external_app,
    'com.sindresorhus.Actions.IsConnectedToVPNIntent': action_external_app,
    'com.sindresorhus.Actions.IsLowPowerModeIntent': action_external_app,
    'com.sindresorhus.Actions.IsSilentModeOnIntent': action_external_app,
    'com.sindresorhus.Actions.IsDarkModeIntent': action_external_app,
    'com.sindresorhus.Actions.GetDeviceOrientationIntent': action_external_app,
    'com.sindresorhus.Actions.GetActionsVersion': action_external_app,
    'com.sindresorhus.Actions.GetBatteryStateIntent': action_external_app,
    'com.sindresorhus.Actions.GetDeviceDetailsExtended': action_external_app,
    'com.apple.AccessibilityUtilities.AXSettingsShortcuts.AXToggleSoundDetectionIntent': action_setting_soundrecognition,
    'com.apple.news.TagIntent': action_external_app,
    'com.omnigroup.OmniFocus2.iPhone.pastetaskpaper': action_external_app,
    'com.apple.AccessibilityUtilities.AXSettingsShortcuts.AXStartGuidedAccessIntent': action_start_guidedaccess,
    'com.apple.AccessibilityUtilities.AXSettingsShortcuts.AXToggleVoiceControlIntent': action_turn_voicecontrol,
    'com.apple.shortcuts.ResetCellularDataStatisticsAction': action_reset_cellulardata_statistics,
    'com.apple.AccessibilityUtilities.AXSettingsShortcuts.AXToggleLiveCaptionsIntent': action_setting_livecaption,
    'is.workflow.actions.pocket.get': action_external_app,
    'com.6X.LockLauncher.RefreshActivityIntent': action_external_app,
    'com.adguard.ios.AdGuardVPN.VpnStateIntent': action_external_app,
    'dk.simonbs.DataJar.CheckIfValueExistsIntent': action_external_app,
    'com.apple.AccessibilityUtilities.AXSettingsShortcuts.AXToggleMonoAudioIntent': action_setting_monoaudio,
    'is.workflow.actions.announcenotifications.set': action_setting_announcenotification,
    'com.apple.NanoSettings.NPRFPingMyPhoneIntent': action_pingmyphone,
    'com.apple.NanoSettings.NPRFSetFlashLightIntent': action_setflashlight,
    'com.apple.NanoSettings.NPRFSetTheaterModeIntent': action_theatermode,
    'com.apple.NanoSettings.NPRFSetWaterLockIntent': action_set_waterlock,
    'com.apple.NanoSettings.NPRFSetSchoolTimeIntent': action_set_schooltime,
    'com.todoist.ios.CreateTaskIntent': action_external_app,
    'com.leomehlig.today.AddTaskIntent': action_external_app,
    'com.rivian.ios.consumer.CloseLiftgateIntent': action_external_app,
    'com.phocusllp.due.add': action_external_app,
    'io.pushcut.Pushcut.RunShortcutIntent': action_external_app,
    'com.apple.AccessibilityUtilities.AXSettingsShortcuts.AXToggleVoiceOverIntent': action_setting_voiceover,
    'com.rivian.ios.consumer.UnlockDoorsIntent': action_external_app,
    'com.microsoft.bing.OpenSydneyIntent': action_external_app,
    'is.workflow.actions.runscene': action_health_workout_log,
    'com.sindresorhus.Actions.BlurImages': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.AuthenticateIntent': action_external_app,
    'is.workflow.actions.trello.add.card': action_external_app,
    'is.workflow.actions.personalhotspot.password.set': action_personalhotspot_password_get,
    'com.apple.iBooks.openin': action_external_app,
    'is.workflow.actions.dropbox.open': action_external_app,
    'is.workflow.actions.addnewcontact': action_add_new_contact,
    'is.workflow.actions.setters.contacts': action_set_contact,
    'com.rivian.ios.consumer.LockDoorsIntent': action_external_app,
    'com.apple.ShortcutsActions.OpenCameraAction': action_open_camera,
    'is.workflow.actions.trello.get': action_external_app,
    'is.workflow.actions.properties.trello': action_external_app,
    'com.sindresorhus.Actions.GetAudioPlaybackDestinationIntent': action_external_app,
    'com.sindresorhus.Actions.GetAverageColorOfImage': action_external_app,
    'com.sindresorhus.Actions.CreateColorImageIntent': action_external_app,
    'company.thebrowser.ArcMobile2.SearchIntent': action_external_app,
    'com.apple.Keynote.KNDocumentPlayIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.GetWorkoutsIntent': action_external_app,
    'com.rivian.ios.consumer.OpenLiftgateIntent': action_external_app,
    'is.workflow.actions.todoist.add': action_external_app,
    'com.apple.AccessibilityUtilities.AXSettingsShortcuts.AXToggleBackgroundSoundsIntent': action_setting_setbackgroundsound,
    'is.workflow.actions.text.trimwhitespace': action_trim,
    'com.apple.AppStore.PageNavigationIntent': action_decayed_action,
    'com.apple.Home.ToggleIntent': action_decayed_action,
    'com.apple.Passbook.DeletePassIntent': action_decayed_action,
    'com.apple.Passbook.AppleCardBillPayIntent': action_decayed_action,
    'com.apple.ShortcutsActions.SetVoiceDataModeAction': action_set_voice_data_mode,
    'com.apple.ShortcutsActions.ToggleCellularPlanAction': action_toggle_cellular_plan,
    'com.alexhay.ToolboxProForShortcuts.GlobalVariablesIntent': action_external_app,
    'com.sindresorhus.Actions.IsDeviceLocked': action_external_app,
    'com.sindresorhus.Actions.WriteTextIntent': action_external_app,
    'com.apple.shortcuts.OpenWorkflowAction': action_openworkflow,
    'AsheKube.app.a-Shell.ExecuteCommandIntent': action_external_app,
    'com.apple.AccessibilityUtilities.AXSettingsShortcuts.AXSetSoundDetectorIntent': action_setting_recognized_sound,
    'com.sindresorhus.Actions.WaitMilliseconds': action_external_app,
    'com.sindresorhus.Actions.IsAudioPlayingIntent': action_external_app,
    'com.apple.DocumentsApp.ScanDocument': action_scan_doc,
    'com.sindresorhus.Actions.ScanDocumentsIntent': action_external_app,
    'com.sindresorhus.Actions.GetEmojisIntent': action_external_app,
    'com.sindresorhus.Actions.SetUniformTypeIdentifier': action_external_app,
    'com.sindresorhus.Actions.GetUniformTypeIdentifierIntent': action_external_app,
    'com.apple.shortcuts.AddShortcutToHomeScreenAction': action_add_workflow_to_screen,
    'com.omnigroup.OmniFocus3.iOS.AddTaskIntent': action_external_app,
    'AsheKube.app.a-Shell-mini.PutFileIntent': action_external_app,
    'AsheKube.app.a-Shell-mini.ExecuteCommandIntent': action_external_app,
    'AsheKube.app.a-Shell-mini.GetFileIntent': action_external_app,
    'com.apple.Numbers.TNiOSAddValuesToFormIntent': action_external_app,
    'com.brogrammers.charty.AddCustomThemeIntent': action_external_app,
    'dk.simonbs.DataJar.InsertValueInArrayIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.HomeIntent': action_external_app,
    'com.bloombuilt.dayone-ios.FindEntriesIntent': action_external_app,
    'com.bloombuilt.dayone-ios.AppendToEntryIntent': action_external_app,
    'is.workflow.actions.dropbox.savefile': action_external_app,
    'com.flexibits.fantastical2.addevent': action_external_app,
    'net.shinyfrog.bear-IOS.add': action_external_app,
    'is.workflow.actions.instapaper.add': action_external_app,
    'ai.perplexity.app.QueryPerplexity': action_external_app,
    'com.apple.Numbers.TNiOSAddValuesToSpreadsheetIntent': action_external_app,
    'dk.simonbs.DataJar.GetKeysIntent': action_external_app,
    'dk.simonbs.DataJar.ViewValueIntent': action_external_app,
    'dk.simonbs.DataJar.GetTypeOfValueIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.QuickMenu2Intent': action_external_app,
    'com.bloombuilt.dayone-ios.CreateEntryIntent': action_external_app,
    'com.sindresorhus.Actions.CreateMenuItem': action_external_app,
    'is.workflow.actions.evernote.new': action_external_app,
    'com.apple.clock.DeleteAlarmIntent': action_delete_alarm,
    'com.alexhay.ToolboxProForShortcuts.ReverseListIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.IsPremiumUnlockedIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.AddToListIntent': action_external_app,
    'ke.bou.WidgetPack.ImageFileIntent': action_external_app,
    'ke.bou.WidgetPack.ModifierClipShapeIntent': action_external_app,
    'ke.bou.WidgetPack.ModifierScaledToFitIntent': action_external_app,
    'ke.bou.WidgetPack.ZStackIntent': action_external_app,
    'ke.bou.WidgetPack.UpdateWidgetIntent': action_external_app,
    'com.alipay.iphoneclient.StartScanIntent': action_external_app,
    'com.alipay.iphoneclient.StartPayIntent': action_external_app,
    'is.workflow.actions.getclassaction': action_get_object_ofclass,
    'com.juniperphoton.MyerList.AddReminderAppIntent': action_external_app,
    'com.juniperphoton.MyerList.EndLiveActivityIntent': action_external_app,
    'app.surfed.app.OpenURLIntent': action_external_app,
    'com.bloombuilt.dayone-mac.CreateEntryIntent': action_external_app,
    'com.sindresorhus.Actions.GlobalVariableSetNumber': action_external_app,
    'com.sindresorhus.Actions.GlobalVariableGetNumber': action_external_app,
    'com.sindresorhus.Actions.GetIndexOfListItem': action_external_app,
    'com.sindresorhus.Actions.HideShortcutsAppIntent': action_external_app,
    'com.sindresorhus.Actions.PrettyPrintDictionariesIntent': action_external_app,
    'com.sindresorhus.Actions.AddToListIntent': action_external_app,
    'dk.simonbs.DataJar.DeleteValueIntent': action_external_app,
    'com.sindresorhus.Actions.DateToUnixTimeIntent': action_external_app,
    'com.sindresorhus.Actions.RemoveDuplicatesFromListIntent': action_external_app,
    'dk.simonbs.DataJar.GetChildCountIntent': action_external_app,
    'com.sindresorhus.Actions.FilterListIntent': action_external_app,
    'ke.bou.WidgetPack.ColorIntent': action_external_app,
    'ke.bou.WidgetPack.VerbatimTextIntent': action_external_app,
    'ke.bou.WidgetPack.ModifierFontIntent': action_external_app,
    'ke.bou.WidgetPack.HorizontalStackIntent': action_external_app,
    'ke.bou.WidgetPack.ModifierFixedFrameIntent': action_external_app,
    'ke.bou.WidgetPack.SpacerIntent': action_external_app,
    'ke.bou.WidgetPack.FontIntent': action_external_app,
    'ke.bou.WidgetPack.ModifierPaddingIntent': action_external_app,
    'ke.bou.WidgetPack.LinkIntent': action_external_app,
    'ke.bou.WidgetPack.VerticalStackIntent': action_external_app,
    'ke.bou.WidgetPack.ModifierBackgroundIntent': action_external_app,
    'ke.bou.WidgetPack.PreviewWidgetIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.CreateMenuIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.HapticFeedbackIntent': action_external_app,
    'com.apple.NanoSettings.NPRFSetAlwaysOnIntent': action_external_app,
    'com.apple.NanoSettings.NPRFSetSilentModeIntent': action_external_app,
    'com.apple.PBBridgeSupport.BridgeIntents.COSSetGizmoFaceIntent': action_external_app,
    'DesignTech-SIA.Spendit.AI_AddTransactionIntent': action_external_app,
    'DesignTech-SIA.Spendit.AI_ViewAccountIntent': action_external_app,
    'com.sindresorhus.Actions.GetUnsplashImageIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.BlurImagesIntent': action_external_app,
    'com.google.chrome.ios.OpenInChromeIncognitoIntent': action_external_app,
    'com.apple.news.TodayIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.IsAudioPlayingIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.CheckForUpdatesIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.ShowNotificationIntent': action_external_app,
    'is.workflow.actions.properties.workflow': action_properties_appstore,
    'is.workflow.actions.runjavascriptforautomation': action_decayed_action,
    'com.alexhay.ToolboxProForShortcuts.CheckGVIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.GetReminderListsIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.GetReminderIDIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.EditReminderIntent': action_external_app,
    'maccatalyst.com.Christopher-Hannah.Text-Case.TextCaseIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.CreateIconIntent': action_external_app,
    'net.shinyfrog.bear-IOS.open': action_external_app,
    'net.shinyfrog.bear-IOS.contents': action_external_app,
    'ke.bou.GizmoPack.UniversalVariablesIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.ScanDocumentIntent': action_external_app,
    'io.pushcut.Pushcut.ShowNotificationIntent': action_external_app,
    'com.culturedcode.ThingsiPad.TAIItemEntity': action_external_app,
    'com.culturedcode.ThingsiPad.TAIEditItems': action_external_app,
    'com.culturedcode.ThingsiPad.TAIAddTodo2': action_external_app,
    'com.sindresorhus.Actions.RandomTextIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.CreateTextImageIntent': action_external_app,
    'com.sindresorhus.Actions.FormatDurationIntent': action_external_app,
    'com.apple.shortcuts.CreateShortcutiCloudLinkAction': action_create_icloudlink,
    'com.brogrammers.charty.NewChartIntent': action_external_app,
    'com.brogrammers.charty.AddSeriesToChartIntent': action_external_app,
    'com.brogrammers.charty.CopyChartToClipboardIntent': action_external_app,
    'org.fastdevsproject.altervista.Device-Monitor.RAMCleanIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.EditFolderBookmarksIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.ListContentsOfBookmarkedFolderIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.EditBookmarkedFileIntent': action_external_app,
    'com.sindresorhus.Actions.GenerateCSVIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.SaveFilesToBookmarkedFoldersIntent': action_external_app,
    'com.sindresorhus.Actions.RemoveEmptyLinesIntent': action_external_app,
    'app.shortcutify.Shortcutify.SpotifyPlayPauseIntent': action_external_app,
    'com.sindresorhus.Actions.GlobalVariableGetText': action_external_app,
    'com.sindresorhus.Actions.GlobalVariableSetText': action_external_app,
    'com.sindresorhus.Actions.RemoveFromListIntent': action_external_app,
    'com.sindresorhus.Actions.ScanQRCodesInImageIntent': action_external_app,
    'com.agiletortoise.Drafts5.QueryDraftsIntent': action_external_app,
    'com.agiletortoise.Drafts5.GetDraftIntent': action_external_app,
    'com.agiletortoise.Drafts5.RunActionIntent': action_external_app,
    'com.omz-software.Pythonista3.PA3RunScriptIntent': action_external_app,
    'com.atow.LaunchCuts.GetFoldersIntent': action_external_app,
    'com.atow.LaunchCuts.GetFolderIntent': action_external_app,
    'com.culturedcode.ThingsiPhone.TAIAddTodo2': action_external_app,
    'is.workflow.actions.silenceunknowncallers.set': action_slientcaller,
    'com.TickTick.task.TTAddTaskToCalendarIntent': action_external_app,
    'com.agiletortoise.Drafts5.CaptureIntent': action_external_app,
    'com.agiletortoise.Drafts-OSX.CaptureIntent': action_external_app,
    'com.google.OPA.OPAAskGoogleIntent': action_external_app,
    'com.grailr.CARROTweather.CurrentForecastIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.BookmarkFolderIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.RemoveItemsFromListIntent': action_external_app,
    'com.sindresorhus.Actions.SetFileCreationModificationDateIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.GetCalendarsIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.CreateCalendarIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.GetAudioIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.GetEventIDIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.EditEventIntent': action_external_app,
    'com.sindresorhus.Actions.RandomDateTimeIntent': action_external_app,
    'com.flexibits.fantastical2.iphone.FKRCreateFromInputIntent': action_external_app,
    'com.culturedcode.ThingsiPad.TAIDeleteItems': action_external_app,
    'com.alexhay.Console.LogMessageIntent': action_external_app,
    'com.iconfactory.TotMobile.QueryDotIntent': action_external_app,
    'com.iconfactory.TotMobile.SetDotIntent': action_external_app,
    'com.sindresorhus.Actions.AskForText': action_external_app,
    'org.joinmastodon.app.SendPostIntent': action_external_app,
    'is.workflow.actions.dropbox.appendfile': action_external_app,
    'com.google.chrome.ios.SearchInChromeIntent': action_external_app,
    'com.zlineman.Jellyfish.ImportShortcutIntent': action_external_app,
    'com.apple.mobilesafari.CreateNewPrivateTab': action_create_private_tab,
    'com.feelthemusi.musi.MPlayMyFavoritesIntent': action_external_app,
    'com.feelthemusi.musi.MSearchIntent': action_external_app,
    'com.apple.ShortcutsActions.CellularPlanEntity': action_filter_cellular,
    'com.apple.ShortcutsActions.SetDefaultCellularPlanAction': action_set_default_cellular,
    'is.workflow.actions.getparentdirectory': action_decayed_action,
    'com.brogrammers.charty.GetInfoAllChartsIntent': action_external_app,
    'com.brogrammers.charty.DeleteChartIntent': action_external_app,
    'com.brogrammers.charty.NewChartWithSeriesIntent': action_external_app,
    'com.brogrammers.charty.StyleAxisIntent': action_external_app,
    'com.brogrammers.charty.AddMovingAverageIntent': action_external_app,
    'com.sindresorhus.Actions.TrimWhitespaceIntent': action_external_app,
    'com.sindresorhus.Actions.ParseCSVIntent': action_external_app,
    'com.sindresorhus.Actions.ReverseListIntent': action_external_app,
    'com.brogrammers.charty.StyleLineSeriesIntent': action_external_app,
    'is.workflow.actions.safari.geturl': action_decayed_action,
    'com.apple.mobileslideshow.OpenCollectionIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.GenerateUUIDIntent': action_external_app,
    'com.omz-software.Pythonista.runscript': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.ConvertCurrencyIntent': action_external_app,
    'com.brogrammers.charty.StyleChartIntent': action_external_app,
    'com.brogrammers.charty.StyleScatterSeriesIntent': action_external_app,
    'com.brogrammers.charty.GroupDataIntent': action_external_app,
    'com.brogrammers.charty.ExportChartAsImageIntent': action_external_app,
    'com.brogrammers.charty.UpdateWidgetsIntent': action_external_app,
    'com.dayonelog.dayoneiphone.post': action_external_app,
    'com.tantsissa.AutoSleep.ReadinessIntent': action_external_app,
    'com.xvision.datamannext.ShowUsageIntent': action_external_app,
    'com.fifteenjugglers.solarwatch.ComputeSolarEventTimeIntent': action_external_app,
    'ch.marcela.ada.LibTerm.RunCommandIntent': action_external_app,
    'com.sindresorhus.Actions.GlobalVariableDelete': action_external_app,
    'com.sindresorhus.Actions.TranscribeAudioIntent': action_external_app,
    'com.apple.shortcuts.TranscribeAudioAction': action_transcribe_audio,
    'com.alexhay.ToolboxProForShortcuts.RecogniseSpeechIntent': action_external_app,
    'com.apple.Numbers.TNiOSOpenAnyDocumentIntent': action_external_app,
    'com.iconfactory.Tot.QueryDotIntent': action_external_app,
    'com.iconfactory.Tot.AddToDotIntent': action_external_app,
    'com.iconfactory.TotMobile.GetDotIntent': action_external_app,
    'com.agiletortoise.Drafts5.OpenDraftIntent': action_external_app,
    'com.iconfactory.Tot.ShowDotIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.GetPhotoAlbumsIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.AddPhotoAlbumIntent': action_external_app,
    'AsheKube.app.a-Shell.PutFileIntent': action_external_app,
    'AsheKube.app.a-Shell.GetFileIntent': action_external_app,
    'com.google.GoogleMobile.SearchImageWithLensIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.CalculateWithSoulverIntent': action_external_app,
    'com.agiletortoise.Drafts5.QueryWorkspaceIntent': action_external_app,
    'co.supertop.Castro-2.GetNowPlayingEpisodeDetailsIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.GetFilesFromBookmarkedFolderIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.DeleteFilesInBookmarkedFolderIntent': action_external_app,
    'dk.simonbs.Jayson.ViewJSONIntent': action_external_app,
    'dk.simonbs.Jayson.GetFileIntent': action_external_app,
    'com.apple.Notes.CreateFolderLinkAction': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.DeleteFromDictionaryIntent': action_external_app,
    'com.brogrammers.charty.AddAverageIntent': action_external_app,
    'com.brogrammers.charty.StyleBarSeriesIntent': action_external_app,
    'com.apple.mobilesafari.ReadingListItemEntity': action_filter_readinglist_item,
    'dk.simonbs.Scriptable.RefreshAllWidgetsIntent': action_external_app,
    'is.workflow.actions.cloudapp.upload': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.TagFilesIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.GenerateThumbnailsIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.GetFileURLIntent': action_external_app,
    'com.culturedcode.ThingsMac.TAIItemEntity': action_external_app,
    'com.culturedcode.ThingsMac.TAIAddTodo2': action_external_app,
    'com.sindresorhus.Actions.GetFileIconIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.SearchForEmojiIntent': action_external_app,
    'com.appliedphasor.working-copy.WriteFileIntent': action_external_app,
    'com.appliedphasor.working-copy.CommitRepositoryIntent': action_external_app,
    'com.appliedphasor.working-copy.PushRepositoryIntent': action_external_app,
    'com.sindresorhus.Actions.GetTitleOfURLIntent': action_external_app,
    'com.Christopher-Hannah.Text-Case.ReplaceIntent': action_external_app,
    'com.minimasoftware.TimerPlus.StartQuickTimerIntent': action_external_app,
    'com.apple.NanoSettings.NPRFSetWakeOnWristRaiseIntent': action_external_app,
    'com.apple.NanoSettings.NPRFSetAutoLaunchAudioAppsIntent': action_external_app,
    'com.apple.PBBridgeSupport.BridgeIntents.COSListGizmoFacesIntent': action_external_app,
    'com.apple.PBBridgeSupport.BridgeIntents.COSGetCurrentGizmoFaceIntent': action_external_app,
    'com.apple.AccessibilityUtilities.AXSettingsShortcuts.AXStartRemoteWatchScreenIntent': action_external_app,
    'net.shinyfrog.bear-IOS.grab': action_external_app,
    'com.ngocluu.goodlinks.GetCurrentLink': action_external_app,
    'com.ngocluu.goodlinks.AddLinkIntent': action_external_app,
    'com.ngocluu.goodlinks.GetCurrentSelection': action_external_app,
    'com.ngocluu.goodlinks.LinkEntity': action_external_app,
    'com.ngocluu.goodlinks.OpenLinkIntent': action_external_app,
    'me.damir.dropover-mac.AddToShelfIntent': action_external_app,
    'is.workflow.actions.file.reveal': action_decayed_action,
    'app.cyan.taio.SaveClippingIntent': action_external_app,
    'is.workflow.actions.properties.note': action_properties_images,
    'is.workflow.actions.properties.shazam': action_properties_images,
    'is.workflow.actions.properties.appearance' : action_properties_images,
    'dk.simonbs.Jayson.PrettifyJSONIntent': action_external_app,
    'com.elgato.eve.EVEMyCamerasIntent': action_external_app,
    'com.anthopak.SmartLightsController.GetCurrentRoomsIntent': action_external_app,
    'br.com.marcosatanaka.play.GetVideoIntent': action_external_app,
    'com.Christopher-Hannah.Text-Case.TextCaseIntent': action_external_app,
    'com.sindresorhus.Actions.ParseJSON5Intent': action_external_app,
    'com.sindresorhus.Actions.SymbolImageIntent': action_external_app,
    'is.workflow.actions.properties.itunesartist': action_properties_images,
    'com.alexhay.ToolboxProForShortcuts.QuickMenuIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.GetMenuItemIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.GetTextFromImageIntent': action_external_app,
    'net.shinyfrog.bear-iOS.SFSearchNotesIntent': action_external_app,
    'net.shinyfrog.bear-iOS.SFAddToNoteIntent': action_external_app,
    'net.shinyfrog.bear-iOS.SFCreateNoteIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.GetMovieDetailsIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.DetectFacesIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.RecogniseObjectsInImageIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.RemoveEmojiIntent': action_external_app,
    'com.obdura.playlistimport.MakePlaylistFromURLIntent': action_external_app,
    'com.obdura.playlistimport.AllImportsFinishedIntent': action_external_app,
    'com.apple.Notes.DeleteNotesLinkAction': action_external_app,
    'com.agiletortoise.Drafts-OSX.OpenDraftIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.CreateRemindersListIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.CreateReminderIntent': action_external_app,
    'dk.simonbs.Scriptable.ParameterizedRunScriptIntent': action_external_app,
    'com.pvieito.HomeBot.HomeBotGetHomeItemsIntent': action_external_app,
    'com.pvieito.HomeBot.HomeBotRunHomeActionIntent': action_external_app,
    'com.starbucks.mystarbucks.SBAOrderItemIntent': action_external_app,
    'com.alexhay.ToolboxPro2.GenerateTextIntent': action_external_app,
    'com.overdesigned.Cheatsheet.CSAddCheatIntent': action_external_app,
    'com.zlineman.Jellyfish.ImportObjectsIntent': action_external_app,
    'com.zlineman.Jellyfish.GrabJellycutIntent': action_external_app,
    'com.7Z88K9GUU8.com.rileytestut.AltStore.RefreshAllIntent': action_external_app,
    'com.openplanetsoftware.Just-Press-Record-for-iOS.StartRecordingIntent': action_external_app,
    'com.bloombuilt.dayone-ios.ShowEntriesIntent': action_external_app,
    'ke.bou.WidgetPack.TextIntent': action_external_app,
    'ke.bou.WidgetPack.ImageIntent': action_external_app,
    'ke.bou.WidgetPack.StackIntent': action_external_app,
    'com.LennartBusch.Milage.TimeStampsIntent': action_external_app,
    'com.LennartBusch.Milage.TripLastDistanceIntent': action_external_app,
    'com.sindresorhus.One-Thing.SetTextIntent': action_external_app,
    'is.workflow.actions.lightroom.import': action_external_app,
    'com.agiletortoise.Drafts-OSX.QueryDraftsIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.FilterListIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.RemoveDuplicatesIntent': action_external_app,
    'com.sindresorhus.Aiko.TranscribeAudioIntent': action_external_app,
    'com.culturedcode.ThingsiPhone.TAIItemEntity': action_external_app,
    'com.culturedcode.ThingsiPhone.TAIShowItems2': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.SwitchCaseIntent': action_external_app,
    'com.sindresorhus.Lock-Screen-One.SetTextIntent': action_external_app,
    'com.rafaelsoh.dime.NewTransactionIntent': action_external_app,
    'com.alexhay.Console.StartLoggingIntent': action_external_app,
    'com.alexhay.Console.OutputMessagesIntent': action_external_app,
    'com.alexhay.Console.ClearMessagesIntent': action_external_app,
    'com.alexhay.Console.LogItemsIntent': action_external_app,
    'in.muditbhargava.LookUp.FindCollectedWordsIntent': action_external_app,
    'com.apple.mobilesafari.BookmarkEntity': action_bookmark_safari,
    'ke.bou.GizmoPack.SnapshotMapIntent': action_external_app,
    'com.iconfactory.TotMobile.AddToDotIntent': action_external_app,
    'dk.simonbs.Retoot.CreateQuoteIntent': action_external_app,
    'com.sindresorhus.Actions.RandomColorIntent': action_external_app,
    'com.sindresorhus.Actions.OverwriteFile': action_external_app,
    'net.shinyfrog.bear-IOS.search': action_external_app,
    'com.culturedcode.ThingsiPhone.TAIEditItems': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.SmartMenuIntent': action_external_app,
    'ke.bou.WidgetPack.ModifierRelativeFrameIntent': action_external_app,
    'com.alexhay.MenuBox.ChooseMenuSetIntent': action_external_app,
    'is.workflow.actions.quit.app': action_decayed_action,
    'is.workflow.actions.startscreensaver': action_decayed_action,
    'com.apple.mobilesafari.CreateNewTab': action_create_newtab,
    'com.apple.mobilesafari.CreateNewTabGroup': action_create_new_tab_group,
    'com.apple.mobilesafari.TabGroupEntity': action_filter_tabgroup,
    'com.apple.mobilesafari.OpenTabGroup': action_open_tabgroup,
    'com.apple.mobilesafari.OpenTab': action_opentab_safari,
    'com.apple.mobilesafari.OpenBookmark': action_open_bookmark,
    'in.muditbhargava.LookUp.ClipboardSearchIntent': action_external_app,
    'com.sindresorhus.Actions.Boolean': action_external_app,
    'com.sindresorhus.Actions.IsAccessibilityFeatureOn': action_external_app,
    'com.microsoft.bing.OpenRewardsIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.FindMoviesIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.FindMovies2Intent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.GetMovieDetails2Intent': action_external_app,
    'com.sindresorhus.Actions.CalculateWithSoulver': action_external_app,
    'com.sindresorhus.Actions.MusicPlaylist_AppEntity': action_external_app,
    'br.com.marcosatanaka.musicbox.GetMusicIntent': action_external_app,
    'br.com.marcosatanaka.music-harbor.ArtistAppEntity': action_external_app,
    'com.skype.skype.call': action_external_app,
    'com.appliedphasor.working-copy.CloneRepositoryIntent': action_external_app,
    'com.sindresorhus.Actions.Authenticate2': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.GetLocationFromCoordsIntent': action_external_app,
    'co.bergen.Darkroom.HSLExportWithDarkroomIntent': action_external_app,
    'com.omnigroup.OmniFocus3.iOS.AddTaskPaperIntent': action_external_app,
    'ke.bou.WidgetPack.SetPropertyIntent': action_external_app,
    'ke.bou.WidgetPack.GradientIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.ScanNFCIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.GetTextFromImagesIAIHIntent': action_external_app,
    'nl.jeffreykuiken.NoirApp.SetEnabledForSiteIntent': action_external_app,
    'nl.jeffreykuiken.NoirApp.SetImageDimmingForSiteIntent': action_external_app,
    'com.alexhay.nautomate.ChooseIntegrationIntent': action_external_app,
    'com.alexhay.nautomate.FindPagesIntent': action_external_app,
    'com.alexhay.nautomate.GetTextFromPageIntent': action_external_app,
    'ke.bou.WidgetPack.ModifierScaledToFillIntent': action_external_app,
    'com.omnigroup.OmniFocus4.AddTaskIntent': action_external_app,
    'com.apple.iBooks.SearchBooksIntent': action_external_app,
    'com.omnigroup.OmniFocus4.FindProjectsIntent': action_external_app,
    'com.omnigroup.OmniFocus4.ShowFromChoiceIntent': action_external_app,
    'com.omnigroup.OmniFocus4.AddTaskPaperIntent': action_external_app,
    'com.omnigroup.OmniFocus3.iOS.FindProjectsIntent': action_external_app,
    'com.omnigroup.OmniFocus3.iOS.ShowFromChoiceIntent': action_external_app,
    'com.apple.Numbers.TSADocumentOpenIntent': action_external_app,
    'fm.overcast.overcast.OCCurrentEpisodeInfoIntent': action_external_app,
    'com.culturedcode.ThingsiPad.TINAddTodoIntent': action_external_app,
    'com.wiheads.paste.GetItemAtIndexIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.ResizeImageExtendedIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.FilterImageIntent': action_external_app,
    'is.workflow.actions.wordpress.post': action_external_app,
    'is.workflow.actions.trello.add.list': action_external_app,
    'is.workflow.actions.trello.add.board': action_external_app,
    'com.sindresorhus.Actions.FormatDateDifferenceIntent': action_external_app,
    'com.agiletortoise.Drafts5.SetDraftIntent': action_external_app,
    'fm.overcast.overcast.OCPlayIntent': action_external_app,
    'com.omnigroup.OmniFocus3.iOS.FindTasksIntent': action_external_app,
    'is.workflow.actions.tumblr.post': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.GetTBPToolsIntent': action_external_app,
    'com.appliedphasor.working-copy.PullRepositoryIntent': action_external_app,
    'com.sindresorhus.Actions.GetFilePathIntent': action_external_app,
    'ch.marcela.ada.Pyto.RunCodeIntent': action_external_app,
    'ke.bou.WidgetPack.ModifierForegroundColorIntent': action_external_app,
    'com.getcardpointers.app.ShortcutsOfferEntity': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.PrettyPrintIntent': action_external_app,
    'is.workflow.actions.filter.windows': action_decayed_action,
    'is.workflow.actions.resizewindow': action_decayed_action,
    'net.shinyfrog.bear.SFCreateNoteIntent': action_external_app,
    'net.shinyfrog.bear-iOS.SFAddTagsToNoteIntent': action_external_app,
    'com.sindresorhus.Actions.GetUserDetailsIntent': action_external_app,
    'com.meal.plan.ios.GetRecipeFromURLIntent': action_external_app,
    'com.orange.telephone.IdentifyPhoneNumber': action_external_app,
    'com.culturedcode.ThingsiPhone.TINAddTodoIntent': action_external_app,
    'com.sindresorhus.Actions.GetRunningAppsIntent': action_external_app,
    'com.sindresorhus.Actions.SortListIntent': action_external_app,
    'com.agiletortoise.Drafts4.addto': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.FindArtistsIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.FindAlbumsIntent': action_external_app,
    'com.apple.iBooks.BookReaderNavigatePagesIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.FindTvShowsIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.GetTvShowDetailsIntent': action_external_app,
    'is.workflow.actions.display.always-on.set': action_decayed_action,
    'com.alexhay.ToolboxProForShortcuts.BookmarkFileIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.EditPendingNotificationsIntent': action_external_app,
    'com.microsoft.to-do.WLAddTaskIntent': action_external_app,
    'ke.bou.WidgetPack.SFSymbolIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.QuickMatchTextIntent': action_external_app,
    'com.sindresorhus.Actions.IsDeviceOrientationIntent': action_external_app,
    'com.apple.mobilesafari.OpenView': action_open_safariview,
    'com.alexhay.ToolboxProForShortcuts.DetectFacesIAIHIntent': action_external_app,
    'com.apple.shortcuts.OpenNavigationDestinationAction': action_decayed_action,
    'com.omz-software.Pythonista.editscript': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.FindPexelPhotosIntent': action_external_app,
    'com.reederapp.5.macOS.GetReadLaterIntent': action_external_app,
    'com.reederapp.5.macOS.OpenReadLaterIntent': action_external_app,
    'ke.bou.GizmoPack.CreateWalletPassIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.GetW3WIntent': action_external_app,
    'art.splashy.GetSplashyWallpaperIntent': action_external_app,
    'com.sindresorhus.Actions.GetDominantColorsOfImage': action_external_app,
    'com.sindresorhus.Actions.GenerateUUIDIntent': action_external_app,
    'com.SideStore.SideStore.ZFY6868JV7.RefreshAllIntent': action_external_app,
    'com.SideStore.SideStore.G44P446W92.RefreshAllIntent': action_external_app,
    'com.P4N4J84A3M.com.rileytestut.AltStore.ViewAppIntent': action_external_app,
    'com.P4N4J84A3M.com.rileytestut.AltStore.RefreshAllIntent': action_external_app,
    'co.zottmann.ActionsForObsidian.CheckForNotes': action_external_app,
    'co.zottmann.ActionsForObsidian.CheckForNote': action_external_app,
    'co.zottmann.ActionsForObsidian.AppendNote': action_external_app,
    'co.zottmann.ActionsForObsidian.CreateNote': action_external_app,
    'com.tantsissa.AutoSleep.SleepRingsIntent': action_external_app,
    'com.lexwarelabs.goodmorning.SleepIntent': action_external_app,
    'is.workflow.actions.hide.app': action_decayed_action,
    'in.muditbhargava.LookUp.AddToCollectionIntent': action_external_app,
    'com.jonny.spring.KJYGetTweetIntent': action_external_app,
    'ke.bou.WidgetPack.ModifierMinimumScaleFactorIntent': action_external_app,
    'fm.overcast.overcast.add': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.GetSymbolNameIntent': action_external_app,
    'org.fastdevsproject.altervista.Device-Monitor.CPUChartIntent': action_external_app,
    'org.fastdevsproject.altervista.Device-Monitor.RAMChartIntent': action_external_app,
    'org.fastdevsproject.altervista.Device-Monitor.RAMDepthCleanIntent': action_external_app,
    'com.openai.chat.OpenVoiceModeIntent': action_external_app,
    'com.apple.iBooks.BookReaderChangeThemeIntent': action_external_app,
    'com.apple.iBooks.BookReaderChangePageNavigationIntent': action_external_app,
    'is.workflow.actions.evernote.getlink': action_external_app,
    'is.workflow.actions.movewindow': action_decayed_action,
    'com.pcalc.mobile.CalcSetRegisterWithValueIntent': action_external_app,
    'com.pcalc.mobile.CalcRunFunctionWithOneParameterIntent': action_external_app,
    'com.pcalc.mobile.CalcRunFunctionWithTwoParametersIntent': action_external_app,
    'com.culturedcode.ThingsMac.TINRunThingsURLIntent': action_external_app,
    'com.apple.AccessibilityUIServer.ToggleMusicHapticsIntent': action_external_app,
    'com.iconfactory.Tot.GetDotIntent': action_external_app,
    'ke.bou.WidgetPack.ModifierShadowIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.GetLocationFromTextIntent': action_external_app,
    'com.shi.AviaryApp.PostTweetIntent': action_external_app,
    'com.twidere.TwidereX.PublishPostIntent': action_external_app,
    'com.ulyssesapp.ios.ULListSheetsIntent': action_external_app,
    'com.ulyssesapp.ios.ULGetIdentifierIntent': action_external_app,
    'com.ulyssesapp.ios.ULGetSheetIntent': action_external_app,
    'net.shinyfrog.bear-iOS.SFAddFilesToNoteIntent': action_external_app,
    'com.waterminder.waterminder.LogCupIntent': action_external_app,
    'com.waterminder.waterminder.LogDrinkIntent': action_external_app,
    'com.waterminder.waterminder.ShowLastDrinkIntent': action_external_app,
    'com.waterminder.waterminder.ShowProgressIntent': action_external_app,
    'com.waterminder.waterminder.ShowRemainingWaterGoalIntent': action_external_app,
    'com.wiheads.paste.ios.GetLatestItemIntent': action_external_app,
    'com.highcaffeinecontent.radio.MRDPlayStationIntent': action_external_app,
    'com.tantsissa.AutoSleep.WristTempIntent': action_external_app,
    'com.omz-software.Pythonista3.PA3AddFileIntent': action_external_app,
    'com.microsoft.to-do.WLShowListIntent': action_external_app,
    'com.XC759DNLDS.com.rileytestut.AltStore.RefreshAllIntent': action_external_app,
    'ai.perplexity.app.OpenVoiceInAppIntent': action_external_app,
    'com.sindresorhus.Actions.TransformTextWithJavaScriptIntent': action_external_app,
    'com.sindresorhus.Actions.ColorIntent': action_external_app,
    'ke.bou.GizmoPack.QueryDocumentIntent': action_external_app,
    'ke.bou.WidgetPack.ModifierOpacityIntent': action_external_app,
    'dev.fuxiao.app.Hamster.RimeDeployIntent': action_external_app,
    #ShareShortcuts
    'com.ZoZoApp.ZoZoApp.CopyContentsToClipboard': action_external_app,
    'com.apple.iWork.Numbers.TNiOSAddValuesToSpreadsheetIntent': action_external_app,
    'com.omnigroup.OmniFocus2.iPhone.newitem': action_external_app,
    'com.tplink.kasa-ios.KasaRunSceneIntent': action_external_app,
    'is.workflow.actions.pinboard.add': action_external_app,
    'io.robbie.HomeAssistant.RenderTemplateIntent': action_external_app,
    'io.robbie.HomeAssistant.CallServiceIntent': action_external_app,
    'com.alexhay.ToolboxProForShortcuts.CreateEventIntent': action_external_app,
    #matt
    'company.thebrowser.ArcMobile2.VoiceSearchIntent': action_external_app,
    'com.culturedcode.ThingsMac.TINAddTodoIntent': action_external_app,
    'com.culturedcode.ThingsMac.beta.TAIAddProject': action_external_app,
    'com.culturedcode.ThingsMac.beta.TAIAddHeading': action_external_app,
    'com.culturedcode.ThingsMac.beta.TAIAddTodo2': action_external_app,
    'com.tapbots.Ivory.PTHIvoryOpenIntent': action_external_app,
    'company.thebrowser.ArcMobile2.CallArcIntent': action_external_app,
    'com.flexibits.fantastical2.iphone.FKRChangeCalendarSetIntent': action_external_app,
    'com.flexibits.fantastical2.iphone.FKROpenOnDateIntent': action_external_app,
    'com.tapbots.Ivory.PTHIvoryPostStatusIntent': action_external_app,
    'is.workflow.actions.filter.apps': action_decayed_action,
    'com.fandango.fandango.UpcomingOrderIntent': action_external_app,
    'com.lifx.lifx.LFXLightSceneIntent': action_external_app,
    'com.culturedcode.ThingsMac.beta.TAIItemEntity': action_external_app,
    'com.culturedcode.ThingsMac.beta.TAIEditItems': action_external_app,
    'com.apple.clock.OpenTab': action_decayed_action,
    'com.culturedcode.ThingsMac.beta.TAIShowItems2': action_external_app,
    'com.culturedcode.ThingsMac.beta.TAIShowList2': action_external_app,
    'com.amazon.Lassen.BookOpenSiriDonationIntent': action_external_app,
    'com.ulyssesapp.mac.ULNewSheetIntent': action_external_app,
    'com.ulyssesapp.mac.ULOpenIntent': action_external_app,
    'com.sindresorhus.One-Thing.GetTextIntent': action_external_app,
    'com.flexibits.fantastical2.iphone.FKRShowScheduleIntent': action_external_app,
    'com.culturedcode.ThingsMac.beta.TINRunThingsURLIntent': action_external_app,
    'com.culturedcode.ThingsMac.beta.TAIAddTodoWithQuickEntry': action_external_app,
    'com.culturedcode.ThingsMac.TINShowTodoIntent': action_external_app,
}


def call_function_by_name(function_name, *args, **kwargs):
    """
    Calls a function based on its name.

    Parameters:
    - function_name (str): The name of the function to call.
    - function_map (dict): A mapping of function names (str) to functions.
    - *args: Positional arguments to pass to the function.
    - **kwargs: Keyword arguments to pass to the function.

    Returns:
    - The result of the function call.

    Raises:
    - ValueError: If the function name is not found in the function map.
    """
    if function_name in function_map:
        return function_map[function_name](*args, **kwargs)
    elif function_name in ['com.apple.AccessibilityUtilities.AXSettingsShortcuts.AXToggleReduceMotionIntent',
                           'is.workflow.actions.finder.getselectedfiles',
                           'is.workflow.actions.cellular.rat.set',
                           'is.workflow.actions.stagemanager.set',
                           'is.workflow.actions.splitscreen',
                           'is.workflow.actions.wunderlist.add',
                           'com.apple.AccessibilityUtilities.AXSettingsShortcuts.AXStartSpeakScreenIntent',
                           'com.apple.AccessibilityUtilities.AXSettingsShortcuts.AXToggleSwitchControlIntent',
                           'is.workflow.actions.runshellscript',
                           'is.workflow.actions.handoff',
                           'com.apple.AccessibilityUtilities.AXSettingsShortcuts.AXToggleWhitePointIntent',
                           'com.apple.AccessibilityUtilities.AXSettingsShortcuts.AXToggleTransparencyIntent']:
        return action_decayed_action(*args, **kwargs)
    else:
        # return None
        raise ValueError(f"Function '{function_name}' not found in function map.")
