# Agent Guidelines

## Commands
- `make install` - Install dependencies in virtual environment
- `make run` - Run the application
- `make lint` - Run code linting with ruff
- `make format` - Format code with ruff
- `pytest tests/` - Run all tests
- `pytest tests/test_file.py` - Run single test file
- `pytest tests/test_file.py::test_name` - Run specific test

## Code Style
- **Imports**: Absolute imports from project root (`from utils.color import Color`)
- **Types**: Type hints required (`position: Vector2`, `screen: pygame.Surface`)
- **Naming**: PascalCase classes, snake_case variables/methods, UPPER_CASE constants
- **Docstrings**: Triple quotes for all classes and methods
- **Line Length**: Max 100 characters (enforced by ruff)
- **Quotes**: Single quotes for strings (enforced by ruff)
- **Indent**: Spaces only (enforced by ruff)

## Architecture
- MVC pattern with views in `views/`, objects in `objects/`, core in `core/`
- Physics constants in `core/world.py`
- Use SI units where possible, pygame coordinates for rendering
- Sprite-based rendering with pygame sprite groups