import pandas as pd


class dataframe:

    # Test Method for merge logic
    def merge_test(self):

        # samples to generate dataframe from sample data!

        # sales = [('account', ['Jones LLC', 'Alpha Co', 'Blue Inc']),
        #          ('Jan', [150, 200, 50]),
        #          ('Feb', [200, 210, 90]),
        #          ('Mar', [140, 215, 95]),
        #          ]
        #
        # df = pd.DataFrame.from_items(sales)
        # print(df)

        # sales = [{'account': 'Jones LLC', 'Jan': 150, 'Feb': 200, 'Mar': 140},
        #          {'account': 'Alpha Co', 'Jan': 200, 'Feb': 210, 'Mar': 215},
        #          {'account': 'Blue Inc', 'Jan': 50, 'Feb': 90, 'Mar': 95}]
        # df = pd.DataFrame(sales)
        # print(df)

        # sales = [('Jones LLC', 150, 200, 50),
        #          ('Alpha Co', 200, 210, 90),
        #          ('Blue Inc', 140, 215, 95)]
        # labels = ['account', 'Jan', 'Feb', 'Mar']
        # df = pd.DataFrame.from_records(sales, columns=labels)
        # print(df)

        # sales = {'account': ['Jones LLC', 'Alpha Co', 'Blue Inc'],
        #          'Jan': [150, 200, 50],
        #          'Feb': [200, 210, 90],
        #          'Mar': [140, 215, 95]}
        # df = pd.DataFrame.from_dict(sales)
        # print(df)


        data1 =  [('foo', 1, 1),
                  ('bar', 2, 2),
                  ('baz', 3, 3),
                  ('foo', 4, 4)]
        labels1 = ['lkey1', 'lkey2', 'value']
        df1 = pd.DataFrame.from_records(data1, columns=labels1)

        data2 = [('foo', 1, 5),
                 ('bar', 2, 6),
                 ('qax', 5, 7),
                 ('bar', 6, 8)]
        labels2 = ['rkey1', 'rkey2', 'value']
        df2 = pd.DataFrame.from_records(data2, columns=labels2)

        #http://pandas.pydata.org/pandas-docs/version/0.19.1/generated/pandas.DataFrame.merge.html
        dfmerge=df1.merge(df2, left_on=['lkey1','lkey2'], right_on=['rkey1','rkey2'], how='outer')
        print(df1)
        print(df2)
        print(dfmerge)

# Test df merge!
dfm=dataframe()
dfm.merge_test()

