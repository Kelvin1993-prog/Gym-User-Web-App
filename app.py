"""
GymGuide — Interactive Workout Planner
Single-file version: guaranteed to work on Streamlit Cloud with no import issues.
Upload ONLY this file + requirements.txt to your GitHub repo root.
"""

import streamlit as st

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="GymGuide – Your Personal Workout Planner",
    page_icon="💪",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ═════════════════════════════════════════════════════════════════════════════
# DATA
# ═════════════════════════════════════════════════════════════════════════════

GOALS = {
    "💪 Build Muscle & Strength": {
        "icon": "💪",
        "desc": "Heavy lifting, compound movements, progressive overload",
        "days": {
            "Monday": "Upper Push", "Tuesday": "Lower A", "Wednesday": "Rest",
            "Thursday": "Upper Pull", "Friday": "Lower B",
            "Saturday": "Rest", "Sunday": "Rest",
        },
    },
    "🏃 General Fitness": {
        "icon": "🏃",
        "desc": "Balanced mix of strength, cardio and flexibility",
        "days": {
            "Monday": "Full Body Strength", "Tuesday": "Cardio & Core",
            "Wednesday": "Rest", "Thursday": "Full Body Strength",
            "Friday": "Cardio & Flexibility", "Saturday": "Active Recovery",
            "Sunday": "Rest",
        },
    },
    "🔥 Weight Loss & Toning": {
        "icon": "🔥",
        "desc": "High-intensity circuits, fat burning & body recomposition",
        "days": {
            "Monday": "HIIT & Circuits", "Tuesday": "Strength & Cardio",
            "Wednesday": "Rest", "Thursday": "HIIT & Circuits",
            "Friday": "Strength & Cardio", "Saturday": "Light Cardio",
            "Sunday": "Rest",
        },
    },
    "🚴 Endurance & Cardio": {
        "icon": "🚴",
        "desc": "Aerobic capacity, stamina and cardiovascular health",
        "days": {
            "Monday": "Steady-State Cardio", "Tuesday": "Interval Training",
            "Wednesday": "Cross Training", "Thursday": "Rest",
            "Friday": "Long Cardio Session", "Saturday": "Recovery Cardio",
            "Sunday": "Rest",
        },
    },
    "🧘 Flexibility & Mobility": {
        "icon": "🧘",
        "desc": "Yoga, stretching, joint health and posture improvement",
        "days": {
            "Monday": "Yoga Flow", "Tuesday": "Mobility Drills",
            "Wednesday": "Rest", "Thursday": "Yoga Flow",
            "Friday": "Deep Stretch", "Saturday": "Active Mobility",
            "Sunday": "Rest",
        },
    },
}

REST_TIPS = [
    ("💤", "Sleep 7–9 hours",     "This is when muscle is built and hormones reset."),
    ("🥩", "Eat enough protein",   "Aim for 1.6–2g per kg of bodyweight daily."),
    ("💧", "Stay hydrated",        "Drink at least 2–3 litres of water today."),
    ("🚶", "Light walk outside",   "20–30 minutes of fresh air aids recovery."),
    ("📖", "Visualise your goals", "Review your plan and track your progress."),
    ("🛁", "Contrast shower",      "Alternating hot/cold water reduces muscle soreness."),
]

