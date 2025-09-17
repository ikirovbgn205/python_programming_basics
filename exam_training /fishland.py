SHELLS = 7.50

price_mackerel_per_kg= float(input())
price_spart_per_kg = float(input())
kg_bonito = float(input())
kg_horse_mackerel = float(input())
kg_shells = int(input())

price_bonito = price_mackerel_per_kg + (price_mackerel_per_kg * 0.60)
final_price_bonito = kg_bonito * price_bonito

price_horse_mackerel = price_spart_per_kg + (price_spart_per_kg * 0.80)
final_price_horse_mackerel = kg_horse_mackerel * price_horse_mackerel

final_price_shells = kg_shells * SHELLS

bill = final_price_bonito + final_price_horse_mackerel + final_price_shells

print(f"{bill:.2f}")
