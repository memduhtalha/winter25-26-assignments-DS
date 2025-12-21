import numpy as np
import pandas as pd

# Teil 1

product_ids = np.arange(1001, 1011)

inventory_data = np.array([
    [50, 15.5, 10.99],
    [120, 3.2, 50.50],
    [30, 25.0, 5.00],
    [10, 5.0, 12.00],
    [200, 10.0, 3.50],
    [5, 2.0, 100.00],
    [80, 20.0, 7.50],
    [15, 8.0, 20.00],
    [60, 12.0, 9.99],
    [300, 40.0, 2.50]
])

print("Shape ist:", inventory_data.shape)
print("Data type ist:", inventory_data.dtype)

# total value berechnen
total_value = inventory_data[:, 0] * inventory_data[:, 2] #Durch spalten zugriff auf current_stock und unit_cost 
print("\nGesamtwert ist:", total_value)

print("\nAusschnitt ist:", inventory_data[3:8])

# Durchschnitt Verkäufe
schnitt = np.mean(inventory_data[:, 1])
print("\nDurchschnitt:", schnitt)

# Kosten erstes Produkt
print("Kosten:", inventory_data[0, 2])


# Teil 2

# 1.
reichweite = inventory_data[:, 0] / inventory_data[:, 1]
maske = reichweite < 4

print("\nKritische Produkte:", inventory_data[maske])

# 2.
# Nachbestellung berechnen
reorder_quantity = (4 * inventory_data[:, 1]) - inventory_data[:, 0]
reorder_quantity = np.maximum(reorder_quantity, 0)
reorder_quantity = reorder_quantity.reshape(10, 1)

# zusammenfügen
daten = np.concatenate((inventory_data, reorder_quantity), axis=1)
print("\nNeu:", daten)


# Teil 3

# 1.
tabelle = pd.DataFrame(daten, columns=['Stock', 'Sales', 'Cost', 'Reorder Qty'])

# 2.
print("\nSpaltenwahl")
print(tabelle[['Stock', 'Reorder Qty']])

print("\nErste 5:")
print(tabelle.head(5))