from src.core import random_primer , check_answer, calculate 
import dearpygui.dearpygui  as dpg

class GUI:
    

    def start():

        dpg.create_context()  
        dpg.create_viewport(width=300, height=300, title="proga") 
        # with dpg.font_registry():
        #     with dpg.font('./fonts/P95-CYR-Regular.otf', size=14, tag='a'):
        #         dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)

        with dpg.window(tag="main"):  
            dpg.add_text(default_value=str(random_primer()))
            dpg.add_input_float()
            dpg.add_button(label="check")

        dpg.setup_dearpygui()  
        dpg.set_primary_window(window="main", value=True)  
        dpg.show_viewport()  
        dpg.start_dearpygui()  
        dpg.destroy_context()  
def grafic_app():
    t=GUI()
    t.start()





















