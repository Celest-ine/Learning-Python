import printing_functions

"""Import another module to use its functions."""

unprinted_designs = ['phone case', 'robot pendant','dedecahedron']
completed_models = []

printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)