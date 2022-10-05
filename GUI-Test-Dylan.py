from argparse import ArgumentDefaultsHelpFormatter
from turtle import color, pos
import dearpygui.dearpygui as dpg


dpg.create_context()


def armStatus():
    dpg.configure_item("status",default_value="Armed")

def disarmStatus():
    dpg.configure_item("status",default_value="Disarmed")
   




with dpg.window(label="Arm/DisArm",tag=("A/D"),width=600,height=25,pos=(0,0)) as window:
    Arm = dpg.add_button(tag="arm",label="Arm",width=200,height=25 ,pos=(0,35),callback=armStatus)
    Disarm = dpg.add_button(label="Disarm",width=200,height=25 ,pos=(300,35),callback=disarmStatus)

with dpg.window(label="Arming Status",tag=("ArmingStatus"),width=200,height=25,pos=(600,0)) as window:
    dpg.add_text(default_value="Disarmed",tag="status")


    




dpg.create_viewport(title='Demo-Gui', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()