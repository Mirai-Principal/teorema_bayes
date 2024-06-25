emails = {
    "hola": "spam",
    "descuento": "spam",
    "oferta": "not spam",
    "aprende": "not spam",
    "registrate": "spam",
    "promocion": "spam",
    "curso": "not spam",
    "educacion": "not spam",
    "programa": "spam",
    "precio": "spam",
}

# Contar la cantidad de correos spam y no spam
spam_count = sum(1 for email in emails.values() if email == "spam")
not_spam_count = sum(1 for email in emails.values() if email == "not spam")
total_emails = len(emails)

#probabilidades a priori
# Calcular P(spam) y P(not spam)
P_spam = spam_count / total_emails
P_not_spam = not_spam_count / total_emails

#probabilidades condicionale
# Calcular P(hola | spam) y P(hola | not spam)
P_hola_given_spam = sum(1 for email, label in emails.items() if email == "hola" and label == "spam") / spam_count
P_hola_given_not_spam = sum(1 for email, label in emails.items() if email == "hola" and label == "not spam") / not_spam_count

# Calcular P(hola)
P_hola = P_hola_given_spam * P_spam + P_hola_given_not_spam * P_not_spam

# Calcular P(spam | hola) usando el teorema de Bayes
P_spam_given_hola = (P_hola_given_spam * P_spam) / P_hola

# Mostrar resultados
print(f"P(spam): {P_spam}")
print(f"P(not spam): {P_not_spam}")
print(f"P(hola | spam): {P_hola_given_spam}")
print(f"P(hola | not spam): {P_hola_given_not_spam}")
print(f"P(hola): {P_hola}")
print(f"P(spam | hola): {P_spam_given_hola}")
