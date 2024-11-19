import matplotlib.pyplot as plt
import pandas as pd


def create_and_save_plot(data, ticker, period, filename=None):
    plt.figure(figsize=(10, 6))

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')

    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")


def calculate_and_display_average_price(data):
    """
    Вычисляет среднее значение цены закрытия ('Close') из переданных данных
    и выводит его в консоль.

    Параметры:
    data (pandas.DataFrame): Данные о ценах акций, которые должны содержать колонку 'Close'.

    Возвращает:
    None: Функция выводит среднее значение цены закрытия в консоль.

    Если колонка 'Close' отсутствует в данных, функция выведет сообщение об ошибке.
    """
    # Проверяем, есть ли колонка 'Close' в данных
    if 'Close' not in data:
        print("Колонка 'Close' отсутствует в данных.")
        return

    # Вычисляем среднее значение колонки 'Close'
    average_price = data['Close'].mean()

    # Выводим результат в консоль
    print(f"Среднее значение цены закрытия: {average_price:.2f}")