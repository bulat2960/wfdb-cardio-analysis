import wfdb

# record - запись кардиограммы
# annotation - данные аннотаций (точки на графике)
# sampfrom -> sampto - интервал показа на графике, использовать только sampto

record = wfdb.rdrecord('mitdb/100', sampto=3000)
annotation = wfdb.rdann('mitdb/100', 'atr', sampto=3000)

# record
# ann
# plot_sym - выводить ли свойства аннотации (свойства точек)
# time_units - как показывать временные интервалы (samples, seconds, minutes)
# title - заголовок
# figsize - размеры длина-высота
wfdb.plot_wfdb(record=record, annotation=annotation) # plot_sym=True)
               # time_units='samples', title='MIT-BIH Record 100')
               # figsize=(10, 5))