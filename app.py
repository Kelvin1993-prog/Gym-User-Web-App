"""
GymGuide v4 — Premium Interactive Workout Planner
Fixes v3: Mobile responsive · Category-correct images · Checkbox day-selector (no "No results") · Any number of days supported
"""
import streamlit as st

st.set_page_config(
    page_title="GymGuide – Premium Workout Planner",
    page_icon="💪",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ═══════════════════════════════════════════════════════════════════════════
#  CATEGORY-CORRECT IMAGES
#  Every exercise has a category; every category has a matched Unsplash photo.
# ═══════════════════════════════════════════════════════════════════════════

CATEGORY_PHOTOS = {
    "chest":     "1526506118085-60ce8714f8c5",
    "back":      "1571019613454-1cb2f99b2d8b",
    "legs":      "1517963628607-235ccdd5476c",
    "shoulders": "1581009146145-b5ef050c2e1e",
    "arms":      "1584466977773-e625c37cdd50",
    "triceps":   "1583454110551-21f2fa2afe61",
    "core":      "1571019614242-c5c5dee9f50b",
    "cardio":    "1538805060514-97d9cc17730c",
    "running":   "1476480862126-209bfaa8edc8",
    "hiit":      "1549060279-7e168fcee0c2",
    "yoga":      "1506126613408-eca07ce68773",
    "stretch":   "1552196563-55cd4e45efb3",
    "mobility":  "1544367567-0f2fcb009e0b",
    "rowing":    "1558618666-fcd25c85cd64",
    "general":   "1540497077202-7c8a3999166f",
}

EX_CAT = {
    "Treadmill Warm-Up": "cardio", "Dynamic Warm-Up": "mobility",
    "Bike Warm-Up": "cardio", "Rowing Machine Warm-Up": "rowing",
    "Circuit Warm-Up": "hiit", "Cardio Warm-Up": "cardio",
    "5-Minute Cardio Warm-Up": "cardio",
    "Barbell Bench Press": "chest", "Dumbbell Chest Fly": "chest",
    "Dumbbell Shoulder Press": "shoulders", "Dumbbell Push Press": "shoulders",
    "Cable Face Pull": "shoulders", "Cable Tricep Pushdown": "triceps",
    "Lat Pulldown": "back", "Seated Cable Row": "back",
    "Dumbbell Bicep Curl": "arms",
    "Barbell Squat": "legs", "Goblet Squat": "legs",
    "Leg Press Machine": "legs", "Romanian Deadlift": "legs",
    "Romanian Deadlift (RDL)": "legs", "Dumbbell Romanian Deadlift": "legs",
    "Conventional Deadlift": "legs", "Walking Lunges": "legs",
    "Leg Curl Machine": "legs", "Leg Extension Machine": "legs",
    "Standing Calf Raise": "legs",
    "Plank Hold": "core", "Plank Variations": "core",
    "Mountain Climbers": "hiit", "Dead Bug": "core", "Core Finisher": "core",
    "Treadmill Intervals": "cardio", "Speed Intervals": "running",
    "HIIT Circuit": "hiit", "20-Min Moderate Cardio": "cardio",
    "Steady-State Cardio": "running", "Long Endurance Session": "running",
    "Easy Recovery Walk/Jog": "running", "Dumbbell Full Body Circuit": "general",
    "Cross-Training Circuit": "rowing", "Light Cardio": "cardio",
    "Easy Walk": "running",
    "Sun Salutation Flow": "yoga", "Standing Balance Poses": "yoga",
    "Floor Poses & Cool Down": "yoga", "Full Body Deep Stretch": "stretch",
    "Active Mobility Flow": "mobility", "Full Body Flexibility": "stretch",
    "Gentle Full Body Stretch": "stretch", "Joint Mobility Circuit": "mobility",
    "Thoracic Mobility": "mobility", "Full Body Mobility": "mobility",
    "Mobility Work": "mobility",
    "Cool Down & Stretching": "stretch", "Cool Down": "stretch",
    "Post-Cardio Stretch": "stretch", "Full Body Cool Down": "stretch",
    "Stretching": "stretch", "Gentle Stretching": "stretch",
    "Gentle Stretch": "stretch",
}

FALLBACK = "1540497077202-7c8a3999166f"

def img_url(name, w=800, h=360):
    pid = CATEGORY_PHOTOS.get(EX_CAT.get(name, "general"), FALLBACK)
    return f"https://images.unsplash.com/photo-{pid}?w={w}&h={h}&fit=crop&q=80"

# ═══════════════════════════════════════════════════════════════════════════
#  GOAL POOLS — support 1–7 training days
# ═══════════════════════════════════════════════════════════════════════════

GOAL_POOLS = {
    "💪 Build Muscle & Strength": {
        "icon": "💪", "color": "#FF3E3E",
        "desc": "Heavy lifting, compound movements, progressive overload",
        1: ["Full Body Strength"],
        2: ["Upper Push", "Lower A"],
        3: ["Upper Push", "Lower A", "Upper Pull"],
        4: ["Upper Push", "Lower A", "Upper Pull", "Lower B"],
        5: ["Upper Push", "Lower A", "Upper Pull", "Lower B", "Upper Push"],
        6: ["Upper Push", "Lower A", "Upper Pull", "Lower B", "Upper Push", "Lower A"],
        7: ["Upper Push", "Lower A", "Upper Pull", "Lower B", "Upper Push", "Lower A", "Lower B"],
    },
    "🏃 General Fitness": {
        "icon": "🏃", "color": "#3E8BFF",
        "desc": "Balanced mix of strength, cardio and flexibility",
        1: ["Full Body Strength"],
        2: ["Full Body Strength", "Cardio & Core"],
        3: ["Full Body Strength", "Cardio & Core", "Full Body Strength"],
        4: ["Full Body Strength", "Cardio & Core", "Full Body Strength", "Cardio & Flexibility"],
        5: ["Full Body Strength", "Cardio & Core", "Full Body Strength", "Cardio & Flexibility", "Active Recovery"],
        6: ["Full Body Strength", "Cardio & Core", "Full Body Strength", "Cardio & Flexibility", "Cardio & Core", "Active Recovery"],
        7: ["Full Body Strength", "Cardio & Core", "Full Body Strength", "Cardio & Flexibility", "Cardio & Core", "Active Recovery", "Full Body Strength"],
    },
    "🔥 Weight Loss & Toning": {
        "icon": "🔥", "color": "#FF8C00",
        "desc": "High-intensity circuits, fat burning & body recomposition",
        1: ["HIIT & Circuits"],
        2: ["HIIT & Circuits", "Strength & Cardio"],
        3: ["HIIT & Circuits", "Strength & Cardio", "HIIT & Circuits"],
        4: ["HIIT & Circuits", "Strength & Cardio", "HIIT & Circuits", "Strength & Cardio"],
        5: ["HIIT & Circuits", "Strength & Cardio", "HIIT & Circuits", "Strength & Cardio", "Light Cardio"],
        6: ["HIIT & Circuits", "Strength & Cardio", "HIIT & Circuits", "Strength & Cardio", "HIIT & Circuits", "Light Cardio"],
        7: ["HIIT & Circuits", "Strength & Cardio", "HIIT & Circuits", "Strength & Cardio", "HIIT & Circuits", "Light Cardio", "Strength & Cardio"],
    },
    "🚴 Endurance & Cardio": {
        "icon": "🚴", "color": "#00C896",
        "desc": "Aerobic capacity, stamina and cardiovascular health",
        1: ["Steady-State Cardio"],
        2: ["Steady-State Cardio", "Interval Training"],
        3: ["Steady-State Cardio", "Interval Training", "Long Cardio Session"],
        4: ["Steady-State Cardio", "Interval Training", "Cross Training", "Long Cardio Session"],
        5: ["Steady-State Cardio", "Interval Training", "Cross Training", "Long Cardio Session", "Recovery Cardio"],
        6: ["Steady-State Cardio", "Interval Training", "Cross Training", "Long Cardio Session", "Recovery Cardio", "Steady-State Cardio"],
        7: ["Steady-State Cardio", "Interval Training", "Cross Training", "Long Cardio Session", "Recovery Cardio", "Steady-State Cardio", "Interval Training"],
    },
    "🧘 Flexibility & Mobility": {
        "icon": "🧘", "color": "#A855F7",
        "desc": "Yoga, stretching, joint health and posture improvement",
        1: ["Yoga Flow"],
        2: ["Yoga Flow", "Mobility Drills"],
        3: ["Yoga Flow", "Mobility Drills", "Deep Stretch"],
        4: ["Yoga Flow", "Mobility Drills", "Yoga Flow", "Deep Stretch"],
        5: ["Yoga Flow", "Mobility Drills", "Yoga Flow", "Deep Stretch", "Active Mobility"],
        6: ["Yoga Flow", "Mobility Drills", "Yoga Flow", "Deep Stretch", "Active Mobility", "Yoga Flow"],
        7: ["Yoga Flow", "Mobility Drills", "Yoga Flow", "Deep Stretch", "Active Mobility", "Yoga Flow", "Mobility Drills"],
    },
}

ALL_DAYS = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
DAY_ABB  = {d: d[:3] for d in ALL_DAYS}

def build_schedule(goal_key, training_days):
    n = max(1, min(7, len(training_days)))
    pool = GOAL_POOLS[goal_key].get(n, GOAL_POOLS[goal_key][4])
    schedule, idx = {}, 0
    for day in ALL_DAYS:
        if day in training_days:
            schedule[day] = pool[idx % len(pool)]
            idx += 1
        else:
            schedule[day] = "Rest"
    return schedule

# ═══════════════════════════════════════════════════════════════════════════
#  EXERCISE DATA
# ═══════════════════════════════════════════════════════════════════════════

EXERCISES = {
    "Upper Push": [
        {"name":"Treadmill Warm-Up","muscle":"Full Body Warm-Up","minutes":10,
         "sets_reps":"10 min continuous","equipment":"Treadmill","difficulty":"Beginner",
         "steps":["Start at walking pace (4–5 km/h)",
                  "Increase to a light jog over 5 minutes",
                  "Keep arms swinging, breathe steadily",
                  "Last 2 min: slow to a walk before lifting"],
         "tip":"Never skip the warm-up — 10 minutes raises core temperature and cuts injury risk dramatically."},
        {"name":"Barbell Bench Press","muscle":"Chest · Shoulders · Triceps","minutes":15,
         "sets_reps":"3 sets × 8–10 reps","equipment":"Barbell · Bench · Rack","difficulty":"Beginner",
         "steps":["Lie flat, grip bar just wider than shoulder-width",
                  "Unrack and hold directly above your chest",
                  "Lower slowly to mid-chest — elbows at 45°",
                  "Drive up explosively until arms are fully extended",
                  "Feet flat, slight arch, core braced throughout"],
         "tip":"Start with the empty bar (20 kg). Master form before adding weight. A spotter is strongly recommended."},
        {"name":"Dumbbell Shoulder Press","muscle":"Shoulders · Triceps","minutes":12,
         "sets_reps":"3 sets × 10–12 reps","equipment":"Dumbbells · Bench","difficulty":"Beginner",
         "steps":["Sit upright, dumbbells at shoulder height, palms forward",
                  "Press overhead in a smooth arc until arms are straight",
                  "Keep slight bend at top — never hard-lock elbows",
                  "Lower slowly back to shoulder height"],
         "tip":"Keep your lower back pressed against the bench. Arching shifts load to your spine, not your shoulders."},
        {"name":"Cable Tricep Pushdown","muscle":"Triceps","minutes":10,
         "sets_reps":"3 sets × 12 reps","equipment":"Cable Machine · Rope or Bar","difficulty":"Beginner",
         "steps":["Pulley at head height, rope or bar attached",
                  "Grip attachment, tuck elbows tight to sides",
                  "Push straight down to full extension",
                  "Return slowly — elbows stay locked at sides"],
         "tip":"If elbows fly forward, the weight is too heavy. Only movement from the elbow joint down counts."},
        {"name":"Dumbbell Chest Fly","muscle":"Chest (Outer)","minutes":10,
         "sets_reps":"3 sets × 12 reps","equipment":"Dumbbells · Flat Bench","difficulty":"Beginner",
         "steps":["Lie on bench, dumbbells above chest with slight elbow bend",
                  "Open arms wide in an arc until deep chest stretch",
                  "Squeeze chest to bring dumbbells back together at top",
                  "Maintain slight elbow bend — never fully straighten"],
         "tip":"Think of hugging a large barrel. Never let elbows drop below shoulder level — that's your injury zone."},
        {"name":"Cool Down & Stretching","muscle":"Chest · Shoulders · Arms","minutes":8,
         "sets_reps":"8 min — hold each 30s","equipment":"Exercise Mat","difficulty":"Beginner",
         "steps":["Chest doorway stretch: 30 sec each side",
                  "Tricep overhead stretch: 30 sec each arm",
                  "Cross-body shoulder stretch: 30 sec each",
                  "Seated forward fold: 60 sec"],
         "tip":"Static stretching post-session reduces next-day soreness and builds long-term flexibility."},
    ],
    "Lower A": [
        {"name":"Dynamic Warm-Up","muscle":"Legs & Hips","minutes":8,
         "sets_reps":"2 rounds","equipment":"None","difficulty":"Beginner",
         "steps":["10 × Leg swings (front-to-back) each leg",
                  "10 × Hip circles each direction",
                  "10 × Slow bodyweight squats",
                  "10 × Walking lunges across the room"],
         "tip":"Dynamic warm-ups activate glutes and hip flexors — the two groups doing most work today."},
        {"name":"Barbell Squat","muscle":"Quads · Glutes · Hamstrings","minutes":18,
         "sets_reps":"3 sets × 8–10 reps","equipment":"Barbell · Squat Rack","difficulty":"Intermediate",
         "steps":["Set bar at shoulder height; step under and rest on upper traps",
                  "Feet shoulder-width, toes slightly out",
                  "Deep breath, brace core hard, sit down and back",
                  "Squat until thighs are parallel to floor or below",
                  "Drive through heels to stand, chest up throughout"],
         "tip":"Spend 2 weeks with just the bar drilling form. This single exercise built more physiques than any other."},
        {"name":"Leg Press Machine","muscle":"Quads · Glutes","minutes":14,
         "sets_reps":"3 sets × 10–12 reps","equipment":"Leg Press Machine","difficulty":"Beginner",
         "steps":["Adjust seat so knees reach ~90° at bottom",
                  "Feet shoulder-width on the platform",
                  "Release handles and lower plate in control",
                  "Push through heels until legs are nearly extended",
                  "Re-engage handles between sets"],
         "tip":"The leg press is ideal for beginners — the machine guides movement so you can focus on effort."},
        {"name":"Romanian Deadlift (RDL)","muscle":"Hamstrings · Glutes","minutes":14,
         "sets_reps":"3 sets × 10 reps","equipment":"Barbell or Dumbbells","difficulty":"Intermediate",
         "steps":["Hold bar at hip height, feet hip-width, soft knee bend",
                  "Hinge at hips — push BACK, not DOWN",
                  "Slide bar down legs until deep hamstring stretch",
                  "Drive hips forward to stand, squeeze glutes at top",
                  "Flat back and shoulders pulled back at all times"],
         "tip":"Imagine closing a car door with your bum — that hip hinge is the whole exercise."},
        {"name":"Leg Curl Machine","muscle":"Hamstrings","minutes":10,
         "sets_reps":"3 sets × 12 reps","equipment":"Lying Leg Curl Machine","difficulty":"Beginner",
         "steps":["Lie face down, pad positioned just above heels",
                  "Curl legs up as far as possible without lifting hips",
                  "Squeeze hamstrings hard at top for 1 full second",
                  "Lower over 3 slow seconds — eccentric phase builds muscle"],
         "tip":"The 3-second lowering is where the real growth happens. Don't just drop the weight."},
        {"name":"Cool Down & Stretching","muscle":"Legs · Hips · Lower Back","minutes":8,
         "sets_reps":"8 min","equipment":"Exercise Mat","difficulty":"Beginner",
         "steps":["Standing quad stretch: 30 sec each leg",
                  "Seated hamstring stretch: 60 sec",
                  "Pigeon pose (glutes): 45 sec each side",
                  "Calf stretch against wall: 30 sec each"],
         "tip":"Tight hips cause the vast majority of lower back pain. Never skip this stretch."},
    ],
    "Upper Pull": [
        {"name":"Rowing Machine Warm-Up","muscle":"Back · Arms · Core","minutes":8,
         "sets_reps":"8 min steady","equipment":"Rowing Machine","difficulty":"Beginner",
         "steps":["Strap feet in, overhand grip on handle",
                  "Sequence: push legs → lean back → pull arms in",
                  "Return: arms extend → lean forward → legs compress",
                  "Aim for 20–24 smooth strokes per minute"],
         "tip":"The rowing machine warms up your entire posterior chain — perfect for a pull day."},
        {"name":"Lat Pulldown","muscle":"Lats · Upper Back","minutes":14,
         "sets_reps":"3 sets × 10–12 reps","equipment":"Lat Pulldown Machine","difficulty":"Beginner",
         "steps":["Sit and lock thighs under the knee pad",
                  "Grip bar wider than shoulder-width, overhand",
                  "Lean back slightly, pull bar to upper chest",
                  "Lead with elbows — imagine tucking them into your back pockets",
                  "Let bar rise slowly to full arm extension"],
         "tip":"Think 'elbows to hips' not 'hands to chest'. This fires your lats instead of just your arms."},
        {"name":"Seated Cable Row","muscle":"Mid-Back · Lats · Rear Delts","minutes":14,
         "sets_reps":"3 sets × 10–12 reps","equipment":"Cable Row Station","difficulty":"Beginner",
         "steps":["Sit tall, feet on platform, slight knee bend",
                  "Grip handle and sit upright before pulling",
                  "Pull toward lower ribcage, elbows driving back",
                  "Squeeze shoulder blades together firmly",
                  "Release in controlled 3-second return"],
         "tip":"Your torso should barely move. Rocking back and forth means you're using momentum, not muscle."},
        {"name":"Dumbbell Bicep Curl","muscle":"Biceps","minutes":10,
         "sets_reps":"3 sets × 12 reps","equipment":"Dumbbells","difficulty":"Beginner",
         "steps":["Stand with dumbbells at sides, palms forward",
                  "Curl both up toward shoulders simultaneously",
                  "Squeeze biceps hard at top — hold 1 second",
                  "Lower slowly over 2–3 seconds",
                  "No swinging — strict reps only"],
         "tip":"Never swing your torso to lift the weight. Alternating arms improves mind-muscle connection."},
        {"name":"Cable Face Pull","muscle":"Rear Delts · Rotator Cuff","minutes":10,
         "sets_reps":"3 sets × 15 reps","equipment":"Cable Machine · Rope","difficulty":"Beginner",
         "steps":["Pulley at face height, rope attachment",
                  "Grip rope thumbs toward you, step back",
                  "Pull rope toward face, elbows flaring wide",
                  "Separate rope at end — squeeze rear delts",
                  "Return slowly under full control"],
         "tip":"The most underrated exercise in any programme. Light weight, high reps. It keeps your shoulders healthy for life."},
        {"name":"Cool Down & Stretching","muscle":"Back · Shoulders · Arms","minutes":8,
         "sets_reps":"8 min","equipment":"Exercise Mat","difficulty":"Beginner",
         "steps":["Child's pose (lats): 60 sec",
                  "Cross-body shoulder stretch: 30 sec each arm",
                  "Doorway bicep/chest stretch: 30 sec each side",
                  "Seated spinal twist: 30 sec each direction"],
         "tip":"Child's pose opens up your lats beautifully after a pull session. Hold it longer if you have time."},
    ],
    "Lower B": [
        {"name":"Bike Warm-Up","muscle":"Legs · Cardiovascular","minutes":10,
         "sets_reps":"10 min steady","equipment":"Stationary Bike","difficulty":"Beginner",
         "steps":["Set resistance to moderate level 3–5",
                  "Pedal at 60–80 RPM for first 5 minutes",
                  "Raise resistance for the final 5 minutes",
                  "Final minute: easy spin to transition to lifting"],
         "tip":"The stationary bike is the superior leg-day warm-up — loads quads and hips without heavy spinal stress."},
        {"name":"Conventional Deadlift","muscle":"Hamstrings · Glutes · Back · Full Body","minutes":20,
         "sets_reps":"3 sets × 6–8 reps","equipment":"Barbell · Weight Plates","difficulty":"Intermediate",
         "steps":["Bar over mid-foot, feet hip-width, grip just outside legs",
                  "Hinge down: back flat, chest up, hips above knees",
                  "Big belly breath — brace like you're about to be punched",
                  "Push the floor away — bar scrapes your shins all the way up",
                  "Lock out: hips extended, glutes squeezed, stand tall",
                  "Hinge down with control — reset position each rep"],
         "tip":"The king of all exercises. Ask a gym trainer to watch your first session — 20 minutes of coaching saves years of bad habits."},
        {"name":"Walking Lunges","muscle":"Quads · Glutes · Balance","minutes":12,
         "sets_reps":"3 sets × 10 each leg","equipment":"Bodyweight or Dumbbells","difficulty":"Beginner",
         "steps":["Stand tall, step forward into a wide lunge",
                  "Lower back knee toward floor — controlled",
                  "Front knee stays above (not past) toes",
                  "Push off front foot and bring back leg forward",
                  "10 steps per leg — torso upright throughout"],
         "tip":"Master bodyweight lunges before adding dumbbells. A long stride protects your knees."},
        {"name":"Leg Extension Machine","muscle":"Quads (Isolation)","minutes":10,
         "sets_reps":"3 sets × 12 reps","equipment":"Leg Extension Machine","difficulty":"Beginner",
         "steps":["Sit with back against pad, knees aligned with pivot",
                  "Shin pad just above feet",
                  "Extend legs upward until almost fully straight",
                  "HOLD — squeeze quads for 1 full second at top",
                  "Lower over 3 slow seconds — never drop"],
         "tip":"Quality of the squeeze matters more than weight on the stack. Squeeze hard every rep."},
        {"name":"Standing Calf Raise","muscle":"Calves","minutes":8,
         "sets_reps":"3 sets × 15–20 reps","equipment":"Step or Calf Machine","difficulty":"Beginner",
         "steps":["Stand on step edge with heels hanging off",
                  "Rise onto toes as high as possible",
                  "HOLD at top for 1 full second",
                  "Lower heels BELOW step for maximum stretch",
                  "No bouncing — every rep fully controlled"],
         "tip":"Calves hate bouncing. Full range, slow reps, high volume — the only thing that builds them."},
        {"name":"Cool Down & Stretching","muscle":"Legs · Glutes · Lower Back","minutes":10,
         "sets_reps":"10 min","equipment":"Exercise Mat","difficulty":"Beginner",
         "steps":["Standing quad stretch: 30 sec each leg",
                  "Figure-four glute stretch: 45 sec each side",
                  "Downward dog calf stretch: 45 sec each leg",
                  "Child's pose for lower back: 60 sec"],
         "tip":"10 minutes here saves hours of stiffness tomorrow. Don't skip it when you're tired — that's exactly when you need it."},
    ],
    "Full Body Strength": [
        {"name":"Cardio Warm-Up","muscle":"Full Body","minutes":8,
         "sets_reps":"8 min","equipment":"Treadmill or Bike","difficulty":"Beginner",
         "steps":["5 min treadmill brisk walk or light jog",
                  "10 × arm circles each direction",
                  "10 × bodyweight squats",
                  "10 × walking lunges"],
         "tip":"Full-body sessions need a warm-up that hits both upper and lower body. This covers both in under 8 minutes."},
        {"name":"Goblet Squat","muscle":"Quads · Glutes · Core","minutes":12,
         "sets_reps":"3 sets × 12 reps","equipment":"Dumbbell or Kettlebell","difficulty":"Beginner",
         "steps":["Hold dumbbell vertically at chest with both hands",
                  "Feet shoulder-width, toes slightly out",
                  "Squat deep — weight keeps chest naturally upright",
                  "Drive through heels to stand"],
         "tip":"The goblet squat is the best way to learn squat mechanics before ever touching a barbell."},
        {"name":"Dumbbell Romanian Deadlift","muscle":"Hamstrings · Glutes","minutes":12,
         "sets_reps":"3 sets × 10 reps","equipment":"Dumbbells","difficulty":"Beginner",
         "steps":["Hold dumbbells in front of thighs, hip-width stance",
                  "Hinge forward at hips — push them back, not down",
                  "Lower dumbbells along legs until hamstrings stretch",
                  "Drive hips forward to stand, squeeze glutes at top"],
         "tip":"Keep dumbbells close to your legs throughout — they should almost brush your shins."},
        {"name":"Dumbbell Push Press","muscle":"Shoulders · Triceps · Legs","minutes":12,
         "sets_reps":"3 sets × 10 reps","equipment":"Dumbbells","difficulty":"Beginner",
         "steps":["Dumbbells at shoulder height, palms facing in",
                  "Dip slightly at knees (about 2 inches)",
                  "Explosively drive through legs and press overhead",
                  "Lower slowly back to shoulders over 2 seconds"],
         "tip":"The leg drive makes this easier than a strict press — a great entry point for building pressing strength."},
        {"name":"Seated Cable Row","muscle":"Back · Biceps","minutes":12,
         "sets_reps":"3 sets × 12 reps","equipment":"Cable Row Station","difficulty":"Beginner",
         "steps":["Sit tall, feet on platform",
                  "Pull handle toward lower ribcage",
                  "Squeeze shoulder blades firmly",
                  "Return to full arm extension in 3 controlled seconds"],
         "tip":"Every full-body day needs a pulling movement. This hits back and biceps together — maximum efficiency."},
        {"name":"Plank Hold","muscle":"Core · Full Body Stability","minutes":8,
         "sets_reps":"3 sets × 30–60 seconds","equipment":"Exercise Mat","difficulty":"Beginner",
         "steps":["Forearms on floor, elbows under shoulders",
                  "Body forms a straight line — head to heels",
                  "Engage core, squeeze glutes, breathe normally",
                  "30 sec beginners / 60 sec intermediate"],
         "tip":"A perfect 30-second plank builds more core strength than a sagging 90-second one. Quality beats duration."},
        {"name":"Cool Down","muscle":"Full Body","minutes":8,
         "sets_reps":"8 min","equipment":"Exercise Mat","difficulty":"Beginner",
         "steps":["Cat-cow spinal stretch: 60 sec",
                  "Hip flexor lunge stretch: 30 sec each side",
                  "Chest doorway stretch: 30 sec",
                  "Child's pose: 60 sec"],
         "tip":"Full-body sessions tax every system. The cool-down separates people who recover well from those who are always sore."},
    ],
    "Cardio & Core": [
        {"name":"Treadmill Intervals","muscle":"Cardiovascular · Legs","minutes":20,
         "sets_reps":"10 × 1 min run / 1 min walk","equipment":"Treadmill","difficulty":"Beginner",
         "steps":["Warm up 3 min at brisk walk",
                  "Run at a challenging pace for 1 full minute",
                  "Walk for 1 minute to recover",
                  "Repeat 10 times then 2-min cool-down walk"],
         "tip":"Intervals burn significantly more calories than steady-state cardio in the same time. Push hard during the run intervals!"},
        {"name":"Plank Variations","muscle":"Core","minutes":10,
         "sets_reps":"3 rounds","equipment":"Exercise Mat","difficulty":"Beginner",
         "steps":["Standard forearm plank: 30 sec",
                  "Left side plank: 20 sec",
                  "Right side plank: 20 sec",
                  "Rest 30 sec then repeat — 3 rounds total"],
         "tip":"Side planks target obliques — the muscles that create a defined waist. Don't skip them."},
        {"name":"Mountain Climbers","muscle":"Core · Cardio · Shoulders","minutes":8,
         "sets_reps":"3 sets × 30 seconds","equipment":"None","difficulty":"Beginner",
         "steps":["Push-up position — wrists under shoulders",
                  "Drive right knee toward chest",
                  "Switch legs rapidly — left in as right extends",
                  "Hips stay level — no bouncing or sagging"],
         "tip":"Mountain climbers are cardio and core training in one. They're harder than they look — pace yourself early."},
        {"name":"Dead Bug","muscle":"Deep Core Stabilisers","minutes":8,
         "sets_reps":"3 sets × 10 each side","equipment":"Exercise Mat","difficulty":"Beginner",
         "steps":["Lie on back — arms to ceiling, knees at 90° above hips",
                  "Slowly lower right arm behind head and extend left leg",
                  "Keep lower back PRESSED into mat the entire time",
                  "Return to start and repeat opposite side"],
         "tip":"One of the safest and most effective core exercises. It teaches your spine to stay stable during limb movement."},
        {"name":"Cool Down","muscle":"Full Body","minutes":8,
         "sets_reps":"8 min","equipment":"Exercise Mat","difficulty":"Beginner",
         "steps":["Lying knee-to-chest: 30 sec each side",
                  "Floor spinal twist: 30 sec each direction",
                  "Cobra pose: 30 sec",
                  "Happy baby pose: 60 sec"],
         "tip":"After cardio and core your spine needs decompression. Don't rush through these poses."},
    ],
    "Cardio & Flexibility": [
        {"name":"Light Cardio","muscle":"Cardiovascular","minutes":20,
         "sets_reps":"20 min steady","equipment":"Treadmill, Bike or Elliptical","difficulty":"Beginner",
         "steps":["Pick your favourite cardio machine",
                  "Set to a comfortable, conversational pace",
                  "Maintain consistent rhythm for 20 minutes",
                  "Last 2 minutes: ease off to cool down"],
         "tip":"End-of-week cardio should feel energising, not draining. Maintain, don't test yourself today."},
        {"name":"Full Body Flexibility","muscle":"Full Body","minutes":25,
         "sets_reps":"Hold each 45–60 seconds","equipment":"Yoga Mat","difficulty":"Beginner",
         "steps":["Standing forward fold: 60 sec",
                  "Seated butterfly stretch: 60 sec",
                  "Hip flexor kneeling lunge: 45 sec each side",
                  "Lying spinal twist: 45 sec each side",
                  "Child's pose: 90 sec to finish"],
         "tip":"Flexibility done consistently compounds into genuinely impressive range of motion over months."},
    ],
    "Active Recovery": [
        {"name":"Easy Walk","muscle":"Cardiovascular — Light","minutes":20,
         "sets_reps":"20 min easy","equipment":"None or Treadmill","difficulty":"Beginner",
         "steps":["Walk at a completely relaxed, comfortable pace",
                  "Focus on slow, deep nasal breathing",
                  "Stand tall, swing arms naturally",
                  "Outdoors is ideal — sunlight amplifies the benefit"],
         "tip":"Active recovery keeps blood moving to repairing muscles. Don't turn it into a workout."},
        {"name":"Full Body Mobility","muscle":"Full Body Joints","minutes":20,
         "sets_reps":"Continuous flow","equipment":"Yoga Mat · Foam Roller","difficulty":"Beginner",
         "steps":["Foam roll major muscle groups: 60 sec each",
                  "Hip 90-90 stretch: 45 sec each side",
                  "World's greatest stretch: 5 reps each side",
                  "Cat-cow spinal flow: 10 slow, deep reps"],
         "tip":"Performed weekly, these 20 minutes produce flexibility improvements that direct training alone never achieves."},
    ],
    "HIIT & Circuits": [
        {"name":"Circuit Warm-Up","muscle":"Full Body","minutes":5,
         "sets_reps":"1 easy round","equipment":"None","difficulty":"Beginner",
         "steps":["20 × Jumping jacks",
                  "10 × Arm circles each direction",
                  "10 × Bodyweight squats",
                  "10 × Hip hinges"],
         "tip":"HIIT demands your heart rate be elevated before the hard intervals. This 5 minutes is non-negotiable."},
        {"name":"HIIT Circuit","muscle":"Full Body — Fat Burning","minutes":25,
         "sets_reps":"4 rounds · 40s on / 20s off","equipment":"None or Dumbbells","difficulty":"Intermediate",
         "steps":["Burpees — 40 sec at maximum effort",
                  "Dumbbell squat to press — 40 sec",
                  "Jump lunges (or walking lunges) — 40 sec",
                  "Push-ups — 40 sec",
                  "Rest 90 sec between complete rounds"],
         "tip":"The 40-second intervals are where fat loss happens. Go as hard as you can — the rest is designed so you can."},
        {"name":"Core Finisher","muscle":"Abs · Obliques","minutes":8,
         "sets_reps":"2 rounds","equipment":"Exercise Mat","difficulty":"Beginner",
         "steps":["Crunches: 20 reps",
                  "Bicycle crunches: 20 reps each side",
                  "Leg raises: 15 reps",
                  "Plank hold: 30 sec to finish"],
         "tip":"Your core is pre-fatigued from the circuit. Even if it's difficult, push through this finisher."},
        {"name":"Cool Down","muscle":"Full Body","minutes":8,
         "sets_reps":"8 min","equipment":"Exercise Mat","difficulty":"Beginner",
         "steps":["Walk slowly for 2 min to lower heart rate",
                  "Seated forward fold: 60 sec",
                  "Pigeon pose: 45 sec each side",
                  "Child's pose: 60 sec"],
         "tip":"After HIIT, keep moving gently for the first 2 minutes before you stretch. Never stop abruptly."},
    ],
    "Strength & Cardio": [
        {"name":"5-Minute Cardio Warm-Up","muscle":"Full Body","minutes":5,
         "sets_reps":"5 min","equipment":"Treadmill or Bike","difficulty":"Beginner",
         "steps":["Light jog or brisk walk for 5 minutes",
                  "Aim for 50–60% of max heart rate",
                  "Breathe through nose if possible",
                  "Finish with 30 sec at faster pace"],
         "tip":"This brief warm-up primes your cardiovascular system for the combined demands ahead."},
        {"name":"Dumbbell Full Body Circuit","muscle":"Full Body","minutes":20,
         "sets_reps":"3 rounds × 12 reps each","equipment":"Dumbbells","difficulty":"Beginner",
         "steps":["Dumbbell squat × 12 reps",
                  "Dumbbell bent-over row × 12 reps",
                  "Dumbbell push press × 12 reps",
                  "Dumbbell Romanian deadlift × 12 reps",
                  "Rest 60–90 sec between rounds"],
         "tip":"Moving straight through exercises keeps heart rate elevated — combined strength and cardio in one go."},
        {"name":"20-Min Moderate Cardio","muscle":"Cardiovascular","minutes":20,
         "sets_reps":"20 min steady state","equipment":"Treadmill, Bike or Elliptical","difficulty":"Beginner",
         "steps":["Choose machine, moderate resistance",
                  "Work at 60–70% max HR — conversational pace",
                  "Maintain pace for 20 minutes",
                  "Last 2 min: reduce intensity to cool down"],
         "tip":"60–70% max HR is the fat-burning zone. Formula: (220 − your age) × 0.65 = your target."},
        {"name":"Cool Down","muscle":"Full Body","minutes":8,
         "sets_reps":"8 min","equipment":"Exercise Mat","difficulty":"Beginner",
         "steps":["Standing quad stretch: 30 sec each leg",
                  "Chest stretch against wall: 30 sec",
                  "Seated hamstring stretch: 60 sec",
                  "5 slow deep breaths"],
         "tip":"Combining strength and cardio is demanding. Sleep and protein are especially important today."},
    ],
    "Light Cardio": [
        {"name":"Steady-State Cardio","muscle":"Cardiovascular","minutes":30,
         "sets_reps":"30 min continuous","equipment":"Treadmill, Bike or Elliptical","difficulty":"Beginner",
         "steps":["Choose preferred machine",
                  "Moderate conversational pace",
                  "Maintain consistent effort for 30 minutes",
                  "Focus on posture and steady breathing"],
         "tip":"Light cardio keeps metabolism elevated without muscular stress. Perfect for active rest days."},
        {"name":"Gentle Stretch","muscle":"Full Body","minutes":15,
         "sets_reps":"15 min","equipment":"Exercise Mat","difficulty":"Beginner",
         "steps":["Neck rolls: 30 sec each direction",
                  "Seated forward fold: 60 sec",
                  "Lying glute stretch: 45 sec each side",
                  "Child's pose: 60 sec",
                  "Cobra stretch: 30 sec × 2"],
         "tip":"Post-cardio your muscles are most pliable. Best time of the week to improve flexibility."},
    ],
    "Steady-State Cardio": [
        {"name":"Steady-State Cardio","muscle":"Cardiovascular · Endurance","minutes":40,
         "sets_reps":"40 min at zone 2","equipment":"Treadmill, Bike or Elliptical","difficulty":"Beginner",
         "steps":["5 min easy warm-up",
                  "Zone 2: 60–70% max HR — genuinely conversational",
                  "Hold pace for 30 minutes — resist going faster",
                  "5 min easy cool-down walk"],
         "tip":"Zone 2 builds your aerobic base — the foundation that makes all other training more effective. It should feel almost too easy. That's correct."},
        {"name":"Post-Cardio Stretch","muscle":"Legs & Hips","minutes":10,
         "sets_reps":"10 min","equipment":"Exercise Mat","difficulty":"Beginner",
         "steps":["Standing calf stretch: 30 sec each",
                  "Hip flexor kneeling stretch: 30 sec each",
                  "IT band stretch: 30 sec each side",
                  "Child's pose: 60 sec"],
         "tip":"Hip flexors and calves take the most stress during sustained cardio. Give them specific attention."},
    ],
    "Interval Training": [
        {"name":"Speed Intervals","muscle":"Cardiovascular · Legs","minutes":30,
         "sets_reps":"8 × 2 min hard / 2 min easy","equipment":"Treadmill or Track","difficulty":"Intermediate",
         "steps":["5 min easy jog warm-up",
                  "2 min at 80–85% max HR — genuinely hard",
                  "2 min recovery at 50% max HR — easy jog or walk",
                  "Repeat 8 times then 5 min easy cool-down"],
         "tip":"Intervals are the most time-efficient cardiovascular training that exists. The work intervals should be uncomfortable."},
        {"name":"Stretching","muscle":"Full Body","minutes":10,
         "sets_reps":"10 min","equipment":"Exercise Mat","difficulty":"Beginner",
         "steps":["Seated hamstring stretch: 60 sec",
                  "Standing quad stretch: 30 sec each",
                  "Kneeling hip flexor stretch: 30 sec each",
                  "Spinal twist: 30 sec each direction"],
         "tip":"Interval training creates significant muscular tension. Stretching post-session maintains stride length."},
    ],
    "Cross Training": [
        {"name":"Cross-Training Circuit","muscle":"Full Body — Active Recovery","minutes":35,
         "sets_reps":"3 machine rotations","equipment":"Various","difficulty":"Beginner",
         "steps":["10 min swimming or aqua jogging (low joint impact)",
                  "10 min rowing machine at moderate pace",
                  "10 min stationary bike",
                  "5 min easy walking cool-down"],
         "tip":"Cross training challenges your cardiovascular system while giving your primary muscles a complete rest."},
        {"name":"Gentle Stretching","muscle":"Full Body","minutes":10,
         "sets_reps":"10 min","equipment":"Exercise Mat","difficulty":"Beginner",
         "steps":["Cat-cow stretch: 60 sec",
                  "Chest opener: 30 sec",
                  "Seated forward fold: 60 sec",
                  "Lying spinal twist: 30 sec each side"],
         "tip":"Cross training days are about active recovery — keep this session easy and enjoy the variety."},
    ],
    "Long Cardio Session": [
        {"name":"Long Endurance Session","muscle":"Cardiovascular","minutes":60,
         "sets_reps":"60 min zone 2–3","equipment":"Treadmill, Bike or Elliptical","difficulty":"Intermediate",
         "steps":["10 min easy warm-up",
                  "40 min at zone 2–3 (65–75% max HR)",
                  "Final 5 min: push to zone 3 (75–80% max HR)",
                  "5 min easy cool-down"],
         "tip":"Long sessions build the aerobic base that makes everything else easier. Fuel properly beforehand."},
        {"name":"Full Body Cool Down","muscle":"Full Body","minutes":10,
         "sets_reps":"10 min","equipment":"Exercise Mat","difficulty":"Beginner",
         "steps":["3 min gentle walking — don't stop abruptly",
                  "Full body stretch: legs, hips, back, shoulders",
                  "5 slow controlled deep breaths",
                  "Foam roll tightest areas: 2 min"],
         "tip":"After 60 min of cardio, a structured wind-down is essential. Hydrate immediately and eat within 30 min."},
    ],
    "Recovery Cardio": [
        {"name":"Easy Recovery Walk/Jog","muscle":"Cardiovascular — Light","minutes":25,
         "sets_reps":"25 min at 40–50% max HR","equipment":"Treadmill or Outdoors","difficulty":"Beginner",
         "steps":["Walk or very light jog — conversation completely effortless",
                  "40–50% of max HR — very easy",
                  "Focus on good posture and relaxed breathing",
                  "Resist every urge to go faster — today is about recovery"],
         "tip":"Recovery cardio flushes lactic acid and brings fresh blood to repairing muscles. Its value is in its gentleness."},
        {"name":"Mobility Work","muscle":"Full Body","minutes":15,
         "sets_reps":"15 min","equipment":"Exercise Mat · Foam Roller","difficulty":"Beginner",
         "steps":["Foam roll quads, hamstrings, calves: 60 sec each",
                  "Hip 90-90 stretch: 45 sec each side",
                  "Ankle circles: 20 each direction",
                  "World's greatest stretch: 5 reps each side"],
         "tip":"Recovery days with mobility work are where the best athletes separate themselves. Use this time well."},
    ],
    "Yoga Flow": [
        {"name":"Sun Salutation Flow","muscle":"Full Body Flexibility","minutes":20,
         "sets_reps":"5 × full salutation","equipment":"Yoga Mat","difficulty":"Beginner",
         "steps":["Mountain → Forward fold → Halfway lift",
                  "Step back to high plank → Lower to Cobra or Upward Dog",
                  "Press up to Downward Dog → hold 5 deep breaths",
                  "Walk feet to hands → Halfway lift → Forward fold → Mountain"],
         "tip":"Move slower than feels natural. Sun salutations warm the entire spine and connect breath to movement."},
        {"name":"Standing Balance Poses","muscle":"Balance · Legs · Core","minutes":15,
         "sets_reps":"30–60 sec each pose","equipment":"Yoga Mat","difficulty":"Beginner",
         "steps":["Tree pose: 30 sec each leg (fix gaze on a still point)",
                  "Warrior I: 45 sec each side",
                  "Warrior II: 45 sec each side",
                  "Warrior III: 20 sec each side"],
         "tip":"Fix your gaze on a completely still point. Balance improves faster than almost any other fitness quality."},
        {"name":"Floor Poses & Cool Down","muscle":"Hips · Hamstrings · Lower Back","minutes":15,
         "sets_reps":"60 seconds each pose","equipment":"Yoga Mat","difficulty":"Beginner",
         "steps":["Seated forward fold: 60 sec",
                  "Butterfly pose: 60 sec",
                  "Supine spinal twist: 45 sec each side",
                  "Savasana — lie completely still: 3 full minutes"],
         "tip":"Savasana is not optional. It's when your nervous system integrates everything from the practice. Never skip it."},
    ],
    "Mobility Drills": [
        {"name":"Joint Mobility Circuit","muscle":"Full Body Joints","minutes":25,
         "sets_reps":"2 rounds × 10 reps each","equipment":"None","difficulty":"Beginner",
         "steps":["Neck: slow circles — 10 each direction",
                  "Shoulders: full arm circles — 10 forward, 10 backward",
                  "Hips: large circles — 10 each direction",
                  "Ankles: circles 10 each direction, then flexion/extension"],
         "tip":"Joint mobility produces synovial fluid — the lubricant that keeps joints healthy for decades."},
        {"name":"Thoracic Mobility","muscle":"Upper Back & Spine","minutes":15,
         "sets_reps":"2 rounds","equipment":"Foam Roller · Mat","difficulty":"Beginner",
         "steps":["Thoracic extension over foam roller: 2 min",
                  "Thread-the-needle rotation: 45 sec each side",
                  "Cat-cow: 10 very slow, deliberate reps",
                  "Open book rotation: 10 each side"],
         "tip":"Most desk workers have severe thoracic stiffness. Fixing this transforms your posture and eliminates neck pain."},
    ],
    "Deep Stretch": [
        {"name":"Full Body Deep Stretch","muscle":"All Major Muscle Groups","minutes":45,
         "sets_reps":"Hold each 60–90 seconds","equipment":"Yoga Mat · Strap (optional)","difficulty":"Beginner",
         "steps":["Hip flexor kneeling lunge: 90 sec each side",
                  "Pigeon pose (glutes/hip rotators): 90 sec each side",
                  "Seated hamstring stretch: 90 sec",
                  "Doorway chest stretch: 60 sec",
                  "Supine spinal twist: 60 sec each side",
                  "Child's pose: 2 full minutes to finish"],
         "tip":"Never force a deep stretch. Breathe into tension and wait for the muscle to release — it always does, given time and breath."},
    ],
    "Active Mobility": [
        {"name":"Active Mobility Flow","muscle":"Full Body","minutes":40,
         "sets_reps":"Continuous flow","equipment":"Yoga Mat","difficulty":"Beginner",
         "steps":["5 min foam rolling — target tightest spots",
                  "10 min joint circles: neck, shoulders, hips, ankles",
                  "10 min slow yoga flow (sun salutations)",
                  "10 min deep stretch — focus on areas trained this week",
                  "5 min box breathing: 4s in, 4s hold, 4s out, 4s hold"],
         "tip":"This weekly session compounds over months into exceptional flexibility and near-zero injury risk."},
    ],
}

REST_TIPS = [
    ("💤","Sleep 7–9 hours",    "This is when your muscles actually repair and grow."),
    ("🥩","Hit your protein",   "Aim for 1.6–2g per kg of bodyweight today."),
    ("💧","Stay hydrated",      "At least 2–3 litres of water throughout the day."),
    ("🚶","Light walk",         "20–30 min easy walking aids blood flow and recovery."),
    ("📋","Review your plan",   "Track your progress and plan your next week."),
    ("🧊","Contrast shower",    "Alternating hot/cold reduces soreness significantly."),
]

# ═══════════════════════════════════════════════════════════════════════════
#  CSS — PREMIUM DARK + FULLY MOBILE RESPONSIVE
# ═══════════════════════════════════════════════════════════════════════════

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html,body,[class*="css"]{font-family:'Inter',sans-serif;}
#MainMenu,footer,header{visibility:hidden;}
.block-container{padding:0.75rem 1rem 3rem !important;max-width:1280px !important;}

/* ── HERO ── */
.hero{position:relative;border-radius:20px;overflow:hidden;min-height:250px;display:flex;align-items:center;margin-bottom:2rem;
  background:url('https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=1400&q=80') center/cover no-repeat;}
.hero-ov{position:absolute;inset:0;border-radius:20px;
  background:linear-gradient(120deg,rgba(5,5,15,0.96) 0%,rgba(5,5,15,0.82) 55%,rgba(5,5,15,0.55) 100%);}
.hero-cnt{position:relative;z-index:2;padding:2.5rem 3rem;}
.h-eye{font-size:0.65rem;font-weight:800;letter-spacing:0.2em;text-transform:uppercase;color:#FF3E3E;margin-bottom:0.6rem;}
.h-ttl{font-size:2.8rem;font-weight:900;color:#fff;line-height:1.05;margin-bottom:0.8rem;}
.h-ttl span{color:#FF3E3E;}
.h-sub{font-size:0.9rem;color:rgba(255,255,255,0.5);max-width:400px;line-height:1.6;margin-bottom:1.2rem;}
.h-pills{display:flex;gap:8px;flex-wrap:wrap;}
.h-pill{padding:5px 12px;border-radius:99px;background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.14);font-size:0.72rem;color:rgba(255,255,255,0.68);font-weight:500;}

/* ── SECTION LABELS ── */
.s-eye{font-size:0.65rem;font-weight:800;letter-spacing:0.15em;text-transform:uppercase;color:#FF3E3E;margin-bottom:0.4rem;}
.s-ttl{font-size:1.5rem;font-weight:800;color:#fff;margin-bottom:1.2rem;}

/* ── GOAL CARDS ── */
.goals-row{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin-bottom:0.5rem;}
.gc{border-radius:16px;padding:1.3rem 1rem;border:1.5px solid rgba(255,255,255,0.07);background:#111118;text-align:center;transition:all 0.2s;}
.gc:hover{border-color:rgba(255,62,62,0.5);transform:translateY(-3px);box-shadow:0 10px 28px rgba(255,62,62,0.15);}
.gc.on{border-color:#FF3E3E;background:rgba(255,62,62,0.08);box-shadow:0 10px 28px rgba(255,62,62,0.2);}
.g-em{font-size:2.1rem;margin-bottom:0.6rem;display:block;}
.g-nm{font-size:0.85rem;font-weight:700;color:#fff;margin-bottom:0.3rem;}
.g-ds{font-size:0.68rem;color:rgba(255,255,255,0.38);line-height:1.4;}

/* ── SCHEDULE BOX ── */
.sb{background:#111118;border-radius:18px;border:1.5px solid rgba(255,255,255,0.07);padding:1.5rem;margin-bottom:1.25rem;}
.sb-hint{font-size:0.78rem;color:rgba(255,255,255,0.38);margin-bottom:0.85rem;line-height:1.5;}
.sb-hint strong{color:rgba(255,255,255,0.65);}

/* ── WEEK VISUAL ── */
.wk{display:grid;grid-template-columns:repeat(7,1fr);gap:6px;margin-bottom:1rem;}
.wk-c{border-radius:10px;padding:10px 4px;text-align:center;border:1.5px solid;}
.wk-t{border-color:#FF3E3E;background:rgba(255,62,62,0.1);}
.wk-r{border-color:rgba(255,255,255,0.07);background:rgba(255,255,255,0.02);}
.wk-d{font-size:0.58rem;font-weight:800;text-transform:uppercase;letter-spacing:0.06em;color:rgba(255,255,255,0.28);margin-bottom:4px;}
.wk-s{font-size:0.58rem;font-weight:700;}
.wk-st{color:#FF3E3E;} .wk-sr{color:rgba(255,255,255,0.2);}

/* ── NOTICE ── */
.notice{background:rgba(255,140,0,0.08);border:1px solid rgba(255,140,0,0.22);border-radius:10px;padding:10px 14px;font-size:0.79rem;color:rgba(255,200,100,0.88);margin-bottom:1rem;}

/* ── SUMMARY ── */
.sum{display:flex;margin-bottom:1.25rem;background:#111118;border-radius:14px;border:1.5px solid rgba(255,255,255,0.07);overflow:hidden;flex-wrap:wrap;}
.sc{flex:1;min-width:70px;padding:1rem 0.5rem;text-align:center;border-right:1px solid rgba(255,255,255,0.05);}
.sc:last-child{border-right:none;}
.sv{font-size:1.5rem;font-weight:900;color:#FF3E3E;line-height:1;}
.sl{font-size:0.58rem;font-weight:700;text-transform:uppercase;letter-spacing:0.08em;color:rgba(255,255,255,0.28);margin-top:3px;}

/* ── VIEW HEADER ── */
.vh{margin-bottom:1rem;}
.vh-eye{font-size:0.62rem;font-weight:800;letter-spacing:0.15em;text-transform:uppercase;color:#FF3E3E;margin-bottom:3px;}
.vh-ttl{font-size:1.7rem;font-weight:900;color:#fff;}

/* ── EXERCISE GRID — CSS grid collapses to 1 col on mobile ── */
.ex-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;}

/* ── EXERCISE CARD ── */
.ex-card{background:#111118;border-radius:18px;border:1.5px solid rgba(255,255,255,0.06);overflow:hidden;transition:border-color 0.2s,box-shadow 0.2s;}
.ex-card:hover{border-color:rgba(255,62,62,0.28);box-shadow:0 8px 28px rgba(0,0,0,0.5);}
.ex-img{position:relative;height:210px;overflow:hidden;background:#0D0D14;}
.ex-img img{width:100%;height:100%;object-fit:cover;display:block;transition:transform 0.4s;}
.ex-card:hover .ex-img img{transform:scale(1.05);}
.ex-g{position:absolute;inset:0;background:linear-gradient(to top,rgba(5,5,15,0.92) 0%,rgba(5,5,15,0.12) 55%,transparent 100%);}
.ex-bs{position:absolute;top:12px;left:12px;right:12px;display:flex;justify-content:space-between;align-items:flex-start;}
.ex-n{width:30px;height:30px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:0.8rem;font-weight:800;color:#fff;backdrop-filter:blur(8px);}
.ex-m{padding:3px 9px;border-radius:99px;font-size:0.58rem;font-weight:800;text-transform:uppercase;letter-spacing:0.07em;color:#fff;background:rgba(255,62,62,0.72);backdrop-filter:blur(8px);}
.ex-nm{position:absolute;bottom:10px;left:13px;right:13px;font-size:0.95rem;font-weight:800;color:#fff;line-height:1.2;}
.ex-body{padding:1.1rem 1.2rem 1.2rem;}
.mr{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:0.9rem;}
.mb{display:inline-flex;align-items:center;gap:4px;padding:4px 9px;border-radius:99px;font-size:0.68rem;font-weight:700;}
.m-t{background:rgba(62,139,255,0.13);color:#60A5FA;}
.m-s{background:rgba(255,62,62,0.13);color:#FF7070;}
.m-e{background:rgba(168,85,247,0.13);color:#C084FC;}
.m-d{background:rgba(0,200,150,0.13);color:#34D399;}
.slbl{font-size:0.6rem;font-weight:800;text-transform:uppercase;letter-spacing:0.12em;color:rgba(255,255,255,0.26);margin-bottom:0.55rem;}
.sul{list-style:none;margin-bottom:0.85rem;}
.sul li{font-size:0.8rem;color:rgba(255,255,255,0.62);padding:4px 0 4px 22px;position:relative;line-height:1.5;border-bottom:1px solid rgba(255,255,255,0.04);}
.sul li:last-child{border-bottom:none;}
.sul li::before{content:attr(data-n);position:absolute;left:0;width:16px;height:16px;background:rgba(255,62,62,0.16);color:#FF3E3E;font-weight:800;font-size:0.62rem;border-radius:4px;display:flex;align-items:center;justify-content:center;top:5px;}
.tip{background:linear-gradient(135deg,rgba(255,140,0,0.08),rgba(255,62,62,0.05));border:1px solid rgba(255,140,0,0.2);border-radius:10px;padding:9px 11px;display:flex;gap:7px;align-items:flex-start;}
.ti{font-size:0.88rem;flex-shrink:0;margin-top:1px;}
.tt{font-size:0.75rem;color:rgba(255,255,255,0.55);line-height:1.5;}
.tb{font-weight:700;color:#FF8C00;}

/* ── REST DAY ── */
.rest-hero{border-radius:18px;overflow:hidden;position:relative;min-height:190px;display:flex;align-items:center;
  background:url('https://images.unsplash.com/photo-1552196563-55cd4e45efb3?w=1200&q=80') center/cover;margin-bottom:1.25rem;}
.rest-ov{position:absolute;inset:0;background:linear-gradient(120deg,rgba(5,20,5,0.93),rgba(10,30,10,0.7));}
.rest-cnt{position:relative;z-index:2;padding:2rem 2.5rem;}
.rt-tag{font-size:0.62rem;font-weight:800;letter-spacing:0.2em;text-transform:uppercase;color:#34D399;margin-bottom:0.4rem;}
.rt-h{font-size:1.7rem;font-weight:900;color:#fff;margin-bottom:0.4rem;}
.rt-sub{font-size:0.83rem;color:rgba(255,255,255,0.48);max-width:360px;line-height:1.6;}
.rg{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;}
.rt{background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.07);border-radius:12px;padding:1rem;}
.rt-ico{font-size:1.15rem;margin-bottom:0.4rem;display:block;}
.rt-ttl{font-size:0.77rem;font-weight:700;color:#fff;margin-bottom:2px;}
.rt-dsc{font-size:0.68rem;color:rgba(255,255,255,0.36);line-height:1.4;}

/* ── STREAMLIT OVERRIDES ── */
.stButton>button{border-radius:99px !important;font-weight:700 !important;font-size:0.78rem !important;
  border:1.5px solid rgba(255,62,62,0.42) !important;color:#FF3E3E !important;
  background:rgba(255,62,62,0.05) !important;padding:0.38rem 1rem !important;transition:all 0.15s !important;}
.stButton>button:hover{background:#FF3E3E !important;color:#fff !important;border-color:#FF3E3E !important;}

/* ── CHECKBOX ROW — make checkboxes look like day-toggle pills ── */
div[data-testid="stCheckbox"] label {font-size:0.78rem !important;font-weight:700 !important;color:rgba(255,255,255,0.55) !important;}

/* ══ MOBILE RESPONSIVE ══ */
@media screen and (max-width:900px){
  .goals-row{grid-template-columns:repeat(3,1fr);}
  .h-ttl{font-size:2.2rem;}
  .hero-cnt{padding:2rem;}
  .rg{grid-template-columns:repeat(2,1fr);}
}
@media screen and (max-width:680px){
  .goals-row{grid-template-columns:repeat(2,1fr);}
  .h-ttl{font-size:1.85rem;}
  .hero-cnt{padding:1.5rem 1.2rem;}
  .h-sub{display:none;}
  .wk{grid-template-columns:repeat(4,1fr);}
  .ex-grid{grid-template-columns:1fr !important;}
  .sum{flex-wrap:wrap;}
  .sc{flex:0 0 50%;border-right:none;border-bottom:1px solid rgba(255,255,255,0.05);}
  .rg{grid-template-columns:1fr 1fr;}
  .rest-cnt{padding:1.5rem 1.2rem;}
  .rt-h{font-size:1.4rem;}
  .s-ttl{font-size:1.25rem;}
  .vh-ttl{font-size:1.3rem;}
}
@media screen and (max-width:420px){
  .goals-row{grid-template-columns:1fr 1fr;}
  .wk{grid-template-columns:repeat(3,1fr);}
  .h-ttl{font-size:1.55rem;}
  .rg{grid-template-columns:1fr;}
  .h-pills{display:none;}
  .block-container{padding:0.4rem 0.5rem 2rem !important;}
  .hero-cnt{padding:1.2rem 1rem;}
}
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════
#  SESSION STATE
# ═══════════════════════════════════════════════════════════════════════════

for k, v in [("goal", None), ("training_days", ["Monday","Tuesday","Thursday","Friday"]), ("viewing_day", None)]:
    if k not in st.session_state:
        st.session_state[k] = v

# ═══════════════════════════════════════════════════════════════════════════
#  HERO
# ═══════════════════════════════════════════════════════════════════════════

st.markdown("""
<div class="hero">
  <div class="hero-ov"></div>
  <div class="hero-cnt">
    <div class="h-eye">Your Personal Training Companion</div>
    <div class="h-ttl">Gym<span>Guide</span><br>Premium</div>
    <div class="h-sub">Pick your goal, choose your training days — get a full visual workout plan that fits your life.</div>
    <div class="h-pills">
      <span class="h-pill">📸 Category-matched images</span>
      <span class="h-pill">⏱ Time per exercise</span>
      <span class="h-pill">📅 1–7 day flexibility</span>
      <span class="h-pill">📱 Mobile friendly</span>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════
#  STEP 1 — GOAL
# ═══════════════════════════════════════════════════════════════════════════

st.markdown('<div class="s-eye">Step 1 of 3</div>', unsafe_allow_html=True)
st.markdown('<div class="s-ttl">Choose your fitness goal</div>', unsafe_allow_html=True)

goal_names = list(GOAL_POOLS.keys())
cols = st.columns(len(goal_names))
for col, gk in zip(cols, goal_names):
    g = GOAL_POOLS[gk]
    cls = "on" if st.session_state.goal == gk else ""
    with col:
        st.markdown(f"""
        <div class="gc {cls}">
          <span class="g-em">{g['icon']}</span>
          <div class="g-nm">{gk.split(' ',1)[1]}</div>
          <div class="g-ds">{g['desc']}</div>
        </div>""", unsafe_allow_html=True)
        if st.button("Select", key=f"g_{gk}"):
            st.session_state.goal = gk
            st.session_state.viewing_day = None
            st.rerun()

# ═══════════════════════════════════════════════════════════════════════════
#  STEP 2 — FLEXIBLE SCHEDULE BUILDER
#  Uses checkboxes (one per day) — no "No results" bug, works on mobile
# ═══════════════════════════════════════════════════════════════════════════

if st.session_state.goal:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="s-eye">Step 2 of 3</div>', unsafe_allow_html=True)
    st.markdown('<div class="s-ttl">Build your weekly schedule</div>', unsafe_allow_html=True)

    st.markdown('<div class="sb">', unsafe_allow_html=True)
    st.markdown("""
    <div class="sb-hint">
      Tick the days you want to <strong>train</strong>. Rest days are automatically assigned to the others.
      You can choose any number from 1 to 7 — the plan adapts to your life.
    </div>""", unsafe_allow_html=True)

    # 7 checkboxes in a row — always shows all 7, no dropdown bugs
    day_cols = st.columns(7)
    selected_days = []
    for col, day in zip(day_cols, ALL_DAYS):
        with col:
            default_val = day in st.session_state.training_days
            checked = st.checkbox(day[:3], value=default_val, key=f"ck_{day}")
            if checked:
                selected_days.append(day)

    st.session_state.training_days = selected_days
    n = len(selected_days)

    if n == 0:
        st.markdown('<div class="notice">👆 Tick at least one day above to build your schedule.</div>',
                    unsafe_allow_html=True)
    else:
        schedule = build_schedule(st.session_state.goal, selected_days)

        if n == 1:
            st.markdown('<div class="notice">💡 1 day/week is a great start! Consider adding more days when you feel ready.</div>', unsafe_allow_html=True)
        elif n == 2:
            st.markdown('<div class="notice">💡 2 days/week builds a solid foundation. 3–4 days gives optimal results.</div>', unsafe_allow_html=True)

        cells = ""
        for day in ALL_DAYS:
            sess = schedule[day]
            is_t = sess != "Rest"
            lbl  = sess[:8].upper() if is_t else "REST"
            cells += (f'<div class="wk-c {"wk-t" if is_t else "wk-r"}">'
                      f'<div class="wk-d">{DAY_ABB[day]}</div>'
                      f'<div class="wk-s {"wk-st" if is_t else "wk-sr"}">{lbl}</div></div>')
        st.markdown(f'<div class="wk">{cells}</div>', unsafe_allow_html=True)
        st.markdown(f'<p style="font-size:0.7rem;color:rgba(255,255,255,0.22);text-align:right;">{n} training · {7-n} rest days per week</p>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════
#  STEP 3 — WORKOUT VIEW
# ═══════════════════════════════════════════════════════════════════════════

if st.session_state.goal and len(st.session_state.training_days) > 0:
    schedule = build_schedule(st.session_state.goal, st.session_state.training_days)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="s-eye">Step 3 of 3</div>', unsafe_allow_html=True)
    st.markdown('<div class="s-ttl">Select a day to view your workout</div>', unsafe_allow_html=True)

    dcols = st.columns(7)
    for col, day in zip(dcols, ALL_DAYS):
        sess = schedule[day]
        with col:
            icon = "😴" if sess == "Rest" else "🏋️"
            if st.button(f"{icon} {day[:3]}", key=f"v_{day}"):
                st.session_state.viewing_day = day
                st.rerun()

    if st.session_state.viewing_day:
        vday    = st.session_state.viewing_day
        session = schedule[vday]
        st.markdown("<br>", unsafe_allow_html=True)

        if session == "Rest":
            tips_html = "".join(
                f'<div class="rt"><span class="rt-ico">{ic}</span>'
                f'<div class="rt-ttl">{ti}</div><div class="rt-dsc">{de}</div></div>'
                for ic, ti, de in REST_TIPS
            )
            st.markdown(f"""
            <div class="rest-hero">
              <div class="rest-ov"></div>
              <div class="rest-cnt">
                <div class="rt-tag">Recovery Day — {vday}</div>
                <div class="rt-h">Rest & Recover 🛌</div>
                <div class="rt-sub">Muscle growth happens during rest. Today is just as important as your training days.</div>
              </div>
            </div>
            <div class="rg">{tips_html}</div>""", unsafe_allow_html=True)

        else:
            exercises = EXERCISES.get(session, [])
            if not exercises:
                st.info(f"Session **{session}** is coming soon!")
            else:
                total_min    = sum(e["minutes"] for e in exercises)
                working_ex   = len([e for e in exercises if "Cool" not in e["name"] and "Warm" not in e["name"]])
                warmup_min   = sum(e["minutes"] for e in exercises if "Warm" in e["name"])
                cooldown_min = sum(e["minutes"] for e in exercises if "Cool" in e["name"])

                st.markdown(f"""
                <div class="vh">
                  <div class="vh-eye">{vday} · {st.session_state.goal.split(' ',1)[1]}</div>
                  <div class="vh-ttl">{session}</div>
                </div>
                <div class="sum">
                  <div class="sc"><div class="sv">{total_min}</div><div class="sl">Total mins</div></div>
                  <div class="sc"><div class="sv">{working_ex}</div><div class="sl">Exercises</div></div>
                  <div class="sc"><div class="sv">{warmup_min}</div><div class="sl">Warm-up</div></div>
                  <div class="sc"><div class="sv">{cooldown_min}</div><div class="sl">Cool-down</div></div>
                </div>""", unsafe_allow_html=True)

                fallback_url = f"https://images.unsplash.com/photo-{FALLBACK}?w=800&h=360&fit=crop&q=80"
                cards = '<div class="ex-grid">'
                for i, ex in enumerate(exercises):
                    is_cool = "Cool" in ex["name"]
                    is_warm = "Warm" in ex["name"]
                    nbg = ("rgba(0,200,150,0.55)" if is_cool
                           else "rgba(62,139,255,0.55)" if is_warm
                           else "rgba(255,62,62,0.55)")
                    src = img_url(ex["name"])
                    lis = "".join(f'<li data-n="{j+1}">{s}</li>' for j,s in enumerate(ex["steps"]))
                    cards += f"""
                    <div class="ex-card">
                      <div class="ex-img">
                        <img src="{src}" alt="{ex['name']}"
                             onerror="this.onerror=null;this.src='{fallback_url}'">
                        <div class="ex-g"></div>
                        <div class="ex-bs">
                          <div class="ex-n" style="background:{nbg};">{i+1}</div>
                          <div class="ex-m">{ex['muscle']}</div>
                        </div>
                        <div class="ex-nm">{ex['name']}</div>
                      </div>
                      <div class="ex-body">
                        <div class="mr">
                          <span class="mb m-t">⏱ {ex['minutes']} min</span>
                          <span class="mb m-s">🔁 {ex['sets_reps']}</span>
                          <span class="mb m-e">🏋️ {ex['equipment']}</span>
                          <span class="mb m-d">⭐ {ex['difficulty']}</span>
                        </div>
                        <div class="slbl">How to perform it</div>
                        <ul class="sul">{lis}</ul>
                        <div class="tip">
                          <span class="ti">💡</span>
                          <div class="tt"><span class="tb">Coach tip: </span>{ex['tip']}</div>
                        </div>
                      </div>
                    </div>"""
                cards += '</div>'
                st.markdown(cards, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════
#  FOOTER
# ═══════════════════════════════════════════════════════════════════════════

st.markdown("""
<div style="text-align:center;padding:2rem 0 0.5rem;font-size:0.7rem;color:rgba(255,255,255,0.16);">
  GymGuide Premium — Always consult a qualified professional before starting a new exercise programme.
</div>""", unsafe_allow_html=True)
