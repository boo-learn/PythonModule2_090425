# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"

text = "Такая, дети, мораль, прости, господи."
komma_num = text.count(",")
punkt_num = text.count(".")

if komma_num > punkt_num :
    print("Запятых больше")

elif punkt_num > komma_num :
    print("Точек больше")

else :
    print("Одинаково")
