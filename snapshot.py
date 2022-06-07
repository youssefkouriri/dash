from dash import Dash, dash_table
import pandas as pd






youssef = ['status', 'wallc-locktime','hostname', 'cpu' ,  'optimalcpu', 'CUSTOM_KPI-No._of_Flops', 'mem', 'power']



app = Dash(__name__)

app.layout = dash_table.DataTable( 
    columns= [{"name": i, "id": i} for i in youssef]

)

if __name__ == '__main__':
    app.run_server(debug=True, port=8003)