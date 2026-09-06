import cs1400.labs.bookstore.formatting as formatting, typing

categories = {"apparel", "books", "dorm", "electronics", "merch", "snacks", "supplies"}

def _default_validate(user_input: str, casted_input, input_name: str):
    if not casted_input: raise Exception("Entered value must have content!")

def _validate_category(user_input: str, casted_input, input_name: str):
    if user_input.lower() in categories: return
    for category in categories: 
        if category.startswith(user_input): raise Exception(f"Category not found: '{user_input}'. Did you mean '{category}'?")
    raise Exception(f"Category not found: '{user_input}'")  

def _validate_above_zero(user_input: str, casted_input, input_name: str):
    if casted_input < 0: raise Exception(f"{input_name.title()} must be above zero!")

def get_valid_input(prompt: str = "", data_type: typing.Callable = str, validate = _default_validate, input_name = "Input"):
    while True:
        user_input = input(prompt + formatting.BOLD).strip()
        print(formatting.RESET, end="")
        try:
            casted_input = data_type(user_input)
            if validate: validate(user_input, casted_input, input_name)

            return casted_input
        except ValueError as e:
            print(formatting.warning(f"Entered value must be an {data_type.__name__}!"))
        except Exception as e:
            print(formatting.warning(e))