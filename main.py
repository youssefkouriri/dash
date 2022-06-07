from turtle import color
from dash import Dash, dash_table, dcc, html, Input, Output, callback
from numpy import empty, maximum, minimum
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import  html
from dash.dash_table import DataTable, FormatTemplate
from dash.dash_table.Format import Sign
import plotly.express as px


percentage = FormatTemplate.percentage(2).sign(Sign.positive)

koora = [{"name": ["", "Design-testname"], "id": "Design-testnameVersionA"}]
youssef = ['status', 'wallc-locktime','hostname', 'cpu' ,  'optimalcpu', 'CUSTOM_KPI-No._of_Flops', 'mem', 'power']

cpu_stage = ['status','cpu','optimalcpu']
stage2 = ['status','wallc-locktime','CUSTOM_KPI-No._of_Flops']
stage3 = ['status','mem','power']

minimum = -0.01
maximum = 0.01
completionRate1 = 50
completionRate2 = 60
for i in youssef:
    if i == "status" or i =="hostname":
       koora.append({"name": [i, "versionA"], "id": i+"VersionA", "hideable": True})
       koora.append({"name": [i, "versionB"], "id": i+"VersionB", "hideable": True})
       #koora.append({"name": [i, "diff"], "id": i+"diff"})
    else:
       koora.append({"name": [i, "versionA"], "id": i+"VersionA", "hideable": True})
       koora.append({"name": [i, "versionB"], "id": i+"VersionB", "hideable": True})
       #koora.append({"name": [i, "diff"], "id": i+"diff"})
       koora.append(dict(id=i+"diff", name=[i, "diff"], type='numeric', format=percentage))

all_columns = ['statusVersionA', 'wallc-locktimeVersionA', 'hostnameVersionA', 'cpuVersionA', 'optimalcpuVersionA', 'CUSTOM_KPI-No._of_FlopsVersionA', 'Design-testnameVersionA', 'statusVersionB', 'wallc-locktimeVersionB', 'hostnameVersionB', 'cpuVersionB', 'optimalcpuVersionB', 'CUSTOM_KPI-No._of_FlopsVersionB', 'statusdiff', 'wallc-locktimediff', 'hostnamediff', 'cpudiff', 'optimalcpudiff', 'CUSTOM_KPI-No._of_Flopsdiff', 'statusVersionA', 'wallc-locktimeVersionA', 'hostnameVersionA', 'cpuVersionA', 'optimalcpuVersionA', 'CUSTOM_KPI-No._of_FlopsVersionA', 'Design-testnameVersionA', 'statusVersionB', 'wallc-locktimeVersionB', 'hostnameVersionB', 'cpuVersionB', 'optimalcpuVersionB', 'CUSTOM_KPI-No._of_FlopsVersionB', 'statusdiff', 'wallc-locktimediff', 'hostnamediff', 'cpudiff', 'optimalcpudiff', 'CUSTOM_KPI-No._of_Flopsdiff', 'statusVersionA', 'wallc-locktimeVersionA', 'hostnameVersionA', 'cpuVersionA', 'optimalcpuVersionA', 'CUSTOM_KPI-No._of_FlopsVersionA', 'memVersionA', 'Design-testnameVersionA', 'statusVersionB', 'wallc-locktimeVersionB', 'hostnameVersionB', 'cpuVersionB', 'optimalcpuVersionB', 'CUSTOM_KPI-No._of_FlopsVersionB', 'memVersionB', 'statusdiff', 'wallc-locktimediff', 'hostnamediff', 'cpudiff', 'optimalcpudiff', 'CUSTOM_KPI-No._of_Flopsdiff', 'memdiff', 'statusVersionA', 'wallc-locktimeVersionA', 'hostnameVersionA', 'cpuVersionA', 'optimalcpuVersionA', 'CUSTOM_KPI-No._of_FlopsVersionA', 'powerVersionA', 'Design-testnameVersionA', 'statusVersionB', 'wallc-locktimeVersionB', 'hostnameVersionB', 'cpuVersionB', 'optimalcpuVersionB', 'CUSTOM_KPI-No._of_FlopsVersionB', 'powerVersionB', 'statusdiff', 'wallc-locktimediff', 'hostnamediff', 'cpudiff', 'optimalcpudiff', 'CUSTOM_KPI-No._of_Flopsdiff', 'powerdiff', 'statusVersionA', 'wallc-locktimeVersionA', 'hostnameVersionA', 'cpuVersionA', 'optimalcpuVersionA', 'CUSTOM_KPI-No._of_FlopsVersionA', 'Design-testnameVersionA', 'statusVersionB', 'wallc-locktimeVersionB', 'hostnameVersionB', 'cpuVersionB', 'optimalcpuVersionB', 'CUSTOM_KPI-No._of_FlopsVersionB', 'statusdiff', 'wallc-locktimediff', 'hostnamediff', 'cpudiff', 'optimalcpudiff', 'CUSTOM_KPI-No._of_Flopsdiff', 'statusVersionA', 'wallc-locktimeVersionA', 'hostnameVersionA', 'cpuVersionA', 'optimalcpuVersionA', 'CUSTOM_KPI-No._of_FlopsVersionA', 'Design-testnameVersionA']
diff_headers = ['wallc-locktimediff', 'cpudiff', 'optimalcpudiff', 'CUSTOM_KPI-No._of_Flopsdiff', 'wallc-locktimediff', 'cpudiff', 'optimalcpudiff', 'CUSTOM_KPI-No._of_Flopsdiff', 'wallc-locktimediff', 'cpudiff', 'optimalcpudiff', 'CUSTOM_KPI-No._of_Flopsdiff', 'memdiff', 'wallc-locktimediff', 'cpudiff', 'optimalcpudiff', 'CUSTOM_KPI-No._of_Flopsdiff', 'powerdiff', 'wallc-locktimediff', 'cpudiff', 'optimalcpudiff', 'CUSTOM_KPI-No._of_Flopsdiff']

