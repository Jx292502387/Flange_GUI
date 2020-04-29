# -*- coding: mbcs -*-
#
#  8 April 2020   JCH
#  SA-193-B7 properties taken from 2010 ASME Code
#
from part import *
from material import *
from section import *
from assembly import *
#
#	Get active model name for use later
#
ThisModels = mdb.models
items = list(ThisModels.keys())
thisName = items[0]
#
mdb.models[thisName].Material(description=
    'Yield Values from Line 15 from 2010 ASME B&PV code, II-D, Table Y-1, pp 560-563 Ultimate Values from Line 34 from 2010 ASME B&PV code, II-D, Table U, pp 470-471 Expansion values from Group 1, 2010 ASME B&PV code, II-D, Table TE-1, pg 708  K and Specific Heat values from Group C, 2010 ASME B&PV code, II-D, Table TCD, pg 726  Modulus from 2010 ASME B&PV code, II-D, Table TM-1, pp 738, Material Group C'
    , name='SA193-B7')
mdb.models[thisName].materials['SA193-B7'].Density(table=((0.28, ), ))
mdb.models[thisName].materials['SA193-B7'].Elastic(table=((29600000.0, 0.3, 
    70.0), (29000000.0, 0.3, 200.0), (28500000.0, 0.3, 300.0), (28000000.0, 
    0.3, 400.0), (27400000.0, 0.3, 500.0), (26900000.0, 0.3, 600.0), (
    26200000.0, 0.3, 700.0), (25600000.0, 0.3, 800.0), (24800000.0, 0.3, 
    900.0), (23900000.0, 0.3, 1000.0), (23000000.0, 0.3, 1100.0), (21800000.0, 
    0.3, 1200.0), (20500000.0, 0.3, 1300.0)), temperatureDependency=ON)
mdb.models[thisName].materials['SA193-B7'].Plastic(table=((105000.0, 0.0, 
    70.0), (110250.0, 0.005058, 70.0), (115500.0, 0.010116, 70.0), (120750.0, 
    0.015175, 70.0), (121458.3333, 0.016529, 70.0), (122166.6667, 0.017996, 
    70.0), (122875.0, 0.019583, 70.0), (123583.3333, 0.0213, 70.0), (
    124291.6667, 0.023156, 70.0), (125000.0, 0.025163, 70.0), (125100.0, 
    0.075458, 70.0), (98000.0, 0.0, 200.0), (102900.0, 0.003274, 200.0), (
    107800.0, 0.006547, 200.0), (112700.0, 0.009821, 200.0), (114750.0, 
    0.012071, 200.0), (116800.0, 0.014783, 200.0), (118850.0, 0.018041, 200.0), 
    (120900.0, 0.021942, 200.0), (122950.0, 0.026598, 200.0), (125000.0, 
    0.032141, 200.0), (125100.0, 0.082436, 200.0), (94100.0, 0.0, 300.0), (
    98805.0, 0.002765, 300.0), (103510.0, 0.005531, 300.0), (108215.0, 
    0.008296, 300.0), (111013.0, 0.010761, 300.0), (113810.0, 0.013869, 300.0), 
    (116608.0, 0.017766, 300.0), (119405.0, 0.022623, 300.0), (122203.0, 
    0.028648, 300.0), (125000.0, 0.036083, 300.0), (125100.0, 0.086379, 300.0), 
    (91500.0, 0.0, 400.0), (96075.0, 0.002517, 400.0), (100650.0, 0.005035, 
    400.0), (105225.0, 0.007552, 400.0), (108521.0, 0.010121, 400.0), (
    111817.0, 0.013446, 400.0), (115113.0, 0.017717, 400.0), (118408.0, 
    0.023163, 400.0), (121704.0, 0.030062, 400.0), (125000.0, 0.038744, 400.0), 
    (125100.0, 0.089039, 400.0), (88500.0, 0.0, 500.0), (92925.0, 0.00229, 
    500.0), (97350.0, 0.004581, 500.0), (101775.0, 0.006871, 500.0), (105646.0, 
    0.009539, 500.0), (109517.0, 0.013088, 500.0), (113388.0, 0.017762, 500.0), 
    (117258.0, 0.023858, 500.0), (121129.0, 0.031741, 500.0), (125000.0, 
    0.041851, 500.0), (125100.0, 0.092146, 500.0), (85300.0, 0.0, 600.0), (
    89565.0, 0.002098, 600.0), (93830.0, 0.004195, 600.0), (98095.0, 0.006293, 
    600.0), (102579.0, 0.009053, 600.0), (107063.0, 0.012823, 600.0), (
    111548.0, 0.017905, 600.0), (116032.0, 0.024673, 600.0), (120516.0, 
    0.03359, 600.0), (125000.0, 0.045216, 600.0), (125100.0, 0.095511, 600.0), 
    (80600.0, 0.0, 700.0), (84630.0, 0.002042, 700.0), (88660.0, 0.004085, 
    700.0), (92690.0, 0.006127, 700.0), (97175.0, 0.008916, 700.0), (101660.0, 
    0.012756, 700.0), (106145.0, 0.01797, 700.0), (110630.0, 0.024959, 700.0), 
    (115115.0, 0.034216, 700.0), (119600.0, 0.046344, 700.0), (119700.0, 
    0.096653, 700.0), (73900.0, 0.0, 800.0), (77595.0, 0.002093, 800.0), (
    81290.0, 0.004186, 800.0), (84985.0, 0.00628, 800.0), (88888.0, 0.009042, 
    800.0), (92790.0, 0.012817, 800.0), (96693.0, 0.017909, 800.0), (100595.0, 
    0.024695, 800.0), (104498.0, 0.033639, 800.0), (108400.0, 0.045304, 800.0), 
    (108500.0, 0.095645, 800.0), (64100.0, 0.0, 900.0), (67305.0, 0.002066, 
    900.0), (70510.0, 0.004132, 900.0), (73715.0, 0.006198, 900.0), (77196.0, 
    0.008974, 900.0), (80677.0, 0.012784, 900.0), (84158.0, 0.017941, 900.0), (
    87638.0, 0.024834, 900.0), (91119.0, 0.033944, 900.0), (94600.0, 0.045855, 
    900.0), (94700.0, 0.096245, 900.0), (50900.0, 0.0, 1000.0), (53445.0, 
    0.001901, 1000.0), (55990.0, 0.003802, 1000.0), (58535.0, 0.005703, 
    1000.0), (61846.0, 0.008572, 1000.0), (65157.0, 0.012613, 1000.0), (
    68468.0, 0.018209, 1000.0), (71778.0, 0.025834, 1000.0), (75089.0, 
    0.036079, 1000.0), (78400.0, 0.049665, 1000.0), (78500.0, 0.100136, 
    1000.0)), temperatureDependency=ON)
