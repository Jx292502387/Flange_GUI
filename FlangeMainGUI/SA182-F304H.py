#  SA182-F304H
#
#  23 April 2020   JCH
#  Ultimate Values from Line 8 from 2010 ASME B&PV code, II-D, Table U, pp 492-493
#  Yield Values from Line 12 from 2004 ASME B&PV code, II-D, Table Y-1, pp 608-611
#  Expansion values from Group 3, 2010 ASME B&PV code, II-D, Table TE-1, pg 711
#  K and Specific Heat values from Group J, 2010 ASME B&PV code, II-D, Table TCD, pg 727
#  Modulus from 2010 ASME B&PV code, II-D, Table TM-1, pp 738, Group G
#
from part import *
from material import *
from section import *
from sketch import *
#
#	Get active model name for use later
#
ThisModels = mdb.models
items = list(ThisModels.keys())
thisName = items[0]
#
mdb.models[thisName].Material(description=
    'SA-182 F304H  S30409  Ultimate Values from Line 8 from 2010 ASME B&PV code, II-D, Table U, pp 492-493 Yield Values from Line 12 from 2004 ASME B&PV code, II-D, Table Y-1, pp 608-611 Expansion values from Group 3, 2010 ASME B&PV code, II-D, Table TE-1, pg 711 K and Specific Heat values from Group J, 2010 ASME B&PV code, II-D, Table TCD, pg 727 Modulus from 2010 ASME B&PV code, II-D, Table TM-1, pp 738, Group G\n'
    , name='SA182-F304H')
mdb.models[thisName].materials['SA182-F304H'].Density(table=((0.28, ), ))
mdb.models[thisName].materials['SA182-F304H'].Elastic(table=((28300000.0, 0.3, 
    70.0), (27500000.0, 0.3, 200.0), (27000000.0, 0.3, 300.0), (26400000.0, 
    0.3, 400.0), (25900000.0, 0.3, 500.0), (25300000.0, 0.3, 600.0), (
    24800000.0, 0.3, 700.0), (24100000.0, 0.3, 800.0), (23500000.0, 0.3, 
    900.0), (22800000.0, 0.3, 1000.0), (22000000.0, 0.3, 1100.0), (21200000.0, 
    0.3, 1200.0), (20300000.0, 0.3, 1300.0), (19200000.0, 0.3, 1400.0), (
    18100000.0, 0.3, 1500.0)), temperatureDependency=ON)
