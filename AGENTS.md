# Agent Guidelines

## Commands
- `make install` - Install dependencies
- `make run` - Run the application
- `make clean` - Remove virtual environment
- `make reinstall` - Clean and reinstall dependencies

## Code Style
- **Imports**: Use absolute imports from project root (e.g., `from utils.color import Color`)
- **Types**: Use type hints consistently (e.g., `position: Vector2D`, `screen: pygame.Surface`)
- **Naming**: PascalCase for classes, snake_case for variables and methods
- **Docstrings**: Use triple quotes for class descriptions
- **Constants**: UPPER_CASE for constants (e.g., `GRAVITY = 9.81`)
- **Error Handling**: Basic error handling with try/except where appropriate
- **Dependencies**: numpy, pygame-ce (see requirements.txt)
