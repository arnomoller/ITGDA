import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from Cube import vertices as cube_vertices, edges as cube_edges
from Pyramid import vertices as pyramid_vertices, edges as pyramid_edges
from Prism import vertices as prism_vertices, edges as prism_edges

class Display:
    def __init__(self):
        self.objects = [
            (cube_vertices, cube_edges),
            (pyramid_vertices, pyramid_edges),
            (prism_vertices, prism_edges)
        ]
        self.current_object = 0
        self.translation = [0, 0, 0]
        self.init_pygame()
        self.main_loop()

    def init_pygame(self):
        pygame.init()
        self.display = (800, 600)
        pygame.display.set_mode(self.display, DOUBLEBUF | OPENGL)
        gluPerspective(45, (self.display[0] / self.display[1]), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -5)

    def draw_object(self, vertices, edges):
        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
        glEnd()

    def translate_obj(self, dx, dy, dz):
        self.translation[0] += dx
        self.translation[1] += dy
        self.translation[2] += dz

    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.current_object = (self.current_object + 1) % len(self.objects)
                    elif event.key == pygame.K_LEFT:
                        self.translate_obj(-0.1, 0, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.translate_obj(0.1, 0, 0)
                    elif event.key == pygame.K_UP:
                        self.translate_obj(0, 0.1, 0)
                    elif event.key == pygame.K_DOWN:
                        self.translate_obj(0, -0.1, 0)
                    elif event.key == pygame.K_PAGEUP:
                        self.translate_obj(0, 0, 0.1)
                    elif event.key == pygame.K_PAGEDOWN:
                        self.translate_obj(0, 0, -0.1)

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            vertices, edges = self.objects[self.current_object]
            glPushMatrix()
            glTranslatef(*self.translation)
            # glRotatef(pygame.time.get_ticks() * 0.05, 1, 1, 1)  # Remove this line to stop rotation
            self.draw_object(vertices, edges)
            glPopMatrix()

            pygame.display.flip()
            pygame.time.wait(10)

if __name__ == "__main__":
    Display()
