from flask import jsonify, Response
from app.services.pandas_service import *
from app.routes import routes_bp as bp

@bp.route('/pandas/iris_summary', methods=['GET'], endpoint='pandas_iris_summary')
def get_numpy_array():
    summary = iris_summary()
    return jsonify(summary), 200

@bp.route('/pandas/iris_correct', methods=['GET'], endpoint='pandas_iris_corrected')
def correct_iris_data():
    try:
        r35, r38=correct_irirs_df()
        return jsonify({'message':'Dataset corrected and saved.',
                        'Corrected rows':{
                            '35th': r35.to_dict(),
                            '38th': r38.to_dict()
                        }}),200  
    except:
        return jsonify({'error':'Unexpected error, try later please.'}),400

@bp.route('/pandas/new_features', methods=['GET'], endpoint='pandas_new_iris_feature')
def add_irirs_features():
    new_features = add_features()

    return jsonify({'messeges':'Operation successed. Added to new features',
                    'head':new_features.to_dict()}),200

@bp.route('/pandas/iris_correlation', methods=['GET'], endpoint='pandas_iris_correlation')
def irirs_correlation():
    correlations,top, bottom = iris_pair_wise()

    return jsonify({'Correlation Matrix':correlations,
                    'Bottom':{
                        'features': bottom,
                        'explanation': "Usually this kind of realtion indicates that there is an inverse relationship that's mean whether the first feature increase the second one decrease."},
                    'Top':{
                        'features':top,
                        'explanation': "When the realtionship between features is positive indicates that both of the features tend to increase together.",
                        }}), 200

@bp.route('/pandas/iris_scatter',methods=['GET'], endpoint='pandas_iris_scatter')
def iris_scatter():
    iris_scatter = scatter_plot()

    return Response(iris_scatter.getvalue(), mimetype='image/png')

@bp.route('/pandas/iris_pairplot', methods=['GET'], endpoint='pandas_iris_pairplot')
def iris_pairplot():
    iris_pairplot = pair_plot()

    return Response(iris_pairplot.getvalue(), mimetype='image/png')