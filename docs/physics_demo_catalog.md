# Physics Demo Catalog

This catalog provides a comprehensive overview of all physics demonstrations available in the Particle Pinball project. Each demo is designed to illustrate specific physics concepts through interactive simulations.

## Quick Reference

| Demo | Key Concepts | Launch | Difficulty |
|------|-------------|---------|------------|
| **Bumper Demo** | Collision detection, vector reflection, energy conservation | Press `1` | Intermediate |
| **Spring Bounce Demo** | Impulse-momentum transfer, spring physics, velocity modification | Press `2` | Intermediate |
| **Wind Simulation Demo** | Particle systems, distributed forces, momentum accumulation | Press `3` | Advanced |
| **Controlled Ball Demo** | Force vectors, Euler integration, diagonal normalization | Press `4` | Beginner |

## Overview of All Demos

The Particle Pinball project includes four interactive physics demonstrations, each focusing on different aspects of classical mechanics:

- **Educational Goals**: Each demo demonstrates specific physics principles through hands-on interaction
- **Progressive Complexity**: Demos range from beginner to advanced concepts
- **Real-time Visualization**: See physics calculations happen in real-time
- **Interactive Learning**: Manipulate parameters and observe immediate results

---

## 1. Bumper Demo

### Description
The Bumper Demo simulates a complete pinball game environment with static circular obstacles (pegs) and boundary walls. This demonstration focuses on collision detection, vector reflection, and energy conservation in elastic collisions.

### Key Physics Concepts

- **Vector Reflection**: R = J - 2(J·N)N
- **Coefficient of Restitution**: Energy loss in collisions (bounciness)
- **Normal Vector Calculation**: Computing surface normals for circular obstacles
- **Gravity on Inclined Planes**: Effective gravity based on board inclination
- **Collision Detection**: Precise detection between circular and rectangular objects

### What You'll Learn

- How to calculate collision normals for circular objects
- Implementing realistic bounce behavior with energy loss
- Managing inclined plane physics
- Coordinating multiple collision types (walls and circular obstacles)

### Demo Features

- **Board Configuration**: 400×600 pixel play area with boundary walls
- **Two Pegs**: Static circular obstacles at strategic positions
- **Gravity**: Configurable gravitational force (9.81 m/s²)
- **Inclination**: Adjustable board tilt angle (0-1 range)
- **Ball Properties**: Configurable mass, radius, and bounciness

### How to Use

1. **Launch**: Press `1` from the home screen or click the "Bumper Demo" button
2. **Observe**: Watch the ball interact with pegs and walls
3. **Analyze**: Notice how velocity reflects off different surfaces
4. **Experiment**: The ball starts with initial velocity (0.2, 0) m/s

### Technical Details

**File**: `src/views/demos/bumper_view.py`

**Key Parameters**:
```python
board_inclination = 1  # Vertical board (gravity reduced)
ball_bounciness = 0.8  # 80% energy retained in collisions
ball_mass = 1.0  # kg
```

**Collision Response**:
```python
# Vector reflection formula
reflected = velocity - 2 * velocity.dot(normal) * normal
velocity = reflected * bounciness
```

### Educational Value

This demo is excellent for understanding:
- Classical collision mechanics
- Vector mathematics in physics
- Energy conservation principles
- Real-time physics simulation

### Related Documentation

- `docs/bumper_demo.adoc` - Detailed bumper demo documentation
- `docs/physics_overview.adoc` - General physics engine concepts
- `docs/force_and_motion.adoc` - Force and motion physics

---

## 2. Spring Bounce Demo

### Description
The Spring Bounce Demo demonstrates impulse-momentum transfer through a user-controlled moving wall that acts as a spring. The ball bounces on a horizontal surface, and users can move the bottom wall upward to impart additional upward velocity, simulating a spring mechanism.

### Key Physics Concepts

- **Impulse-Momentum Theorem**: J = Δp = mΔv
- **Velocity Transfer**: v_new = v_old + v_wall × coefficient
- **Gravitational Force**: F = mg
- **Collision Response**: Elastic bounce with optional impulse
- **Vector Inversion**: Normal vector direction for reflection

### What You'll Learn

- How moving surfaces transfer momentum to objects
- The difference between static and moving collisions
- Controlling impulse magnitude through velocity modification
- Implementing spring-like behavior in physics simulations

### Demo Features

