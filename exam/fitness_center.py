customers = int(input())

back = 0
chest = 0
legs = 0
stomach = 0
protein_shake = 0
protein_bar = 0

for _ in range(customers):
    customer_target = str(input())

    if customer_target == 'Back':
        back += 1
    elif customer_target == 'Chest':
        chest += 1
    elif customer_target == 'Legs':
        legs += 1
    elif customer_target == 'Abs':
        stomach += 1
    elif customer_target == 'Protein shake':
        protein_shake += 1
    elif customer_target == 'Protein bar':
        protein_bar += 1

training_customers = back + chest + legs + stomach
percent_training = training_customers / customers * 100
protein_customers = protein_shake + protein_bar
percent_protein = protein_customers / customers * 100

print(f'{back} - back')
print(f'{chest} - chest')
print(f'{legs} - legs')
print(f'{stomach} - abs')
print(f'{protein_shake} - protein shake')
print(f'{protein_bar} - protein bar')
print(f'{percent_training:.2f}% - work out')
print(f'{percent_protein:.2f}% - protein')