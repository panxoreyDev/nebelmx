from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    
    csv_file_path = r"C:\Users\MXRodrigEl1\Desktop\Nestlé\Nivel de Servicio\PLEYADES\OTR.csv"
        
    #LEE EL FILE CSV DE LA CARPETA ANTES PROPORCIONADA EN FILEPATH                                      
    csv_file =  pd.read_csv(csv_file_path, 
                                 sep=',', 
                                 encoding='latin',
                                 header=0,
                                 index_col=False,
                                 low_memory=False
                                 )
    
    # Leer los dataframes desde archivos CSV o desde una base de datos
    inventario_df = csv_file
    forecast_df = csv_file
    ventas_df = csv_file

    # Convertir los dataframes a una lista de listas
    inventario = inventario_df.values.tolist()
    forecast = forecast_df.values.tolist()
    ventas = ventas_df.values.tolist()

    # Renderizar la plantilla HTML y pasar los datos de los dataframes como argumentos
    return render_template('template.html', inventario=inventario, forecast=forecast, ventas=ventas)

if __name__ == '__main__':
    app.run(debug=True)
