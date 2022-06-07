from dash import Dash, dash_table
import pandas as pd
from dash.dependencies import Input, Output
from dash.dash_table import DataTable, FormatTemplate
from dash.dash_table.Format import Sign

app = Dash(__name__)


percentage = FormatTemplate.percentage(2).sign(Sign.positive)

koora = [{"name": ["", "Design-testname"], "id": "Design-testnameVersionA"}]
youssef = ['status', 'wallc-locktime','hostname',  'cpu', 'optimalcpu', 'CUSTOM_KPI-No._of_Flops', 'mem', 'power']

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

records = [{'statusVersionA': 'PASS', 'wallc-locktimeVersionA': 542.0, 'hostnameVersionA': 'svr-inn-clpqor-32.inn.mentorg.com', 'cpuVersionA': 432.0, 'optimalcpuVersionA': 432.0, 'CUSTOM_KPI-No._of_FlopsVersionA': 159439.0, 'Design-testnameVersionA': '/powerpro/tests/main/qa_repository/shasta_qor/testcases/ati/pa_data/ati_tcc0.1_prob0.4.def high SKIP_VISA', 
'statusVersionB': 'PASS', 'wallc-locktimeVersionB': 530.0, 'hostnameVersionB': 'svr-inn-clpqor-32.inn.mentorg.com', 'cpuVersionB': 450.0, 'optimalcpuVersionB': 430.0, 'CUSTOM_KPI-No._of_FlopsVersionB': 159430.0, 'statusdiff': '', 'wallc-locktimediff': 0.0226, 'hostnamediff': '', 'cpudiff': -0.04, 'optimalcpudiff': 0.0047, 'CUSTOM_KPI-No._of_Flopsdiff': 0.0001}, {'statusVersionA': 'FAIL', 'wallc-locktimeVersionA': 642.0, 'hostnameVersionA': 'svr-inn-clpqor-32.inn.mentorg.com', 'cpuVersionA': 332.0, 'optimalcpuVersionA': 
332.0, 'CUSTOM_KPI-No._of_FlopsVersionA': 259439.0, 'Design-testnameVersionA': '/powerpro/tests/main/qa_repository/shasta_qor/testcases/ati/pa_data/ati_cg_pa_rc_integrated.def high SKIP_VISB', 'statusVersionB': 'FAIL', 'wallc-locktimeVersionB': 647.0, 'hostnameVersionB': 'svr-inn-clpqor-32.inn.mentorg.com', 'cpuVersionB': 339.0, 'optimalcpuVersionB': 320.0, 'CUSTOM_KPI-No._of_FlopsVersionB': 259410.0, 'statusdiff': '', 'wallc-locktimediff': -0.0077, 'hostnamediff': '', 'cpudiff': -0.0206, 'optimalcpudiff': 0.0375, 'CUSTOM_KPI-No._of_Flopsdiff': 0.0001}, {'statusVersionA': 'PASS', 'wallc-locktimeVersionA': 742.0, 'hostnameVersionA': 'svr-inn-clpqor-32.inn.mentorg.com', 'cpuVersionA': 232.0, 'optimalcpuVersionA': 232.0, 'CUSTOM_KPI-No._of_FlopsVersionA': 359439.0, 'memVersionA': 200.0, 'Design-testnameVersionA': '/powerpro/tests/main/qa_repository/shasta_qor/testcases/Ipars/Ipars.def high SKIP_VISC', 'statusVersionB': 'PASS', 'wallc-locktimeVersionB': 749.0, 'hostnameVersionB': 'svr-inn-clpqor-32.inn.mentorg.com', 'cpuVersionB': 132.0, 
'optimalcpuVersionB': 332.0, 'CUSTOM_KPI-No._of_FlopsVersionB': 359430.0, 'memVersionB': 250.0, 'statusdiff': '', 'wallc-locktimediff': -0.0093, 'hostnamediff': '', 'cpudiff': 0.7576, 'optimalcpudiff': -0.3012, 'CUSTOM_KPI-No._of_Flopsdiff': 0.0, 'memdiff': -0.2}, {'statusVersionA': 'PASS', 'wallc-locktimeVersionA': 842.0, 'hostnameVersionA': 'svr-inn-clpqor-32.inn.mentorg.com', 'cpuVersionA': 132.0, 'optimalcpuVersionA': 132.0, 'CUSTOM_KPI-No._of_FlopsVersionA': 459439.0, 'powerVersionA': 300.0, 'Design-testnameVersionA': '/powerpro/tests/main/qa_repository/shasta_qor/testcases/Ipars/Ipars.def high SKIP_VISD', 'statusVersionB': 'PASS', 'wallc-locktimeVersionB': 842.0, 'hostnameVersionB': 'svr-inn-clpqor-32.inn.mentorg.com', 'cpuVersionB': 130.0, 'optimalcpuVersionB': 133.0, 'CUSTOM_KPI-No._of_FlopsVersionB': 459440.0, 'powerVersionB': 310.0, 'statusdiff': '', 'wallc-locktimediff': 0.0, 'hostnamediff': '', 'cpudiff': 0.0154, 'optimalcpudiff': -0.0075, 'CUSTOM_KPI-No._of_Flopsdiff': -0.0, 'powerdiff': -0.0323}, {'statusVersionA': 'FAIL', 'wallc-locktimeVersionA': 942.0, 'hostnameVersionA': 'svr-inn-clpqor-32.inn.mentorg.com', 'cpuVersionA': 532.0, 'optimalcpuVersionA': 532.0, 'CUSTOM_KPI-No._of_FlopsVersionA': 559439.0, 'Design-testnameVersionA': '/powerpro/tests/main/qa_repository/shasta_qor/testcases/Ipars/Ipars.def high SKIP_VISE', 'statusVersionB': 'FAIL', 'wallc-locktimeVersionB': 942.0, 'hostnameVersionB': 'svr-inn-clpqor-32.inn.mentorg.com', 'cpuVersionB': 539.0, 'optimalcpuVersionB': 531.0, 'CUSTOM_KPI-No._of_FlopsVersionB': 559439.0, 'statusdiff': '', 'wallc-locktimediff': 0.0, 'hostnamediff': '', 'cpudiff': -0.013, 'optimalcpudiff': 0.0019, 'CUSTOM_KPI-No._of_Flopsdiff': 0.0}, {'statusVersionA': 'FAIL', 'wallc-locktimeVersionA': 942.0, 'hostnameVersionA': 'svr-inn-clpqor-32.inn.mentorg.com', 'cpuVersionA': 532.0, 'optimalcpuVersionA': 532.0, 'CUSTOM_KPI-No._of_FlopsVersionA': 559439.0, 'Design-testnameVersionA': '/powerpro/tests/main/qa_repository/shasta_qor/testcases/Ipars/Ipars.def high SKIP_VISF'}]

app.layout = dash_table.DataTable(
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
            [
                {
                    'if': {
                        'filter_query': '{{{}}} is blank'.format(col),
                        'column_id': col
                    },
                    'backgroundColor': '#F1F1F1',
                    'color': 'white'
                } for col in all_columns
            ]+
             [ {
                'if': {
                    'filter_query': ('{{{col}}} >= {min}' + (' && {{{col}}} <= {max}')).format(col = col,min = -0.01,max =0.01),
                    'column_id': col
                },
                'backgroundColor': '#000000',
                'color': 'white'
            } for col in diff_headers 
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
        
)


if __name__ == '__main__':
    app.run_server(debug=True)
