import cs1400.labs.bookstore.validation as validation, cs1400.labs.bookstore.formatting as formatting, random, json

items = {}
low_stock_items = []

def init_inventory():
    global items, low_stock_items
    try:
        with open("items.json", "r+") as items_json:
            content = items_json.read()
            if not content: save_inventory(); return

            json_decoded_content = json.loads(content)
            items = json_decoded_content["items"]
            low_stock_items = json_decoded_content["low_stock_items"]
    except Exception as e:
        pass # print(formatting.warning(e))

def save_inventory():
    with open("items.json", "w") as items_json:
        content_to_save = {"items": items, "low_stock_items": low_stock_items}
        items_json.write(json.dumps(content_to_save, indent="\t"))

def get_category_prompt():
    prompt_text = "Please enter one of the following categories ("
    for category in sorted(validation.categories):
        prompt_text += category + ", "
    prompt_text = prompt_text[:-2] + "): "

    return prompt_text

def add():
    formatting.display_header("Adding Item")
    item_name = validation.get_valid_input("What is the name of the item you would like to add: ").title()
    item_category = validation.get_valid_input(get_category_prompt(), str, validation._validate_category).lower()
    price = validation.get_valid_input(f"What is the price per item: {formatting.BOLD}{formatting.UL}{formatting.GREEN}$", float, validation._validate_above_zero, "price")
    quantity = validation.get_valid_input("What is the current stock of the product: ", int, validation._validate_above_zero, "quantity")

    # add the item
    item_id = ""
    while item_id in items or not item_id:
        item_id = f"{item_category[:3].lower()}_{item_name[:3].lower()}_{random.randint(0, 999):03d}"

    items[item_id] = (item_name, item_category, price, quantity)
    if quantity < 5: low_stock_items.append(item_id)
    print(f"{formatting.BOLD}Added item {formatting.YELLOW}'{item_name}'{formatting.RESET + formatting.BOLD} to items!{formatting.RESET}")

def catalogue():
    formatting.display_header("Catalogue")
    if len(items) > 0: print("Items: ")
    else: print(f"{formatting.YELLOW}No items added yet.{formatting.RESET}")
    for id, item in items.items():
        print(f"• {formatting.BOLD}{id}{formatting.RESET}", get_product_info(item))

def format_list(list_to_format):
    output_list = ""
    for item in list_to_format:
        output_list += str(item) + ", "
    return output_list[:-2]

def get_product_info(item):
    return f"('{item[0]}' | {item[1].title()} | {formatting.money(item[2])} | qty: {item[3]})"

def report():
    formatting.display_header("Inventory Report")
    print(f"• {formatting.BOLD}Total count of products:{formatting.RESET} {len(items)}")
    print(f"• {formatting.BOLD}Categories:{formatting.RESET}", format_list(validation.categories))
    print(f"• {formatting.BOLD}Low stock items:{formatting.RESET}", format_list(low_stock_items))

    sum = 0
    for item in items.values():
        sum += (item[2] * item[3])
    print(f"• {formatting.BOLD}Total value of items: {formatting.money(sum)}")

def search():
    formatting.display_header("Searching Catalogue")
    query = validation.get_valid_input("What would you like to search for: ", str, None)
    if not query: raise Exception("No results found for empty query.")

    if query in items:
        print(f"\nExact Match: \n• {formatting.BOLD}{query}{formatting.RESET} {get_product_info(items[query])}")
    
    for key, item in items.items():
       if not query in key: continue
       if not query in items: print("\nPartial Matches: ")
       break
    else: raise Exception(f"{formatting.YELLOW}No results found matching query '{query}'.{formatting.RESET}")

    for key, item in items.items():
        if query in items or not query in key: continue

        # highlight query in output
        chars = list(key)
        query_start_index = key.find(query)
        chars.insert(query_start_index, formatting.BOLD)
        chars.insert(query_start_index + len(query) + 1, formatting.RESET)
        print("•", ("").join(chars), get_product_info(item))