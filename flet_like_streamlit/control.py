import flet
from flet import Page, Text, Container, ElevatedButton, OutlinedButton, Page, colors



def header(page:Page, value, color="black", size=30, bgcolor=None, weight="bold", italic=False):
    t = Text(value=value, color=color, size=size, bgcolor=bgcolor, weight=weight, italic=italic)
    page.controls.append(t)
    page.update()

def subheader(page:Page, value, color="black", size=15, bgcolor=None, weight="bold", italic=False):
    t = Text(value=value, color=color, size=size, bgcolor=bgcolor, weight=weight, italic=italic)
    page.controls.append(t)
    page.update()

