# Agent Guidelines for Particle Pinball Project

## Build/Lint/Test Commands
- Install dependencies: `pip install -r requirements.txt`
- Run tests: `python -m pytest tests/`
- Run single test: `python -m pytest tests/test_file.py::test_function`
- Lint code: `python -m flake8 .`
- Type check: `python -m mypy .`

## Code Style Guidelines
- Use snake_case for variables and functions
- Use PascalCase for classes
- Import standard library first, then third-party, then local modules
- Use type hints consistently
- Keep functions short and focused
- Use docstrings for all public functions and classes
- Handle exceptions appropriately with try/except blocks
- Follow PEP 8 formatting standards

## Development Plan: Hybrid 3D/2D Particle Pinball with Pygame-ce

### Project Architecture Overview
- **3D Visualization**: All board components and the ball rendered in 3D using custom software renderer
- **2D Physics**: All collision detection and physics calculations performed in 2D for simplicity and performance
- **2D Editor**: Level editor is 2D top-down focused, no Z-axis component overlap
- **Custom Engine**: No OpenGL/DirectX - pure Python 3D rendering from scratch using pygame-ce

### Team Structure & Responsibilities

**3D Engine Team (Alex, Olivier)**
- Custom 3D rendering engine implementation
- 3D to 2D projection systems
- Camera controls and viewport management
- 3D object representation and transformation
- Performance optimization for real-time rendering

**Level Editor Team (Florian, Mehdi)**
- 2D level editor interface and tools (top-down view)
- Component creation and manipulation on 2D plane
- Board file format design and serialization
- Physics component integration (ramps as speed modifiers)
- User interaction and workflow design

### Phase 1: Core Engine & Physics Foundation

#### 1.1 Custom 3D Engine (Engine Team)
- Implement 3D to 2D projection (perspective projection matrix)
- Build transformation matrices (translation, rotation, scaling)
- Create camera system with position, rotation, and field of view
- Implement basic 3D object rendering (wireframe then filled polygons)
- Z-buffering for proper depth sorting
- Basic lighting model (flat shading)

#### 1.2 2D Physics System (Both Teams)
- Vector2D class with all operations
- Ball class with 2D position, velocity, acceleration
- Force system (gravity, collision forces)
- Collision detection algorithms (circle-line, circle-circle, circle-polygon)
- Integration methods (Euler, Verlet integration)
- Coefficient of restitution and friction modeling

### Phase 2: Tech Demo Development

**Critical**: Create individual tech demos for each interaction type to validate physics and rendering:

#### 2.1 Falling Demo
- Ball affected by gravity and board inclination
- Adjustable board angle to test different gravity effects
- Visual feedback of velocity and acceleration vectors
- Energy conservation validation

#### 2.2 Collision Response Demo
- Ball hitting static obstacles (walls, bumpers)
- Different material properties (bounce, friction)
- Momentum and energy conservation verification
- Visual collision normal and response vectors

#### 2.3 Flipper Mechanics Demo
- Animated flipper collision detection
- Timing and force application
- Ball trajectory prediction
- Multiple flipper configurations

#### 2.4 Ramp System Demo
- Ball speed modification based on ramp profiles
- Acceleration/deceleration zones
- Visual feedback of speed changes
- Transition between different speed zones

#### 2.5 Advanced Interactions Demo
- Spinner mechanisms
- Multi-ball interactions
- Magnetic fields (if implemented)
- Special effects (particle systems)

### Phase 3: Component Integration

#### 3.1 2D Editor Architecture (Editor Team)
- 2D top-down viewport with mouse controls (pan: drag, zoom: scroll)
- Grid system with snapping
- Object selection and transformation gizmos (2D only)
- Component library with pre-built pinball elements
- Ramp profile editor for speed/acceleration curves
- Visual preview of 3D appearance in separate window

#### 3.2 Rendering-Physics Bridge (Both Teams)
- 3D object to 2D physics shape mapping
- Coordinate system transformation
- Visual debugging overlay (show 2D physics shapes on 3D view)
- Performance optimization strategies

### Phase 4: File Format & Data Management

