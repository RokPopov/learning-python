"""Interesting Facts
Try to create a dictionary that has a listing of people and includes one interesting fact about each of them. Display
each person and their interesting fact on the screen. From there, alter a fact about one of the people on the list.
Also, add an extra person and corresponding fact to the list. Display the newly created list of people and facts.
Try running the program multiple times and take note of whether the order changes."""

fun_facts = {
    "Jeff": "Was born in France.",
    "David": "Was a mascot in college.",
    "Ana": "Has arachnophobia."
}

def display_fun_facts(fun_facts):
    for fact in fun_facts:
        print("{0}: {1}".format(fact, fun_facts[fact]))


display_fun_facts(fun_facts)

fun_facts["David"] = "Can't juggle."
fun_facts["Mirza"] = "Can dunk."
fun_facts["Ana"] = "Can run fast."

display_fun_facts(fun_facts)