"""
GymGuide v3 — Premium Interactive Workout Planner
• Pictorial exercise guides (images per exercise)
• Fully flexible schedule (user picks their own training days)
• Premium dark fitness app aesthetic
"""

import streamlit as st

st.set_page_config(
    page_title="GymGuide – Premium Workout Planner",
    page_icon="💪",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ═══════════════════════════════════════════════════════════════════════════
#  EXERCISE IMAGE MAP  (Unsplash photo IDs — free to embed)
# ═══════════════════════════════════════════════════════════════════════════

IMG = {
    # ── Warm-ups ──────────────────────────────────────────────────────────
    "Treadmill Warm-Up":        "1538805060514-97d9cc17730c",
    "Dynamic Warm-Up":          "1544367567-0f2fcb009e0b",
    "Bike Warm-Up":             "1534438327276-14e5300c3a48",
    "Rowing Machine Warm-Up":   "1558618666-fcd25c85cd64",
    "Circuit Warm-Up":          "1549060279-7e168fcee0c2",
    "Cardio Warm-Up":           "1538805060514-97d9cc17730c",
    "5-Minute Cardio Warm-Up":  "1538805060514-97d9cc17730c",
    # ── Chest / Push ──────────────────────────────────────────────────────
    "Barbell Bench Press":      "1534368959876-26bf04f2c947",
    "Dumbbell Chest Fly":       "1526506118085-60ce8714f8c5",
    "Dumbbell Shoulder Press":  "1581009146145-b5ef050c2e1e",
    "Dumbbell Push Press":      "1581009146145-b5ef050c2e1e",
    "Cable Tricep Pushdown":    "1583454110551-21f2fa2afe61",
    # ── Back / Pull ───────────────────────────────────────────────────────
    "Lat Pulldown":             "1571019613454-1cb2f99b2d8b",
    "Seated Cable Row":         "1576678927484-cc907957088c",
    "Cable Face Pull":          "1576678927484-cc907957088c",
    # ── Arms ──────────────────────────────────────────────────────────────
    "Dumbbell Bicep Curl":      "1584466977773-e625c37cdd50",
    # ── Legs ──────────────────────────────────────────────────────────────
    "Barbell Squat":            "1517963628607-235ccdd5476c",
    "Goblet Squat":             "1517963628607-235ccdd5476c",
    "Leg Press Machine":        "1534438327276-14e5300c3a48",
    "Romanian Deadlift":        "1526506118085-60ce8714f8c5",
    "Romanian Deadlift (RDL)":  "1526506118085-60ce8714f8c5",
    "Dumbbell Romanian Deadlift": "1526506118085-60ce8714f8c5",
    "Conventional Deadlift":    "1526506118085-60ce8714f8c5",
    "Leg Curl Machine":         "1534438327276-14e5300c3a48",
    "Leg Extension Machine":    "1534438327276-14e5300c3a48",
    "Walking Lunges":           "1434682881908-b43d0467b798",
    "Standing Calf Raise":      "1434682881908-b43d0467b798",
    # ── Core ──────────────────────────────────────────────────────────────
    "Plank Hold":               "1571019614242-c5c5dee9f50b",
    "Plank Variations":         "1571019614242-c5c5dee9f50b",
    "Mountain Climbers":        "1549060279-7e168fcee0c2",
    "Dead Bug":                 "1571019614242-c5c5dee9f50b",
    "Core Finisher":            "1571019614242-c5c5dee9f50b",
    # ── Cardio ────────────────────────────────────────────────────────────
    "Treadmill Intervals":      "1538805060514-97d9cc17730c",
    "Speed Intervals":          "1476480862126-209bfaa8edc8",
    "HIIT Circuit":             "1549060279-7e168fcee0c2",
    "20-Min Moderate Cardio":   "1538805060514-97d9cc17730c",
    "Steady-State Cardio":      "1476480862126-209bfaa8edc8",
    "Long Endurance Session":   "1476480862126-209bfaa8edc8",
    "Easy Recovery Walk/Jog":   "1476480862126-209bfaa8edc8",
    "Cross-Training Circuit":   "1540497077202-7c8a3999166f",
    "Dumbbell Full Body Circuit": "1540497077202-7c8a3999166f",
    # ── Compound ──────────────────────────────────────────────────────────
    "Dumbbell Full Body":       "1540497077202-7c8a3999166f",
    # ── Yoga / Mobility ───────────────────────────────────────────────────
    "Sun Salutation Flow":      "1506126613408-eca07ce68773",
    "Standing Balance Poses":   "1506126613408-eca07ce68773",
    "Floor Poses & Cool Down":  "1552196563-55cd4e45efb3",
    "Full Body Deep Stretch":   "1552196563-55cd4e45efb3",
    "Active Mobility Flow":     "1552196563-55cd4e45efb3",
    "Full Body Flexibility":    "1552196563-55cd4e45efb3",
    "Gentle Full Body Stretch": "1552196563-55cd4e45efb3",
    "Joint Mobility Circuit":   "1544367567-0f2fcb009e0b",
    "Thoracic Mobility":        "1544367567-0f2fcb009e0b",
    "Full Body Mobility":       "1544367567-0f2fcb009e0b",
    "Mobility Work":            "1544367567-0f2fcb009e0b",
    "Easy Walk":                "1476480862126-209bfaa8edc8",
    # ── Cool-downs ────────────────────────────────────────────────────────
    "Cool Down & Stretching":   "1552196563-55cd4e45efb3",
    "Cool Down":                "1552196563-55cd4e45efb3",
    "Post-Cardio Stretch":      "1552196563-55cd4e45efb3",
    "Full Body Cool Down":      "1552196563-55cd4e45efb3",
    "Stretching":               "1552196563-55cd4e45efb3",
    "Gentle Stretching":        "1552196563-55cd4e45efb3",
    "Gentle Stretch":           "1552196563-55cd4e45efb3",
    "_fallback":                "1517963628607-235ccdd5476c",
}

def img_url(name, w=800, h=380):
    pid = IMG.get(name, IMG["_fallback"])
    return f"https://images.unsplash.com/photo-{pid}?w={w}&h={h}&fit=crop&q=80"

# ═══════════════════════════════════════════════════════════════════════════
#  GOAL SESSION POOLS  (sessions for 3 / 4 / 5 / 6 training days)
# ═══════════════════════════════════════════════════════════════════════════

GOAL_POOLS = {
    "💪 Build Muscle & Strength": {
        "icon": "💪", "color": "#FF3E3E",
        "desc": "Heavy lifting, compound movements, progressive overload",
        3: ["Full Body Strength", "Full Body Strength", "Full Body Strength"],
        4: ["Upper Push", "Lower A", "Upper Pull", "Lower B"],
        5: ["Upper Push", "Lower A", "Upper Pull", "Lower B", "Upper Push"],
        6: ["Upper Push", "Lower A", "Upper Pull", "Lower B", "Upper Push", "Lower A"],
    },
    "🏃 General Fitness": {
        "icon": "🏃", "color": "#3E8BFF",
        "desc": "Balanced mix of strength, cardio and flexibility",
        3: ["Full Body Strength", "Cardio & Core", "Full Body Strength"],
        4: ["Full Body Strength", "Cardio & Core", "Full Body Strength", "Cardio & Flexibility"],
        5: ["Full Body Strength", "Cardio & Core", "Full Body Strength", "Cardio & Flexibility", "Active Recovery"],
        6: ["Full Body Strength", "Cardio & Core", "Full Body Strength", "Cardio & Flexibility", "Cardio & Core", "Active Recovery"],
    },
    "🔥 Weight Loss & Toning": {
        "icon": "🔥", "color": "#FF8C00",
        "desc": "High-intensity circuits, fat burning & body recomposition",
        3: ["HIIT & Circuits", "Strength & Cardio", "HIIT & Circuits"],
        4: ["HIIT & Circuits", "Strength & Cardio", "HIIT & Circuits", "Strength & Cardio"],
        5: ["HIIT & Circuits", "Strength & Cardio", "HIIT & Circuits", "Strength & Cardio", "Light Cardio"],
        6: ["HIIT & Circuits", "Strength & Cardio", "HIIT & Circuits", "Strength & Cardio", "HIIT & Circuits", "Light Cardio"],
    },
    "🚴 Endurance & Cardio": {
        "icon": "🚴", "color": "#00C896",
        "desc": "Aerobic capacity, stamina and cardiovascular health",
        3: ["Steady-State Cardio", "Interval Training", "Long Cardio Session"],
        4: ["Steady-State Cardio", "Interval Training", "Cross Training", "Long Cardio Session"],
        5: ["Steady-State Cardio", "Interval Training", "Cross Training", "Long Cardio Session", "Recovery Cardio"],
        6: ["Steady-State Cardio", "Interval Training", "Cross Training", "Long Cardio Session", "Recovery Cardio", "Steady-State Cardio"],
    },
    "🧘 Flexibility & Mobility": {
        "icon": "🧘", "color": "#A855F7",
        "desc": "Yoga, stretching, joint health and posture improvement",
        3: ["Yoga Flow", "Mobility Drills", "Deep Stretch"],
        4: ["Yoga Flow", "Mobility Drills", "Yoga Flow", "Deep Stretch"],
        5: ["Yoga Flow", "Mobility Drills", "Yoga Flow", "Deep Stretch", "Active Mobility"],
        6: ["Yoga Flow", "Mobility Drills", "Yoga Flow", "Deep Stretch", "Active Mobility", "Yoga Flow"],
    },
}

ALL_DAYS = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
DAY_ABB  = {"Monday":"Mon","Tuesday":"Tue","Wednesday":"Wed",
             "Thursday":"Thu","Friday":"Fri","Saturday":"Sat","Sunday":"Sun"}

def build_schedule(goal_key, training_days):
    pool_data = GOAL_POOLS[goal_key]
    n = max(3, min(6, len(training_days)))
    pool = pool_data.get(n, pool_data[4])
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
         "steps":["Start at a comfortable walking pace (4–5 km/h)",
                  "Gradually increase to a light jog over 5 minutes",
                  "Keep arms swinging naturally, breathe steadily",
                  "Last 2 minutes: reduce to walking to transition into lifting"],
         "tip":"Never skip your warm-up — 10 minutes of light cardio raises your core temperature and primes your muscles."},
        {"name":"Barbell Bench Press","muscle":"Chest · Shoulders · Triceps","minutes":15,
         "sets_reps":"3 sets × 8–10 reps","equipment":"Barbell · Bench · Rack","difficulty":"Beginner",
         "steps":["Lie flat on the bench, grip bar just wider than shoulder-width",
                  "Unrack and hold the bar directly above your chest",
                  "Lower the bar slowly to mid-chest — elbows at 45°",
                  "Drive the bar back up explosively until arms are fully extended",
                  "Keep feet flat, back slightly arched, core braced throughout"],
         "tip":"Start with just the empty bar (20 kg) to nail your form before adding any weight. A spotter is highly recommended!"},
        {"name":"Dumbbell Shoulder Press","muscle":"Shoulders · Triceps","minutes":12,
         "sets_reps":"3 sets × 10–12 reps","equipment":"Dumbbells · Adjustable Bench","difficulty":"Beginner",
         "steps":["Sit upright on a bench, dumbbells at shoulder height, palms facing forward",
                  "Press dumbbells overhead in a smooth arc until arms are straight",
                  "Keep a slight elbow bend at the top — never hard-lock them",
                  "Lower slowly back to shoulder height and repeat"],
         "tip":"Keep your lower back firmly against the bench. Excessive arching shifts load onto your spine, not your shoulders."},
        {"name":"Cable Tricep Pushdown","muscle":"Triceps","minutes":10,
         "sets_reps":"3 sets × 12 reps","equipment":"Cable Machine · Rope or Bar","difficulty":"Beginner",
         "steps":["Set the pulley to head height and attach a rope or straight bar",
                  "Grip the attachment and tuck your elbows tight to your sides",
                  "Push straight down until your arms are fully extended",
                  "Slowly return to the start — elbows stay locked at your sides at all times"],
         "tip":"If your elbows fly forward, the weight is too heavy. The only movement should come from the elbow joint downwards."},
        {"name":"Dumbbell Chest Fly","muscle":"Chest (Outer)","minutes":10,
         "sets_reps":"3 sets × 12 reps","equipment":"Dumbbells · Flat Bench","difficulty":"Beginner",
         "steps":["Lie on a flat bench, dumbbells above chest with a slight elbow bend",
                  "Open your arms wide in an arc until you feel a deep chest stretch",
                  "Squeeze your chest to bring the dumbbells back together at the top",
                  "Maintain the slight elbow bend throughout — never fully straighten"],
         "tip":"Think of hugging a large barrel. Don't let elbows drop below shoulder level — that's your warning zone for injury."},
        {"name":"Cool Down & Stretching","muscle":"Chest · Shoulders · Arms","minutes":8,
         "sets_reps":"8 min — hold each 30s","equipment":"Exercise Mat","difficulty":"Beginner",
         "steps":["Chest doorway stretch: 30 seconds each side",
                  "Tricep overhead stretch: 30 seconds each arm",
                  "Shoulder cross-body stretch: 30 seconds each",
                  "Seated forward fold: 60 seconds"],
         "tip":"Static stretching post-workout lengthens the muscle you just worked and dramatically reduces next-day soreness."},
    ],

    "Lower A": [
        {"name":"Dynamic Warm-Up","muscle":"Legs & Hips","minutes":8,
         "sets_reps":"2 rounds","equipment":"None","difficulty":"Beginner",
         "steps":["10 × Leg swings (front-to-back) each leg",
                  "10 × Hip circles each direction",
                  "10 × Bodyweight squats (slow and controlled)",
                  "10 × Walking lunges across the room"],
         "tip":"Dynamic warm-ups activate your glutes and hip flexors — the two groups that will do the most work today."},
        {"name":"Barbell Squat","muscle":"Quads · Glutes · Hamstrings","minutes":18,
         "sets_reps":"3 sets × 8–10 reps","equipment":"Barbell · Squat Rack","difficulty":"Intermediate",
         "steps":["Set the bar at shoulder height; step under it and rest it on your upper traps",
                  "Stand feet shoulder-width apart, toes slightly out",
                  "Take a deep breath, brace your core hard, then sit down and back",
                  "Squat until thighs are parallel to the floor — or below",
                  "Drive through your heels to stand, keeping your chest tall throughout"],
         "tip":"Beginners: spend the first 2 weeks with just the bar, drilling the movement pattern. Good form here prevents years of injury."},
        {"name":"Leg Press Machine","muscle":"Quads · Glutes","minutes":14,
         "sets_reps":"3 sets × 10–12 reps","equipment":"Leg Press Machine","difficulty":"Beginner",
         "steps":["Adjust the seat so your knees reach ~90° at the bottom",
                  "Place feet shoulder-width apart on the platform",
                  "Release the safety handles and lower the plate in control",
                  "Push through your heels until legs are almost (not fully) extended",
                  "Re-engage safety handles between sets"],
         "tip":"The leg press is perfect for beginners — the machine guides your movement so you can focus purely on effort and range of motion."},
        {"name":"Romanian Deadlift (RDL)","muscle":"Hamstrings · Glutes","minutes":14,
         "sets_reps":"3 sets × 10 reps","equipment":"Barbell or Dumbbells","difficulty":"Intermediate",
         "steps":["Stand holding the bar at hip height, feet hip-width apart, soft knee bend",
                  "Hinge at the hips — think BACK, not DOWN",
                  "Slide the bar down your legs until you feel a deep hamstring stretch",
                  "Drive your hips forward to return upright, squeezing glutes at the top",
                  "Keep your back flat, shoulders pulled back throughout"],
         "tip":"Imagine closing a car door with your bum. That hip-hinge is the entire movement — get it right and your hamstrings will grow fast."},
        {"name":"Leg Curl Machine","muscle":"Hamstrings","minutes":10,
         "sets_reps":"3 sets × 12 reps","equipment":"Lying Leg Curl Machine","difficulty":"Beginner",
         "steps":["Lie face down with the pad positioned just above your heels",
                  "Curl your legs upward as far as possible without lifting your hips",
                  "Squeeze the hamstrings hard at the top for 1 full second",
                  "Lower over 3 slow seconds — this eccentric phase is where growth happens"],
         "tip":"The 3-second lowering phase is where most of the muscle growth happens. Don't just drop the weight — make it earn its place."},
        {"name":"Cool Down & Stretching","muscle":"Legs · Hips · Lower Back","minutes":8,
         "sets_reps":"8 min","equipment":"Exercise Mat","difficulty":"Beginner",
         "steps":["Standing quad stretch: 30 seconds each leg",
                  "Seated hamstring stretch: 60 seconds",
                  "Pigeon pose (glutes): 45 seconds each side",
                  "Calf stretch against wall: 30 seconds each"],
         "tip":"Tight hips and hamstrings cause the vast majority of lower back pain in gym-goers. Stretch after every single session — no exceptions."},
    ],

    "Upper Pull": [
        {"name":"Rowing Machine Warm-Up","muscle":"Back · Arms · Core","minutes":8,
         "sets_reps":"8 min steady","equipment":"Rowing Machine","difficulty":"Beginner",
         "steps":["Strap feet in, grip the handle with an overhand grip",
                  "SEQUENCE: push legs → lean back → pull arms in",
                  "Reverse to return: arms extend → lean forward → legs compress",
                  "Target 20–24 strokes per minute — smooth, not rushed"],
         "tip":"The rowing machine is the perfect warm-up for a pull day — it activates your entire posterior chain before you load it."},
        {"name":"Lat Pulldown","muscle":"Lats · Upper Back","minutes":14,
         "sets_reps":"3 sets × 10–12 reps","equipment":"Lat Pulldown Machine","difficulty":"Beginner",
         "steps":["Sit and lock your thighs under the knee pad",
                  "Grip the bar wider than shoulder-width, overhand",
                  "Lean back slightly and pull the bar to your upper chest",
                  "Lead with your elbows — imagine tucking them into your back pockets",
                  "Let the bar rise slowly to full arm extension between reps"],
         "tip":"Think 'elbows to hips' not 'hands to chest'. This mental cue fires your lats instead of just your arms — game changer."},
        {"name":"Seated Cable Row","muscle":"Mid-Back · Lats · Rear Delts","minutes":14,
         "sets_reps":"3 sets × 10–12 reps","equipment":"Cable Row Station","difficulty":"Beginner",
         "steps":["Sit tall with feet on the platform, slight knee bend",
                  "Grip the handle — don't lean back to start",
                  "Pull toward your lower ribcage, elbows driving back",
                  "Squeeze shoulder blades together at the end of each pull",
                  "Return in a controlled 3-second release back to start"],
         "tip":"Your torso should barely move. If you're rocking back and forth, you're using momentum — not muscle. Drop the weight and stay strict."},
        {"name":"Dumbbell Bicep Curl","muscle":"Biceps","minutes":10,
         "sets_reps":"3 sets × 12 reps","equipment":"Dumbbells","difficulty":"Beginner",
         "steps":["Stand with dumbbells at your sides, palms facing forward",
                  "Curl both dumbbells up toward your shoulders",
                  "Squeeze your biceps hard at the top — hold 1 second",
                  "Lower slowly over 2–3 seconds back to the start",
                  "Control is everything — no swinging, no momentum"],
         "tip":"Alternating arms improves mind-muscle connection. Whichever style you use — NEVER swing your torso to lift the weight. Strict reps only."},
        {"name":"Cable Face Pull","muscle":"Rear Delts · Rotator Cuff","minutes":10,
         "sets_reps":"3 sets × 15 reps","equipment":"Cable Machine · Rope","difficulty":"Beginner",
         "steps":["Set the pulley at face height and attach a rope",
                  "Grip the rope with thumbs pointing toward you, step back",
                  "Pull the rope toward your face, flaring elbows out wide",
                  "Separate the rope at the end — squeeze rear delts and rotator cuffs",
                  "Return slowly under full control"],
         "tip":"This is the most underrated exercise in any programme. Light weight, high reps, every session. It keeps your shoulders healthy for life."},
        {"name":"Cool Down & Stretching","muscle":"Back · Shoulders · Arms","minutes":8,
         "sets_reps":"8 min","equipment":"Exercise Mat","difficulty":"Beginner",
         "steps":["Child's pose (lats): 60 seconds",
                  "Cross-body shoulder stretch: 30 seconds each arm",
                  "Doorway chest/bicep stretch: 30 seconds each side",
                  "Seated spinal twist: 30 seconds each direction"],
         "tip":"Your lats and mid-back worked hard today. Child's pose will open them up beautifully — hold it longer if you have time."},
    ],

    "Lower B": [
        {"name":"Bike Warm-Up","muscle":"Legs · Cardiovascular","minutes":10,
         "sets_reps":"10 min steady","equipment":"Stationary Bike","difficulty":"Beginner",
         "steps":["Set resistance to a moderate level (3–5)",
                  "Pedal at 60–80 RPM for the first 5 minutes",
                  "Raise resistance slightly for the final 5 minutes",
                  "Final minute: easy spin to transition into lifting"],
         "tip":"The stationary bike is the superior leg-day warm-up — it loads your quads, hamstrings and hips through range without heavy spinal load."},
        {"name":"Conventional Deadlift","muscle":"Hamstrings · Glutes · Back · Full Body","minutes":20,
         "sets_reps":"3 sets × 6–8 reps","equipment":"Barbell · Weight Plates","difficulty":"Intermediate",
         "steps":["Bar over mid-foot, feet hip-width apart, grip just outside your legs",
                  "Hinge down: back flat, chest up, hips above knees, arms straight",
                  "Big breath into your belly — brace your core like you're about to be punched",
                  "Push the floor away with your legs — the bar should stay scraping your shins",
                  "Lock out at the top: hips fully extended, glutes squeezed, stand tall",
                  "Hinge back down with control — reset your whole position before the next rep"],
         "tip":"The king of all exercises. Ask a gym trainer to watch your first session — 20 minutes of coaching here saves years of bad habits."},
        {"name":"Walking Lunges","muscle":"Quads · Glutes · Balance","minutes":12,
         "sets_reps":"3 sets × 10 each leg","equipment":"Bodyweight or Dumbbells","difficulty":"Beginner",
         "steps":["Stand tall, step forward with one leg into a wide lunge",
                  "Lower the back knee toward the floor — controlled, not crashing",
                  "Front knee stays directly above (not past) your toes",
                  "Push through the front foot and bring the back leg forward to lunge again",
                  "10 steps per leg — keep your torso upright the whole time"],
         "tip":"Master bodyweight lunges for 2 sessions before adding dumbbells. A long stride (not a short shuffle) is essential for protecting your knees."},
        {"name":"Leg Extension Machine","muscle":"Quads (Isolation)","minutes":10,
         "sets_reps":"3 sets × 12 reps","equipment":"Leg Extension Machine","difficulty":"Beginner",
         "steps":["Sit with your back against the pad; adjust so knees align with the machine's pivot",
                  "Position the shin pad just above your feet",
                  "Extend your legs upward until almost fully straight",
                  "HOLD at the top — squeeze your quads for a full 1 second",
                  "Lower over 3 slow seconds — do not drop the weight"],
         "tip":"This is a pure isolation move. The quality of the contraction at the top matters more than the weight on the stack. Squeeze hard every rep."},
        {"name":"Standing Calf Raise","muscle":"Calves","minutes":8,
         "sets_reps":"3 sets × 15–20 reps","equipment":"Step or Calf Machine","difficulty":"Beginner",
         "steps":["Stand on the edge of a step with heels hanging off",
                  "Rise up onto your toes as high as possible",
                  "HOLD at the top for 1 full second — feel every fibre contract",
                  "Lower your heels BELOW the step for the maximum stretch",
                  "No bouncing — every rep fully controlled"],
         "tip":"Calves are slow-twitch muscles that hate bouncing. Full range, slow reps, high volume — that's the only thing that builds them."},
        {"name":"Cool Down & Stretching","muscle":"Legs · Glutes · Lower Back","minutes":10,
         "sets_reps":"10 min","equipment":"Exercise Mat","difficulty":"Beginner",
         "steps":["Standing quad stretch: 30 seconds each leg",
                  "Figure-four glute stretch (lying): 45 seconds each side",
                  "Downward dog calf stretch: 45 seconds each leg",
                  "Child's pose for lower back: 60 seconds"],
         "tip":"You put your legs through serious work today. Don't skip this — the 10 minutes you spend here now saves you hours of stiffness tomorrow."},
    ],

    "Full Body Strength": [
        {"name":"Cardio Warm-Up","muscle":"Full Body","minutes":8,
         "sets_reps":"8 min","equipment":"Treadmill or Bike","difficulty":"Beginner",
         "steps":["5 min treadmill at brisk walk or light jog",
                  "10 × arm circles each direction",
                  "10 × bodyweight squats",
                  "10 × walking lunges"],
         "tip":"Full-body sessions demand a warm-up that hits both upper and lower body. This sequence covers both in under 8 minutes."},
        {"name":"Goblet Squat","muscle":"Quads · Glutes · Core","minutes":12,
         "sets_reps":"3 sets × 12 reps","equipment":"Dumbbell or Kettlebell","difficulty":"Beginner",
         "steps":["Hold a dumbbell vertically at your chest with both hands",
                  "Feet shoulder-width apart, toes turned slightly out",
                  "Squat deep — the weight in front keeps your chest naturally upright",
                  "Drive through your heels to stand"],
         "tip":"The goblet squat is the single best way to learn the squat pattern before ever touching a barbell. Master this first."},
        {"name":"Dumbbell Romanian Deadlift","muscle":"Hamstrings · Glutes","minutes":12,
         "sets_reps":"3 sets × 10 reps","equipment":"Dumbbells","difficulty":"Beginner",
         "steps":["Hold dumbbells in front of thighs, stand hip-width apart",
                  "Hinge forward at the hips — push them back, not down",
                  "Lower dumbbells along your legs until hamstrings stretch",
                  "Drive hips forward to return, squeezing glutes at the top"],
         "tip":"Keep the dumbbells as close to your legs as possible — they should almost brush your shins. This keeps your back safe and the tension on your hamstrings."},
        {"name":"Dumbbell Push Press","muscle":"Shoulders · Triceps · Legs","minutes":12,
         "sets_reps":"3 sets × 10 reps","equipment":"Dumbbells","difficulty":"Beginner",
         "steps":["Hold dumbbells at shoulder height, palms facing in",
                  "Dip slightly at the knees (about 2 inches)",
                  "Explosively drive up through your legs and press dumbbells overhead",
                  "Lower slowly back to shoulders over 2 seconds"],
         "tip":"The leg drive makes this easier than a strict press — it's a great entry point for building pressing strength safely."},
        {"name":"Seated Cable Row","muscle":"Back · Biceps","minutes":12,
         "sets_reps":"3 sets × 12 reps","equipment":"Cable Row Station","difficulty":"Beginner",
         "steps":["Sit tall at the cable station, feet on the platform",
                  "Pull the handle toward your lower ribcage",
                  "Squeeze shoulder blades together firmly",
                  "Return to full arm extension in a controlled 3 seconds"],
         "tip":"Every full-body day needs a pulling movement. This one hits your back and biceps together — maximum efficiency."},
        {"name":"Plank Hold","muscle":"Core · Full Body Stability","minutes":8,
         "sets_reps":"3 sets × 30–60 seconds","equipment":"Exercise Mat","difficulty":"Beginner",
         "steps":["Forearms on the floor, elbows under shoulders",
                  "Body forms a straight line — head to heels",
                  "Engage your core, squeeze your glutes, breathe normally",
                  "30 sec for beginners, 60 sec for intermediate"],
         "tip":"A strong core is the foundation of every other lift. A perfect 30-second plank builds more than a sloppy 90-second one."},
        {"name":"Cool Down","muscle":"Full Body","minutes":8,
         "sets_reps":"8 min","equipment":"Exercise Mat","difficulty":"Beginner",
         "steps":["Cat-cow spinal stretch: 60 seconds",
                  "Hip flexor kneeling lunge: 30 seconds each side",
                  "Chest doorway stretch: 30 seconds",
                  "Child's pose: 60 seconds"],
         "tip":"Full-body sessions tax every system in your body. The cool-down is what separates people who recover well from those who are always sore."},
    ],

    "Cardio & Core": [
        {"name":"Treadmill Intervals","muscle":"Cardiovascular · Legs","minutes":20,
         "sets_reps":"10 × 1 min run / 1 min walk","equipment":"Treadmill","difficulty":"Beginner",
         "steps":["Warm up 3 minutes at brisk walk",
                  "Run at a challenging pace for 1 full minute",
                  "Recover with walking for 1 minute",
                  "Repeat 10 times, then 2-minute cool-down walk"],
         "tip":"Intervals burn significantly more calories than steady-state cardio in the same window of time. Push during the run intervals!"},
        {"name":"Plank Variations","muscle":"Core","minutes":10,
         "sets_reps":"3 rounds","equipment":"Exercise Mat","difficulty":"Beginner",
         "steps":["Standard forearm plank: 30 seconds",
                  "Left side plank: 20 seconds",
                  "Right side plank: 20 seconds",
                  "Rest 30 seconds then repeat — 3 rounds total"],
         "tip":"Side planks target the obliques — the muscles that create the appearance of a defined waist. Don't skip them."},
        {"name":"Mountain Climbers","muscle":"Core · Cardio · Shoulders","minutes":8,
         "sets_reps":"3 sets × 30 seconds","equipment":"None","difficulty":"Beginner",
         "steps":["Push-up position — wrists under shoulders, body straight",
                  "Drive your right knee toward your chest",
                  "Switch legs rapidly — left knee in as right extends out",
                  "Hips stay level — no bouncing them up or sagging them down"],
         "tip":"Mountain climbers are both a cardio and core exercise disguised as one. They're harder than they look — pace yourself in the first set."},
        {"name":"Dead Bug","muscle":"Deep Core Stabilisers","minutes":8,
         "sets_reps":"3 sets × 10 each side","equipment":"Exercise Mat","difficulty":"Beginner",
         "steps":["Lie on your back — arms pointing to ceiling, knees at 90° above hips",
                  "Slowly lower your right arm behind your head while extending your left leg",
                  "Keep your lower back PRESSED into the mat the entire time",
                  "Return to start and repeat on the opposite side"],
         "tip":"This is one of the safest and most effective core exercises ever developed. It teaches your spine to stay stable while your limbs move — exactly what real life demands."},
        {"name":"Cool Down","muscle":"Full Body","minutes":8,
         "sets_reps":"8 min","equipment":"Exercise Mat","difficulty":"Beginner",
         "steps":["Lying knee-to-chest: 30 seconds each side",
                  "Floor spinal twist: 30 seconds each direction",
                  "Cobra pose (abs): 30 seconds",
                  "Happy baby pose (hips): 60 seconds"],
         "tip":"After cardio and core work your spine needs decompression. These poses specifically target that — don't rush through them."},
    ],

    "Cardio & Flexibility": [
        {"name":"Light Cardio","muscle":"Cardiovascular","minutes":20,
         "sets_reps":"20 min steady","equipment":"Treadmill, Bike or Elliptical","difficulty":"Beginner",
         "steps":["Pick your favourite cardio machine",
                  "Set to a comfortable, conversational pace",
                  "Maintain consistent rhythm for 20 minutes",
                  "Last 2 minutes: ease off to cool down"],
         "tip":"End-of-week cardio should leave you feeling energised, not drained. Keep it moderate — you're maintaining fitness, not testing it."},
        {"name":"Full Body Flexibility","muscle":"Full Body","minutes":25,
         "sets_reps":"Hold each 45–60 seconds","equipment":"Yoga Mat","difficulty":"Beginner",
         "steps":["Standing forward fold: 60 seconds",
                  "Seated butterfly stretch: 60 seconds",
                  "Hip flexor kneeling lunge: 45 seconds each side",
                  "Lying spinal twist: 45 seconds each side",
                  "Child's pose: 90 seconds to finish"],
         "tip":"Flexibility done consistently compounds over months into genuinely impressive range of motion. Consistency beats intensity here — every time."},
    ],

    "Active Recovery": [
        {"name":"Easy Walk","muscle":"Cardiovascular — Light","minutes":20,
         "sets_reps":"20 min easy","equipment":"None or Treadmill","difficulty":"Beginner",
         "steps":["Walk at a completely comfortable, relaxed pace",
                  "Focus on slow, deep nasal breathing",
                  "Stand tall, swing arms naturally",
                  "Outdoors is ideal — sunlight and fresh air compound the benefits"],
         "tip":"Active recovery keeps blood moving to your muscles, flushing out waste products from the week's training. Don't turn it into a workout."},
        {"name":"Full Body Mobility","muscle":"Full Body Joints","minutes":20,
         "sets_reps":"Continuous flow","equipment":"Yoga Mat · Foam Roller","difficulty":"Beginner",
         "steps":["Foam roll major muscle groups: 60 seconds each area",
                  "Hip 90-90 stretch: 45 seconds each side",
                  "World's greatest stretch: 5 reps each side",
                  "Cat-cow spinal flow: 10 slow, deep reps"],
         "tip":"This session is about accumulation, not intensity. Performed weekly, these 20 minutes produce flexibility improvements that direct training never achieves."},
    ],

    "HIIT & Circuits": [
        {"name":"Circuit Warm-Up","muscle":"Full Body","minutes":5,
         "sets_reps":"1 easy round","equipment":"None","difficulty":"Beginner",
         "steps":["20 × Jumping jacks",
                  "10 × Arm circles each direction",
                  "10 × Bodyweight squats",
                  "10 × Hip hinges"],
         "tip":"HIIT demands your heart rate be elevated before you go into the hard intervals. Never skip this 5 minutes — it prevents injury and improves performance."},
        {"name":"HIIT Circuit","muscle":"Full Body — Fat Burning","minutes":25,
         "sets_reps":"4 rounds · 40s on / 20s off","equipment":"None or Dumbbells","difficulty":"Intermediate",
         "steps":["Burpees — 40 seconds at absolute max effort",
                  "Dumbbell squat to press — 40 seconds",
                  "Jump lunges (or walking lunges) — 40 seconds",
                  "Push-ups — 40 seconds",
                  "Rest 90 seconds between complete rounds"],
         "tip":"The 40-second work intervals are where fat loss happens. Go as hard as you possibly can — the 20-second rest is designed to be just enough to continue."},
        {"name":"Core Finisher","muscle":"Abs · Obliques","minutes":8,
         "sets_reps":"2 rounds","equipment":"Exercise Mat","difficulty":"Beginner",
         "steps":["Crunches: 20 reps",
                  "Bicycle crunches: 20 reps each side",
                  "Leg raises: 15 reps",
                  "Plank hold: 30 seconds to finish"],
         "tip":"Your core is already pre-fatigued from the circuit — this finisher squeezes extra work out of that fatigue. Even if it's difficult, push through it."},
        {"name":"Cool Down","muscle":"Full Body","minutes":8,
         "sets_reps":"8 min","equipment":"Exercise Mat","difficulty":"Beginner",
         "steps":["Walk slowly for 2 minutes to lower your heart rate",
                  "Seated forward fold: 60 seconds",
                  "Pigeon pose: 45 seconds each side",
                  "Child's pose: 60 seconds"],
         "tip":"After HIIT your heart rate needs to come down gradually. Don't sit down immediately — keep moving gently for the first 2 minutes before you stretch."},
    ],

    "Strength & Cardio": [
        {"name":"5-Minute Cardio Warm-Up","muscle":"Full Body","minutes":5,
         "sets_reps":"5 min","equipment":"Treadmill or Bike","difficulty":"Beginner",
         "steps":["Light jog or brisk walk for 5 minutes",
                  "Aim for 50–60% of your max heart rate",
                  "Breathe through your nose if possible",
                  "Finish with 30 seconds at a faster pace"],
         "tip":"This brief warm-up primes your cardiovascular system before both the strength and cardio elements of this session."},
        {"name":"Dumbbell Full Body Circuit","muscle":"Full Body","minutes":20,
         "sets_reps":"3 rounds × 12 reps each","equipment":"Dumbbells","difficulty":"Beginner",
         "steps":["Dumbbell squat × 12 reps",
                  "Dumbbell bent-over row × 12 reps",
                  "Dumbbell push press × 12 reps",
                  "Dumbbell Romanian deadlift × 12 reps",
                  "Rest 60–90 seconds between rounds"],
         "tip":"Moving straight through all 4 exercises keeps your heart rate elevated — giving you a combined strength and cardio stimulus in one go."},
        {"name":"20-Min Moderate Cardio","muscle":"Cardiovascular","minutes":20,
         "sets_reps":"20 min steady state","equipment":"Treadmill, Bike or Elliptical","difficulty":"Beginner",
         "steps":["Pick your machine and set to moderate resistance",
                  "Work at 60–70% max HR — you should be able to hold a conversation",
                  "Maintain consistent pace for 20 minutes",
                  "Last 2 minutes: reduce intensity to cool down"],
         "tip":"60–70% max HR is the fat-burning zone. Formula to find yours: 220 minus your age = max HR. Multiply by 0.65 to get your target."},
        {"name":"Cool Down","muscle":"Full Body","minutes":8,
         "sets_reps":"8 min","equipment":"Exercise Mat","difficulty":"Beginner",
         "steps":["Standing quad stretch: 30 seconds each leg",
                  "Chest stretch against wall: 30 seconds",
                  "Seated hamstring stretch: 60 seconds",
                  "5 slow, deep breaths"],
         "tip":"Combining strength and cardio in one session is demanding. Sleep, protein intake and hydration are especially important on these days."},
    ],

    "Light Cardio": [
        {"name":"Steady-State Cardio","muscle":"Cardiovascular","minutes":30,
         "sets_reps":"30 min continuous","equipment":"Treadmill, Bike or Elliptical","difficulty":"Beginner",
         "steps":["Choose your preferred cardio machine",
                  "Moderate pace — you should be able to hold a full conversation",
                  "Maintain consistent effort for 30 minutes",
                  "Focus on posture and slow, steady breathing"],
         "tip":"Light cardio on active rest days keeps your metabolism elevated without adding muscular stress. Perfect for a Saturday or low-energy day."},
        {"name":"Gentle Stretch","muscle":"Full Body","minutes":15,
         "sets_reps":"15 min","equipment":"Exercise Mat","difficulty":"Beginner",
         "steps":["Neck rolls: 30 seconds each direction",
                  "Seated forward fold: 60 seconds",
                  "Lying glute stretch: 45 seconds each side",
                  "Child's pose: 60 seconds",
                  "Cobra stretch: 30 seconds × 2"],
         "tip":"The stretching after light cardio is where your muscles are most pliable. This is the best time of the week to improve your flexibility."},
    ],

    "Steady-State Cardio": [
        {"name":"Steady-State Cardio","muscle":"Cardiovascular · Endurance","minutes":40,
         "sets_reps":"40 min at zone 2","equipment":"Treadmill, Bike or Elliptical","difficulty":"Beginner",
         "steps":["5 min easy warm-up",
                  "Zone 2 pace: 60–70% max HR — genuinely conversational",
                  "Hold this pace for 30 minutes — resist the urge to push harder",
                  "5 min easy cool-down walk"],
         "tip":"Zone 2 builds your aerobic base — the foundation that makes every other form of training more effective. It should feel almost too easy. That's correct."},
        {"name":"Post-Cardio Stretch","muscle":"Legs & Hips","minutes":10,
         "sets_reps":"10 min","equipment":"Exercise Mat","difficulty":"Beginner",
         "steps":["Standing calf stretch: 30 seconds each",
                  "Hip flexor kneeling stretch: 30 seconds each",
                  "IT band stretch: 30 seconds each side",
                  "Child's pose: 60 seconds"],
         "tip":"Hip flexors and calves take the most stress during sustained cardio. Give them specific attention after every long session."},
    ],

    "Interval Training": [
        {"name":"Speed Intervals","muscle":"Cardiovascular · Legs","minutes":30,
         "sets_reps":"8 × 2 min hard / 2 min easy","equipment":"Treadmill or Track","difficulty":"Intermediate",
         "steps":["5 min easy jog warm-up",
                  "2 minutes at 80–85% max HR — this should be genuinely hard",
                  "2 minutes recovery — easy jog or walk at 50% max HR",
                  "Repeat 8 times, then 5 min easy cool-down"],
         "tip":"Intervals are the most time-efficient cardiovascular training that exists. Push hard during the work intervals — they should be uncomfortable. That's the point."},
        {"name":"Stretching","muscle":"Full Body","minutes":10,
         "sets_reps":"10 min","equipment":"Exercise Mat","difficulty":"Beginner",
         "steps":["Seated hamstring stretch: 60 seconds",
                  "Standing quad stretch: 30 seconds each",
                  "Kneeling hip flexor stretch: 30 seconds each",
                  "Spinal twist: 30 seconds each direction"],
         "tip":"Interval training creates significant muscular tension. Stretching post-session reduces stiffness and keeps your stride length healthy over time."},
    ],

    "Cross Training": [
        {"name":"Cross-Training Circuit","muscle":"Full Body — Active Recovery","minutes":35,
         "sets_reps":"3 machine rotations","equipment":"Various","difficulty":"Beginner",
         "steps":["10 min swimming or aqua jogging (low joint impact)",
                  "10 min rowing machine at moderate pace",
                  "10 min stationary bike",
                  "5 min easy walking cool-down"],
         "tip":"Cross training challenges your cardiovascular system while giving your primary running or cycling muscles a complete rest. This prevents overuse injuries and builds overall fitness."},
        {"name":"Gentle Stretching","muscle":"Full Body","minutes":10,
         "sets_reps":"10 min","equipment":"Exercise Mat","difficulty":"Beginner",
         "steps":["Cat-cow stretch: 60 seconds",
                  "Chest opener: 30 seconds",
                  "Seated forward fold: 60 seconds",
                  "Lying spinal twist: 30 seconds each side"],
         "tip":"Cross training days are about active recovery, not performance. Keep everything easy and enjoy the change of pace."},
    ],

    "Long Cardio Session": [
        {"name":"Long Endurance Session","muscle":"Cardiovascular","minutes":60,
         "sets_reps":"60 min zone 2–3","equipment":"Treadmill, Bike or Elliptical","difficulty":"Intermediate",
         "steps":["10 min easy warm-up",
                  "40 min at zone 2–3 (65–75% max HR)",
                  "Final 5 min: push to zone 3 (75–80% max HR)",
                  "5 min easy cool-down"],
         "tip":"Long sessions build the aerobic base that makes everything easier. Fuel properly beforehand — a carb-rich meal 60–90 minutes before is ideal."},
        {"name":"Full Body Cool Down","muscle":"Full Body","minutes":10,
         "sets_reps":"10 min","equipment":"Exercise Mat","difficulty":"Beginner",
         "steps":["3 min gentle walking (don't stop abruptly)",
                  "Full-body stretch sequence: legs, hips, back, shoulders",
                  "5 slow, controlled deep breaths",
                  "Foam rolling if available: 2 minutes on tightest areas"],
         "tip":"After 60 minutes of cardio your body needs a structured wind-down. Hydrate immediately and eat a recovery meal within 30 minutes."},
    ],

    "Recovery Cardio": [
        {"name":"Easy Recovery Walk/Jog","muscle":"Cardiovascular — Light","minutes":25,
         "sets_reps":"25 min at 40–50% max HR","equipment":"Treadmill or Outdoors","difficulty":"Beginner",
         "steps":["Walk or very light jog — conversation should feel completely effortless",
                  "40–50% of max HR — this is very easy",
                  "Focus on good posture and relaxed, natural breathing",
                  "Resist every urge to go faster — today is about recovery"],
         "tip":"Recovery cardio flushes lactic acid and brings fresh blood to muscles still repairing from harder sessions. Its value is completely in the gentleness."},
        {"name":"Mobility Work","muscle":"Full Body","minutes":15,
         "sets_reps":"15 min","equipment":"Exercise Mat · Foam Roller","difficulty":"Beginner",
         "steps":["Foam roll quads, hamstrings and calves: 60 seconds each",
                  "Hip 90-90 stretch: 45 seconds each side",
                  "Ankle circles: 20 each direction",
                  "World's greatest stretch: 5 reps each side"],
         "tip":"Recovery days with mobility work are where the best athletes separate themselves. Don't waste yours by doing nothing — use the 15 minutes."},
    ],

    "Yoga Flow": [
        {"name":"Sun Salutation Flow","muscle":"Full Body Flexibility","minutes":20,
         "sets_reps":"5 × full salutation","equipment":"Yoga Mat","difficulty":"Beginner",
         "steps":["Mountain pose → Forward fold → Halfway lift",
                  "Step back to high plank → Lower to Cobra or Upward Dog",
                  "Press up to Downward Dog → hold 5 deep breaths",
                  "Walk feet to hands → Halfway lift → Forward fold → Mountain pose"],
         "tip":"Sun salutations warm up your entire spine and integrate breath with movement. Move slower than feels natural — speed kills the benefit."},
        {"name":"Standing Balance Poses","muscle":"Balance · Legs · Core","minutes":15,
         "sets_reps":"30–60 sec each pose","equipment":"Yoga Mat","difficulty":"Beginner",
         "steps":["Tree pose: 30 seconds each leg (gaze fixed on a still point)",
                  "Warrior I: 45 seconds each side",
                  "Warrior II: 45 seconds each side",
                  "Warrior III: 20 seconds each side"],
         "tip":"Fix your gaze on a completely still point (called drishti in yoga). Balance improves faster than almost any other fitness quality with regular practice."},
        {"name":"Floor Poses & Cool Down","muscle":"Hips · Hamstrings · Lower Back","minutes":15,
         "sets_reps":"60 seconds each pose","equipment":"Yoga Mat","difficulty":"Beginner",
         "steps":["Seated forward fold (Paschimottanasana): 60 seconds",
                  "Butterfly pose: 60 seconds",
                  "Supine spinal twist: 45 seconds each side",
                  "Savasana — lie completely still: 3 full minutes"],
         "tip":"Savasana (the final rest) is not optional. It's when your nervous system integrates everything from the practice. Skipping it is like baking a cake then removing it too early."},
    ],

    "Mobility Drills": [
        {"name":"Joint Mobility Circuit","muscle":"Full Body Joints","minutes":25,
         "sets_reps":"2 rounds × 10 reps each","equipment":"None","difficulty":"Beginner",
         "steps":["Neck: slow controlled circles — 10 each direction",
                  "Shoulders: full arm circles — 10 forward, 10 backward",
                  "Hips: large hip circles — 10 each direction",
                  "Ankles: circles — 10 each direction, then 10 flexion/extension"],
         "tip":"Joint mobility work produces synovial fluid — the lubricant that keeps your joints healthy for decades. 10 minutes daily compounds into extraordinary long-term joint health."},
        {"name":"Thoracic Mobility","muscle":"Upper Back & Spine","minutes":15,
         "sets_reps":"2 rounds","equipment":"Foam Roller · Mat","difficulty":"Beginner",
         "steps":["Thoracic extension over foam roller: 2 minutes — segment by segment",
                  "Thread-the-needle rotation stretch: 45 seconds each side",
                  "Cat-cow: 10 very slow, very deliberate reps",
                  "Open book rotation: 10 each side"],
         "tip":"Most desk workers have severe thoracic (mid-back) stiffness. Working on this consistently transforms your posture, eliminates neck pain, and makes every pressing exercise stronger."},
    ],

    "Deep Stretch": [
        {"name":"Full Body Deep Stretch","muscle":"All Major Muscle Groups","minutes":45,
         "sets_reps":"Hold each 60–90 seconds","equipment":"Yoga Mat · Strap (optional)","difficulty":"Beginner",
         "steps":["Hip flexor kneeling lunge: 90 seconds each side",
                  "Pigeon pose (glutes/hip rotators): 90 seconds each side",
                  "Seated hamstring stretch with strap: 90 seconds",
                  "Doorway chest stretch: 60 seconds",
                  "Supine spinal twist: 60 seconds each side",
                  "Child's pose: 2 minutes to finish"],
         "tip":"Never force a deep stretch by pulling harder. Breathe into the area of tension and wait for the muscle to release on its own — it always does, given time and breath."},
    ],

    "Active Mobility": [
        {"name":"Active Mobility Flow","muscle":"Full Body","minutes":40,
         "sets_reps":"Continuous flow","equipment":"Yoga Mat","difficulty":"Beginner",
         "steps":["5 min foam rolling — hit your tightest spots",
                  "10 min joint circles: neck, shoulders, hips, ankles",
                  "10 min slow yoga flow (sun salutations)",
                  "10 min deep stretching — focus on the areas you trained this week",
                  "5 min box breathing: 4s in, 4s hold, 4s out, 4s hold"],
         "tip":"This weekly session compounds over months into genuinely exceptional flexibility and joint health. Athletes who do this consistently almost never get injured."},
    ],
}