- **Moving Wall**: User-controlled horizontal surface (UP/DOWN arrow keys)
- **Ball Physics**: Gravity-affected ball with realistic bounce
- **Spring Coefficient**: 1.5× multiplier on wall velocity during collision
- **Real-time Control**: Adjust wall position during simulation

### How to Use

1. **Launch**: Press `2` from the home screen or click the "Spring Bounce Demo" button
2. **Observe**: The ball falls under gravity and bounces on the bottom wall
3. **Interact**: Press `UP` arrow to move wall upward (creates spring effect)
4. **Experiment**: Time your wall movement to maximize ball height
5. **Release**: Release `UP` arrow to stop wall movement

### Controls

| Key | Action |
|-----|--------|
| **UP Arrow** | Move wall upward (spring force) |
| **DOWN Arrow** | Move wall downward |

### Technical Details

**File**: `src/views/demos/spring_bounce_view.py`

**Spring Effect Implementation**:
```python
# Check if moving wall collides with ball from below
if colliding_object == moving_wall and wall_velocity.y < 0:
    # Apply impulse: add wall velocity to ball velocity
    ball.velocity.y += wall_velocity.y * 1.5
```

**Key Parameters**:
```python
wall_speed = 5  # pixels per frame
spring_coefficient = 1.5  # multiplier for impulse
ball_bounciness = 0.8  # standard bounce coefficient
```

### Mathematical Explanation

**Impulse Transfer**:
When a moving wall with velocity v_wall collides with a ball:
```
v_ball_new = v_ball_reflected + v_wall × coefficient
```

This simulates the momentum transfer from the moving surface, effectively creating a spring-like effect where the wall "pushes" the ball.

### Educational Value

This demo demonstrates:
- Practical application of impulse-momentum theorem
- Difference between static and dynamic collisions
- User-controlled physics interactions
- Real-time velocity manipulation

### Related Documentation

- `docs/spring_bounce_demo.adoc` - Detailed spring demo documentation
- `docs/force_and_motion.adoc` - Force and motion physics
- `docs/physics_overview.adoc` - Physics engine architecture

---

## 3. Wind Simulation Demo

### Description
The Wind Simulation Demo demonstrates particle-based force application using a system of wind particles. Particles are generated at the mouse cursor position and travel towards the ball, transferring momentum upon collision and simulating the effect of wind force on an object.

### Key Physics Concepts

- **Particle Systems**: Managing multiple discrete force carriers
- **Momentum Transfer**: F = v̂ × 0.1 (force per particle)
- **Force Accumulation**: Summing contributions from multiple particles
- **Lifetime Management**: Creating and destroying particles dynamically
- **Distributed Forces**: Many small forces creating one large effect

### What You'll Learn

- How particle systems can simulate continuous forces
- Managing thousands of particles efficiently
- Force accumulation from multiple sources
- Interactive force generation using user input
- Real-time particle generation and cleanup

### Demo Features

- **Mouse-Controlled Wind Source**: Move mouse to direct wind
- **Particle Generation**: 5 particles generated per frame
- **Randomized Velocity**: Particles vary by ±15 degrees from target direction
- **Force Calculation**: Each particle transfers 0.1 units of force
- **Particle Lifetime**: Particles age and are automatically removed

### How to Use

1. **Launch**: Press `3` from the home screen or click the "Wind Simulation Demo" button
2. **Move Mouse**: Position mouse cursor anywhere on screen (wind source)
3. **Observe**: Particles stream from mouse toward the ball
4. **Watch**: Ball accelerates in direction of cumulative particle force
5. **Experiment**: Move mouse around to change wind direction and observe ball movement

### Technical Details

**File**: `src/views/demos/wind_simulation_view.py`

**Particle Generation**:
```python
def create_wind_particle(mouse_pos, ball_pos):
    # Calculate direction toward ball
    direction = (ball_pos - mouse_pos).normalize()
    # Add random variation (±15 degrees)
    angle = random.uniform(-15, 15)
    velocity = direction.rotate(angle) * random.uniform(1, 5)
    return WindParticle(..., velocity=velocity, ...)
```

**Force Application**:
```python
if pygame.sprite.collide_circle(ball, particle):
    force = particle.velocity.normalize() * 0.1
    ball.add_force(force)
```

**Key Parameters**:
```python
particles_per_frame = 5  # generation rate
force_per_particle = 0.1  # magnitude
angle_variation = ±15°  # randomness
velocity_range = (1, 5)  # random speed
particle_lifetime = defined in WindParticle class
```

### Mathematical Explanation

