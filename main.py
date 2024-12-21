# pip install pandas
# pip install matplotlib
# pip install seaborn
# pip install plotly


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# загрузка данных
dataSet = pd.read_csv("visualization_comparison_data.csv")
dataSet['Date'] = pd.to_datetime(dataSet['Date'])  # преобразование даты

# matplotlib визуализации
def plotMatplotlib(dataSet):
    plt.figure(figsize=(16, 10))

    # Линейный график
    plt.subplot(3, 2, 1)
    plt.plot(dataSet['Date'], dataSet['Sales'], marker='o', linestyle='-', label='Sales', color='blue')
    plt.title("Matplotlib: линейный график продаж")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.xticks(rotation=45)
    plt.legend()

    # Гистограмма
    plt.subplot(3, 2, 2)
    plt.hist(dataSet['Profit'], bins=10, color='skyblue', edgecolor='black')
    plt.title("Matplotlib: гистограмма прибыли")
    plt.xlabel("Profit")
    plt.ylabel("Frequency")

    # Точечный график
    plt.subplot(3, 2, 3)
    colorMap = {'A': 'red', 'B': 'blue', 'C': 'green'}
    plt.scatter(dataSet['Sales'], dataSet['Profit'], c=dataSet['Category'].map(colorMap), label="Categories")
    plt.title("Matplotlib: точечный график")
    plt.xlabel("Sales")
    plt.ylabel("Profit")
    plt.legend(colorMap, title="Category")

    # Круговая диаграмма
    plt.subplot(3, 2, 4)
    category_counts = dataSet['Category'].value_counts()
    plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', colors=['red', 'blue', 'green'])
    plt.title("Matplotlib: круговая диаграмма категорий")

    # График с наложением нескольких серий
    plt.subplot(3, 2, 5)
    for category in dataSet['Category'].unique():
        subset = dataSet[dataSet['Category'] == category]
        plt.plot(subset['Date'], subset['Sales'], label=category)
    plt.title("Matplotlib: сравнение продаж по категориям")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.legend()

    plt.tight_layout()
    plt.show()

# seaborn визуализации
def plotSeaborn(dataSet):
    plt.figure(figsize=(16, 10))

    # Линейный график
    plt.subplot(3, 2, 1)
    sns.lineplot(data=dataSet, x='Date', y='Sales', marker='o', label='Sales')
    plt.title("Seaborn: линейный график продаж")
    plt.xticks(rotation=45)

    # Гистограмма
    plt.subplot(3, 2, 2)
    sns.histplot(dataSet['Profit'], kde=True, bins=10, color='purple')
    plt.title("Seaborn: гистограмма прибыли")

    # Точечный график
    plt.subplot(3, 2, 3)
    sns.scatterplot(data=dataSet, x='Sales', y='Profit', hue='Category', palette='deep', s=100)
    plt.title("Seaborn: точечный график")

    # Ящик с усами (Box Plot)
    plt.subplot(3, 2, 4)
    sns.boxplot(data=dataSet, x='Category', y='Sales', palette='pastel')
    plt.title("Seaborn: ящик с усами (Sales по категориям)")

    # Тепловая карта корреляции
    plt.subplot(3, 2, 5)
    correlation = dataSet[['Sales', 'Profit']].corr()
    sns.heatmap(correlation, annot=True, cmap='coolwarm')
    plt.title("Seaborn: тепловая карта корреляции")

    plt.tight_layout()
    plt.show()

# plotly визуализации
def plotPlotly(dataSet):
    # Линейный график
    figLinePlotly = px.line(dataSet, x='Date', y='Sales', title="Plotly: линейный график продаж")
    figLinePlotly.show()

    # Гистограмма
    figHistPlotly = px.histogram(dataSet, x='Profit', nbins=10, title="Plotly: гистограмма прибыли", color_discrete_sequence=['orange'])
    figHistPlotly.show()

    # Точечный график
    figScatterPlotly = px.scatter(dataSet, x='Sales', y='Profit', color='Category', size='Profit',
                                  title="Plotly: точечный график", hover_data=['Category'])
    figScatterPlotly.show()

    # Сложная круговая диаграмма
    figPiePlotly = px.pie(dataSet, names='Category', values='Sales', title="Plotly: круговая диаграмма категорий")
    figPiePlotly.show()

    # Линейный график с анимацией
    figAnimatedLinePlotly = px.line(dataSet, x='Date', y='Sales', color='Category', line_group='Category',
                                    title="Plotly: анимация продаж по категориям", markers=True)
    figAnimatedLinePlotly.show()

# вызов функций
plotMatplotlib(dataSet)
plotSeaborn(dataSet)
plotPlotly(dataSet)
