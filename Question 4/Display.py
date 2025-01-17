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
        self.rotation = [0, 0, 0]  # Store rotation angles in degrees
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

    def rotate_obj(self, dx, dy, dz):
        self.rotation[0] += dx
        self.rotation[1] += dy
        self.rotation[2] += dz

    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.current_object = (self.current_object + 1) % len(self.objects)
                        # Keep current rotation and translation when swapping objects
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
                    elif event.key == pygame.K_w:
                        self.rotate_obj(1, 0, 0)  # Rotate around x-axis positively
                    elif event.key == pygame.K_s:
                        self.rotate_obj(-1, 0, 0)  # Rotate around x-axis negatively
                    elif event.key == pygame.K_a:
                        self.rotate_obj(0, 1, 0)  # Rotate around y-axis positively
                    elif event.key == pygame.K_d:
                        self.rotate_obj(0, -1, 0)  # Rotate around y-axis negatively
                    elif event.key == pygame.K_q:
                        self.rotate_obj(0, 0, 1)  # Rotate around z-axis positively
                    elif event.key == pygame.K_e:
                        self.rotate_obj(0, 0, -1)  # Rotate around z-axis negatively

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            # Apply transformations
            glPushMatrix()
            glTranslatef(*self.translation)
            glRotatef(self.rotation[0], 1, 0, 0)
            glRotatef(self.rotation[1], 0, 1, 0)
            glRotatef(self.rotation[2], 0, 0, 1)

            # Draw current object
            vertices, edges = self.objects[self.current_object]
            self.draw_object(vertices, edges)

            glPopMatrix()

            pygame.display.flip()
            pygame.time.wait(10)

if __name__ == "__main__":
    Display()