records = [{'statusVersionA': 'FAIL', 'wallc-locktimeVersionA': 542.0, 'hostnameVersionA': 'svr-inn-clpqor-32.inn.mentorg.com', 'cpuVersionA': 432.0, 'optimalcpuVersionA': 432.0, 'CUSTOM_KPI-No._of_FlopsVersionA': 159439.0, 'Design-testnameVersionA': '/powerpro/tests/main/qa_repository/shasta_qor/testcases/ati/pa_data/ati_tcc0.1_prob0.4.def high SKIP_VISA', 
'statusVersionB': 'PASS', 'wallc-locktimeVersionB': 530.0, 'hostnameVersionB': 'svr-inn-clpqor-32.inn.mentorg.com', 'cpuVersionB': 450.0, 'optimalcpuVersionB': 430.0, 'CUSTOM_KPI-No._of_FlopsVersionB': 159430.0, 'statusdiff': '', 'wallc-locktimediff': 0.0226, 'hostnamediff': '', 'cpudiff': -0.04, 'optimalcpudiff': 0.0047, 'CUSTOM_KPI-No._of_Flopsdiff': 0.0001}, {'statusVersionA': 'PASS', 'wallc-locktimeVersionA': 642.0, 'hostnameVersionA': 'svr-inn-clpqor-32.inn.mentorg.com', 'cpuVersionA': 332.0, 'optimalcpuVersionA': 
332.0, 'CUSTOM_KPI-No._of_FlopsVersionA': 259439.0, 'Design-testnameVersionA': '/powerpro/tests/main/qa_repository/shasta_qor/testcases/ati/pa_data/ati_cg_pa_rc_integrated.def high SKIP_VISB', 'statusVersionB': 'FAIL', 'wallc-locktimeVersionB': 647.0, 'hostnameVersionB': 'svr-inn-clpqor-32.inn.mentorg.com', 'cpuVersionB': 339.0, 'optimalcpuVersionB': 320.0, 'CUSTOM_KPI-No._of_FlopsVersionB': 259410.0, 'statusdiff': '', 'wallc-locktimediff': -0.0077, 'hostnamediff': '', 'cpudiff': -0.0206, 'optimalcpudiff': 0.0375, 'CUSTOM_KPI-No._of_Flopsdiff': 0.0001}, {'statusVersionA': 'PASS', 'wallc-locktimeVersionA': 742.0, 'hostnameVersionA': 'svr-inn-clpqor-32.inn.mentorg.com', 'cpuVersionA': 232.0, 'optimalcpuVersionA': 232.0, 'CUSTOM_KPI-No._of_FlopsVersionA': 359439.0, 'memVersionA': 200.0, 'Design-testnameVersionA': '/powerpro/tests/main/qa_repository/shasta_qor/testcases/Ipars/Ipars.def high SKIP_VISC', 'statusVersionB': 'PASS', 'wallc-locktimeVersionB': 749.0, 'hostnameVersionB': 'svr-inn-clpqor-32.inn.mentorg.com', 'cpuVersionB': 132.0, 
'optimalcpuVersionB': 332.0, 'CUSTOM_KPI-No._of_FlopsVersionB': 359430.0, 'memVersionB': 250.0, 'statusdiff': '', 'wallc-locktimediff': -0.0093, 'hostnamediff': '', 'cpudiff': 0.7576, 'optimalcpudiff': -0.3012, 'CUSTOM_KPI-No._of_Flopsdiff': 0.0, 'memdiff': -0.2}, {'statusVersionA': 'PASS', 'wallc-locktimeVersionA': 842.0, 'hostnameVersionA': 'svr-inn-clpqor-32.inn.mentorg.com', 'cpuVersionA': 132.0, 'optimalcpuVersionA': 132.0, 'CUSTOM_KPI-No._of_FlopsVersionA': 459439.0, 'powerVersionA': 300.0, 'Design-testnameVersionA': '/powerpro/tests/main/qa_repository/shasta_qor/testcases/Ipars/Ipars.def high SKIP_VISD', 'statusVersionB': 'PASS', 'wallc-locktimeVersionB': 842.0, 'hostnameVersionB': 'svr-inn-clpqor-32.inn.mentorg.com', 'cpuVersionB': 130.0, 'optimalcpuVersionB': 133.0, 'CUSTOM_KPI-No._of_FlopsVersionB': 459440.0, 'powerVersionB': 310.0, 'statusdiff': '', 'wallc-locktimediff': 0.0, 'hostnamediff': '', 'cpudiff': 0.0154, 'optimalcpudiff': -0.0075, 'CUSTOM_KPI-No._of_Flopsdiff': -0.0, 'powerdiff': -0.0323}, {'statusVersionA': 'FAIL', 'wallc-locktimeVersionA': 942.0, 'hostnameVersionA': 'svr-inn-clpqor-32.inn.mentorg.com', 'cpuVersionA': 532.0, 'optimalcpuVersionA': 532.0, 'CUSTOM_KPI-No._of_FlopsVersionA': 559439.0, 'Design-testnameVersionA': '/powerpro/tests/main/qa_repository/shasta_qor/testcases/Ipars/Ipars.def high SKIP_VISE', 'statusVersionB': 'FAIL', 'wallc-locktimeVersionB': 942.0, 'hostnameVersionB': 'svr-inn-clpqor-32.inn.mentorg.com', 'cpuVersionB': 539.0, 'optimalcpuVersionB': 531.0, 'CUSTOM_KPI-No._of_FlopsVersionB': 559439.0, 'statusdiff': '', 'wallc-locktimediff': 0.0, 'hostnamediff': '', 'cpudiff': -0.013, 'optimalcpudiff': 0.0019, 'CUSTOM_KPI-No._of_Flopsdiff': 0.0}, {'statusVersionA': 'FAIL', 'wallc-locktimeVersionA': 942.0, 'hostnameVersionA': 'svr-inn-clpqor-32.inn.mentorg.com', 'cpuVersionA': 532.0, 'optimalcpuVersionA': 532.0, 'CUSTOM_KPI-No._of_FlopsVersionA': 559439.0, 'Design-testnameVersionA': '/powerpro/tests/main/qa_repository/shasta_qor/testcases/Ipars/Ipars.def high SKIP_VISF'}]  

