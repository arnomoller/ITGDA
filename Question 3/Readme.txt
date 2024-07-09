# 3D Object Display Application

## Description
This application displays 3D objects (cube, triangular pyramid, and triangular prism) on the screen using OpenGL and PyGame. The user can cycle through the models with a key press, displaying one object at a time in the center of the screen. The user can also translate the objects along the x, y, and z axes using specific keys.

## Controls
- **SPACE**: Cycle through the 3D objects (cube, pyramid, prism).
- **Arrow Keys**: Translate the object on the x and y axes.
  - **LEFT ARROW**: Translate left (negative x direction).
  - **RIGHT ARROW**: Translate right (positive x direction).
  - **UP ARROW**: Translate up (positive y direction).
  - **DOWN ARROW**: Translate down (negative y direction).
- **Page Up/Page Down**: Translate the object on the z axis.
  - **PAGE UP**: Translate forward (positive z direction).
  - **PAGE DOWN**: Translate backward (negative z direction).
- **Close Window**: Quit the application.

## Requirements
- Python 3.x
- PyGame
- PyOpenGL

## Installation
1. Install the required packages:
   ```bash
   pip install pygame PyOpenGL

### Explanation

- **`translate_obj` function**: Updates the current translation vector for the object.
- **Key Events in `main_loop`**:
  - Arrow keys for translating along the x and y axes.
  - Page Up/Page Down keys for translating along the z axis.
  - Spacebar to cycle through the objects while maintaining their translation.
- **Translation Applied**: `glTranslatef(*self.translation)` ensures that the current translation is applied to the object being drawn.

By following these steps, you can translate the objects and cycle through them while keeping the translations consistent.
