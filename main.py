import numpy as np
import wfdb
from wfdb import processing

# fs - частота сэмпла

# Показать список аннотаций (кажется будет полезно)
# wfdb.show_ann_labels()

# Показать список классов аннотаций (зачем оно?)
# wfdb.show_ann_classes()


# record - запись кардиограммы
# annotation - данные аннотаций (точки на графике)
# sampfrom -> sampto - интервал показа на графике, использовать только sampto

record = wfdb.rdrecord('mitdb/100', sampto=3000, channels=[0])
annotation = wfdb.rdann('mitdb/100', 'atr', sampto=3000)

# Физический сигнал записи
p_signal = record.p_signal

# Грязный хак для превращения столбца в строку, иначе падает на find_peaks
p_signal = np.append(p_signal[0], p_signal[1:])

hard_peaks, soft_peaks = processing.find_peaks(p_signal)
print("hard\n", hard_peaks)
print("soft\n", soft_peaks)

xqrs = processing.XQRS(p_signal, record.fs)
xqrs.detect()

# Находит индексы R (самые большие пики)
print("qrs inds\n", xqrs.qrs_inds)

# вычисляет частоту сердцебиения
heart_rate = processing.compute_hr(len(p_signal), xqrs.qrs_inds, record.fs)

for index in xqrs.qrs_inds:
    print(index, heart_rate[index])

# record
# ann
# plot_sym - выводить ли свойства аннотации (свойства точек)
# time_units - как показывать временные интервалы (samples, seconds, minutes)
# title - заголовок
# figsize - размеры длина-высота
wfdb.plot_wfdb(record=record, annotation=annotation, plot_sym=True,
               time_units='samples', title='MIT-BIH Record 100',
               figsize=(20, 10))