EXERCISES = {

    "Upper Push": [
        {"name": "Treadmill Warm-Up", "muscle": "Full Body Warm-Up", "minutes": 10,
         "sets_reps": "10 min continuous", "equipment": "Treadmill", "difficulty": "Beginner",
         "steps": ["Start at a comfortable walking pace (4–5 km/h)",
                   "Gradually increase to a light jog over 5 minutes",
                   "Keep arms swinging naturally, breathe steadily",
                   "Last 2 minutes: return to walking to transition into lifting"],
         "tip": "Never skip your warm-up — it primes your muscles and reduces injury risk."},
        {"name": "Barbell Bench Press", "muscle": "Chest · Shoulders · Triceps", "minutes": 15,
         "sets_reps": "3 sets × 8–10 reps", "equipment": "Barbell, Bench, Rack", "difficulty": "Beginner",
         "steps": ["Lie flat on the bench, grip bar just wider than shoulder-width",
                   "Unrack the bar and hold it directly above your chest",
                   "Lower bar slowly to mid-chest — elbows at about 45°",
                   "Drive the bar back up explosively until arms are extended",
                   "Keep feet flat, back slightly arched, core braced throughout"],
         "tip": "Start with just the barbell (20 kg) to practise form. A spotter is highly recommended!"},
        {"name": "Dumbbell Shoulder Press", "muscle": "Shoulders · Triceps", "minutes": 12,
         "sets_reps": "3 sets × 10–12 reps", "equipment": "Dumbbells, Adjustable Bench", "difficulty": "Beginner",
         "steps": ["Sit on an upright bench, dumbbells at shoulder height, palms forward",
                   "Press dumbbells overhead until arms are straight",
                   "Don't fully lock out elbows — keep a slight bend at the top",
                   "Lower dumbbells slowly back to shoulder height and repeat"],
         "tip": "Keep your lower back pressed into the bench. Arching excessively strains your spine."},
        {"name": "Cable Tricep Pushdown", "muscle": "Triceps", "minutes": 10,
         "sets_reps": "3 sets × 12 reps", "equipment": "Cable Machine, Rope or Bar", "difficulty": "Beginner",
         "steps": ["Set the cable pulley to head height and attach a straight bar or rope",
                   "Grip the attachment, tuck elbows tight to your sides",
                   "Push handle straight down until arms are fully extended",
                   "Slowly return to start — elbows must NOT move forward or back"],
         "tip": "If your elbows fly forward, the weight is too heavy. Elbows stay locked at your sides."},
        {"name": "Dumbbell Chest Fly", "muscle": "Chest (Outer)", "minutes": 10,
         "sets_reps": "3 sets × 12 reps", "equipment": "Dumbbells, Flat Bench", "difficulty": "Beginner",
         "steps": ["Lie on a flat bench, hold dumbbells above chest with slight elbow bend",
                   "Open arms wide in a large arc, feeling a deep chest stretch at the bottom",
                   "Squeeze your chest to bring dumbbells back together at the top",
                   "Maintain the slight elbow bend throughout — never fully straighten arms"],
         "tip": "Think of hugging a large tree. Don't let the dumbbells drop too low — shoulder height is your limit."},
        {"name": "Cool Down & Stretching", "muscle": "Full Body", "minutes": 8,
         "sets_reps": "8 min — hold each stretch 30s", "equipment": "Exercise Mat", "difficulty": "Beginner",
         "steps": ["Chest doorway stretch: 30 seconds each side",
                   "Tricep overhead stretch: 30 seconds each arm",
                   "Shoulder cross-body stretch: 30 seconds each",
                   "Seated forward fold for back and hamstrings: 60 seconds"],
         "tip": "Static stretching after training improves flexibility and reduces next-day soreness."},
    ],

    "Lower A": [
        {"name": "Dynamic Warm-Up", "muscle": "Legs & Hips", "minutes": 8,
         "sets_reps": "2 rounds of circuit", "equipment": "None", "difficulty": "Beginner",
         "steps": ["10 × Leg swings (front-to-back) each leg",
                   "10 × Hip circles each direction",
                   "10 × Bodyweight squats (slow and controlled)",
                   "10 × Walking lunges across the room"],
         "tip": "Dynamic warm-ups activate your hip flexors and glutes — essential before heavy leg work."},
        {"name": "Barbell Squat", "muscle": "Quads · Glutes · Hamstrings", "minutes": 18,
         "sets_reps": "3 sets × 8–10 reps", "equipment": "Barbell, Squat Rack", "difficulty": "Intermediate",
         "steps": ["Set bar at shoulder height in the rack; step under and rest it on your traps",
                   "Feet shoulder-width apart, toes turned out slightly",
                   "Take a deep breath, brace your core, then sit down and back",
                   "Squat until thighs are parallel to the floor (or below)",
                   "Drive through your heels to stand back up — chest stays up throughout"],
         "tip": "Beginners: start with just the bar and practise the movement for 2 weeks before adding plates."},
        {"name": "Leg Press Machine", "muscle": "Quads · Glutes", "minutes": 14,
         "sets_reps": "3 sets × 10–12 reps", "equipment": "Leg Press Machine", "difficulty": "Beginner",
         "steps": ["Adjust the seat so knees bend to ~90° at the bottom",
                   "Place feet shoulder-width on the platform",
                   "Release safety handles and lower the plate toward you in control",
                   "Push through your heels until legs are nearly (not fully) extended"],
         "tip": "Perfect for beginners — the machine guides movement so you can build quad strength safely."},
        {"name": "Romanian Deadlift", "muscle": "Hamstrings · Glutes", "minutes": 14,
         "sets_reps": "3 sets × 10 reps", "equipment": "Barbell or Dumbbells", "difficulty": "Intermediate",
         "steps": ["Stand holding a bar at hip height, feet hip-width, soft knee bend",
                   "Hinge at the hips — push them BACK, not down",
                   "Let the bar slide down your legs until you feel a hamstring stretch",
                   "Drive hips forward to return upright — squeeze glutes at the top",
                   "Keep your back flat and shoulders pulled back throughout"],
         "tip": "Imagine closing a car door with your bum — that hip-hinge pattern is exactly what you need."},
        {"name": "Leg Curl Machine", "muscle": "Hamstrings", "minutes": 10,
         "sets_reps": "3 sets × 12 reps", "equipment": "Lying Leg Curl Machine", "difficulty": "Beginner",
         "steps": ["Lie face down, position the pad just above your heels",
                   "Curl legs upward as far as possible without lifting your hips",
                   "Squeeze hamstrings hard at the top for 1 second",
                   "Lower slowly over 3 seconds — the eccentric phase builds the most muscle"],
         "tip": "The slow lowering phase is where most muscle growth happens. Don't just drop the weight!"},
        {"name": "Cool Down & Stretching", "muscle": "Legs & Hips", "minutes": 8,
         "sets_reps": "8 min", "equipment": "Exercise Mat", "difficulty": "Beginner",
         "steps": ["Standing quad stretch: 30 seconds each leg",
                   "Seated hamstring stretch: 60 seconds",
                   "Pigeon pose for glutes: 45 seconds each side",
                   "Calf stretch against wall: 30 seconds each"],
         "tip": "Tight hips and hamstrings are the #1 cause of lower back pain. Stretch every session!"},
    ],

    "Upper Pull": [
        {"name": "Rowing Machine Warm-Up", "muscle": "Back, Arms & Core", "minutes": 8,
         "sets_reps": "8 min steady pace", "equipment": "Rowing Machine", "difficulty": "Beginner",
         "steps": ["Strap feet in, grip the handle with an overhand grip",
                   "Push with legs first, then lean back slightly, then pull arms in",
                   "Reverse the sequence to return: arms extend, lean forward, legs bend",
                   "Keep a consistent rhythm — aim for 20–24 strokes per minute"],
         "tip": "The rowing machine warms up your entire back and arms — perfect prep for a pull day!"},
        {"name": "Lat Pulldown", "muscle": "Lats · Upper Back", "minutes": 14,
         "sets_reps": "3 sets × 10–12 reps", "equipment": "Lat Pulldown Machine", "difficulty": "Beginner",
         "steps": ["Sit and adjust the knee pad to secure your legs",
                   "Grip the bar wider than shoulder-width, overhand grip",
                   "Lean back slightly and pull bar to your upper chest",
                   "Lead with your elbows — imagine tucking them into your back pockets",
                   "Let the bar rise slowly with full arm extension between reps"],
         "tip": "Think 'elbows to hips' not 'hands to chest'. This engages your lats far more effectively."},
        {"name": "Seated Cable Row", "muscle": "Mid-Back · Lats · Rear Delts", "minutes": 14,
         "sets_reps": "3 sets × 10–12 reps", "equipment": "Cable Row Station", "difficulty": "Beginner",
         "steps": ["Sit with feet on the platform, slight bend in knees, back straight",
                   "Grip the handle and sit tall — don't lean back excessively",
                   "Pull handle toward your lower ribcage, leading with elbows",
                   "Squeeze shoulder blades together firmly at the end of the pull",
                   "Extend arms back out in a slow, controlled 3-second return"],
         "tip": "Your torso should barely move. If you're rocking back and forth, reduce the weight."},
        {"name": "Dumbbell Bicep Curl", "muscle": "Biceps", "minutes": 10,
         "sets_reps": "3 sets × 12 reps", "equipment": "Dumbbells", "difficulty": "Beginner",
         "steps": ["Stand with dumbbells at your sides, palms facing forward",
                   "Curl both dumbbells up toward your shoulders simultaneously",
                   "Squeeze biceps hard at the top — hold 1 second",
                   "Lower slowly over 2–3 seconds back to start",
                   "Don't swing your back or use momentum — control is everything"],
         "tip": "Alternate arms for better mind-muscle connection. NEVER swing your back!"},
        {"name": "Cable Face Pull", "muscle": "Rear Delts · Rotator Cuff", "minutes": 10,
         "sets_reps": "3 sets × 15 reps", "equipment": "Cable Machine, Rope Attachment", "difficulty": "Beginner",
         "steps": ["Set the pulley at face height, attach the rope",
                   "Grip the rope with thumbs pointing toward you, step back",
                   "Pull the rope toward your face, flaring elbows out to the sides",
                   "Separate the rope at the end, squeezing rear delts",
                   "Return slowly to the start position"],
         "tip": "The #1 shoulder health exercise. Light weight, high reps, always. Don't skip this one!"},
        {"name": "Cool Down & Stretching", "muscle": "Back, Shoulders & Arms", "minutes": 8,
         "sets_reps": "8 min", "equipment": "Exercise Mat", "difficulty": "Beginner",
         "steps": ["Child's pose — 60 seconds to open up lats",
                   "Cross-body shoulder stretch: 30 seconds each arm",
                   "Doorway chest/bicep stretch: 30 seconds each side",
                   "Seated spinal twist: 30 seconds each direction"],
         "tip": "A few minutes of cool-down stretching after a pull session massively reduces next-day soreness."},
    ],

    "Lower B": [
        {"name": "Bike Warm-Up", "muscle": "Legs & Cardiovascular", "minutes": 10,
         "sets_reps": "10 min steady", "equipment": "Stationary Bike", "difficulty": "Beginner",
         "steps": ["Set resistance to a comfortable level (around level 3–5)",
                   "Pedal at 60–80 RPM for the first 5 minutes",
                   "Increase resistance slightly for the final 5 minutes",
                   "Finish with 1 minute easy to prepare for lifting"],
         "tip": "The bike warms up your quads, hamstrings and hips perfectly before leg day."},
        {"name": "Conventional Deadlift", "muscle": "Hamstrings · Glutes · Back · Full Body", "minutes": 20,
         "sets_reps": "3 sets × 6–8 reps", "equipment": "Barbell, Weight Plates", "difficulty": "Intermediate",
         "steps": ["Bar over mid-foot, stand hip-width apart, grip just outside legs",
                   "Hinge down: flatten back, chest up, hips above knees",
                   "Take a big breath into your belly and brace your core firmly",
                   "Push the floor away with your legs — bar stays close to your body",
                   "Lock out at the top: stand tall, hips fully extended, glutes squeezed",
                   "Hinge back down with control, resetting your position each rep"],
         "tip": "The king of all exercises. Ask a gym staff member to check your form on your first session."},
        {"name": "Walking Lunges", "muscle": "Quads · Glutes · Balance", "minutes": 12,
         "sets_reps": "3 sets × 10 reps each leg", "equipment": "Bodyweight or Dumbbells", "difficulty": "Beginner",
         "steps": ["Stand tall, step forward with one leg into a wide lunge",
                   "Lower your back knee toward the floor — don't let it slam down",
                   "Front knee stays directly above (not past) your toes",
                   "Push off your front foot and step forward with the other leg",
                   "Continue for 10 steps per leg"],
         "tip": "Start with bodyweight before grabbing dumbbells. A long stride keeps stress off the knee."},
        {"name": "Leg Extension Machine", "muscle": "Quads (Isolation)", "minutes": 10,
         "sets_reps": "3 sets × 12 reps", "equipment": "Leg Extension Machine", "difficulty": "Beginner",
         "steps": ["Sit with your back against the pad, adjust so knees align with the pivot",
                   "Position the shin pad just above your feet",
                   "Extend your legs upward until almost straight",
                   "Hold and squeeze your quads for 1 full second at the top",
                   "Lower slowly over 3 seconds — do NOT drop the weight"],
         "tip": "Medium weight with maximum squeeze beats heavy weight with no squeeze every time."},
        {"name": "Standing Calf Raise", "muscle": "Calves", "minutes": 8,
         "sets_reps": "3 sets × 15–20 reps", "equipment": "Calf Raise Machine or Step", "difficulty": "Beginner",
         "steps": ["Stand on the edge of a step or plate with heels hanging off",
                   "Rise up on your toes as high as possible",
                   "Hold at the top for 1 full second — feel the contraction",
                   "Lower heels BELOW the step level for a full stretch",
                   "Don't bounce — each rep should be fully controlled"],
         "tip": "Calves love high reps and slow, full-range movements. Bouncing up and down does nothing!"},
        {"name": "Cool Down & Stretching", "muscle": "Legs, Glutes & Lower Back", "minutes": 10,
         "sets_reps": "10 min", "equipment": "Exercise Mat", "difficulty": "Beginner",
         "steps": ["Standing quad stretch: 30 seconds each leg",
                   "Lying glute stretch (figure-four): 45 seconds each side",
                   "Downward dog calf stretch: 45 seconds each leg",
                   "Child's pose for lower back: 60 seconds"],
         "tip": "Your legs carry you everywhere — give them the care they deserve after a tough session."},
    ],

    "Full Body Strength": [
        {"name": "Cardio Warm-Up", "muscle": "Full Body", "minutes": 8,
         "sets_reps": "8 min", "equipment": "Treadmill or Bike", "difficulty": "Beginner",
         "steps": ["5 minutes on treadmill at brisk walking or light jog",
                   "10 × arm circles each direction",
                   "10 × bodyweight squats",
                   "10 × walking lunges"],
         "tip": "A general warm-up for full body days should include both lower and upper body movements."},
        {"name": "Goblet Squat", "muscle": "Quads · Glutes · Core", "minutes": 12,
         "sets_reps": "3 sets × 12 reps", "equipment": "Dumbbell or Kettlebell", "difficulty": "Beginner",
         "steps": ["Hold a dumbbell vertically at your chest with both hands",
                   "Feet shoulder-width apart, toes turned slightly out",
                   "Squat deep — the dumbbell keeps your chest upright naturally",
                   "Drive through your heels to stand back up"],
         "tip": "The goblet squat is the best teaching tool for squat mechanics before moving to a barbell."},
        {"name": "Dumbbell Push Press", "muscle": "Shoulders · Triceps · Legs", "minutes": 12,
         "sets_reps": "3 sets × 10 reps", "equipment": "Dumbbells", "difficulty": "Beginner",
         "steps": ["Hold dumbbells at shoulder height, palms facing in",
                   "Dip slightly at the knees, then explosively drive dumbbells overhead",
                   "Fully extend arms at the top, stand tall",
                   "Lower back to shoulders in a slow, controlled manner"],
         "tip": "The slight leg drive makes this easier than a strict press — great for building shoulder strength."},
        {"name": "Seated Cable Row", "muscle": "Back · Biceps", "minutes": 12,
         "sets_reps": "3 sets × 12 reps", "equipment": "Cable Row Station", "difficulty": "Beginner",
         "steps": ["Sit tall at the cable row station, feet on platform",
                   "Grip the handle and pull toward your lower ribcage",
                   "Squeeze shoulder blades together at the end of each pull",
                   "Extend arms slowly back to the start position"],
         "tip": "Full body days benefit from compound pulling movements — hits your back and biceps simultaneously."},
        {"name": "Plank Hold", "muscle": "Core · Full Body Stability", "minutes": 8,
         "sets_reps": "3 sets × 30–60 seconds", "equipment": "Exercise Mat", "difficulty": "Beginner",
         "steps": ["Get into a push-up position, rest on forearms instead of hands",
                   "Body should form a straight line from head to heels",
                   "Engage your core, squeeze your glutes, breathe normally",
                   "Hold for 30 seconds (beginner) or 60 seconds (intermediate)"],
         "tip": "Quality beats duration. A solid 30-second plank beats a sagging 90-second one every time."},
        {"name": "Cool Down", "muscle": "Full Body", "minutes": 8,
         "sets_reps": "8 min", "equipment": "Exercise Mat", "difficulty": "Beginner",
         "steps": ["Cat-cow spinal stretch: 60 seconds",
                   "Hip flexor kneeling lunge stretch: 30 seconds each side",
                   "Chest doorway stretch: 30 seconds",
                   "Child's pose: 60 seconds"],
         "tip": "Full body workouts are demanding. Take your cool-down seriously to recover faster."},
    ],

    "Cardio & Core": [
        {"name": "Treadmill Intervals", "muscle": "Cardiovascular · Legs", "minutes": 20,
         "sets_reps": "10 × 1 min run / 1 min walk", "equipment": "Treadmill", "difficulty": "Beginner",
         "steps": ["Warm up 3 minutes at brisk walking pace",
                   "Increase speed to a challenging jog for 1 minute",
                   "Recover at walking pace for 1 minute",
                   "Repeat 10 times, then cool down walking for 2 minutes"],
         "tip": "Intervals burn far more calories than steady-state cardio in the same time."},
        {"name": "Plank Variations", "muscle": "Core", "minutes": 10,
         "sets_reps": "3 rounds", "equipment": "Exercise Mat", "difficulty": "Beginner",
         "steps": ["Standard plank hold: 30 seconds",
                   "Left side plank: 20 seconds",
                   "Right side plank: 20 seconds",
                   "Rest 30 seconds, then repeat for 3 total rounds"],
         "tip": "Side planks target your obliques — the muscles that give you a defined waist."},
        {"name": "Mountain Climbers", "muscle": "Core · Cardio · Shoulders", "minutes": 8,
         "sets_reps": "3 sets × 30 seconds", "equipment": "None (Floor Space)", "difficulty": "Beginner",
         "steps": ["Get into a push-up position, wrists under shoulders",
                   "Drive your right knee toward your chest, then switch legs rapidly",
                   "Keep your hips level — don't let them rise or sag",
                   "Move as fast as you can while maintaining good form"],
         "tip": "Mountain climbers double as cardio and core work. They're harder than they look!"},
        {"name": "Cool Down", "muscle": "Full Body", "minutes": 8,
         "sets_reps": "8 min", "equipment": "Exercise Mat", "difficulty": "Beginner",
         "steps": ["Lying knee-to-chest stretch: 30 seconds each side",
                   "Spinal twist on floor: 30 seconds each direction",
                   "Cobra pose for abs: 30 seconds",
                   "Happy baby pose for hips: 60 seconds"],
         "tip": "After cardio and core work, your spine needs some love. Don't skip the cool-down stretches."},
    ],

    "Cardio & Flexibility": [
        {"name": "Light Cardio", "muscle": "Cardiovascular", "minutes": 20,
         "sets_reps": "20 min steady", "equipment": "Treadmill, Bike or Elliptical", "difficulty": "Beginner",
         "steps": ["Choose your favourite cardio machine",
                   "Set to a moderate pace — conversational effort",
                   "Maintain consistent rhythm for 20 minutes",
                   "Last 2 minutes: reduce pace to cool down"],
         "tip": "End-of-week cardio should feel energising, not exhausting. Keep it moderate."},
        {"name": "Full Body Flexibility", "muscle": "Full Body", "minutes": 25,
         "sets_reps": "Hold each 45–60 seconds", "equipment": "Yoga Mat", "difficulty": "Beginner",
         "steps": ["Standing forward fold: 60 seconds",
                   "Seated butterfly stretch: 60 seconds",
                   "Hip flexor kneeling lunge: 45 seconds each side",
                   "Lying spinal twist: 45 seconds each side",
                   "Child's pose to finish: 90 seconds"],
         "tip": "End-of-week flexibility work compounds over months. Consistency beats intensity here."},
    ],

    "Active Recovery": [
        {"name": "Easy Walk", "muscle": "Cardiovascular — Light", "minutes": 20,
         "sets_reps": "20 min easy", "equipment": "None or Treadmill", "difficulty": "Beginner",
         "steps": ["Walk at a comfortable, relaxed pace",
                   "Focus on deep, slow breathing",
                   "Swing arms naturally, stand tall",
                   "Outdoors is ideal for added mental benefit"],
         "tip": "Active recovery keeps blood flowing to your muscles, clearing waste products and speeding up repair."},
        {"name": "Full Body Mobility", "muscle": "Full Body Joints", "minutes": 20,
         "sets_reps": "Continuous flow", "equipment": "Yoga Mat, Foam Roller (optional)", "difficulty": "Beginner",
         "steps": ["Foam roll major muscle groups: 60 seconds each area",
                   "Hip 90-90 stretch: 45 seconds each side",
                   "World's greatest stretch: 5 reps each side",
                   "Cat-cow spinal flow: 10 slow reps"],
         "tip": "Saturday mobility sessions compound over months into exceptional flexibility. Make this a habit."},
    ],

    "HIIT & Circuits": [
        {"name": "Circuit Warm-Up", "muscle": "Full Body", "minutes": 5,
         "sets_reps": "1 round easy", "equipment": "None", "difficulty": "Beginner",
         "steps": ["20 × jumping jacks",
                   "10 × arm circles each direction",
                   "10 × bodyweight squats",
                   "10 × hip hinges"],
         "tip": "HIIT sessions demand a proper warm-up — your heart rate needs to be ready for high-intensity work."},
        {"name": "HIIT Circuit", "muscle": "Full Body — Fat Burning", "minutes": 25,
         "sets_reps": "4 rounds, 40s work / 20s rest", "equipment": "None or Dumbbells", "difficulty": "Intermediate",
         "steps": ["Burpees — 40 seconds at max effort",
                   "Dumbbell squat to press — 40 seconds",
                   "Jump lunges (or walking lunges) — 40 seconds",
                   "Push-ups — 40 seconds",
                   "Rest 90 seconds between complete rounds"],
         "tip": "Push as hard as you can during the 40-second work intervals — that's where the fat burning happens."},
        {"name": "Core Finisher", "muscle": "Abs · Obliques", "minutes": 8,
         "sets_reps": "2 rounds", "equipment": "Exercise Mat", "difficulty": "Beginner",
         "steps": ["Crunches: 20 reps",
                   "Bicycle crunches: 20 reps each side",
                   "Leg raises: 15 reps",
                   "30-second plank to finish"],
         "tip": "Finish HIIT sessions with a core finisher — your abs are pre-fatigued, making this extra effective."},
        {"name": "Cool Down", "muscle": "Full Body", "minutes": 8,
         "sets_reps": "8 min", "equipment": "Exercise Mat", "difficulty": "Beginner",
         "steps": ["Walk slowly for 2 minutes to lower heart rate",
                   "Seated forward fold: 60 seconds",
                   "Pigeon pose: 45 seconds each side",
                   "Child's pose: 60 seconds"],
         "tip": "After intense HIIT, your heart rate needs to come down gradually. Never sit or lie down immediately."},
    ],

    "Strength & Cardio": [
        {"name": "Cardio Warm-Up", "muscle": "Full Body", "minutes": 5,
         "sets_reps": "5 min", "equipment": "Treadmill or Bike", "difficulty": "Beginner",
         "steps": ["Light jog or brisk walk for 5 minutes",
                   "Get heart rate up to about 50–60% of your max",
                   "Breathe through your nose if possible",
                   "Finish with 30 seconds at a faster pace"],
         "tip": "A brief cardio warm-up prepares your cardiovascular system for the mixed demands of this session."},
        {"name": "Dumbbell Full Body Circuit", "muscle": "Full Body", "minutes": 20,
         "sets_reps": "3 rounds × 12 reps each", "equipment": "Dumbbells", "difficulty": "Beginner",
         "steps": ["Dumbbell squat × 12 reps",
                   "Dumbbell bent-over row × 12 reps",
                   "Dumbbell push press × 12 reps",
                   "Dumbbell Romanian deadlift × 12 reps",
                   "Rest 60–90 seconds between rounds"],
         "tip": "Move through each exercise back-to-back for a combined strength + cardio effect."},
        {"name": "20-Min Moderate Cardio", "muscle": "Cardiovascular", "minutes": 20,
         "sets_reps": "20 min steady state", "equipment": "Treadmill, Bike or Elliptical", "difficulty": "Beginner",
         "steps": ["Choose a machine and set to moderate resistance/speed",
                   "Work at 60–70% of max heart rate — you should be able to talk",
                   "Maintain consistent pace throughout",
                   "Last 2 minutes: reduce intensity to cool down"],
         "tip": "The fat burning zone is 60–70% of your max HR. Formula: 220 − your age = max heart rate."},
        {"name": "Cool Down", "muscle": "Full Body", "minutes": 8,
         "sets_reps": "8 min", "equipment": "Exercise Mat", "difficulty": "Beginner",
         "steps": ["Standing quad stretch: 30 seconds each leg",
                   "Chest stretch against wall: 30 seconds",
                   "Seated hamstring stretch: 60 seconds",
                   "Deep breathing: 5 slow breaths"],
         "tip": "Combining strength and cardio is very demanding. Prioritise sleep and protein on these days."},
    ],

    "Light Cardio": [
        {"name": "Steady-State Cardio", "muscle": "Cardiovascular", "minutes": 30,
         "sets_reps": "30 min continuous", "equipment": "Treadmill, Bike, or Elliptical", "difficulty": "Beginner",
         "steps": ["Choose your preferred cardio machine",
                   "Set to a comfortable, moderate pace — conversational effort",
                   "Maintain consistent effort for 30 minutes",
                   "Focus on good posture and steady breathing"],
         "tip": "Light cardio on active recovery days keeps your metabolism up without stressing your muscles."},
        {"name": "Gentle Stretch", "muscle": "Full Body Flexibility", "minutes": 15,
         "sets_reps": "15 min", "equipment": "Exercise Mat", "difficulty": "Beginner",
         "steps": ["Neck rolls: 30 seconds each direction",
                   "Seated forward fold: 60 seconds",
                   "Lying glute stretch: 45 seconds each side",
                   "Child's pose: 60 seconds",
                   "Cobra stretch: 30 seconds × 2"],
         "tip": "Saturday is your chance to improve flexibility while the week's training is still fresh."},
    ],

    "Steady-State Cardio": [
        {"name": "Steady-State Cardio", "muscle": "Cardiovascular · Endurance", "minutes": 40,
         "sets_reps": "40 min at zone 2", "equipment": "Treadmill, Bike or Elliptical", "difficulty": "Beginner",
         "steps": ["Warm up 5 minutes at easy pace",
                   "Settle into Zone 2 — 60–70% max HR, conversational pace",
                   "Maintain this for 30 minutes without stopping",
                   "Cool down 5 minutes at easy walking pace"],
         "tip": "Zone 2 cardio builds your aerobic base — the foundation of all endurance fitness."},
        {"name": "Post-Cardio Stretch", "muscle": "Legs & Hips", "minutes": 10,
         "sets_reps": "10 min", "equipment": "Exercise Mat", "difficulty": "Beginner",
         "steps": ["Standing calf stretch: 30 seconds each",
                   "Hip flexor kneeling stretch: 30 seconds each",
                   "IT band stretch: 30 seconds each side",
                   "Child's pose: 60 seconds"],
         "tip": "After long cardio sessions, your hip flexors and calves are especially tight. Give them attention."},
    ],

    "Interval Training": [
        {"name": "Speed Intervals", "muscle": "Cardiovascular · Legs", "minutes": 30,
         "sets_reps": "8 × 2 min hard / 2 min easy", "equipment": "Treadmill or Outdoor Track", "difficulty": "Intermediate",
         "steps": ["Warm up 5 minutes at easy jog",
                   "Run at 80–85% max HR for 2 minutes (hard effort)",
                   "Recover at 50% max HR for 2 minutes (easy jog or walk)",
                   "Repeat 8 times, then cool down 5 minutes easy"],
         "tip": "Intervals are the most time-efficient way to build cardiovascular fitness."},
        {"name": "Stretching", "muscle": "Full Body", "minutes": 10,
         "sets_reps": "10 min", "equipment": "Exercise Mat", "difficulty": "Beginner",
         "steps": ["Seated hamstring stretch: 60 seconds",
                   "Quad stretch standing: 30 seconds each",
                   "Hip flexor stretch kneeling: 30 seconds each",
                   "Spinal twist: 30 seconds each direction"],
         "tip": "Never skip stretching after intervals — your muscles have worked hard at speed."},
    ],

    "Cross Training": [
        {"name": "Cross-Training Circuit", "muscle": "Full Body — Active Recovery", "minutes": 35,
         "sets_reps": "3 rotations", "equipment": "Various", "difficulty": "Beginner",
         "steps": ["10 min swimming or aqua jogging (low-impact)",
                   "10 min on the rowing machine at moderate pace",
                   "10 min cycling on the stationary bike",
                   "5 min cool down walking"],
         "tip": "Cross training gives your primary cardio muscles a break while still working your cardiovascular system."},
        {"name": "Gentle Stretching", "muscle": "Full Body", "minutes": 10,
         "sets_reps": "10 min", "equipment": "Exercise Mat", "difficulty": "Beginner",
         "steps": ["Cat-cow stretch: 60 seconds",
                   "Chest opener stretch: 30 seconds",
                   "Seated forward fold: 60 seconds",
                   "Lying spinal twist: 30 seconds each side"],
         "tip": "Cross training days are about active recovery — keep this session easy."},
    ],

    "Long Cardio Session": [
        {"name": "Long Endurance Session", "muscle": "Cardiovascular", "minutes": 60,
         "sets_reps": "60 min zone 2–3", "equipment": "Treadmill, Bike or Elliptical", "difficulty": "Intermediate",
         "steps": ["Warm up 10 minutes at easy pace",
                   "Settle into zone 2–3 (65–75% max HR) for 40 minutes",
                   "Final 5 minutes: push to zone 3 (75–80% max HR)",
                   "Cool down 5 minutes easy"],
         "tip": "Long sessions build the aerobic base that makes everything else easier. Fuel properly beforehand."},
        {"name": "Full Body Cool Down", "muscle": "Full Body", "minutes": 10,
         "sets_reps": "10 min", "equipment": "Exercise Mat", "difficulty": "Beginner",
         "steps": ["Walk 3 minutes to lower heart rate gradually",
                   "Full body stretching: legs, hips, back, shoulders",
                   "Deep breathing: 5 slow, controlled breaths",
                   "Foam rolling if available: 2 minutes total"],
         "tip": "After an hour of cardio, a thorough cool-down is essential. Hydrate well and eat within 30 minutes."},
    ],

    "Recovery Cardio": [
        {"name": "Easy Recovery Walk/Jog", "muscle": "Cardiovascular — Light", "minutes": 25,
         "sets_reps": "25 min easy", "equipment": "Treadmill or Outdoors", "difficulty": "Beginner",
         "steps": ["Walk or very light jog at 40–50% max HR",
                   "Conversation should be completely easy at this pace",
                   "Focus on good posture and relaxed breathing",
                   "No pushing — this is about blood flow, not fitness gains"],
         "tip": "Recovery cardio flushes lactic acid from your muscles and speeds up recovery."},
        {"name": "Mobility Work", "muscle": "Full Body", "minutes": 15,
         "sets_reps": "15 min", "equipment": "Exercise Mat, Foam Roller", "difficulty": "Beginner",
         "steps": ["Foam roll quads, hamstrings and calves: 60 seconds each",
                   "Hip 90-90 stretch: 45 seconds each side",
                   "Ankle circles: 20 each direction",
                   "World's greatest stretch: 5 reps each side"],
         "tip": "Recovery days and mobility work are where elite athletes separate themselves from amateurs."},
    ],

    "Yoga Flow": [
        {"name": "Sun Salutation Flow", "muscle": "Full Body Flexibility", "minutes": 20,
         "sets_reps": "5 × full sun salutation", "equipment": "Yoga Mat", "difficulty": "Beginner",
         "steps": ["Mountain pose → Forward fold → Halfway lift",
                   "Step back to plank → Lower to cobra/upward dog",
                   "Push to downward dog → Hold 5 breaths",
                   "Walk feet forward → Halfway lift → Forward fold → Mountain pose"],
         "tip": "Sun salutations warm up your entire spine and connect movement with breath. Move slowly."},
        {"name": "Standing Balance Poses", "muscle": "Balance · Legs · Core", "minutes": 15,
         "sets_reps": "30–60 seconds each pose", "equipment": "Yoga Mat", "difficulty": "Beginner",
         "steps": ["Tree pose: 30 seconds each leg",
                   "Warrior I: 45 seconds each side",
                   "Warrior II: 45 seconds each side",
                   "Warrior III: 20 seconds each side"],
         "tip": "Fix your gaze on a still point (drishti) to improve balance. It gets better with consistent practice."},
        {"name": "Floor Poses & Cool Down", "muscle": "Hips, Hamstrings & Lower Back", "minutes": 15,
         "sets_reps": "60 seconds each pose", "equipment": "Yoga Mat", "difficulty": "Beginner",
         "steps": ["Seated forward fold: 60 seconds",
                   "Butterfly pose: 60 seconds",
                   "Supine spinal twist: 45 seconds each side",
                   "Savasana (rest): 3 minutes"],
         "tip": "Savasana is not optional! This is when your nervous system integrates all the benefits of the practice."},
    ],

    "Mobility Drills": [
        {"name": "Joint Mobility Circuit", "muscle": "Full Body Joints", "minutes": 25,
         "sets_reps": "2 rounds × 10 reps each", "equipment": "None", "difficulty": "Beginner",
         "steps": ["Neck: slow circles 10 each direction",
                   "Shoulders: arm circles 10 forward, 10 backward",
                   "Hips: hip circles 10 each direction",
                   "Ankles: circles 10 each direction, then flexion/extension"],
         "tip": "Joint mobility increases synovial fluid — this is what keeps your joints healthy long-term."},
        {"name": "Thoracic Mobility", "muscle": "Upper Back & Spine", "minutes": 15,
         "sets_reps": "2 rounds", "equipment": "Foam Roller, Mat", "difficulty": "Beginner",
         "steps": ["Thoracic extension over foam roller: 2 minutes",
                   "Thread-the-needle stretch: 45 seconds each side",
                   "Cat-cow: 10 slow reps",
                   "Open book rotation: 10 each side"],
         "tip": "Most people have poor thoracic mobility from sitting at desks. This will transform your posture."},
    ],

    "Deep Stretch": [
        {"name": "Full Body Deep Stretch", "muscle": "All Major Muscle Groups", "minutes": 45,
         "sets_reps": "Hold each 60–90 seconds", "equipment": "Yoga Mat, Straps (optional)", "difficulty": "Beginner",
         "steps": ["Hip flexor kneeling lunge stretch: 90 seconds each",
                   "Pigeon pose (glutes): 90 seconds each side",
                   "Seated hamstring stretch: 90 seconds",
                   "Doorway chest stretch: 60 seconds",
                   "Supine spinal twist: 60 seconds each side",
                   "Child's pose: 2 minutes to finish"],
         "tip": "Never force deep stretches. Breathe into areas of tension and allow the muscle to relax over 60–90 seconds."},
    ],

    "Active Mobility": [
        {"name": "Active Mobility Flow", "muscle": "Full Body", "minutes": 40,
         "sets_reps": "Continuous flow", "equipment": "Yoga Mat", "difficulty": "Beginner",
         "steps": ["5 min foam rolling: target tight areas",
                   "10 min joint circles: neck, shoulders, hips, ankles",
                   "10 min yoga flow: sun salutations at slow pace",
                   "10 min deep stretching: focus on areas worked this week",
                   "5 min breathing: box breathing (4s in, 4s hold, 4s out, 4s hold)"],
         "tip": "Saturday active mobility sessions compound over months into exceptional flexibility and joint health."},
    ],
}

