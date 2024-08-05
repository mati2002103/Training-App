class Exercise:
    def __init__(self, name, muscle_group, sets, reps):
        self.name = name
        self.muscle_group = muscle_group
        self.sets = sets
        self.reps = reps

    def __str__(self):
        return f"{self.name} - {self.sets}x{self.reps} ({self.muscle_group})"


class LegsExercise(Exercise):
    def __init__(self, name, sets, reps, exercise_type="core"):
        super().__init__(name, "Legs", sets, reps)
        self.exercise_type = exercise_type


class ChestExercise(Exercise):
    def __init__(self, name, sets, reps, exercise_type="core"):
        super().__init__(name, "Chest", sets, reps)
        self.exercise_type = exercise_type


class BackExercise(Exercise):
    def __init__(self, name, sets, reps, exercise_type="core"):
        super().__init__(name, "Back", sets, reps)
        self.exercise_type = exercise_type


class WorkoutPlan:
    def __init__(self, name):
        self.name = name
        self.exercises = []

    def add_exercise(self, exercise):
        self.exercises.append(exercise)

    def __str__(self):
        plan = f"Workout Plan: {self.name}\n"
        plan += "\n".join(str(exercise) for exercise in self.exercises)
        return plan
