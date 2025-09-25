"""
Keeps global values that can be accessed anywhere in the application.
They can be constants or variables.
Can be seen as the application global state.
"""

# Real-world to pixel scale (pixels per meter)
PIXEL_PER_METER = 100

# Time scale factor (simulation speed)
time_scale = 1.0

# Frame rate for physics calculations
FPS = 60
DT = 1.0 / FPS  # Time step in seconds

# Forces
GRAVITY = 9.81