mdb.models[thisName].materials['SA193-B7'].Expansion(table=((6.4e-06, 70.0), (
    6.5e-06, 100.0), (6.6e-06, 150.0), (6.7e-06, 200.0), (6.8e-06, 250.0), (
    6.9e-06, 300.0), (7e-06, 350.0), (7.1e-06, 400.0), (7.2e-06, 450.0), (
    7.3e-06, 500.0), (7.3e-06, 550.0), (7.4e-06, 600.0), (7.5e-06, 650.0), (
    7.6e-06, 700.0), (7.7e-06, 750.0), (7.8e-06, 800.0), (7.9e-06, 850.0), (
    7.9e-06, 900.0), (8e-06, 950.0), (8.1e-06, 1000.0), (8.1e-06, 1050.0), (
    8.2e-06, 1100.0), (8.3e-06, 1150.0), (8.3e-06, 1200.0), (8.4e-06, 1250.0), 
    (8.4e-06, 1300.0)), temperatureDependency=ON)
mdb.models[thisName].materials['SA193-B7'].Conductivity(table=((1.975, 70.0), 
    (1.9667, 100.0), (1.9583, 150.0), (1.9583, 200.0), (1.95, 250.0), (1.95, 
    300.0), (1.9417, 350.0), (1.925, 400.0), (1.9167, 450.0), (1.8917, 500.0), 
    (1.875, 550.0), (1.85, 600.0), (1.825, 650.0), (1.8, 700.0), (1.775, 
    750.0), (1.75, 800.0), (1.7167, 850.0), (1.6917, 900.0), (1.6667, 950.0), (
    1.6417, 1000.0), (1.6167, 1050.0), (1.5917, 1100.0), (1.5583, 1150.0), (
    1.525, 1200.0), (1.475, 1250.0), (1.3833, 1300.0)), temperatureDependency=
    ON)
mdb.models[thisName].materials['SA193-B7'].SpecificHeat(table=((0.10671707, 
    70.0), (0.108151785, 100.0), (0.11114365, 150.0), (0.114551356, 200.0), (
    0.117386153, 250.0), (0.120606223, 300.0), (0.123477988, 350.0), (
    0.125971123, 400.0), (0.129174934, 450.0), (0.131418308, 500.0), (
    0.134014341, 550.0), (0.136556359, 600.0), (0.139270452, 650.0), (
    0.142174704, 700.0), (0.145289827, 750.0), (0.14863965, 800.0), (
    0.151516221, 850.0), (0.155970329, 900.0), (0.160216972, 950.0), (
    0.164841859, 1000.0), (0.170620849, 1050.0), (0.177021793, 1100.0), (
    0.182307265, 1150.0), (0.189112103, 1200.0), (0.199903504, 1250.0), (
    0.209200381, 1300.0)), temperatureDependency=ON)
mdb.models['Model-1'].HomogeneousSolidSection(name='Bolt-Section', 
            material='SA-193-B7', thickness=None)
#
#   Print out message indicating the material property loaded
#
print "Completed SA193-B7 properties"
#