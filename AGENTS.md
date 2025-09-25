# Agent Guidelines

## Project Overview

Particle Pinball is an educational physics simulation project that implements a pinball game as a platform for experimenting with mathematical and physics concepts. The project uses pygame for graphics and implements custom physics simulation.

## Architecture

### Core Components
- **App**: Main application class handling pygame initialization and main loop
- **Views**: MVC pattern with different views (HomeView, GameView, FallingBallView)
- **Objects**: Game objects (Ball, Board, Wall, Peg, Bumper) with physics properties
- **Core**: Global state and physics constants
- **Utils**: Helper classes and utilities

### Key Design Patterns
- **Model-View-Controller (MVC)**: Separation of game logic, rendering, and input handling
- **Sprite-based Rendering**: Uses pygame's sprite system for efficient rendering
- **Component Architecture**: Modular design allowing easy addition of new game objects

## Commands

### Development Commands
- `make install` - Install dependencies in virtual environment
- `make run` - Run the application
- `make clean` - Remove virtual environment
- `make reinstall` - Clean and reinstall dependencies
- `make requirements` - Generate requirements.txt from current environment

### Testing Commands
- `make test` - Run all tests (when implemented)
- `make lint` - Run code linting with ruff
- `make format` - Format code with ruff

## Code Style

### Python Style Guidelines
- **Imports**: Use absolute imports from project root (e.g., `from utils.color import Color`)
- **Types**: Use type hints consistently (e.g., `position: Vector2`, `screen: pygame.Surface`)
- **Naming**: 
  - PascalCase for classes (e.g., `Ball`, `GameView`)
  - snake_case for variables and methods (e.g., `ball_velocity`, `update_position`)
  - UPPER_CASE for constants (e.g., `GRAVITY = 9.81`)
- **Docstrings**: Use triple quotes for all class and method descriptions
- **Error Handling**: Basic error handling with try/except where appropriate
- **Line Length**: Maximum 100 characters (enforced by ruff)

### Documentation Standards
- **Class Docstrings**: Describe the purpose and main functionality
- **Method Docstrings**: Include Args, Returns, and any important notes
- **Inline Comments**: Explain complex physics calculations and algorithms
- **File Headers**: Brief description of file purpose at the top

### Physics Implementation Guidelines
- **Units**: Use SI units where possible (meters, kilograms, seconds)
- **Constants**: Define physics constants in `core/world.py`
- **Integration**: Use Euler integration for simplicity, document if using other methods
- **Collisions**: Implement proper collision detection and response
- **Performance**: Optimize collision detection with spatial partitioning if needed

## Dependencies

### Core Dependencies
- **pygame-ce**: Graphics and game engine framework
- **numpy**: Mathematical operations and vector calculations

### Development Dependencies
- **ruff**: Code formatting and linting
- **pytest**: Testing framework (to be implemented)

## File Structure Conventions

### Directory Organization
```
src/
├── core/          # Core engine and global state
├── objects/       # Game objects with physics
├── utils/         # Utility classes and helpers
├── views/         # UI views and controllers
└── main.py        # Application entry point
```

### File Naming
- Use snake_case for Python files (e.g., `falling_ball_view.py`)
- Keep files focused on single responsibility
- Group related functionality in the same directory

## Physics Implementation

### Key Physics Concepts
- **Gravity**: `F = mg` with board inclination modifier
- **Velocity**: Vector2 for 2D motion
- **Collisions**: Circle-line and circle-circle detection
- **Energy**: Conservation of energy in collisions
- **Integration**: Euler method for position updates

### Constants and Units
- `GRAVITY = 9.81` m/s²
- Positions in pixels (converted to meters for physics calculations)
- Time in seconds (using pygame's clock for frame timing)
- Mass in kilograms
- Velocity in pixels/second

## Development Workflow

### Adding New Features
1. Create appropriate object class in `objects/`
2. Add physics properties and methods
3. Update view classes to handle new object
4. Add to sprite groups for rendering
5. Test collision detection and response

### Debugging Physics
- Use print statements for velocity and position values
- Visualize vectors with drawing functions
- Check energy conservation in collisions
- Verify boundary conditions

### Performance Considerations
- Use sprite groups for efficient rendering
- Implement spatial partitioning for many objects
- Optimize collision detection algorithms
- Profile frame rate and optimize bottlenecks

## Testing Guidelines

### Unit Testing
- Test individual physics calculations
- Verify collision detection algorithms
- Check energy conservation
- Test boundary conditions

### Integration Testing
- Test complete physics pipeline
- Verify view switching
- Test user input handling
- Check rendering performance

### Acceptance Testing
- Verify game playability
- Test all demo scenarios
- Check performance on target hardware
- Verify mathematical accuracy

## Common Issues and Solutions

### Physics Issues
- **Ball tunneling**: Reduce time step or implement continuous collision detection
- **Energy gain**: Check collision response calculations
- **Instability**: Verify integration method and time steps
- **Jitter**: Implement proper collision resolution

### Rendering Issues
- **Flickering**: Double buffering handled by pygame
- **Performance**: Reduce number of objects or optimize rendering
- **Z-ordering**: Use sprite group draw order
- **Scaling**: Handle different screen resolutions

### Code Quality
- **Linting errors**: Run `make lint` and fix issues
- **Type errors**: Check type hints and imports
- **Style issues**: Run `make format` to fix formatting
- **Documentation**: Update docstrings for new features

## Future Enhancements

### Planned Features
- Particle system integration
- Advanced collision detection
- Multiple integration methods
- Sound effects and music
- Score tracking and game states
- Level editor

### Technical Improvements
- Component-based architecture
- Event system for game events
- Save/load game states
- Network multiplayer support
- Mobile device support

## Contributing

### Pull Request Process
1. Fork the repository
2. Create feature branch
3. Follow code style guidelines
4. Add tests for new features
5. Update documentation
6. Submit pull request with clear description

### Code Review Checklist
- Code follows style guidelines
- All tests pass
- Documentation is updated
- Physics calculations are verified
- Performance impact is considered
- No breaking changes to existing features
