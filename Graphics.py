import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
try:
	import pygame
except ImportError:
	print("pygame not available")
	pygame = None

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]

# pygame = None

class TextPrint(object):
    """
    This is a simple class that will help us print to the screen
    It has nothing to do with the joysticks, just outputting the
    information.
    """
    def __init__(self):
        """ Constructor """
        self.reset()
        self.x_pos = 10
        self.y_pos = 10
        if pygame == None:
            return
        self.font = pygame.font.SysFont("arial", 24)
 
    def print(self, my_screen, text_string):
        if pygame == None:
            return
        text_bitmap = self.font.render(text_string, True, WHITE)
        my_screen.blit(text_bitmap, [self.x_pos, self.y_pos])
        self.y_pos += self.line_height
 
    def reset(self):
        """ Reset text to the top of the screen. """
        self.x_pos = 10
        self.y_pos = 10
        self.line_height = 20
 
    def indent(self):
        """ Indent the next line of text """
        self.x_pos += 10
 
    def unindent(self):
        """ Unindent the next line of text """
        self.x_pos -= 10


class Graphics:

    screen = None
    clock = None
    textPrint = None
    disabled = True
    keyCallback = None
    mouseCallback = None

    def __init__(self):
        pass

    def init(self, title, size):
        if pygame == None:
            return
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.textPrint = TextPrint()
        self.disabled = False

    def quit(self):
        if pygame == None or self.disabled:
            return
        pygame.quit()

    def setKeyCallback(self, cb):
        self.keyCallback = cb

    def setMouseCallback(self, cb):
        self.mouseCallback = cb 

    def fill(self, color):
        if pygame == None or self.disabled:
            return
        self.screen.fill(color)

    def flip(self):
        if pygame == None or self.disabled:
            return
        pygame.display.flip()
        self.clock.tick(60)
        self.textPrint.reset()

    def fps(self):
        if pygame == None or self.disabled:
            return 0
        return self.clock.get_fps()
    
    def print(self, value):
        if pygame == None or self.disabled:
            return
        self.textPrint.print(self.screen, value)

    def circle(self, x, y, r, color, width):
        if pygame == None or self.disabled:
            return
        pygame.draw.circle(self.screen, color, [int(x), int(y)], int(r), width)

    def line(self, x1, y1, x2, y2, width, color):
        if pygame == None or self.disabled:
            return
        pygame.draw.line(self.screen, color, [x1, y1], [x2, y2], width)

    def processKeys(self, key):
        return {
            pygame.K_a: lambda: "A",
            pygame.K_b: lambda: "B",
            pygame.K_c: lambda: "C",
            pygame.K_d: lambda: "D",
            pygame.K_e: lambda: "E",
            pygame.K_f: lambda: "F",
            pygame.K_g: lambda: "G",
            pygame.K_h: lambda: "H",
            pygame.K_i: lambda: "I",
            pygame.K_j: lambda: "J",
            pygame.K_k: lambda: "K",
            pygame.K_l: lambda: "L",
            pygame.K_m: lambda: "M",
            pygame.K_n: lambda: "N",
            pygame.K_o: lambda: "O",
            pygame.K_p: lambda: "P",
            pygame.K_q: lambda: "Q",
            pygame.K_r: lambda: "R",
            pygame.K_s: lambda: "S",
            pygame.K_t: lambda: "T",
            pygame.K_u: lambda: "U",
            pygame.K_v: lambda: "V",
            pygame.K_w: lambda: "W",
            pygame.K_x: lambda: "X",
            pygame.K_y: lambda: "Y",
            pygame.K_z: lambda: "Z",
        }.get(key, lambda: None)()

    def queryEvents(self):
        if pygame == None or self.disabled:
            return False
        done = False
        for event in pygame.event.get():   # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True   # Flag that we are done so we exit this loop
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if self.mouseCallback != None:
                    self.mouseCallback(pos[0], pos[1])
            elif event.type == pygame.KEYDOWN:
                # Figure out if it was an arrow key. If so
                # adjust speed.
                # see https://www.pygame.org/docs/ref/key.html
                key = None
                if event.key == pygame.K_ESCAPE:
                    done = True 
                else:
                    key = self.processKeys(event.key)
                
                if key != None and self.keyCallback != None:
                    self.keyCallback(key)

        return done
