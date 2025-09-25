# API Documentation

This document provides detailed API documentation for the key classes and methods in the Particle Pinball project.

## Table of Contents

1. [Core Classes](#core-classes)
2. [Game Objects](#game-objects)
3. [Views](#views)
4. [Utilities](#utilities)

---

## Core Classes

### App

The main application class that handles pygame initialization and the main game loop.

#### Constructor
```python
App(width=800, height=600, fullscreen=True, filename=None)
```

**Parameters:**
- `width` (int): Window width (default: 800)
- `height` (int): Window height (default: 600)
- `fullscreen` (bool): Whether to start in fullscreen mode (default: True)
- `filename` (str): Optional filename parameter (default: None)

#### Methods

##### `run()`
Runs the main application loop.

**Returns:** None

**Description:**
Handles events, updates views, and renders the screen at 60 FPS. Exits on QUIT event or ESC key press.

---

## Game Objects

### Ball

A ball object with physics properties for the pinball game.

#### Constructor
```python
Ball(x=0, y=0, radius=10, mass=1.0, bounciness=0.8, color=Color.RED)
```

**Parameters:**
- `x` (float): Initial x position of the ball
- `y` (float): Initial y position of the ball
- `radius` (int): Radius of the ball in pixels
- `mass` (float): Mass of the ball in kilograms
- `bounciness` (float): Coefficient of restitution (0 to 1)
- `color` (tuple): RGB color of the ball

#### Properties

##### `x` (float)
The current x position of the ball.

##### `y` (float)
The current y position of the ball.

##### `radius` (int)
The radius of the ball in pixels.

##### `mass` (float)
The mass of the ball in kilograms.

##### `bounciness` (float)
The coefficient of restitution (0 to 1), where 1.0 is perfectly elastic and 0.0 is perfectly inelastic.

##### `velocity` (Vector2)
The current velocity vector of the ball in pixels/second.

##### `forces` (list[Vector2])
List of force vectors currently acting on the ball.

#### Methods

##### `update()`
Updates the ball's position based on its velocity.

**Returns:** None

**Description:**
Applies the current velocity to the ball's position using Euler integration: `x(t+Δt) = x(t) + v(t)Δt`

##### `draw(screen)`
Draws the ball on the screen.

**Parameters:**
- `screen` (pygame.Surface): The surface to draw the ball on

**Returns:** None

##### `set_velocity(velocity)`
Sets the ball's velocity.

**Parameters:**
- `velocity` (Vector2): The new velocity vector for the ball

**Returns:** None

##### `apply_forces()`
Calculates a new velocity based on all forces applied to the ball.

**Returns:** None

**Description:**
Applies Newton's second law (F = ma) to calculate acceleration from the sum of all forces, then updates velocity using Euler integration. Clears the forces list after application.

##### `add_force(force)`
Adds a force to the ball's force list.

**Parameters:**
- `force` (Vector2): The force vector to add to the ball

**Returns:** None

**Description:**
The force will be applied in the next physics update when `apply_forces()` is called.

### Board

The game board that contains all walls and defines the play area.

#### Constructor
```python
Board(boundaries=None, ball=None, components=None, inclination=1.0)
```

**Parameters:**
- `boundaries` (list[Wall]): List of walls defining the board edges
- `ball` (Ball): The ball object on the board
- `components` (list[Sprite]): List of additional components on the board
- `inclination` (float): Board inclination angle modifier

**Properties**

##### `boundaries` (Group)
Sprite group containing all boundary walls.

##### `ball` (Ball)
The ball object on the board.

##### `components` (Group)
Sprite group containing additional components.

##### `inclination` (float)
Board inclination angle modifier for gravity calculations.

#### Methods

##### `draw(surface)`
Draws the board and its boundaries on the given surface.

**Parameters:**
- `surface` (pygame.Surface): The surface to draw the board on

**Returns:** None

##### `update()`
Updates the board's state.

**Returns:** None

**Description:**
Updates all components on the board, including the ball and any other dynamic objects.

##### `add_component(component)`
Adds a component to the board.

**Parameters:**
- `component` (Sprite): The component to add to the board

**Returns:** None

##### `remove_component(component)`
Removes a component from the board.

**Parameters:**
- `component` (Sprite): The component to remove from the board

**Returns:** None

### Wall

A wall object that serves as a boundary or obstacle in the pinball game.

#### Constructor
```python
Wall(x, y, width, height, color=Color.WHITE)
```

**Parameters:**
- `x` (int): The x-coordinate of the wall's top-left corner
- `y` (int): The y-coordinate of the wall's top-left corner
- `width` (int): The width of the wall in pixels
- `height` (int): The height of the wall in pixels
- `color` (tuple): RGB color tuple for the wall (default: white)

### Peg

A small round object that acts as a passive obstacle.

#### Constructor
```python
Peg(position, radius, color=(255, 255, 255))
```

**Parameters:**
- `position` (Vector2): The center position of the peg
- `radius` (int): The radius of the peg in pixels
- `color` (tuple): RGB color tuple for the peg (default: white)

#### Methods

##### `draw(screen)`
Draws the peg on the screen.

**Parameters:**
- `screen` (pygame.Surface): The surface to draw the peg on

**Returns:** None

##### `update()`
Updates the peg's state.

**Returns:** None

**Description:**
Since pegs are static obstacles, this method does nothing.

### Bumper

A round obstacle that pushes back the ball with a given strength.

#### Constructor
```python
Bumper(position, radius, strength=1.0, color=(255, 255, 255))
```

**Parameters:**
- `position` (Vector2): The center position of the bumper
- `radius` (int): The radius of the bumper in pixels
- `strength` (float): The force multiplier applied to the ball on collision
- `color` (tuple): RGB color tuple for the bumper (default: white)

#### Properties

##### `strength` (float)
The force multiplier applied to the ball on collision.

#### Methods

##### `draw(screen)`
Draws the bumper on the screen.

**Parameters:**
- `screen` (pygame.Surface): The surface to draw the bumper on

**Returns:** None

##### `update()`
Updates the bumper's state.

**Returns:** None

**Description:**
Since bumpers are static obstacles, this method does nothing. The force application is handled during collision detection.

---

## Views

### View

Base class for all views in the application.

#### Methods

##### `handle_event(event)`
Handles a pygame event.

**Parameters:**
- `event` (Event): The pygame event to handle

**Returns:** View - The view to switch to (usually self)

##### `update()`
Updates the view's state.

**Returns:** None

##### `draw(screen)`
Draws the view on the screen.

**Parameters:**
- `screen` (pygame.Surface): The surface to draw on

**Returns:** None

### HomeView

The home/landing screen view of the application with interactive navigation buttons.

#### Constructor
```python
HomeView(width, height, font)
```

**Parameters:**
- `width` (int): Screen width
- `height` (int): Screen height
- `font` (pygame.font.Font): Font for rendering text

**Description:**
Creates an interactive home screen with buttons for navigating to different views. Automatically detects available views and creates clickable buttons with keyboard shortcuts.

#### Properties

##### `available_views` (list)
List of dictionaries containing view information:
- `name` (str): Display name for the view
- `class` (class): View class to instantiate
- `key` (int): Pygame key code for keyboard shortcut

##### `buttons` (list)
List of button dictionaries containing:
- `rect` (Rect): Button rectangle for collision detection
- `view_info` (dict): Associated view information
- `hover` (bool): Whether mouse is hovering over the button

#### Methods

##### `draw(screen)`
Draws the home view on the screen with interactive buttons.

**Parameters:**
- `screen` (pygame.Surface): The surface to draw on

**Returns:** None

**Description:**
Renders the home screen with title, subtitle, interactive buttons with hover effects, keyboard shortcuts, and user instructions. Buttons change color when hovered over.

##### `handle_event(event)`
Handles pygame events for the home view including mouse clicks and keyboard shortcuts.

**Parameters:**
- `event` (pygame.event.Event): The event to handle

**Returns:** View - HomeView or selected view if a button is clicked/key is pressed

**Description:**
Processes both keyboard shortcuts (1, 2, etc.) and mouse clicks on buttons. Returns the appropriate view instance when a selection is made.

### GameView

The main game view for the complete pinball game experience.

#### Constructor
```python
GameView()
```

**Description:**
Initializes the game view with board, ball, and input handling. Sets up the game board with boundary walls, creates the ball, initializes input key states, and prepares sprite groups for efficient rendering and collision detection.

#### Methods

##### `update()`
Updates the game state including ball physics.

**Returns:** GameView - Self for view chaining

**Description:**
Handles the game logic updates including physics calculations, collision detection, and game state management.

##### `handle_event(event)`
Handles pygame events for the game view.

**Parameters:**
- `event` (pygame.event.Event): The event to handle

**Returns:** GameView - Self for view chaining

##### `draw(screen)`
Draws the game view on the screen.

**Parameters:**
- `screen` (pygame.Surface): The surface to draw on

**Returns:** None

### FallingBallView

A demonstration view showing a ball falling under gravity.

#### Constructor
```python
FallingBallView()
```

**Description:**
Creates a ball, board with boundaries, and sets up the physics simulation for the falling ball demonstration.

#### Methods

##### `update()`
Updates the falling ball simulation state.

**Returns:** FallingBallView - Self for view chaining

**Description:**
Applies gravity to the ball and updates the position of all objects. The ball's velocity is set based on gravity and board inclination.

##### `handle_event(event)`
Handles pygame events for the falling ball view.

**Parameters:**
- `event` (pygame.event.Event): The event to handle

**Returns:** FallingBallView - Self for view chaining

##### `draw(screen)`
Draws the falling ball view on the screen.

**Parameters:**
- `screen` (pygame.Surface): The surface to draw on

**Returns:** None

##### `create_board_boundaries_group()`
Creates and returns a group of wall boundaries for the board.

**Returns:** pygame.sprite.Group - A sprite group containing all boundary walls

**Description:**
Creates four walls (left, right, top, bottom) that form the boundaries of the playing area for the falling ball demonstration.

##### `create_board_objects_group()`
Creates and returns a group of interactive objects on the board.

**Returns:** pygame.sprite.Group - A sprite group containing all interactive objects

**Description:**
Currently includes only the ball, but can be extended to include other interactive objects like pegs, bumpers, etc.

---

## Utilities

### Color

A collection of predefined color constants for the game.

#### Constants

##### Primary Colors
- `RED` = (255, 0, 0)
- `GREEN` = (0, 255, 0)
- `BLUE` = (0, 0, 255)

##### Secondary Colors
- `YELLOW` = (255, 255, 0)
- `PURPLE` = (128, 0, 128)
- `ORANGE` = (255, 165, 0)
- `TURQUOISE` = (64, 224, 208)

##### Neutral Colors
- `WHITE` = (255, 255, 255)
- `BLACK` = (0, 0, 0)
- `GREY` = (128, 128, 128)

---

## Physics Constants

### GRAVITY

```python
GRAVITY = 9.81  # m/s²
```

The gravitational acceleration constant used in physics calculations. This value is modified by board inclination to create the effect of a tilted pinball table.

---

## Usage Examples

### Creating a Ball
```python
from objects.ball import Ball
from utils.colors import Color

# Create a red ball at position (100, 100)
ball = Ball(x=100, y=100, radius=10, mass=1.0, bounciness=0.8, color=Color.RED)
```

### Creating a Board
```python
from objects.board import Board
from objects.wall import Wall
from objects.ball import Ball

# Create walls
walls = [
    Wall(x=50, y=50, width=10, height=400),
    Wall(x=450, y=50, width=10, height=400),
    Wall(x=50, y=50, width=400, height=10),
    Wall(x=50, y=450, width=400, height=10)
]

# Create ball
ball = Ball(x=250, y=250, radius=8, mass=1.0, bounciness=0.8)

# Create board
board = Board(boundaries=walls, ball=ball, inclination=0.5)
```

### Applying Forces to a Ball
```python
from pygame import Vector2

# Add gravity force
gravity_force = Vector2(0, 9.81 * ball.mass)
ball.add_force(gravity_force)

# Apply all forces and update velocity
ball.apply_forces()
```

### Creating Different Views
```python
from views.home_view import HomeView
from views.game_view import GameView
from views.falling_ball_view import FallingBallView

# Create different views
home_view = HomeView(width=800, height=600, font=font)
game_view = GameView()
falling_view = FallingBallView()
```

This API documentation provides a comprehensive reference for all major classes and methods in the Particle Pinball project. For more detailed information about physics implementations and demo scenarios, see the `physics_demo_catalog.md` file.