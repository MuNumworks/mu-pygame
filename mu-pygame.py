## Pygame like - Kojiverse Productions
## Snapshot :: 0.1
## Will work on any numworks OS
## (for now, worked just on mu 1.4.3)

################## imports ################

from kandinsky import fill_rect as fl,fill_circle as fc,draw_string as dr,draw_line as dl,wait_vblank
from ion import *
from time import sleep

################## const ##################

K_OK = KEY_OK; K_BACK = KEY_BACK; K_LEFT = KEY_LEFT; K_RIGHT = KEY_RIGHT; K_UP = KEY_UP; K_DOWN = KEY_DOWN

LOC_KEYS_ = (K_OK,K_DOWN,K_UP,K_RIGHT,K_LEFT)

FULLSCREEN = 0x00000001
NOFRAME = 0x00000010

################## class ##################

class init:
  def __init__(self)->None:
    """ Init but idk what the fuck this func is supposed to do in original pygame """
    return

class __Surface:
  def __init__(self, width: int, height: int)->None:
    """ Create an surface for draw, blit, ..."""
    self.width = width
    self.height = height
    self.to_do = {
      "rect" : list(),
      "line" : list(),
      "circle" : list(),
      "polygon" : list(),
    }
    return

  def fill(self, color: str | int)->None:
    """ Fill itself into specified color """
    Check._color(color)
    fl(0,display.YPLUS,self.width,self.height,color)
    return

class Check:
  def __init__()->None:
    """ Private class to check args type """
    return

  def _int(*args)->None:
    """ Check if args are integers """
    for i in args:
      if type(i)!=int:
        raise ValueError("An integer was expected instead of %s"%i)
    return

  def _color(*args)->None:
    """ Check if args are color """
    for i in args:
      if not (type(i)==str and len(i)==7 and i[0]=="#" or type(i)==tuple):
        raise ValueError("A tuple was expected instead of %s"%i)
    return

  def _rect(*args)->None:
    """ Check if args are Rects """
    for i in args:
      if type(i)==__Surface:
        raise ValueError("A pygame.Rect was expected instead of %s"%i)
    return

  def _tuple(*args)->None:
    """ Check if args are tuples """
    for i in args:
      if type(i)!=tuple:
        raise ValueError("A tuple was expected instead of %s"%i)

class Display:
  def __init__(self)->None:
    """ Display class for pygame numworks """
    self.width,self.height = None,None
    self.caption = "Pygame window"
    self.YPLUS = 18
    self.surface = None
    return

  def __refresh_screen(self)->None:
    """ Refresh window (size, caption) """
    fl(0,self.YPLUS,self.width,self.height,"#000000")
    if self.YPLUS:
      fl(0,0,self.width,self.YPLUS,"#ffffff")
      dr(self.caption,5,0)
    return

  def set_caption(self, caption: str)->None:
    """ Set display's caption """
    self.caption = caption
    self.__refresh_screen()
    return

  def set_mode(self, size: tuple, flags: int)->__Surface:
    """ Create an Surface object """
    self.width,self.height = size
    Check._int(self.width,self.height)
    if self.height+self.YPLUS>222:
      self.height = 222
    if flags==1:self.width,self.height = 320,222
    if flags==16:self.YPLUS = 0
    if flags==17:self.YPLUS = 0;self.width,self.height=320,222
    self.surface = __Surface(self.width,self.height)
    self.__refresh_screen()
    return self.surface

  def flip(self)->None:
    """ Update display """
    wait_vblank()
    [fl(*rect) for rect in self.surface.to_do["rect"]]
    [fc(*circle) for circle in self.surface.to_do["circle"]]
    [dl(*line) for line in self.surface.to_do["line"]]
    return

  def get_surface(self)->__Surface:
    """ Return self.surface """
    return self.surface

class draw:
  @staticmethod
  def rect(surface: __Surface, color: tuple | str, rect: Rect | tuple)->None:
    """ Drawing a rect on a surface """
    Check._color(color)
    Check._rect(rect)
    surface.to_do["rect"].append(rect._get_infos(display.YPLUS)+(color,))
    return

  @staticmethod
  def circle(surface: __Surface, color: tuple | str, pos: tuple, radius: int, width: int = 0)->None:
    """ Drawing a circle on a surface """
    Check._color(color)
    Check._int(radius,width)
    Check._tuple(pos)
    surface.to_do["circle"].append((pos[0],pos[1]+display.YPLUS,radius,color))
    return

  @staticmethod
  def line(surface: __Surface, color: tuple | str, startpos: tuple, endpos: tuple)->None:
    """ Drawing a line on a surface """
    Check._color(color)
    Check._tuple(startpos,endpos)
    surface.to_do["line"].append((startpos[0],startpos[1]+display.YPLUS,endpos[0],endpos[1]+display.YPLUS,color))
    return

class Rect:
  def __init__(self, x: int, y: int, width: int, height: int)->None:
    """ Class for Rect objects """
    self.x,self.y = x,y
    self.width,self.height = width,height

  def __str__(self)->None:
    """ Return Rect """
    return "Rect({%s}, {%s}, {%s}, {%s})"%(self.x,self.y,self.width,self.height)

  def _get_infos(self, yplus: int = 0)->tuple:
    """ Return tuplize rect """
    Check._int(yplus)
    return (self.x,self.y+yplus,self.width,self.height)

  def move(self, x: int, y: int) -> Rect:
    """ Move itself by x,y """
    Check._int(x,y)
    return Rect(self.x+x,self.y+y,self.width,self.height)

  def move_to(self, x: int, y: int) -> None:
    """ Move itself at x,y """
    Check._int(x,y)
    self.x,self.y=x,y
    return

  def colliderect(self, other: Rect)->bool:
    """ Return if itself is in collision with another rect """
    return mu.colliderect((self.x,self.y,self.width,self.height),(other.x,other.y,other.width,other.height))

class key:
  @staticmethod
  def get_pressed()->dict:
    """ Get all keys and their status """
    return {key:keydown(key) for key in LOC_KEYS_}

################## assignements ###########

display = Display()