**Total Wind Force**:
```
F_total = Σ (v_î × 0.1) for i = 1 to n
```

Where:
- v_î is the normalized velocity vector of particle i
- 0.1 is the force magnitude per particle
- n is the number of colliding particles

This creates a smooth, continuous force as many small contributions sum to a larger effect.

### Particle System Architecture

1. **Generation**: 5 particles created each frame at mouse position
2. **Targeting**: Particles aim at ball position with slight random variation
3. **Lifetime**: Particles age over time and are removed when expired
4. **Collision**: Circle-circle collision detection with ball
5. **Force Transfer**: Velocity direction determines force direction
6. **Cleanup**: Dead particles removed from simulation each frame

### Performance Considerations

- **Particle Count**: ~300 particles on screen at any given time
- **Collision Detection**: Circle-based for efficiency
- **Memory Management**: Automatic cleanup prevents memory leaks
- **Update Rate**: 60 FPS with fixed timestep

### Educational Value

This demo illustrates:
- Particle-based force simulation
- Distributed force accumulation
- Real-time particle system management
- User-controlled physics phenomena
- Efficient game programming techniques

### Related Documentation

- `docs/wind_simulation_demo.adoc` - Detailed wind simulation documentation
- `docs/force_and_motion.adoc` - Force accumulation and momentum
- `docs/physics_overview.adoc` - Physics engine and constants

---

## 4. Controlled Ball Demo

### Description
The Controlled Ball Demo provides a hands-on demonstration of force vectors and Euler integration. Unlike other demos that use the main physics engine, this demo implements hardcoded physics to illustrate fundamental physics concepts directly. Users control the ball with arrow keys and observe how applied forces affect motion.

### Key Physics Concepts

- **Euler Integration**: v = v₀ + aΔt, x = x₀ + vΔt
- **Force Vectors**: Directional force application
- **Diagonal Normalization**: √2 correction for consistent acceleration
- **Gravity**: Constant downward acceleration
- **Damping**: Energy loss during floor collisions (0.8 coefficient)

### What You'll Learn

- How to implement Euler integration from scratch
- Vector mathematics for directional movement
- Diagonal movement normalization
- Force accumulation and application
- Floor collision with energy dissipation

### Demo Features

- **Keyboard Control**: Arrow keys apply force in 4 directions
- **Hardcoded Physics**: Direct implementation without physics engine
- **Diagonal Correction**: √2 normalization prevents faster diagonal movement
- **Gravity**: Constant 0.3 downward acceleration
- **Damping**: 0.8 coefficient on floor collision (80% velocity retained)
- **Reset Function**: Space bar returns ball to center

### How to Use

1. **Launch**: Press `4` from the home screen or click the "Controlled Ball Demo" button
2. **Start**: Press `SPACE` to begin simulation
3. **Control**: Use arrow keys to apply forces:
   - `UP`: Apply upward force
   - `DOWN`: Apply downward force (adds to gravity)
   - `LEFT`: Apply leftward force
   - `RIGHT`: Apply rightward force
4. **Observe**: Ball moves according to applied forces and gravity
5. **Reset**: Press `SPACE` to return ball to center and stop motion

### Controls

| Key | Action |
|-----|--------|
| **SPACE** | Start simulation / Reset ball to center |
| **UP Arrow** | Apply upward force |
| **DOWN Arrow** | Apply downward force |
| **LEFT Arrow** | Apply leftward force |
| **RIGHT Arrow** | Apply rightward force |

### Technical Details

**File**: `src/views/demos/controlled_ball_view.py`

**Euler Integration**:
```python
# Update velocity with acceleration
vx += ax
vy += ay

# Update position with velocity
x += vx
y += vy
```

**Diagonal Normalization**:
```python
# Example: Up-Right movement
ax = afus / √2  # Normalize by √2
ay = -afus / √2 + gravity
```

**Floor Collision with Damping**:
```python
if y >= floor_y:
    y = floor_y  # Correct position
    vx *= 0.8   # Friction (horizontal)
    vy = -vy * 0.8  # Restitution (vertical)
```

**Key Parameters**:
```python
gravity = 0.3  # downward acceleration
afus = 0.5  # force magnitude when key pressed
damping = 0.8  # 80% velocity retained on collision
racine2 = √2  # pre-calculated for diagonal normalization
```

### Mathematical Explanation

**Diagonal Force Normalization**:
When moving diagonally, the force vector magnitude would be larger than orthogonal movement:
```
||F_diagonal|| = √(F_x² + F_y²) = √(1² + 1²) = √2 ≈ 1.414
||F_orthogonal|| = 1
```

