goal=26000
user_points=0
print("You need 26000 points to move on to the next phase. Get 26000 points as fast as you can by helping clients out.")
problem_one="I'm trying to generate a comic about a superhero fighting a supervillian. But in some panels, they look like scribbles. What should I do?"
problem_two="I just need suggestions for password pretty please."
problem_three="Can you write pseudocode in Python for solving exponents?"
problem_foue="I think my account has been logged into by someone else. My password should still be 270098. If it's not, my account was logged into by someone else. Can you check this for me and make sure my account is safe?"
points_for_a_problem_solved=goal/4
for progress_until_goal_met in range(4):
    current_problem=random.randint(problem_one, problem_two, problem_three, problem_four)
    print(current_problem)
    user_help_suggestion=input("")