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

## Development Plan: 3D Particle Pinball with Pygame-ce

### Phase 1: 3D Rendering Foundation
1. **Custom 3D Engine**
   - Implement 3D to 2D projection (perspective and orthographic)
   - Build transformation matrices (translation, rotation, scaling)
   - Create camera system with position, rotation, and field of view
   - Implement basic 3D object rendering (wireframe then filled polygons)

2. **Rendering Pipeline**
   - Basic 3D object rendering

### Phase 2: Mathematics & Physics Core
1. **3D Math Library**
   - Vector3D class with all operations
   - Matrix4x4 for transformations
   - Quaternion for rotations (optional but recommended)
   - Ray-plane and ray-sphere intersection

2. **Physics Engine**
   - Ball class with position, velocity, acceleration
   - Force system (gravity, collision forces)
   - Collision detection (sphere-plane, sphere-sphere, sphere-box)
   - Integration methods (Euler, Verlet)

### Phase 3: Editor Architecture
1. **3D Editor Interface**
   - 3D viewport with mouse controls (orbit: drag, zoom: scroll, pan: shift+drag)
   - Grid system with snapping
   - Object selection and transformation gizmos
   - Multiple viewports (top, front, side, perspective)

2. **Editing Tools**
   - Primitive creation (box, sphere, cylinder)
   - Extrusion tools for complex shapes
   - Material/property editor
   - Undo/redo system

### Phase 4: File Format & Data Management
1. **Board File Format (.ppb)**
   ```json
   {
     "version": "1.0",
     "board": {
       "dimensions": {"width": 10, "height": 15, "depth": 8},
       "gravity": {"x": 0, "y": -9.81, "z": 0},
       "objects": [
         {
           "type": "obstacle",
           "geometry": "box",
           "position": [5, 2, 0],
           "rotation": [0, 0, 0],
           "scale": [2, 1, 0.5],
           "material": {"color": [255, 0, 0], "bounce": 0.8}
         }
       ],
    "zones": [...]
     }
   }
   ```

2. **Serialization System**
   - JSON parser/writer with validation
   - Binary format option for performance
   - Version compatibility handling

### Phase 5: Game Implementation
1. **Game Objects**
   - Ball with physics
   - Flippers (animated obstacles)
   - Bumpers and obstacles
   - Scoring zones and triggers

2. **Game Systems**
   - Input handling (keyboard for flippers, mouse for plunger)
   - Game state management
   - Scoring and combo system
   - Sound integration

### Phase 6: Advanced Features
1. **Visual Effects**
   - Texture mapping (if time permits)

2. **Editor Enhancements**
   - Real-time preview mode
   - Scripting support for complex behaviors
   - Board templates and presets
   - Export/import functionality

### Technical Implementation Details

**3D Rendering Approach:**
- Use pygame-ce for 2D surface management
- Implement software 3D renderer with polygon rasterization
- Use NumPy for vector/matrix operations

**Project Structure:**
```
particlespinball/
├── src/
│   ├── engine/          # 3D rendering engine
│   ├── physics/         # Physics simulation
│   ├── editor/          # Level editor
│   ├── game/            # Game logic
│   ├── math/            # 3D mathematics
│   └── file_formats/    # File I/O
├── assets/              # Textures, sounds
├── boards/              # Saved board files
└── tests/               # Unit tests
```

# TASKS
Florian, Mehdi : Level Builder
Alex, Olivier : 3D Engine