mdb.models[thisName].materials['SA182-F304H'].Plastic(table=((30000.0, 0.0, 
    70.0), (34500.0, 0.003688, 70.0), (40416.7, 0.00741, 70.0), (46333.3, 
    0.013533, 70.0), (52250.0, 0.022987, 70.0), (58166.7, 0.036887, 70.0), (
    64083.3, 0.056538, 70.0), (70000.0, 0.083448, 70.0), (70100.0, 0.133975, 
    70.0), (25000.0, 0.0, 200.0), (28750.0, 0.003426842, 200.0), (35008.3, 
    0.00746288, 200.0), (41266.7, 0.014294736, 200.0), (47525.0, 0.024975367, 
    200.0), (53783.3, 0.040721631, 200.0), (60041.7, 0.062913161, 200.0), (
    66300.0, 0.093091395, 200.0), (66400.0, 0.143647502, 200.0), (22400.0, 0.0, 
    300.0), (25760.0, 0.003360827, 300.0), (31766.7, 0.00750182, 300.0), (
    37773.3, 0.01456501, 300.0), (43780.0, 0.025635501, 300.0), (49786.7, 
    0.041952218, 300.0), (55793.3, 0.06490409, 300.0), (61800.0, 0.096026798, 
    300.0), (61900.0, 0.146623437, 300.0), (20700.0, 0.0, 400.0), (23805.0, 
    0.003294, 400.0), (29787.5, 0.007557, 400.0), (35770.0, 0.014888, 400.0), (
    41752.5, 0.026403, 400.0), (47735.0, 0.043361, 400.0), (53717.5, 0.067153, 
    400.0), (59700.0, 0.099302, 400.0), (59800.0, 0.14992, 400.0), (19400.0, 
    0.0, 500.0), (22310.0, 0.003217359, 500.0), (28458.3, 0.007645917, 500.0), 
    (34606.7, 0.015329695, 500.0), (40755.0, 0.027422176, 500.0), (46903.3, 
    0.045197444, 500.0), (53051.7, 0.070041631, 500.0), (59200.0, 0.103446086, 
    500.0), (59300.0, 0.154068847, 500.0), (18400.0, 0.0, 600.0), (21160.0, 
    0.003154471, 600.0), (27500.0, 0.007746554, 600.0), (33840.0, 0.015775278, 
    600.0), (40180.0, 0.02842151, 600.0), (46520.0, 0.046965578, 600.0), (
    52860.0, 0.072777827, 600.0), (59200.0, 0.107311302, 600.0), (59300.0, 
    0.157933996, 600.0), (17600.0, 0.0, 700.0), (20240.0, 0.00310743, 700.0), (
    26733.3, 0.007844149, 700.0), (33226.7, 0.016173561, 700.0), (39720.0, 
    0.029294615, 700.0), (46213.3, 0.048486395, 700.0), (52706.7, 0.075098902, 
    700.0), (59200.0, 0.110546108, 700.0), (59300.0, 0.161168749, 700.0), (
    16900.0, 0.0, 800.0), (19435.0, 0.003078, 800.0), (25962.5, 0.007918, 
    800.0), (32490.0, 0.016459, 800.0), (39017.5, 0.02991, 800.0), (45545.0, 
    0.049546, 800.0), (52072.5, 0.076699, 800.0), (58600.0, 0.112753, 800.0), (
    58700.0, 0.163382, 800.0), (16200.0, 0.0, 900.0), (18630.0, 0.003067876, 
    900.0), (24991.7, 0.007945984, 900.0), (31353.3, 0.016565571, 900.0), (
    37715.0, 0.03013818, 900.0), (44076.7, 0.049936417, 900.0), (50438.3, 
    0.077285787, 900.0), (56800.0, 0.113558703, 900.0), (56900.0, 0.164207656, 
    900.0), (15500.0, 0.0, 1000.0), (17825.0, 0.003081, 1000.0), (23787.5, 
    0.007911, 1000.0), (29750.0, 0.016433, 1000.0), (35712.5, 0.029854, 
    1000.0), (41675.0, 0.04945, 1000.0), (47637.5, 0.076556, 1000.0), (53600.0, 
    0.112557, 1000.0), (53700.0, 0.163244, 1000.0), (15371.5, 0.0, 1100.0), (
    17677.2, 0.003249, 1100.0), (22359.2, 0.007605, 1100.0), (27041.2, 
    0.015133, 1100.0), (31723.2, 0.026973, 1100.0), (36405.2, 0.044393, 
    1100.0), (41087.2, 0.068782, 1100.0), (45769.1, 0.101647, 1100.0), (
    45869.1, 0.152453, 1100.0), (14420.1, 0.0, 1200.0), (16583.1, 0.003308, 
    1200.0), (20681.7, 0.007544, 1200.0), (24780.3, 0.014813, 1200.0), (
    28879.0, 0.026228, 1200.0), (32977.6, 0.043041, 1200.0), (37076.2, 
    0.066645, 1200.0), (41174.8, 0.098566, 1200.0), (41274.8, 0.149462, 
    1200.0), (13132.2, 0.0, 1300.0), (15102.0, 0.003427, 1300.0), (18389.9, 
    0.007463, 1300.0), (21677.9, 0.014295, 1300.0), (24965.8, 0.024977, 
    1300.0), (28253.7, 0.040724, 1300.0), (31541.6, 0.062918, 1300.0), (
    34829.6, 0.093098, 1300.0), (34929.6, 0.144159, 1300.0), (11456.6, 0.0, 
    1400.0), (13175.1, 0.003661, 1400.0), (15486.4, 0.00741, 1400.0), (17797.7, 
    0.013595, 1400.0), (20109.0, 0.023158, 1400.0), (22420.3, 0.037224, 
    1400.0), (24731.6, 0.05711, 1400.0), (27042.9, 0.084329, 1400.0), (27142.9, 
    0.135698, 1400.0), (9424.0, 0.0, 1500.0), (10837.6, 0.004167, 1500.0), (
    12147.4, 0.007538, 1500.0), (13457.2, 0.012831, 1500.0), (14767.0, 
    0.020788, 1500.0), (16076.8, 0.032326, 1500.0), (17386.5, 0.048557, 
    1500.0), (18696.3, 0.070814, 1500.0), (18796.3, 0.122804, 1500.0)), 
    temperatureDependency=ON)