# ═════════════════════════════════════════════════════════════════════════════
# CSS
# ═════════════════════════════════════════════════════════════════════════════

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
html,body,[class*="css"]{font-family:'Inter',sans-serif;}
#MainMenu,footer,header{visibility:hidden;}
.block-container{padding:0 2rem 2rem 2rem !important;max-width:1200px !important;}
.hero{background:linear-gradient(135deg,#1a1a2e 0%,#16213e 50%,#0f3460 100%);border-radius:20px;padding:3rem 2.5rem;margin-bottom:2rem;position:relative;overflow:hidden;}
.hero::before{content:'';position:absolute;top:-60px;right:-60px;width:300px;height:300px;background:radial-gradient(circle,rgba(229,57,53,.25) 0%,transparent 70%);border-radius:50%;}
.hero-title{font-size:2.8rem;font-weight:800;color:#fff;margin:0 0 .5rem;line-height:1.1;}
.hero-title span{color:#e53935;}
.hero-sub{font-size:1.1rem;color:rgba(255,255,255,.7);margin:0 0 1.5rem;}
.hero-chips{display:flex;gap:10px;flex-wrap:wrap;}
.chip{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:99px;padding:6px 16px;font-size:.8rem;color:rgba(255,255,255,.85);font-weight:500;}
.section-label{font-size:.75rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#e53935;margin-bottom:.75rem;}
.section-title{font-size:1.5rem;font-weight:700;color:#1a1a2e;margin-bottom:1.5rem;}
.goal-card{border-radius:16px;padding:1.5rem;border:2px solid #e8e8e8;background:#fff;text-align:center;}
.goal-card.selected{border-color:#e53935;background:#fff5f5;box-shadow:0 8px 24px rgba(229,57,53,.2);}
.goal-icon{font-size:2.5rem;margin-bottom:.75rem;}
.goal-name{font-size:1rem;font-weight:700;color:#1a1a2e;margin-bottom:.4rem;}
.goal-desc{font-size:.8rem;color:#666;line-height:1.4;}
.week-grid{display:grid;grid-template-columns:repeat(7,1fr);gap:6px;margin-bottom:1.5rem;}
.week-cell{border-radius:10px;padding:10px 4px;text-align:center;border:1.5px solid;}
.week-cell-train{border-color:#e53935;background:#fff5f5;}
.week-cell-rest{border-color:#e0e0e0;background:#fafafa;}
.wc-day{font-size:.7rem;font-weight:700;color:#999;text-transform:uppercase;margin-bottom:4px;}
.wc-type{font-size:.68rem;font-weight:700;}
.wc-type-train{color:#e53935;}
.wc-type-rest{color:#9e9e9e;}
.summary-bar{background:#1a1a2e;border-radius:16px;padding:1.2rem 1.5rem;margin-bottom:1.5rem;display:flex;gap:2rem;flex-wrap:wrap;}
.sum-item{text-align:center;}
.sum-val{font-size:1.4rem;font-weight:800;color:#e53935;}
.sum-label{font-size:.72rem;color:rgba(255,255,255,.6);text-transform:uppercase;letter-spacing:.06em;font-weight:600;margin-top:2px;}
.ex-card{background:#fff;border-radius:16px;border:1.5px solid #f0f0f0;overflow:hidden;margin-bottom:1rem;box-shadow:0 2px 12px rgba(0,0,0,.05);}
.ex-header{padding:1.2rem 1.4rem 1rem;display:flex;align-items:flex-start;gap:1rem;border-bottom:1px solid #f5f5f5;}
.ex-num{width:36px;height:36px;border-radius:10px;color:#fff;font-size:.85rem;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0;}
.ex-title{font-size:1.05rem;font-weight:700;color:#1a1a2e;margin-bottom:4px;}
.ex-muscle{font-size:.78rem;color:#e53935;font-weight:600;text-transform:uppercase;letter-spacing:.05em;}
.ex-body{padding:1rem 1.4rem 1.2rem;}
.ex-meta-row{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:1rem;}
.ex-badge{display:inline-flex;align-items:center;gap:5px;padding:5px 12px;border-radius:99px;font-size:.78rem;font-weight:600;}
.badge-time{background:#e3f2fd;color:#1565c0;}
.badge-sets{background:#fce4ec;color:#c62828;}
.badge-equip{background:#f3e5f5;color:#6a1b9a;}
.badge-diff{background:#e8f5e9;color:#2e7d32;}
.steps-title{font-size:.78rem;font-weight:700;color:#999;text-transform:uppercase;letter-spacing:.07em;margin-bottom:.5rem;}
.steps-list{list-style:none;padding:0;margin:0 0 .75rem;}
.steps-list li{font-size:.87rem;color:#333;padding:4px 0 4px 24px;position:relative;line-height:1.5;}
.steps-list li::before{content:attr(data-n);position:absolute;left:0;color:#e53935;font-weight:700;font-size:.8rem;}
.tip-box{background:linear-gradient(135deg,#fff8e1,#fff3e0);border-left:3px solid #ff9800;border-radius:0 8px 8px 0;padding:8px 12px;font-size:.82rem;color:#5d4037;line-height:1.5;}
.tip-label{font-weight:700;color:#e65100;}
.rest-banner{background:linear-gradient(135deg,#e8f5e9,#c8e6c9);border-radius:20px;padding:3rem 2rem;text-align:center;border:2px solid #a5d6a7;}
.rest-icon{font-size:4rem;margin-bottom:1rem;}
.rest-title{font-size:1.6rem;font-weight:800;color:#1b5e20;margin-bottom:.5rem;}
.rest-sub{font-size:.95rem;color:#2e7d32;max-width:420px;margin:0 auto 1.5rem;line-height:1.6;}
.rest-tips{display:grid;grid-template-columns:1fr 1fr;gap:10px;max-width:480px;margin:0 auto;}
.rest-tip-item{background:#fff;border-radius:12px;padding:12px;border:1px solid #a5d6a7;font-size:.82rem;color:#2e7d32;text-align:left;}
.rest-tip-item strong{display:block;font-weight:700;margin-bottom:2px;color:#1b5e20;}
.stButton>button{border-radius:99px !important;font-weight:600 !important;border:2px solid #e53935 !important;color:#e53935 !important;background:#fff !important;padding:.5rem 1.5rem !important;}
.stButton>button:hover{background:#e53935 !important;color:#fff !important;}
.divider{border:none;border-top:1.5px solid #f0f0f0;margin:1.5rem 0;}
</style>
""", unsafe_allow_html=True)

# ═════════════════════════════════════════════════════════════════════════════
# SESSION STATE
# ═════════════════════════════════════════════════════════════════════════════

if "goal" not in st.session_state:
    st.session_state.goal = None
if "day" not in st.session_state:
    st.session_state.day = None

# ═════════════════════════════════════════════════════════════════════════════
# HERO
# ═════════════════════════════════════════════════════════════════════════════

st.markdown("""
<div class="hero">
    <div class="hero-title">💪 Gym<span>Guide</span></div>
    <div class="hero-sub">Your personalised workout planner — choose your goal, pick your day, and train with confidence.</div>
    <div class="hero-chips">
        <span class="chip">✅ Beginner friendly</span>
        <span class="chip">⏱ Time per exercise</span>
        <span class="chip">🏋️ Equipment listed</span>
        <span class="chip">📋 Step-by-step guides</span>
        <span class="chip">💡 Pro tips included</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ═════════════════════════════════════════════════════════════════════════════
# STEP 1 — GOAL SELECTOR
# ═════════════════════════════════════════════════════════════════════════════

st.markdown('<div class="section-label">Step 1</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">What is your fitness goal?</div>', unsafe_allow_html=True)

goal_names = list(GOALS.keys())
cols = st.columns(len(goal_names))
for col, gk in zip(cols, goal_names):
    with col:
        sel = "selected" if st.session_state.goal == gk else ""
        g = GOALS[gk]
        st.markdown(f"""
        <div class="goal-card {sel}">
            <div class="goal-icon">{g['icon']}</div>
            <div class="goal-name">{gk.split(' ', 1)[1]}</div>
            <div class="goal-desc">{g['desc']}</div>
        </div>""", unsafe_allow_html=True)
        if st.button("Select", key=f"g_{gk}"):
            st.session_state.goal = gk
            st.session_state.day = None
            st.rerun()

# ═════════════════════════════════════════════════════════════════════════════
# STEP 2 — DAY SELECTOR
# ═════════════════════════════════════════════════════════════════════════════

DAY_ABB = {"Monday":"MON","Tuesday":"TUE","Wednesday":"WED",
            "Thursday":"THU","Friday":"FRI","Saturday":"SAT","Sunday":"SUN"}

if st.session_state.goal:
    schedule = GOALS[st.session_state.goal]["days"]

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    st.markdown('<div class="section-label">Step 2</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Select your training day</div>', unsafe_allow_html=True)

    cells = ""
    for day, session in schedule.items():
        is_rest = session == "Rest"
        cells += (f'<div class="week-cell {"week-cell-rest" if is_rest else "week-cell-train"}">'
                  f'<div class="wc-day">{DAY_ABB[day]}</div>'
                  f'<div class="wc-type {"wc-type-rest" if is_rest else "wc-type-train"}">'
                  f'{"REST" if is_rest else session.upper()[:8]}</div></div>')
    st.markdown(f'<div class="week-grid">{cells}</div>', unsafe_allow_html=True)

    day_cols = st.columns(len(schedule))
    for col, (day, session) in zip(day_cols, schedule.items()):
        with col:
            label = f"😴 {day[:3]}" if session == "Rest" else f"🏋️ {day[:3]}"
            if st.button(label, key=f"d_{day}"):
                st.session_state.day = day
                st.rerun()

# ═════════════════════════════════════════════════════════════════════════════
# STEP 3 — WORKOUT / REST DAY
# ═════════════════════════════════════════════════════════════════════════════

if st.session_state.goal and st.session_state.day:
    goal_key = st.session_state.goal
    day      = st.session_state.day
    session  = GOALS[goal_key]["days"][day]

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    st.markdown('<div class="section-label">Step 3 — Your Workout</div>', unsafe_allow_html=True)

    if session == "Rest":
        tip_cards = "".join(
            f'<div class="rest-tip-item"><strong>{ic} {ti}</strong>{de}</div>'
            for ic, ti, de in REST_TIPS
        )
        st.markdown(f"""
        <div class="rest-banner">
            <div class="rest-icon">🛌</div>
            <div class="rest-title">Rest & Recovery Day</div>
            <div class="rest-sub">Muscles grow during rest, not during the workout itself.
            Today is just as important as your training days.</div>
            <div class="rest-tips">{tip_cards}</div>
        </div>""", unsafe_allow_html=True)

    else:
        exercises = EXERCISES.get(session, [])
        if not exercises:
            st.info(f"Exercises for **{session}** are coming soon!")
        else:
            total_min    = sum(e["minutes"] for e in exercises)
            working_ex   = len([e for e in exercises if "Cool" not in e["name"] and "Warm" not in e["name"]])
            warmup_min   = sum(e["minutes"] for e in exercises if "Warm" in e["name"])
            cooldown_min = sum(e["minutes"] for e in exercises if "Cool" in e["name"])

            st.markdown(f"""
            <div style="margin-bottom:1rem;">
                <h2 style="font-size:1.6rem;font-weight:800;color:#1a1a2e;margin-bottom:4px;">{day} — {session}</h2>
                <p style="color:#666;font-size:0.9rem;">{goal_key}</p>
            </div>
            <div class="summary-bar">
                <div class="sum-item"><div class="sum-val">{total_min} min</div><div class="sum-label">Total Duration</div></div>
                <div class="sum-item"><div class="sum-val">{working_ex}</div><div class="sum-label">Working Exercises</div></div>
                <div class="sum-item"><div class="sum-val">{warmup_min} min</div><div class="sum-label">Warm-Up</div></div>
                <div class="sum-item"><div class="sum-val">{cooldown_min} min</div><div class="sum-label">Cool Down</div></div>
            </div>""", unsafe_allow_html=True)

            for idx, ex in enumerate(exercises):
                is_cool = "Cool" in ex["name"]
                is_warm = "Warm" in ex["name"]
                num_bg  = "#4caf50" if is_cool else ("#1565c0" if is_warm else "#1a1a2e")
                steps_html = "".join(
                    f'<li data-n="{i+1}">{s}</li>' for i, s in enumerate(ex["steps"])
                )
                st.markdown(f"""
                <div class="ex-card">
                    <div class="ex-header">
                        <div class="ex-num" style="background:{num_bg};">{idx+1}</div>
                        <div>
                            <div class="ex-title">{ex['name']}</div>
                            <div class="ex-muscle">{ex['muscle']}</div>
                        </div>
                    </div>
                    <div class="ex-body">
                        <div class="ex-meta-row">
                            <span class="ex-badge badge-time">⏱ {ex['minutes']} minutes</span>
                            <span class="ex-badge badge-sets">🔁 {ex['sets_reps']}</span>
                            <span class="ex-badge badge-equip">🏋️ {ex['equipment']}</span>
                            <span class="ex-badge badge-diff">⭐ {ex['difficulty']}</span>
                        </div>
                        <div class="steps-title">How to do it</div>
                        <ul class="steps-list">{steps_html}</ul>
                        <div class="tip-box"><span class="tip-label">💡 Tip: </span>{ex['tip']}</div>
                    </div>
                </div>""", unsafe_allow_html=True)

# ═════════════════════════════════════════════════════════════════════════════
# FOOTER
# ═════════════════════════════════════════════════════════════════════════════

st.markdown("""
<hr class='divider'>
<div style="text-align:center;padding:1rem 0 .5rem;font-size:.8rem;color:#aaa;">
    GymGuide — Built as a personal fitness companion.
    Always consult a professional before starting a new exercise programme.
</div>""", unsafe_allow_html=True)