#### 4.1 Board File Format (.ppb)
```json
{
  "version": "1.0",
  "metadata": {
    "name": "Board Name",
    "author": "Author Name",
    "description": "Board description"
  },
  "board": {
    "dimensions": {"width": 10, "height": 15, "depth": 8},
    "inclination": {"x": 0, "z": 15},  // Board tilt angles
    "gravity": 9.81,
    "objects": [
      {
        "type": "obstacle",
        "geometry": "box",
        "position_3d": [5, 2, 0],
        "rotation_3d": [0, 0, 0],
        "scale_3d": [2, 1, 0.5],
        "physics_2d": {
          "shape": "rectangle",
          "vertices": [[0, 0], [2, 0], [2, 1], [0, 1]],
          "material": {"bounce": 0.8, "friction": 0.3},
          "speed_modifier": 1.0  // For ramps: >1.0 = accelerate, <1.0 = decelerate
        },
        "visual": {"color": [255, 0, 0], "wireframe": false}
      }
    ],
    "zones": [...]
  }
}
```

#### 4.2 Serialization System
- JSON parser/writer with validation
- Schema validation for board files
- Version compatibility handling
- Import/export utilities

### Phase 5: Game Implementation

#### 5.1 Game Objects Integration
- Ball with 3D rendering and 2D physics
- Flippers with animation and collision
- Bumpers with visual feedback
- Scoring zones and triggers

#### 5.2 Game Systems
- Input handling (keyboard for flippers, mouse for plunger)
- Game state management
- Scoring and combo system
- Sound integration (if time permits)

### Phase 6: Advanced Features

#### 6.1 Visual Enhancements
- Basic lighting and shading
- Particle effects for collisions
- Smooth animations and transitions

#### 6.2 Editor Enhancements
- Real-time physics preview
- Component scripting interface
- Board templates and presets
- Performance profiling tools

### Technical Implementation Details

**Hybrid 3D/2D Architecture:**
- **3D Rendering**: Custom software renderer using pygame-ce for surface management
- **2D Physics**: All collision detection and physics calculations in 2D space
- **Coordinate Mapping**: 3D visual positions map to 2D physics positions
- **Performance**: Separate rendering and physics update loops for optimization

**3D Rendering Approach:**
- Use pygame-ce for 2D surface management
- Implement software 3D renderer with polygon rasterization
- Use NumPy for vector/matrix operations
- Z-buffering for proper depth sorting
- Basic lighting model (flat shading with normals)

**2D Physics Approach:**
- Separate 2D coordinate system for physics calculations
- Circle-based collision detection for the ball
- Polygon-based collision for obstacles
- Speed modifier zones for ramps (no actual 3D incline physics)
- Efficient spatial partitioning for performance
- Verlet integration for stable physics

**Project Structure:**
```
particlespinball/
├── src/
│   ├── engine/          # 3D rendering engine (Engine Team)
│   │   ├── renderer/    # Core rendering pipeline
│   │   ├── camera/      # Camera system
│   │   ├── objects/     # 3D object representations
│   │   └── math3d/      # 3D mathematics utilities
│   ├── physics/         # 2D physics simulation (Shared)
│   │   ├── core/        # Physics engine core
│   │   ├── collisions/  # Collision detection algorithms
│   │   └── integrators/ # Integration methods
│   ├── editor/          # Level editor (Editor Team)
│   │   ├── ui/          # User interface components
│   │   ├── tools/       # Editing tools
│   │   ├── components/  # Pre-built components
│   │   ├── viewport/    # 2D viewport management
│   │   └── ramp_editor/ # Ramp profile editor
│   ├── game/            # Game logic (Shared)
│   │   ├── objects/     # Game objects
│   │   ├── systems/     # Game systems
│   │   └── input/       # Input handling
│   ├── file_formats/    # File I/O (Editor Team)
│   │   ├── json/        # JSON format handling
│   │   └── validation/  # Schema validation
│   └── demos/           # Tech demos (Both Teams)
│       ├── falling/     # Falling physics demo
│       ├── collisions/  # Collision response demo
│       ├── flippers/    # Flipper mechanics demo
│       └── ramps/       # Ramp system demo
├── assets/              # Textures, sounds, models
├── boards/              # Saved board files
├── tests/               # Unit tests
│   ├── engine/         # Engine tests
│   ├── physics/        # Physics tests
│   └── editor/         # Editor tests
└── docs/                # Documentation
    ├── api/            # API documentation
    ├── tutorials/      # Tutorial files
    └── specifications/ # Technical specifications
```

