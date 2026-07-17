# Nombre del estudiante: HELVER ANDRES AYA GALEANO
# Grupo: 213022A_2202
# Programa: Ingeniería de Sistemas
# Código Fuente: autoría propia

#Se declaran las variables constantes: se elige la categoria "Bebidas" y el precio limite para la promoción es de $10000
desc = 0.15
cat_prom = "Bebidas"
prec_lim = 10000

#Se crea el arreglo con 6 productos
menu = [
    ["Hamburguesa", "Comidas", 18000],
    ["Pizza", "Comidas", 22000],
    ["Jugo Natural", "Bebidas", 12000],
    ["Gaseosa", "Bebidas", 8000],
    ["Helado", "Postres", 9000],
    ["Café", "Bebidas", 15000]
]

#Se programa la función (módulo) que calcula la aplicación del descuento con base en las condiciones: categoría y precio límite definidos
def calcular_precio_final(cat, prec_bas):
    
    if cat == cat_prom and prec_bas > prec_lim:
        prec_fin = prec_bas - (prec_bas * desc)
    else:
        prec_fin = prec_bas

    return prec_fin


def mostrar_menu():
    print("MENÚ DEL RESTAURANTE")
    print("********************")
    print("")

    for prod in menu:
        nom_prod = prod[0]
        cat_prod = prod[1]
        prec_base_prod = prod[2]

        prec_fin = calcular_precio_final(cat_prod, prec_base_prod)

        print(f"{nom_prod:12} {cat_prod:12} ${prec_base_prod:8,.0f} ${prec_fin:8,.0f}")

    print("")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Promoción del 15% de descuento en la categoría de",cat_prom)
    print("La promoción aplica para productos con precio mayor a $",prec_lim)

mostrar_menu()