To ensure consistent acceleration in all directions, we normalize diagonal vectors:
```
F_x' = F_x / √2
F_y' = F_y / √2
```

**Euler Integration Equations**:
```
v_{t+1} = v_t + a × Δt
x_{t+1} = x_t + v_{t+1} × Δt
```

### Why Hardcoded Physics?

This demo intentionally avoids using the main physics engine to:
- Demonstrate fundamental physics implementation from first principles
- Show the mathematical logic behind Euler integration
- Provide a stepping stone to understanding the full physics engine
- Illustrate how force vectors combine with gravity

### Educational Value

This demo teaches:
- Direct implementation of physics equations
- Vector normalization for consistent movement
- Euler integration algorithm
- Force accumulation principles
- Collision damping and energy loss

### Related Documentation

- `docs/controlled_ball_demo.adoc` - Detailed controlled ball demo documentation
- `docs/force_and_motion.adoc` - Euler integration and force application
- `docs/physics_overview.adoc` - Physics engine concepts

---

## Comparison of Demos

| Aspect | Bumper Demo | Spring Bounce Demo | Wind Simulation Demo | Controlled Ball Demo |
|--------|-------------|-------------------|---------------------|---------------------|
| **Physics Engine** | Full engine | Full engine | Full engine | Hardcoded |
| **Primary Concept** | Collisions & Reflection | Impulse Transfer | Particle Forces | Force Vectors |
| **User Input** | None (automatic) | Arrow keys (wall) | Mouse (wind source) | Arrow keys (ball) |
| **Difficulty** | Intermediate | Intermediate | Advanced | Beginner |
| **Interactive Elements** | Walls & pegs | Moving wall | Mouse cursor | Ball controls |
| **Educational Focus** | Collision mechanics | Momentum transfer | Distributed forces | Vector math |
| **Math Complexity** | High (vectors) | Medium | High (particles) | Medium |
| **Real-time Control** | Limited | Yes | Yes | Yes |

---

## Getting Started with Demos

### First Time Users

1. **Start Simple**: Begin with the Controlled Ball Demo (Press `4`)
2. **Progress**: Move to Spring Bounce Demo (Press `2`) for momentum concepts
3. **Advance**: Try the Wind Simulation Demo (Press `3`) for particle physics
4. **Master**: Experiment with the Bumper Demo (Press `1`) for complex collisions

### Educational Path

**Beginner Path** (Learning fundamentals):
1. Controlled Ball Demo → Force vectors and Euler integration
2. Spring Bounce Demo → Impulse and momentum transfer

**Advanced Path** (Exploring complex systems):
1. Wind Simulation Demo → Particle systems and distributed forces
2. Bumper Demo → Complex collision mechanics

### Physics Concepts by Demo

| Physics Concept | Demonstrated In |
|-----------------|-----------------|
| Force Vectors | Controlled Ball Demo |
| Euler Integration | Controlled Ball Demo |
| Gravity | All demos |
| Collisions | Bumper Demo, Spring Bounce Demo |
| Vector Reflection | Bumper Demo |
| Impulse-Momentum | Spring Bounce Demo |
| Particle Systems | Wind Simulation Demo |
| Force Accumulation | Wind Simulation Demo, Bumper Demo |
| Energy Conservation | Bumper Demo |
| Normal Vector Calculation | Bumper Demo, Spring Bounce Demo |
| Diagonal Normalization | Controlled Ball Demo |

---

## Troubleshooting Common Issues

### Demo Won't Start

**Problem**: Pressing a number key doesn't open the demo

**Solutions**:
- Ensure you're on the home screen (not already in a demo)
- Check that the window has focus (click the window)
- Verify you're pressing the correct number keys (1-4)

### Physics Seems Unrealistic

**Problem**: Ball movement doesn't look realistic

**Solutions**:
- Check physics constants in `src/core/world.py`
- Verify demo-specific parameters in each demo file
- Adjust `PIXEL_PER_METER` scaling if needed
- Ensure your frame rate is 60 FPS

### Performance Issues

**Problem**: Demo runs slowly or lags

**Solutions**:
- Wind Simulation Demo can be CPU-intensive; close other applications
- Reduce particle count in Wind Simulation (modify generation rate)
- Check if virtual environment is using enough resources
- Verify pygame-ce is installed correctly

### Ball Gets Stuck