# TEAM RESPONSIBILITIES

## 3D Engine Team (Alex, Olivier)
**Primary Focus**: Custom 3D rendering engine from scratch
**Key Deliverables**:
- 3D to 2D projection system
- Camera controls and viewport management
- 3D object rendering pipeline
- Performance optimization for real-time rendering
- Integration with physics system

**Technical Knowledge to Acquire**:
- 3D transformation matrices and linear algebra
- Perspective projection mathematics
- Z-buffering and depth sorting algorithms
- Polygon rasterization techniques
- Basic lighting models and shading

## Level Editor Team (Florian, Mehdi)
**Primary Focus**: 2D level editor and component system
**Key Deliverables**:
- 2D top-down editor interface and tools
- Component creation and manipulation system
- Board file format design and serialization
- Physics component integration (ramps as speed modifiers)
- User workflow and interaction design
- Ramp profile editor for speed curves

**Technical Knowledge to Acquire**:
- 2D user interface design patterns
- Object selection and transformation gizmos
- File format design and validation
- Component-based architecture
- User experience design for 2D editors
- Speed modifier physics implementation

## SHARED RESPONSIBILITIES
**Tech Demo Development**: Both teams collaborate on creating individual tech demos for each interaction type
**Integration**: Coordinate between 3D rendering and 2D physics systems
**Testing**: Ensure cross-team compatibility and performance
**Documentation**: Maintain comprehensive documentation for all systems

## DEVELOPMENT WORKFLOW
1. **Week 1-2**: Core engine and physics foundation development
2. **Week 3-4**: Individual tech demo creation and validation
3. **Week 5-6**: Component integration and editor development
4. **Week 7-8**: Game implementation and polish
5. **Week 9-10**: Testing, optimization, and documentation

## KEY TECHNICAL CHALLENGES & SOLUTIONS

### Challenge 1: 3D Rendering Performance
**Problem**: Software-based 3D rendering can be slow
**Solutions**:
- Implement spatial partitioning for culling
- Use efficient polygon rasterization algorithms
- Optimize matrix operations with NumPy
- Implement level-of-detail systems

### Challenge 2: 3D/2D Coordinate Mapping
**Problem**: Maintaining consistency between 3D visual and 2D physics coordinates
**Solutions**:
- Create unified coordinate transformation system
- Implement visual debugging overlays
- Design clear API for coordinate conversion
- Use transformation matrices for consistency

### Challenge 3: Real-time Physics Performance
**Problem**: Complex collision detection can be computationally expensive
**Solutions**:
- Implement spatial partitioning (grid or quadtree)
- Use efficient collision algorithms
- Optimize with early rejection tests
- Separate physics and rendering update loops

### Challenge 4: Editor Usability
**Problem**: 2D editing needs to be intuitive while representing 3D concepts
**Solutions**:
- Implement intuitive 2D camera controls
- Use visual gizmos for 2D transformations
- Include snapping and grid systems
- Provide visual preview of 3D appearance
- Create intuitive ramp profile editing interface

## USEFUL LIBRARIES & TOOLS
- **NumPy**: For efficient vector/matrix operations
- **Pygame-ce**: For 2D surface management and input handling
- **JSON Schema**: For board file validation
- **Matplotlib**: For physics debugging and visualization
- **Pytest**: For comprehensive testing framework

## LEARNING RESOURCES
- **3D Graphics**: "Computer Graphics: Principles and Practice" by Foley et al.
- **Physics**: "Game Physics Engine Development" by Ian Millington
- **Linear Algebra**: Khan Academy or 3Blue1Brown for intuitive understanding
- **Pygame**: Official documentation and community tutorials
- **Software Rendering**: "Building a 3D Engine in Python" tutorials
