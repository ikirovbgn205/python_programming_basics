CHICKEN_MENU_PRICE = 10.35
FISH_MENU_PRICE = 12.40
VEG_MENU_PRICE = 8.15

chicken_menu = int(input())
fish_menu = int(input())
veg_menu = int(input())
all_menu_price = (chicken_menu * CHICKEN_MENU_PRICE
                  + fish_menu * FISH_MENU_PRICE +
                  veg_menu * VEG_MENU_PRICE)
desert_price = all_menu_price * 0.20
delivery_price = 2.50

final_price = all_menu_price + desert_price + delivery_price

print(final_price)
