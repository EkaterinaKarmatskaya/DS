import pandas as pd

df = pd.read_csv("data.csv")

# Фильтрация данных  по нужным типам "basic sale", "fast sale", "quick sale"
types_to_include = ["basic sale", "fast sale", "quick sale"]
df_filtered = df[df["type"].isin(types_to_include)]

# Сгруппировать по дате и посчитать сумму amount
result_df = df_filtered.groupby("payment_date")["amount"].sum().reset_index()

# Переименовать столбец в "volume"
result_df.rename(columns={"amount": "volume"}, inplace=True)

# Добавление индекса
df = df.sort_values("payment_date").reset_index(drop=True)

# Выводим результат
print(result_df)
print("Количество уникальных строк:", len(result_df))

# Проверка наличия пропусков дат, если даты идут последовательно, то ОК,
result_df["payment_date"] = pd.to_datetime(result_df["payment_date"], format="%Y-%m-%d")

print("Пробелы в диапазонах дат:", (result_df.payment_date - result_df.payment_date.shift(1)).mean())

# Если есть пропуски дат, то нужно заполнить. Создание диапазона дат без пробелов:
date_range = pd.date_range(
    start=result_df.payment_date.min(), end=result_df.payment_date.max(), freq="D"
)

print("Создано уникальных строк без пропуска даты:", len(date_range))

# Создание пустого датафрейма без пропуска дат, где ключ payment_date из исходного датафрейма и их объединение
df_date_range = pd.DataFrame({"payment_date": date_range})
df_full = pd.merge(df_date_range, result_df, how="left", on="payment_date")

# Замена всех нулевых значений в итоговом датафрейме на True
df_full.fillna(0, inplace=True)

# Выгрузка датафрейма в CSV для дальнейшей с ним работы
df_full.to_csv('df_full.csv')