designs=[]
for dict1 in records:
    for key in dict1:
        if key =='Design-testnameVersionA':
            designs.append(dict1[key])

def implement_headers(headers):
  table_final = [{"name": ["", "Design-testname"], "id": "Design-testnameVersionA"}]
  for i in headers:
    if i == "status" or i =="hostname":
       table_final.append({"name": [i, "versionA"], "id": i+"VersionA", "hideable": True})
       table_final.append({"name": [i, "versionB"], "id": i+"VersionB", "hideable": True})
       #koora.append({"name": [i, "diff"], "id": i+"diff"})
    else:
       table_final.append({"name": [i, "versionA"], "id": i+"VersionA", "hideable": True})
       table_final.append({"name": [i, "versionB"], "id": i+"VersionB", "hideable": True})
       #table_final.append({"name": [i, "diff"], "id": i+"diff", 'format': "percentage"})
       table_final.append(dict(id=i+"diff", name=[i, "diff"], type='numeric', format=percentage))
  return table_final      
#print(implement_headers(cpu_stage))


def show_degradation(num,records):
    table = []
    dic1 = {}
    for dict in records:
        for key in dict:
            if key.endswith("diff"):
                try:
                   if dict[key] >= num:
                        dic1.update({"Design-testnameVersionA":dict["Design-testnameVersionA"]})
                        dic1.update({"statusVersionA":dict["statusVersionA"]})
                        dic1.update({"statusVersionB":dict["statusVersionB"]})
                        dic1.update({key.replace("diff","VersionA"): dict[key.replace("diff","VersionA")]})
                        dic1.update({key.replace("diff","VersionB"): dict[key.replace("diff","VersionB")]})
                        dic1.update({key:dict[key]})
                        table.append(dic1)
                        dic1 ={}
                        
                    
                          
                except:
                    continue        

                        
    return  pd.DataFrame(table)