mdb.models[thisName].materials['SA182-F304H'].Expansion(table=((8.5e-06, 
    70.0), (8.6e-06, 100.0), (8.8e-06, 150.0), (8.9e-06, 200.0), (9.1e-06, 
    250.0), (9.2e-06, 300.0), (9.4e-06, 350.0), (9.5e-06, 400.0), (9.6e-06, 
    450.0), (9.7e-06, 500.0), (9.8e-06, 550.0), (9.9e-06, 600.0), (9.9e-06, 
    650.0), (1e-05, 700.0), (1e-05, 750.0), (1.01e-05, 800.0), (1.02e-05, 
    850.0), (1.02e-05, 900.0), (1.03e-05, 950.0), (1.03e-05, 1000.0), (
    1.04e-05, 1050.0), (1.04e-05, 1100.0), (1.05e-05, 1150.0), (1.06e-05, 
    1200.0), (1.06e-05, 1250.0), (1.07e-05, 1300.0), (1.07e-05, 1350.0), (
    1.08e-05, 1400.0), (1.08e-05, 1450.0), (1.08e-05, 1500.0)), 
    temperatureDependency=ON)
mdb.models[thisName].materials['SA182-F304H'].Conductivity(table=((0.71667, 
    70.0), (0.725, 100.0), (0.75, 150.0), (0.775, 200.0), (0.8, 250.0), (
    0.81667, 300.0), (0.84167, 350.0), (0.86667, 400.0), (0.88333, 450.0), (
    0.90833, 500.0), (0.925, 550.0), (0.94167, 600.0), (0.96667, 650.0), (
    0.98333, 700.0), (1.0, 750.0), (1.025, 800.0), (1.04167, 850.0), (1.05833, 
    900.0), (1.075, 950.0), (1.09167, 1000.0), (1.11667, 1050.0), (1.13333, 
    1100.0), (1.15, 1150.0), (1.16667, 1200.0), (1.19167, 1250.0), (1.20833, 
    1300.0), (1.225, 1350.0), (1.24167, 1400.0), (1.25833, 1450.0), (1.275, 
    1500.0)), temperatureDependency=ON)
mdb.models[thisName].materials['SA182-F304H'].SpecificHeat(table=((0.11771, 
    70.0), (0.1183, 100.0), (0.12079, 150.0), (0.12321, 200.0), (0.12558, 
    250.0), (0.12659, 300.0), (0.12886, 350.0), (0.13027, 400.0), (0.13119, 
    450.0), (0.1333, 500.0), (0.13338, 550.0), (0.13422, 600.0), (0.13545, 
    650.0), (0.13625, 700.0), (0.13627, 750.0), (0.13816, 800.0), (0.1389, 
    850.0), (0.13888, 900.0), (0.13959, 950.0), (0.13956, 1000.0), (0.1413, 
    1050.0), (0.14196, 1100.0), (0.1419, 1150.0), (0.14254, 1200.0), (0.14417, 
    1250.0), (0.14408, 1300.0), (0.14468, 1350.0), (0.14526, 1400.0), (0.14583, 
    1450.0), (0.1464, 1500.0)), temperatureDependency=ON)
mdb.models['Model-1'].HomogeneousSolidSection(name='Flange-Section', 
            material='SA182-F304H', thickness=None)
#
print "Completed SA182-F304H properties"
#
