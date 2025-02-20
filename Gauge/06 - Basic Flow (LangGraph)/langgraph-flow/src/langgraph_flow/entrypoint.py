# def check_entrypoint(func):
#     def wrapper(input):
#         print("Checking Entrypoint", input)
#         return func(input)
#     return wrapper

# # @check_entrypoint
# def print_output(input):
#     print("Output From The Workflow", input)

# # print_output("Hello From Function")
# check_entrypoint(print_output)("| Hello From Function")