from sqlalchemy import create_engine

import pandas as pd
import sys
import getopt
import configparser

argv = sys.argv[1:]
opts, args = getopt.getopt(argv, 'f:t:')

print(opts)
if len(opts) == 0:
    print('falta parametros: -f <<arquivo csv>>  -t <<tabela do postgres>>')
    print('ex.:  python importCSVtoPostgre.py -f Fast_Food_Restaurants_US.csv -t fast-food')
else:
    config = configparser.ConfigParser()
    config.read('app_config.ini')
    cfg = {
        'host': config.get('dev', 'SQL_HOST'),
        'user': config.get('dev', 'SQL_USER'),
        'passw': config.get('dev', 'SQL_PASSWORD'),
        'nameSQL': config.get('dev', 'SQL_NAME'),
        'port': config.get('dev', 'SQL_PORT'),
        'db': config.get('dev', 'SQL_DATABASE'),
        'file': '',
        'nameTable': ''
    }

    try:
        cfg['file'] = '' if opts[0][0] != '-f' else opts[0][1]
        cfg['table'] = '' if opts[1][0] != '-t' else opts[1][1]
    except IndexError:
        print("An exception occurred")

    df = pd.read_csv(cfg['file'])
    df.drop(df.columns[0], axis=1, inplace=True)
    engine = create_engine(
        '{}://{}:{}@{}:{}/{}'.format(
            cfg['nameSQL'], cfg['user'], cfg['passw'], cfg['host'], cfg['port'], cfg['db']
        )
    )
    df.to_sql(cfg['table'], engine, index=True, if_exists='append')