def show_improvement(num,records):
    table = []
    dic1 = {}
    for dict in records:
        for key in dict:
            if key.endswith("diff"):
                try:
                   if dict[key] <= num:
                        dic1.update({"Design-testnameVersionA":dict["Design-testnameVersionA"]})
                        dic1.update({"statusVersionA":dict["statusVersionA"]})
                        dic1.update({"statusVersionB":dict["statusVersionB"]})
                        dic1.update({key.replace("diff","VersionA"): dict[key.replace("diff","VersionA")]})
                        dic1.update({key.replace("diff","VersionB"): dict[key.replace("diff","VersionB")]})
                        dic1.update({key:dict[key]})
                        table.append(dic1)
                        dic1 ={}
                        
                    
                          
                except:
                    continue        

                        
    return  pd.DataFrame(table) 

def show_range(min,max,records):
    table = []
    dic1 = {}
    for dict in records:
        for key in dict:
            if key.endswith("diff"):
                try:
                   if dict[key] < max and dict[key]> min:
                        dic1.update({"Design-testnameVersionA":dict["Design-testnameVersionA"]})
                        dic1.update({"statusVersionA":dict["statusVersionA"]})
                        dic1.update({"statusVersionB":dict["statusVersionB"]})
                        dic1.update({key.replace("diff","VersionA"): dict[key.replace("diff","VersionA")]})
                        dic1.update({key.replace("diff","VersionB"): dict[key.replace("diff","VersionB")]})
                        dic1.update({key:dict[key]})
                        table.append(dic1)
                        dic1 ={}
                        
                         
                    
                          
                except:
                    continue        

                        
    return  pd.DataFrame(table)                                 
#print(show_range(-0.4,-0.05,records))


    
 
