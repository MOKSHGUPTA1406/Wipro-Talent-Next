import os

def main():
    filename = input("Enter the file name: ")
    if not filename.endswith('.txt') and not os.path.exists(filename):
        filename += '.txt'
        
    items_purchased = 0
    free_items = 0
    amount_to_pay = 0
    discount_given = 0
    
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line == '(blank line)':
                    continue
                    
                parts = line.split()
                if len(parts) >= 2:
                    item = " ".join(parts[:-1])
                    price_str = parts[-1]
                    
                    if item.lower() == 'discount':
                        try:
                            discount_given = int(price_str)
                        except ValueError:
                            pass
                    else:
                        if price_str.lower() == 'free':
                            free_items += 1
                            items_purchased += 1
                        else:
                            try:
                                price = int(price_str)
                                items_purchased += 1
                                amount_to_pay += price
                            except ValueError:
                                pass
                                
        final_amount = amount_to_pay - discount_given
        
        print(f"No of items purchased: {items_purchased}")
        print(f"No of free items: {free_items}")
        print(f"Amount to pay: {amount_to_pay}")
        print(f"Discount given: {discount_given}")
        print(f"Final amount paid: {final_amount}")
        
    except FileNotFoundError:
        print("Error: The specified file does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