REST_TIPS = [
    ("💤","Sleep 7–9 hours",     "This is when your muscles repair and grow."),
    ("🥩","Hit your protein",    "Aim for 1.6–2g per kg of bodyweight today."),
    ("💧","Stay hydrated",       "At least 2–3 litres of water throughout the day."),
    ("🚶","Light walk",          "20–30 minutes of easy walking aids recovery."),
    ("📋","Review your plan",    "Track your progress and plan next week."),
    ("🧊","Contrast therapy",    "Hot/cold shower alternation reduces soreness."),
]

# ═══════════════════════════════════════════════════════════════════════════
#  CSS — PREMIUM DARK FITNESS APP
# ═══════════════════════════════════════════════════════════════════════════

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 1rem 1.5rem 3rem !important; max-width: 1280px !important; }

/* ── HERO ── */
.hero {
    position: relative;
    border-radius: 24px;
    overflow: hidden;
    margin-bottom: 2.5rem;
    min-height: 280px;
    display: flex;
    align-items: center;
    background: url('https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=1400&q=80') center/cover no-repeat;
}
.hero-overlay {
    position: absolute; inset: 0;
    background: linear-gradient(120deg, rgba(5,5,15,0.95) 0%, rgba(5,5,15,0.80) 60%, rgba(5,5,15,0.5) 100%);
    border-radius: 24px;
}
.hero-content { position: relative; z-index: 2; padding: 3rem 3.5rem; }
.hero-eyebrow {
    font-size: 0.7rem; font-weight: 700; letter-spacing: 0.2em;
    text-transform: uppercase; color: #FF3E3E;
    margin-bottom: 0.75rem;
}
.hero-title {
    font-size: 3.2rem; font-weight: 900; color: #fff;
    line-height: 1.05; margin-bottom: 1rem;
}
.hero-title span { color: #FF3E3E; }
.hero-sub { font-size: 1rem; color: rgba(255,255,255,0.6); max-width: 460px; line-height: 1.6; margin-bottom: 1.5rem; }
.hero-pills { display: flex; gap: 8px; flex-wrap: wrap; }
.hero-pill {
    padding: 5px 14px; border-radius: 99px;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    font-size: 0.75rem; color: rgba(255,255,255,0.75); font-weight: 500;
}

/* ── SECTION LABELS ── */
.sec-eyebrow {
    font-size: 0.68rem; font-weight: 800; letter-spacing: 0.15em;
    text-transform: uppercase; color: #FF3E3E; margin-bottom: 0.5rem;
}
.sec-title {
    font-size: 1.6rem; font-weight: 800; color: #fff; margin-bottom: 1.5rem;
}

/* ── GOAL CARDS ── */
.goals-row { display: grid; grid-template-columns: repeat(5, 1fr); gap: 12px; margin-bottom: 0.5rem; }
.goal-card {
    border-radius: 18px; padding: 1.5rem 1rem;
    border: 1.5px solid rgba(255,255,255,0.08);
    background: #111118; cursor: pointer;
    text-align: center; transition: all 0.2s;
}
.goal-card:hover {
    border-color: rgba(255,62,62,0.5);
    transform: translateY(-4px);
    box-shadow: 0 12px 32px rgba(255,62,62,0.15);
}
.goal-card.active {
    border-color: #FF3E3E;
    background: rgba(255,62,62,0.08);
    box-shadow: 0 12px 32px rgba(255,62,62,0.2);
}
.goal-emoji { font-size: 2.4rem; margin-bottom: 0.7rem; display: block; }
.goal-name  { font-size: 0.9rem; font-weight: 700; color: #fff; margin-bottom: 0.4rem; }
.goal-desc  { font-size: 0.72rem; color: rgba(255,255,255,0.45); line-height: 1.4; }

/* ── SCHEDULE BUILDER ── */
.schedule-box {
    background: #111118; border-radius: 20px;
    border: 1.5px solid rgba(255,255,255,0.08);
    padding: 1.75rem; margin-bottom: 1.5rem;
}
.week-visual { display: grid; grid-template-columns: repeat(7,1fr); gap: 8px; margin-bottom: 1.5rem; }
.wv-cell {
    border-radius: 12px; padding: 12px 4px;
    text-align: center; border: 1.5px solid;
    transition: all 0.2s;
}
.wv-train { border-color: #FF3E3E; background: rgba(255,62,62,0.10); }
.wv-rest  { border-color: rgba(255,255,255,0.08); background: rgba(255,255,255,0.03); }
.wv-day   { font-size: 0.65rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; color: rgba(255,255,255,0.35); margin-bottom: 5px; }
.wv-session { font-size: 0.62rem; font-weight: 700; }
.wv-s-train { color: #FF3E3E; }
.wv-s-rest  { color: rgba(255,255,255,0.25); }

/* ── DAY PICKER BUTTONS ── */
.day-row { display: flex; gap: 8px; flex-wrap: wrap; margin: 1rem 0 1.5rem; }
.day-btn {
    padding: 10px 18px; border-radius: 99px; font-size: 0.82rem; font-weight: 700;
    border: 1.5px solid; cursor: pointer; transition: all 0.15s;
    font-family: 'Inter', sans-serif;
}
.day-btn-active  { border-color: #FF3E3E; background: #FF3E3E; color: #fff; }
.day-btn-rest    { border-color: rgba(255,255,255,0.15); background: transparent; color: rgba(255,255,255,0.4); }
.day-btn-current { outline: 2px solid #FF8C00; outline-offset: 2px; }

/* ── SUMMARY STRIP ── */
.summary-strip {
    display: flex; gap: 0; margin-bottom: 1.5rem;
    background: #111118; border-radius: 16px;
    border: 1.5px solid rgba(255,255,255,0.08);
    overflow: hidden;
}
.sum-cell { flex: 1; padding: 1rem 0.5rem; text-align: center; border-right: 1px solid rgba(255,255,255,0.06); }
.sum-cell:last-child { border-right: none; }
.sum-val   { font-size: 1.6rem; font-weight: 900; color: #FF3E3E; line-height: 1; }
.sum-lbl   { font-size: 0.65rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: rgba(255,255,255,0.35); margin-top: 4px; }

/* ── EXERCISE CARD ── */
.ex-card {
    background: #111118; border-radius: 20px;
    border: 1.5px solid rgba(255,255,255,0.07);
    overflow: hidden; margin-bottom: 1.25rem;
    transition: border-color 0.2s, box-shadow 0.2s;
}
.ex-card:hover {
    border-color: rgba(255,62,62,0.25);
    box-shadow: 0 8px 32px rgba(0,0,0,0.4);
}
.ex-img-wrap {
    position: relative; height: 240px; overflow: hidden;
    background: #0D0D14;
}
.ex-img-wrap img {
    width: 100%; height: 100%; object-fit: cover;
    display: block; transition: transform 0.4s;
}
.ex-card:hover .ex-img-wrap img { transform: scale(1.04); }
.ex-img-gradient {
    position: absolute; inset: 0;
    background: linear-gradient(to top, rgba(5,5,15,0.85) 0%, rgba(5,5,15,0.1) 60%, transparent 100%);
}
.ex-img-badges {
    position: absolute; top: 14px; left: 14px; right: 14px;
    display: flex; justify-content: space-between; align-items: flex-start;
}
.ex-num-badge {
    width: 34px; height: 34px; border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.85rem; font-weight: 800; color: #fff;
    backdrop-filter: blur(8px);
}
.ex-muscle-badge {
    padding: 4px 12px; border-radius: 99px;
    font-size: 0.65rem; font-weight: 800; text-transform: uppercase;
    letter-spacing: 0.08em; color: #fff;
    backdrop-filter: blur(8px);
    background: rgba(255,62,62,0.7);
}
.ex-img-title {
    position: absolute; bottom: 14px; left: 18px; right: 18px;
}
.ex-img-name {
    font-size: 1.1rem; font-weight: 800; color: #fff; line-height: 1.2;
}

/* ── EXERCISE BODY ── */
.ex-body { padding: 1.4rem 1.5rem 1.5rem; }
.meta-row { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 1.2rem; }
.meta-badge {
    display: inline-flex; align-items: center; gap: 5px;
    padding: 5px 13px; border-radius: 99px;
    font-size: 0.72rem; font-weight: 700;
}
.m-time  { background: rgba(62,139,255,0.15); color: #60A5FA; }
.m-sets  { background: rgba(255,62,62,0.15);  color: #FF7070; }
.m-equip { background: rgba(168,85,247,0.15); color: #C084FC; }
.m-diff  { background: rgba(0,200,150,0.15);  color: #34D399; }

.steps-lbl {
    font-size: 0.65rem; font-weight: 800; text-transform: uppercase;
    letter-spacing: 0.12em; color: rgba(255,255,255,0.3); margin-bottom: 0.7rem;
}
.steps-list { list-style: none; margin-bottom: 1rem; }
.steps-list li {
    font-size: 0.85rem; color: rgba(255,255,255,0.7);
    padding: 5px 0 5px 26px; position: relative; line-height: 1.5;
    border-bottom: 1px solid rgba(255,255,255,0.04);
}
.steps-list li:last-child { border-bottom: none; }
.steps-list li::before {
    content: attr(data-n);
    position: absolute; left: 0;
    width: 18px; height: 18px;
    background: rgba(255,62,62,0.2);
    color: #FF3E3E; font-weight: 800; font-size: 0.7rem;
    border-radius: 5px; display: flex; align-items: center; justify-content: center;
    top: 6px;
}
.tip-wrap {
    background: linear-gradient(135deg, rgba(255,140,0,0.1), rgba(255,62,62,0.08));
    border: 1px solid rgba(255,140,0,0.25);
    border-radius: 12px; padding: 12px 14px;
    display: flex; align-items: flex-start; gap: 10px;
}
.tip-icon { font-size: 1rem; flex-shrink: 0; margin-top: 1px; }
.tip-text  { font-size: 0.8rem; color: rgba(255,255,255,0.65); line-height: 1.5; }
.tip-bold  { font-weight: 700; color: #FF8C00; }

/* ── REST DAY ── */
.rest-hero {
    border-radius: 24px; overflow: hidden; position: relative;
    min-height: 220px; display: flex; align-items: center;
    background: url('https://images.unsplash.com/photo-1552196563-55cd4e45efb3?w=1200&q=80') center/cover;
    margin-bottom: 1.5rem;
}
.rest-overlay {
    position: absolute; inset: 0;
    background: linear-gradient(120deg, rgba(5,20,5,0.92), rgba(10,30,10,0.75));
}
.rest-content { position: relative; z-index: 2; padding: 2.5rem 3rem; }
.rest-tag  { font-size: 0.65rem; font-weight: 800; letter-spacing: 0.2em; text-transform: uppercase; color: #34D399; margin-bottom: 0.5rem; }
.rest-h    { font-size: 2rem; font-weight: 900; color: #fff; margin-bottom: 0.5rem; }
.rest-sub  { font-size: 0.9rem; color: rgba(255,255,255,0.55); max-width: 400px; line-height: 1.6; }
.rest-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }
.rest-tip  {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 14px; padding: 1rem;
}
.rt-icon  { font-size: 1.3rem; margin-bottom: 0.5rem; display: block; }
.rt-title { font-size: 0.8rem; font-weight: 700; color: #fff; margin-bottom: 3px; }
.rt-desc  { font-size: 0.72rem; color: rgba(255,255,255,0.4); line-height: 1.4; }

/* ── ALERT / NOTICE ── */
.notice {
    background: rgba(255,140,0,0.08);
    border: 1px solid rgba(255,140,0,0.25);
    border-radius: 12px; padding: 12px 16px;
    font-size: 0.82rem; color: rgba(255,200,100,0.9);
    margin-bottom: 1rem;
}

/* ── STREAMLIT OVERRIDES ── */
.stButton > button {
    border-radius: 99px !important;
    font-weight: 700 !important;
    font-size: 0.82rem !important;
    border: 1.5px solid rgba(255,62,62,0.5) !important;
    color: #FF3E3E !important;
    background: rgba(255,62,62,0.05) !important;
    transition: all 0.15s !important;
    padding: 0.45rem 1.2rem !important;
}
.stButton > button:hover {
    background: #FF3E3E !important;
    color: #fff !important;
    border-color: #FF3E3E !important;
}
div[data-testid="stMultiSelect"] { margin-bottom: 1rem; }
div[data-testid="stMultiSelect"] label {
    font-size: 0.82rem; font-weight: 700;
    color: rgba(255,255,255,0.5) !important;
    text-transform: uppercase; letter-spacing: 0.06em;
}
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════
#  SESSION STATE
# ═══════════════════════════════════════════════════════════════════════════

for key, default in [("goal", None), ("training_days", ["Monday","Tuesday","Thursday","Friday"]),
                      ("viewing_day", None)]:
    if key not in st.session_state:
        st.session_state[key] = default

# ═══════════════════════════════════════════════════════════════════════════
#  HERO
# ═══════════════════════════════════════════════════════════════════════════

st.markdown("""
<div class="hero">
  <div class="hero-overlay"></div>
  <div class="hero-content">
    <div class="hero-eyebrow">Your Personal Training Companion</div>
    <div class="hero-title">Gym<span>Guide</span><br>Premium</div>
    <div class="hero-sub">
      Build your schedule your way. Pick your goal, choose your training days,
      and get a step-by-step visual guide for every exercise.
    </div>
    <div class="hero-pills">
      <span class="hero-pill">📸 Visual exercise guides</span>
      <span class="hero-pill">⏱ Time per exercise</span>
      <span class="hero-pill">🏋️ Equipment listed</span>
      <span class="hero-pill">📅 Flexible scheduling</span>
      <span class="hero-pill">💡 Pro coaching tips</span>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════
#  STEP 1 — GOAL
# ═══════════════════════════════════════════════════════════════════════════

st.markdown('<div class="sec-eyebrow">Step 1 of 3</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-title">Choose your fitness goal</div>', unsafe_allow_html=True)

goal_names = list(GOAL_POOLS.keys())
cols = st.columns(len(goal_names))
for col, gk in zip(cols, goal_names):
    g = GOAL_POOLS[gk]
    active_cls = "active" if st.session_state.goal == gk else ""
    with col:
        st.markdown(f"""
        <div class="goal-card {active_cls}">
            <span class="goal-emoji">{g['icon']}</span>
            <div class="goal-name">{gk.split(' ',1)[1]}</div>
            <div class="goal-desc">{g['desc']}</div>
        </div>""", unsafe_allow_html=True)
        if st.button("Select", key=f"g_{gk}"):
            st.session_state.goal = gk
            st.session_state.viewing_day = None
            st.rerun()

# ═══════════════════════════════════════════════════════════════════════════
#  STEP 2 — FLEXIBLE SCHEDULE BUILDER
# ═══════════════════════════════════════════════════════════════════════════

if st.session_state.goal:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="sec-eyebrow">Step 2 of 3</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-title">Build your weekly schedule</div>', unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="schedule-box">', unsafe_allow_html=True)

        st.markdown("""
        <p style="font-size:0.82rem;color:rgba(255,255,255,0.45);margin-bottom:0.75rem;">
        Select <strong style="color:rgba(255,255,255,0.7)">3–6 training days</strong> below — rest days are automatically assigned to the remaining days.
        You have full flexibility to choose any combination that fits your life.
        </p>""", unsafe_allow_html=True)

        selected = st.multiselect(
            "Your training days",
            options=ALL_DAYS,
            default=st.session_state.training_days,
            key="day_picker",
        )
        st.session_state.training_days = selected

        n = len(selected)
        if n < 3:
            st.markdown('<div class="notice">⚠️ Select at least 3 training days to build your schedule.</div>',
                        unsafe_allow_html=True)
        elif n > 6:
            st.markdown('<div class="notice">⚠️ Maximum 6 training days. Please deselect some days.</div>',
                        unsafe_allow_html=True)
        else:
            schedule = build_schedule(st.session_state.goal, selected)

            # Week visual grid
            cells_html = ""
            for day in ALL_DAYS:
                sess = schedule[day]
                is_train = sess != "Rest"
                label = sess[:8].upper() if is_train else "REST"
                cells_html += (
                    f'<div class="wv-cell {"wv-train" if is_train else "wv-rest"}">'
                    f'<div class="wv-day">{DAY_ABB[day]}</div>'
                    f'<div class="wv-session {"wv-s-train" if is_train else "wv-s-rest"}">{label}</div>'
                    f'</div>'
                )
            st.markdown(f'<div class="week-visual">{cells_html}</div>', unsafe_allow_html=True)
            st.markdown(
                f'<p style="font-size:0.75rem;color:rgba(255,255,255,0.3);text-align:right;">'
                f'{n} training days · {7-n} rest days per week</p>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════
#  STEP 3 — WORKOUT VIEW
# ═══════════════════════════════════════════════════════════════════════════

if st.session_state.goal and 3 <= len(st.session_state.training_days) <= 6:
    schedule = build_schedule(st.session_state.goal, st.session_state.training_days)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="sec-eyebrow">Step 3 of 3</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-title">Select a day to view your workout</div>', unsafe_allow_html=True)

    # Day pick buttons
    day_cols = st.columns(7)
    for col, day in zip(day_cols, ALL_DAYS):
        sess = schedule[day]
        is_rest = sess == "Rest"
        is_viewing = st.session_state.viewing_day == day
        with col:
            label = f"{'😴' if is_rest else '🏋️'} {DAY_ABB[day]}"
            if st.button(label, key=f"view_{day}"):
                st.session_state.viewing_day = day
                st.rerun()

    # Workout content
    if st.session_state.viewing_day:
        vday    = st.session_state.viewing_day
        session = schedule[vday]
        st.markdown("<br>", unsafe_allow_html=True)

        if session == "Rest":
            tip_html = "".join(
                f'<div class="rest-tip"><span class="rt-icon">{ic}</span>'
                f'<div class="rt-title">{ti}</div><div class="rt-desc">{de}</div></div>'
                for ic, ti, de in REST_TIPS
            )
            st.markdown(f"""
            <div class="rest-hero">
              <div class="rest-overlay"></div>
              <div class="rest-content">
                <div class="rest-tag">Recovery Day — {vday}</div>
                <div class="rest-h">Rest & Recover 🛌</div>
                <div class="rest-sub">
                  Muscle growth happens during rest, not during the workout.
                  Today is just as important as your training days.
                </div>
              </div>
            </div>
            <div class="rest-grid">{tip_html}</div>
            """, unsafe_allow_html=True)

        else:
            exercises = EXERCISES.get(session, [])
            if not exercises:
                st.info(f"Session **{session}** is coming soon!")
            else:
                total_min    = sum(e["minutes"] for e in exercises)
                working_ex   = len([e for e in exercises if "Cool" not in e["name"] and "Warm" not in e["name"]])
                warmup_min   = sum(e["minutes"] for e in exercises if "Warm" in e["name"])
                cooldown_min = sum(e["minutes"] for e in exercises if "Cool" in e["name"])

                # Header
                st.markdown(f"""
                <div style="margin-bottom:1.25rem;">
                  <p style="font-size:0.65rem;font-weight:800;letter-spacing:0.15em;text-transform:uppercase;color:#FF3E3E;margin-bottom:4px;">
                    {vday} · {st.session_state.goal.split(' ',1)[1]}
                  </p>
                  <h2 style="font-size:1.8rem;font-weight:900;color:#fff;margin-bottom:0;">{session}</h2>
                </div>""", unsafe_allow_html=True)

                # Summary strip
                st.markdown(f"""
                <div class="summary-strip">
                  <div class="sum-cell"><div class="sum-val">{total_min}</div><div class="sum-lbl">Total mins</div></div>
                  <div class="sum-cell"><div class="sum-val">{working_ex}</div><div class="sum-lbl">Exercises</div></div>
                  <div class="sum-cell"><div class="sum-val">{warmup_min}</div><div class="sum-lbl">Warm-up</div></div>
                  <div class="sum-cell"><div class="sum-val">{cooldown_min}</div><div class="sum-lbl">Cool-down</div></div>
                </div>""", unsafe_allow_html=True)

                # Exercise cards — 2 per row
                for row_start in range(0, len(exercises), 2):
                    row_exs = exercises[row_start:row_start+2]
                    cols_ex = st.columns(len(row_exs))
                    for col_ex, (ex, abs_idx) in zip(cols_ex, [(e, row_start+i) for i,e in enumerate(row_exs)]):
                        with col_ex:
                            is_cool = "Cool" in ex["name"]
                            is_warm = "Warm" in ex["name"]
                            num_bg  = ("rgba(0,200,150,0.5)" if is_cool
                                       else "rgba(62,139,255,0.5)" if is_warm
                                       else "rgba(255,62,62,0.5)")

                            img_src = img_url(ex["name"])
                            steps_li = "".join(
                                f'<li data-n="{i+1}">{s}</li>'
                                for i, s in enumerate(ex["steps"])
                            )
                            st.markdown(f"""
                            <div class="ex-card">
                              <div class="ex-img-wrap">
                                <img src="{img_src}" alt="{ex['name']}"
                                     onerror="this.src='https://images.unsplash.com/photo-1517963628607-235ccdd5476c?w=800&h=380&fit=crop&q=80'">
                                <div class="ex-img-gradient"></div>
                                <div class="ex-img-badges">
                                  <div class="ex-num-badge" style="background:{num_bg};">{abs_idx+1}</div>
                                  <div class="ex-muscle-badge">{ex['muscle']}</div>
                                </div>
                                <div class="ex-img-title">
                                  <div class="ex-img-name">{ex['name']}</div>
                                </div>
                              </div>
                              <div class="ex-body">
                                <div class="meta-row">
                                  <span class="meta-badge m-time">⏱ {ex['minutes']} min</span>
                                  <span class="meta-badge m-sets">🔁 {ex['sets_reps']}</span>
                                  <span class="meta-badge m-equip">🏋️ {ex['equipment']}</span>
                                  <span class="meta-badge m-diff">⭐ {ex['difficulty']}</span>
                                </div>
                                <div class="steps-lbl">How to perform it</div>
                                <ul class="steps-list">{steps_li}</ul>
                                <div class="tip-wrap">
                                  <span class="tip-icon">💡</span>
                                  <div class="tip-text"><span class="tip-bold">Coach tip: </span>{ex['tip']}</div>
                                </div>
                              </div>
                            </div>""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════
#  FOOTER
# ═══════════════════════════════════════════════════════════════════════════

st.markdown("""
<div style="text-align:center;padding:2.5rem 0 1rem;font-size:0.75rem;color:rgba(255,255,255,0.2);">
  GymGuide Premium — Built as a personal fitness companion.<br>
  Always consult a qualified professional before starting a new exercise programme.
</div>""", unsafe_allow_html=True)
