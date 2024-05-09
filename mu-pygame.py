## mu pygame  - Kojiverse Productions
## Snapshot :: 0.2
## Will work on any numworks OS
## (for now, just worked on mu 1.4.3)

################## imports ################

from kandinsky import fill_rect as fl,fill_circle as fc,draw_string as dr,draw_line as dl,wait_vblank
from ion import *
import time as sys_time

################## const ##################

K_OK = KEY_OK; K_BACK = KEY_BACK; K_LEFT = KEY_LEFT; K_RIGHT = KEY_RIGHT; K_UP = KEY_UP; K_DOWN = KEY_DOWN

LOC_KEYS_ = (K_OK,K_DOWN,K_UP,K_RIGHT,K_LEFT)

FULLSCREEN = 0x00000001
NOFRAME    = 0x00000010
QUIT       = 0x10000000
KEYDOWN    = 0x00000100
KEYUP      = 0x00000200

__all__ = [
  "Display",
  "Display.set_mode",
  "Display.set_caption",
  "Display.flip",
  "Surface",
  "Surface.fill"
  "Rect",
  "Rect.colliderect",
  "Rect.move_to",
  "Rect.move",
  "draw",
  "draw.rect",
  "draw.line",
  "draw.circle",
  "time",
  "time.delay",
  "time.Clock",
  "Clock",
  "Clock.tick",
  "Clock.get_fps"
  "key",
  "key.get_pressed",
]

################## utils ##################

presses = {key:[None,None] for key in LOC_KEYS_}

def presses_update():
  for key in presses.keys():
    presses[key][-2]=presses[key][-1]
    presses[key][-1]=keydown(key)

click = lambda key:presses[key][-1] and not presses[key][-2]
release = lambda key:presses[key][-2] and not presses[key][-1]

################## class ##################

class init:
  def __init__(self)->None:
    """ Init but idk what the fuck this func is supposed to do in the original pygame """
    return

class Surface:
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
      if type(i)!=Rect:
        raise ValueError("A pygame.Rect object was expected instead of %s"%i)
    return

  def _tuple(*args)->None:
    """ Check if args are tuples """
    for i in args:
      if type(i)!=tuple:
        raise ValueError("A tuple was expected instead of %s"%i)
    return

  def _surface(*args)->None:
    for i in args:
      if type(i)!=Surface:
        raise ValueError("A pygame.Surface object was expected instead of %s"%i)
    return

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
    if not self.surface:
      fl(0,self.YPLUS,self.width,self.height,"#000000")
    if self.YPLUS:
      fl(0,0,self.width,self.YPLUS,"#ffffff")
      dr(self.caption[:self.width//10-1],5,0)
    return

  def set_caption(self, caption: str)->None:
    """ Set display's caption """
    self.caption = caption
    self.__refresh_screen()
    return

  def set_mode(self, size: tuple, flags: int = 0)->Surface:
    """ Create an Surface object """
    self.width,self.height = size
    Check._int(self.width,self.height)
    if flags & NOFRAME:
      self.YPLUS = 0
    if flags & FULLSCREEN:
      self.width = 320
      self.height = 222-self.YPLUS
    if self.height+self.YPLUS>222:
      self.height = 222

    self.surface = Surface(self.width,self.height)
    self.__refresh_screen()
    return self.surface

  def flip(self)->None:
    """ Update display """
    self.__refresh_screen()
    wait_vblank()
    [fl(*rect) for rect in self.surface.to_do["rect"]]
    [fc(*circle) for circle in self.surface.to_do["circle"]]
    [dl(*line) for line in self.surface.to_do["line"]]
    self.surface.to_do = {"rect":list(),"circle":list(),"line":list(),"polygon":list()}
    return

  def get_surface(self)->__Surface:
    """ Return self.surface """
    return self.surface

class draw:
  @staticmethod
  def rect(surface: Surface, color: tuple | str, rect: Rect | tuple)->None:
    """ Drawing a rect on a surface """
    Check._color(color)
    Check._rect(rect)
    surface.to_do["rect"].append(rect._get_infos(display.YPLUS)+(color,))
    return

  @staticmethod
  def circle(surface: Surface, color: tuple | str, pos: tuple, radius: int, width: int = 0)->None:
    """ Drawing a circle on a surface """
    Check._color(color)
    Check._int(radius,width)
    Check._tuple(pos)
    surface.to_do["circle"].append((pos[0],pos[1]+display.YPLUS,radius,color))
    return

  @staticmethod
  def line(surface: Surface, color: tuple | str, startpos: tuple, endpos: tuple)->None:
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

class time:
  @staticmethod
  def Clock()->Clock:
    """ Returning pygame.Clock object """
    return Clock()

  @staticmethod
  def delay(delay: int)->None:
    """ Stop for speciefieds milliseconds """
    sys_time.sleep(delay/1000)
    return

class Clock:
  def __init__(self)->None:
    """ Class for pygame.clock objec """
    self.start_time = sys_time.monotonic()
    self.last_elapse = None
    self.elapsed_time = []
    return

  def tick(self, fps: int = 60)->None:
    """ Wait for targeted fps """
    if not self.last_elapse:
      self.last_elapse = self.start_time
    while sys_time.monotonic() - self.last_elapse < 1/fps:
      pass
    self.elapsed_time.append(sys_time.monotonic() - self.last_elapse)
    if len(self.elapsed_time)>30:
      del self.elapsed_time[0]
    self.last_elapse = sys_time.monotonic()
    return

  def get_fps(self)->float:
    """ Returning average clock FPS (based on last 30 values)"""
    return 1/((sum(self.elapsed_time)/len(self.elapsed_time)+0.00001)+0.00001)

################## assignements ###########

display = Display()
event = Events()