#dff = pd.DataFrame(records) 
#dff = dff[dff["statusVersionA"]== 'FAIL']           
#print(dff)
#print(pd.DataFrame(records)["Design-testnameVersionA"]== '/powerpro/tests/main/qa_repository/shasta_qor/testcases/ati/pa_data/ati_cg_pa_rc_integrated.def high SKIP_VISB')

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container([

      dcc.Markdown('# Table For Main Metrics', style={'textAlign':'center'}),

      dbc.Label("Show number of Testcases"),
       row_drop := dcc.Dropdown(value=5, clearable=False, style={'width':'20%'},
                             options=[1,3,4, 5,len(records)]),

                                              
                             
      dbc.Row([dbc.Label("Select Testcase"),
        dbc.Col([
            design_drop := dcc.Dropdown([x for x in sorted(pd.DataFrame(records)["Design-testnameVersionA"].unique())], multi= True,style={'width':'80%'})
        ])
        

    ], justify="between", className='mt-3 mb-4'), 

    switches := html.Div(
    [
        
        dbc.Checklist(
            options=[
                {"label": "PASS", "value": 1},
                {"label": "FAIL", "value": 2},
                
            ],
            value=[],
            id="switches-input",
            inline=True,
            switch=True,
        ),
    ]
),
                     
button_group := html.Div(
    [
        dbc.RadioItems(
            id="radios",
            className="btn-group",
            inputClassName="btn-check",
            labelClassName="btn btn-outline-primary",
            labelCheckedClassName="active",
            options=[
                {"label": "show [5,10] % degradation", "value": 1},
                {"label": "show > 10 % degradation", "value": 2},
                {"label": "show > 10 % improvement", "value": 3},
                {"label": "show [5,10] % improvement ", "value": 4},
                {"label": "reset ", "value": 5}
                
            ],
            value=0,
            
        )
        
    ],
    className="radio-group",
),
dbc.Label("Select stage"),
       row_stage := dcc.Dropdown(value="main metrics", clearable=False, style={'width':'32%'},
                             options=["main metrics","cpu stage"]),    

                          
            
    my_table :=  dash_table.DataTable(
    columns= koora,
    data=records,
    
    filter_action= "native",
    merge_duplicate_headers=True,
    page_action='native',     # all data is passed to the table up-front
    page_size=5,
    
    hidden_columns=[],
    tooltip_data=[
        {
            column: {'value': str(value), 'type': 'markdown'}
            for column, value in row.items()
        } for row in records
    ],
    
      style_data_conditional=([
        {
            'if': {
                'filter_query': '{statusVersionA} = FAIL',
                'column_id': 'statusVersionA'
            },
            'backgroundColor': '#FF4136',
            'color': 'white',
            'fontWeight': 'bold'
        },
        {
            'if': {
                'filter_query': '{statusVersionB} = FAIL',
                'column_id': 'statusVersionB'
            },
            'backgroundColor': '#FF4136',
            'color': 'white',
            'fontWeight': 'bold'
        },
        {
            'if': {
                'filter_query': '{statusVersionB} = PASS',
                'column_id': 'statusVersionB'
            },
             'backgroundColor': '#3D9970',
            'color': 'white',
            'fontWeight': 'bold'
        },
          {
            'if': {
                'filter_query': '{statusVersionA} = PASS',
                'column_id': 'statusVersionA'
            },
            'backgroundColor': '#3D9970',
            'color': 'white',
            'fontWeight': 'bold'
        },
        {
            'if':{
                'column_type': 'any'
            },
            'textAlign': 'left'
        }
    ] +
    [ {
                'if': {
                    'filter_query': '{{{}}} < {}'.format(col, -0.01),
                    'column_id': col
                },
                'backgroundColor': '#3D9970',
                'color': 'white'
            } for col in diff_headers 
            ] +
         [ {
                'if': {
                    'filter_query': '{{{}}} > {}'.format(col, 0.01),
                    'column_id': col
                },
                'backgroundColor': '#FF4136',
                'color': 'white'
            } for col in diff_headers 
            ]+
            
             [ {
                'if': {
                    'filter_query': ('{{{col}}} >= {min}' + (' && {{{col}}} <= {max}')).format(col = col,min = minimum,max =maximum),
                    'column_id': col
                },
                'backgroundColor': '#000000',
                'color': 'white'
            } for col in diff_headers 
            ]+
            [
                {
                    'if': {
                        'filter_query': '{{{}}} is blank'.format(col),
                        'column_id': col
                    },
                    'backgroundColor': '#F1F1F1',
                    'color': 'white'
                } for col in all_columns
            ]
    ),
     style_data={                # overflow cells' content into multiple lines
            'whiteSpace': 'normal',
            'height': 'auto'
        },
        
        style_table={'overflowX': 'scroll','overflowY': 'auto'},
        
        style_header={
        
    #     'color': 'black',
        'fontWeight': 'bold',
    #     'border': '1px solid black' 
     },
    # style_cell={ 'border': '1px solid black' }
        
),


dbc.Label("Completion rate VersionA"),
progress1 := dbc.Progress(label= str(completionRate1)+"%", value=completionRate1,color="info",striped=True,animated=True,style={"height": "30px",'width':'32%'}),
dbc.Label("Completion rate VersionB"),
progress2 := dbc.Progress(label= str(completionRate2)+"%", value=completionRate2,color="info",striped=True,animated=True,style={"height": "30px",'width':'32%'}),



])
@callback(
    [Output(my_table, 'data'),
    Output(my_table, 'page_size'),Output(my_table, 'columns')],
    [Input(design_drop, 'value'),
    Input(row_drop, 'value'),Input("switches-input", 'value'),Input("radios", "value"),Input(row_stage, 'value')]
    

    
)
def update_dropdown_options(design_v, row_v,s_v,n,stage):
    dff = pd.DataFrame(records)
    string1 =""

    if design_v:
        dff = dff[dff["Design-testnameVersionA"].isin(design_v)]

    if s_v == [2]:
        dff = dff[(dff["statusVersionA"]== 'FAIL') | (dff["statusVersionB"]== 'FAIL') ] 
    elif s_v == [1]:
        dff = dff[(dff["statusVersionA"]== 'PASS') | (dff["statusVersionB"]== 'PASS')  ]  
    if n == 1:
        dff = show_range(0.05,0.1,records)
        

    if n == 2:
        dff = show_degradation(0.1,records)
    if n ==3:
        dff = show_improvement(-0.1,records) 
    if n==4:
        dff = show_range(-0.1,-0.05,records)   
    if n==5:
        dff=dff          
          
    if stage == "main metrics":
        row = implement_headers(youssef)      
    if stage == "cpu stage":
        row = implement_headers(cpu_stage)
    

    return dff.to_dict('records'), row_v,row


if __name__ == '__main__':
    app.run_server(debug=True, port=8001)
