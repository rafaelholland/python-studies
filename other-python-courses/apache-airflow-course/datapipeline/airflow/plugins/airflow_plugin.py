from airflow.plugins_manager import AirflowPlugin
from airflow.plugins.twitter_operator import TwitterOperator

class AluraAirflowPlugin(AirflowPlugin):
    name = "alura"
    operators = [TwitterOperator]