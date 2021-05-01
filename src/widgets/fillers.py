"""Module with fillers created from sg.Text()"""
import PySimpleGUI as sg


def horizontal_filler(height, background_color):
    return sg.Text(
        text='',
        background_color=background_color,
        size=(0, height)
    )
    
    
def vertical_filler(width, background_color):
    return sg.Text(
        text='',
        background_color=background_color,
        size=(width, 0)
    )