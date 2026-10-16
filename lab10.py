import random, math

random.seed(7)
N = 50                                      # a tiny "model" with 50 weights

def random_weights():
    return [random.gauss(0, 1) for _ in range(N)]

def distance(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))

# --- The real owner trains: random start, many small noisy steps ---
start = random_weights()
target = random_weights()                   # where training ends up
real = [start]
w = start
for _ in range(30):
    w = [x + 0.15 * (t - x) + random.gauss(0, 0.05) for x, t in zip(w, target)]
    real.append(w)
final = real[-1]                            # the finished model (the thief has this)

# --- The rules (predicates) ---
MAX_STEP = 3.0                              # rule 1: each step must be small
MIN_START_DISTANCE = 6.0                    # rule 2: start must be far from the final model

def small_steps(history):
    return all(distance(history[i], history[i + 1]) < MAX_STEP for i in range(len(history) - 1))

def far_start(history):
    return distance(history[0], history[-1]) > MIN_START_DISTANCE

MIN_WANDER = 1.3                            # rule 3: the path must not be too straight

def wanders(history):
    walked = sum(distance(history[i], history[i + 1]) for i in range(len(history) - 1))
    straight = distance(history[0], history[-1])
    return walked / straight > MIN_WANDER

MIN_SLOWDOWN = 1.5                          # rule 4: early steps must be bigger than late steps

def slows_down(history):
    steps = [distance(history[i], history[i + 1]) for i in range(len(history) - 1)]
    third = max(1, len(steps) // 3)
    early = sum(steps[:third]) / third
    late = sum(steps[-third:]) / third
    return early / late > MIN_SLOWDOWN

def check(name, history):
    print(f"{name:<32} small: {small_steps(history)!s:<6} far: {far_start(history)!s:<6} wanders: {wanders(history)!s:<6} slows: {slows_down(history)}")

# --- Faker A: random start, then one giant jump to the final model ---
faker_a = [random_weights(), final]

# --- Faker B: start as a copy of the final model, plus tiny wiggles ---
faker_b = [[x + random.gauss(0, 0.05) for x in final] for _ in range(30)] + [final]

# --- Faker C: random start, then a straight line of tiny steps to the final ---
s = random_weights()
faker_c = [[a + (b - a) * k / 30 for a, b in zip(s, final)] for k in range(31)]

# --- Faker D: straight line of tiny steps, plus random wobble on every step ---
s = random_weights()
faker_d = [[a + (b - a) * k / 30 + random.gauss(0, 0.1) for a, b in zip(s, final)] for k in range(31)]
faker_d[-1] = final

check("1. real owner", real)
check("2. faker A (one big jump)", faker_a)
check("3. faker B (starts at the end)", faker_b)
check("4. faker C (straight tiny steps)", faker_c)
check("5. faker D (straight + wobble)", faker_d)