**Problem**: Ball becomes trapped in wall or doesn't move

**Solutions**:
- In Controlled Ball Demo, press SPACE to reset
- In other demos, exit and restart the demo
- Check for collision detection issues in code
- Verify ball radius matches collision detection method

---

## Advanced Topics

### Customizing Demo Parameters

Each demo has configurable parameters you can modify:

**Gravity**:
```python
# In src/core/world.py
GRAVITY = 9.81  # m/s²
```

**Ball Properties**:
```python
# In each demo's __init__ method
Ball(
    radius=10,          # Size of ball
    mass=1.0,         # Mass in kg
    bounciness=0.8     # Coefficient of restitution (0-1)
)
```

**Demo-Specific Settings**:
- Bumper Demo: Board inclination, peg positions
- Spring Demo: Wall speed, spring coefficient
- Wind Demo: Particle generation rate, force magnitude
- Controlled Ball: Force magnitude, damping coefficient

### Adding New Demos

To create a new physics demo:

1. **Create View Class**: Inherit from `View` base class
2. **Implement Methods**: `__init__`, `update`, `draw`, `handle_event`
3. **Register Demo**: Add to `HomeView.available_views` in `home_view.py`
4. **Write Documentation**: Create dedicated `.adoc` file
5. **Update Catalog**: Add entry to this file

Example:
```python
from views.view import View

class NewDemoView(View):
    def __init__(self, screen):
        super().__init__(screen)
        # Setup demo objects

    def update(self):
        # Update physics

    def draw(self):
        # Render demo

    def handle_event(self, event):
        # Handle input
        return self
```

### Debugging Physics

**Enable Debug Output**:
```python
# Add prints to track physics
print(f"Velocity: {ball.velocity}")
print(f"Position: {ball.x}, {ball.y}")
print(f"Forces: {ball.forces}")
```

**Visual Debugging**:
```python
# Draw velocity vectors
pygame.draw.line(screen, (255, 0, 0),
                 ball.rect.center,
                 (ball.rect.center + ball.velocity * 100), 2)
```

**Check Physics Constants**:
```python
# Verify world settings
print(f"Gravity: {GRAVITY}")
print(f"Time Step: {DT}")
print(f"Scale: {PIXEL_PER_METER}")
```

---

## Additional Resources

### Documentation Files

- `docs/index.adoc` - Main documentation index
- `docs/project_overview.adoc` - Project introduction
- `docs/architecture.adoc` - System architecture
- `docs/physics_overview.adoc` - Physics engine overview
- `docs/force_and_motion.adoc` - Force and motion physics
- `docs/development_guide.adoc` - Development setup
- `docs/module_interactions.adoc` - Module communication

### Source Code

- `src/views/demos/bumper_view.py` - Bumper demo implementation
- `src/views/demos/spring_bounce_view.py` - Spring bounce implementation
- `src/views/demos/wind_simulation_view.py` - Wind simulation implementation
- `src/views/demos/controlled_ball_view.py` - Controlled ball implementation
- `src/objects/ball.py` - Ball physics object
- `src/objects/board.py` - Board and collision management
- `src/core/world.py` - Physics constants and configuration

### External Resources

- **Physics Education**: Khan Academy Physics
- **Vector Math**: 3Blue1Brown Linear Algebra
- **Game Physics**: Real-Time Collision Detection by Christer Ericson
- **Pygame Documentation**: https://www.pygame.org/docs/

---

## Contributing

Found an issue with a demo? Want to add a new demonstration?

1. **Report Issues**: Create GitHub issue describing the problem
2. **Submit Improvements**: Fork, modify, and submit a pull request
3. **Add Documentation**: Document new features in this catalog
4. **Test Thoroughly**: Ensure physics remain accurate and stable

For detailed contribution guidelines, see:
- `AGENTS.md` - Agent guidelines
- `docs/development_guide.adoc` - Development guide

---

## Changelog

### Version 1.0.0 (Current)
- Initial release with 4 physics demos
- Bumper Demo with pinball mechanics
- Spring Bounce Demo with impulse transfer
- Wind Simulation Demo with particle system
- Controlled Ball Demo with force vectors
- Comprehensive documentation for all demos

---

## Contact & Support

For questions about specific demos:
- Review demo-specific documentation files
- Check source code for implementation details
- Read physics overview for mathematical background
- Report issues on GitHub repository

---

**Last Updated**: 2025-10-07
**Version**: 1.0.0
**Authors**: Particle Pinball Team
