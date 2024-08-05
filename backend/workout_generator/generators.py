import random
from .exercises import LegsExercise, ChestExercise, BackExercise, WorkoutPlan

class WorkoutPlanGenerator:
    @staticmethod
    def generate_fbw_plan(num_core_exercises_per_group=2, num_optional_exercises_per_group=1):
        plan = WorkoutPlan("Full Body Workout")

        # Example pool of exercises for each muscle group
        leg_exercises = [
            LegsExercise("Squats", 3, 12, "core"),
            LegsExercise("Lunges", 3, 15, "core"),
            LegsExercise("Leg Press", 3, 10, "core"),
            LegsExercise("Leg Curl", 3, 12, "core"),
            LegsExercise("Deadlift", 3, 10, "core"),
            LegsExercise("Step Ups", 3, 15, "core"),
            LegsExercise("Bulgarian Split Squat", 3, 12, "core"),
            LegsExercise("Calf Raises", 3, 15, "core"),
            LegsExercise("Hamstring Curl", 3, 12, "core"),
            LegsExercise("Leg Extension", 3, 15, "core"),
            LegsExercise("Glute Bridge", 3, 12, "optional"),
            LegsExercise("Seated Leg Press", 3, 15, "optional"),
            LegsExercise("Reverse Lunges", 3, 12, "optional"),
            LegsExercise("Jump Squats", 3, 15, "optional"),
            LegsExercise("Single Leg Deadlift", 3, 12, "optional"),
            LegsExercise("Goblet Squats", 3, 15, "optional"),
            LegsExercise("Side Lunges", 3, 12, "optional"),
            LegsExercise("Box Jumps", 3, 15, "optional"),
            LegsExercise("Front Squats", 3, 12, "optional"),
            LegsExercise("Smith Machine Squats", 3, 15, "optional")
        ]

        chest_exercises = [
            ChestExercise("Bench Press", 3, 10, "core"),
            ChestExercise("Push Ups", 3, 15, "core"),
            ChestExercise("Incline Bench Press", 3, 10, "core"),
            ChestExercise("Chest Fly", 3, 12, "core"),
            ChestExercise("Dumbbell Press", 3, 10, "core"),
            ChestExercise("Dumbbell Fly", 3, 12, "core"),
            ChestExercise("Cable Crossover", 3, 15, "core"),
            ChestExercise("Decline Bench Press", 3, 10, "core"),
            ChestExercise("Pec Deck Machine", 3, 12, "core"),
            ChestExercise("Dips", 3, 15, "core"),
            ChestExercise("Push-Up Variations", 3, 15, "optional"),
            ChestExercise("Resistance Band Press", 3, 12, "optional"),
            ChestExercise("Incline Dumbbell Fly", 3, 10, "optional"),
            ChestExercise("Landmine Press", 3, 12, "optional"),
            ChestExercise("Close-Grip Bench Press", 3, 10, "optional"),
            ChestExercise("Smith Machine Bench Press", 3, 12, "optional"),
            ChestExercise("Chest Dips", 3, 15, "optional"),
            ChestExercise("Incline Push-Ups", 3, 12, "optional"),
            ChestExercise("Decline Dumbbell Press", 3, 10, "optional"),
            ChestExercise("Single Arm Chest Press", 3, 12, "optional")
        ]

        back_exercises = [
            BackExercise("Deadlift", 3, 10, "core"),
            BackExercise("Pull Ups", 3, 8, "core"),
            BackExercise("Bent Over Rows", 3, 12, "core"),
            BackExercise("Lat Pulldown", 3, 10, "core"),
            BackExercise("Seated Row", 3, 12, "core"),
            BackExercise("T-Bar Row", 3, 10, "core"),
            BackExercise("One Arm Dumbbell Row", 3, 12, "core"),
            BackExercise("Chin Ups", 3, 15, "core"),
            BackExercise("Inverted Rows", 3, 15, "core"),
            BackExercise("Face Pulls", 3, 12, "core"),
            BackExercise("Back Extension", 3, 12, "optional"),
            BackExercise("Cable Row", 3, 15, "optional"),
            BackExercise("Single Arm Cable Row", 3, 12, "optional"),
            BackExercise("Landmine Row", 3, 15, "optional"),
            BackExercise("Straight Arm Pulldown", 3, 12, "optional"),
            BackExercise("Close Grip Lat Pulldown", 3, 10, "optional"),
            BackExercise("Wide Grip Lat Pulldown", 3, 12, "optional"),
            BackExercise("Reverse Grip Bent Over Rows", 3, 10, "optional"),
            BackExercise("Renegade Rows", 3, 12, "optional"),
            BackExercise("Smith Machine Row", 3, 15, "optional")
        ]

        # Randomly select core and optional exercises from each group
        selected_leg_exercises = random.sample([ex for ex in leg_exercises if ex.exercise_type == "core"], num_core_exercises_per_group)
        selected_leg_exercises += random.sample([ex for ex in leg_exercises if ex.exercise_type == "optional"], num_optional_exercises_per_group)

        selected_chest_exercises = random.sample([ex for ex in chest_exercises if ex.exercise_type == "core"], num_core_exercises_per_group)
        selected_chest_exercises += random.sample([ex for ex in chest_exercises if ex.exercise_type == "optional"], num_optional_exercises_per_group)

        selected_back_exercises = random.sample([ex for ex in back_exercises if ex.exercise_type == "core"], num_core_exercises_per_group)
        selected_back_exercises += random.sample([ex for ex in back_exercises if ex.exercise_type == "optional"], num_optional_exercises_per_group)

        for exercise in selected_leg_exercises + selected_chest_exercises + selected_back_exercises:
            plan.add_exercise(exercise)

        return plan

class WeekWorkoutPlanGenerator:
    @staticmethod
    def generate_week_fbw_plan(able_to_train_days_per_week):
        week_plan = {}
        daily_plan_generator = WorkoutPlanGenerator()
        
        for i, able_to_train in enumerate(able_to_train_days_per_week):
            if able_to_train:
                day_plan = daily_plan_generator.generate_fbw_plan()
                week_plan[f"Day {i+1}"] = day_plan
        
        return week_plan

if __name__ == "__main__":
    week_generator = WeekWorkoutPlanGenerator()
    # Example: True means training day, False means rest day
    able_to_train_days_per_week = [True, False, True, False, True, False, True]

    week_plan = week_generator.generate_week_fbw_plan(able_to_train_days_per_week)
    
    for day, plan in week_plan.items():
        print(f"{day}:")
        print(plan)
        print("\n" + "-"*30 + "\n")
