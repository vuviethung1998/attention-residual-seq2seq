from pandas import read_csv
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # data = read_csv('../data/actual_data.csv')
    # # shape (8759,1)
    # data = data.groupby(['time'],as_index=False).agg({'load': 'sum'})
    # load_data = data['load'].to_numpy()
    # load_data = np.expand_dims(load_data, axis=1)
    # np.savez('../data/actual_data.npz', data = load_data)

    data = read_csv('../data/temp_electric_holiday_increase.csv')
    # shape (8759,1)
    # data = data.groupby(['time'],as_index=False).agg({'load': 'sum'})
    load_data = data[['power','holiday','dayOfWeek','increase']].to_numpy()
    # load_data = data['power'].to_numpy()
    load_data = np.expand_dims(load_data, axis=1)
    np.savez('../data/electric_holiday_increase.npz', data = load_data)
    raw_data = np.load('../data/electric_holiday_increase.npz')['data']
    print(raw_data)
